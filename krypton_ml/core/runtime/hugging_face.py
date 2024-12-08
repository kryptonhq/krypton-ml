from typing import Any, Dict
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM


class HuggingFaceHandler:
    """Handler for HuggingFace models in Krypton ML"""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize HuggingFace model handler

        Args:
            config: Model configuration containing:
                - model_name: Name of HF model
                - task: Task type (generation, seq2seq, etc)
                - device: cuda/cpu (optional)
                - model_kwargs: Additional kwargs for model loading
                - generation_kwargs: Default generation parameters
        """
        self.model_name = config["model_name"]
        self.task = config.get("task", "generation")
        self.device = config.get(
            "device", "cuda" if torch.cuda.is_available() else "cpu"
        )
        self.model_kwargs = config.get("model_kwargs", {})
        self.generation_kwargs = config.get("generation_kwargs", {})

        # Load model and tokenizer
        self._load_model()

    def _load_model(self):
        """Load appropriate HF model and tokenizer with proper padding setup"""
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        # Handle padding token setup
        if self.tokenizer.pad_token is None:
            # For GPT-style models, use EOS token as padding
            if self.tokenizer.eos_token is not None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            else:
                # Add a padding token if neither pad nor eos token exists
                self.tokenizer.add_special_tokens({"pad_token": "[PAD]"})

        # Load the model
        if self.task == "generation":
            model_class = AutoModelForCausalLM
        elif self.task == "seq2seq":
            model_class = AutoModelForSeq2SeqLM
        else:
            raise ValueError(f"Unsupported task: {self.task}")

        self.model = model_class.from_pretrained(
            self.model_name, **self.model_kwargs
        ).to(self.device)

        # Resize embeddings if we added new tokens
        if len(self.tokenizer) != self.model.config.vocab_size:
            self.model.resize_token_embeddings(len(self.tokenizer))

        self.model.eval()

    def predict(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate predictions using the HF model"""
        # Get input text
        text = input_data.get("text")
        if not text:
            raise ValueError("Input text is required")

        # Merge default and request-specific generation params
        generation_params = {
            **self.generation_kwargs,
            **input_data.get("generation_params", {}),
        }

        # Tokenize with proper padding
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            pad_to_multiple_of=8,  # Optional: for efficiency on some hardware
            truncation=True,  # Add truncation for safety
            max_length=self.tokenizer.model_max_length,  # Respect model's max length
        ).to(self.device)

        # Generate
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                pad_token_id=self.tokenizer.pad_token_id,  # Explicitly set pad token ID
                **generation_params,
            )

        # Decode
        generated_text = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)

        return {
            "generated_text": generated_text[0],
            "model_info": {"model_name": self.model_name, "task": self.task},
        }
