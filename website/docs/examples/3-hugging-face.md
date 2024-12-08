---
sidebar_position: 3
---

# HuggingFace Models (Experimental)

:::caution Experimental Feature
HuggingFace integration is currently in beta and under active development. We're working on adding support for more model types and improving the integration. The API and configuration format might change in future releases.

Current examples showcase basic integration with three models (GPT-2, T5, and Phi-2). More examples and model types will be added soon.
:::

## Configuration

To use a HuggingFace model, add it to your `config.yaml` with type `huggingface`. Here's the basic structure:

```yaml
- name: model-name
  type: huggingface
  description: Description of your model
  endpoint: your/desired/endpoint
  hf_model_name: "model-id-on-huggingface"
  hf_task: "task-type"
  hf_generation_kwargs:
    parameter1: value1
    parameter2: value2
```

### Parameters

- `hf_model_name`: The model ID from HuggingFace Hub (e.g., "gpt2", "microsoft/phi-2")
- `hf_task`: Task type ("generation" or "seq2seq")
- `hf_generation_kwargs`: Model-specific generation parameters
- `endpoint`: Your custom API endpoint path

## Example Models

### GPT-2 Text Generation

This example serves the GPT-2 model for text generation:

```yaml
- name: gpt2-model
  type: huggingface
  description: GPT-2 text generation model
  endpoint: models/gpt2/generate
  hf_model_name: "gpt2"
  hf_task: "generation"
  hf_generation_kwargs:
    max_length: 100
    temperature: 0.7
    top_p: 0.9
```

**Usage Example:**
```bash
curl -X 'POST' \
  'http://localhost:5000/models/gpt2/generate' \
  -H 'Content-Type: application/json' \
  -d '{
    "text": "Once upon a time",
    "generation_params": {
      "max_length": 200,
      "temperature": 0.7
    }
  }'
```

### T5 Translation

This example uses T5-small for text translation:

```yaml
- name: t5-translator
  type: huggingface
  description: T5 translation model
  endpoint: models/t5/translate
  hf_model_name: "t5-small"
  hf_task: "seq2seq"
  hf_generation_kwargs:
    max_length: 50
```

**Usage Example:**
```bash
curl -X 'POST' \
  'http://localhost:5000/models/t5/translate' \
  -H 'Content-Type: application/json' \
  -d '{
    "text": "translate English to German: Hello, how are you?"
  }'
```

### Microsoft's Phi-2

This example serves the Phi-2 model for efficient text generation:

```yaml
- name: phi2-generate
  type: huggingface
  description: Microsoft's Phi-2 small language model
  endpoint: models/phi2/generate
  hf_model_name: "microsoft/phi-2"
  hf_task: "generation"
  hf_generation_kwargs:
    max_length: 200
    temperature: 0
    top_p: 0.9
    do_sample: true
```

**Usage Example:**
```bash
curl -X 'POST' \
  'http://localhost:5000/models/phi2/generate' \
  -H 'Content-Type: application/json' \
  -d '{
    "text": "Write a short story about a robot:",
    "generation_params": {
      "max_length": 150,
      "temperature": 0.7
    }
  }'
```

## Generation Parameters

### Common Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| max_length | Maximum length of generated text | Model specific |
| temperature | Controls randomness (0.0 to 1.0) | 1.0 |
| top_p | Nucleus sampling parameter | 1.0 |
| do_sample | Whether to use sampling | true |

You can set default parameters in `hf_generation_kwargs` and override them per request using `generation_params` in the API call.
