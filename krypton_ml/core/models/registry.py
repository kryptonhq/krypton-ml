from abc import abstractmethod, ABC
from typing import List, Any, Dict

from pydantic import BaseModel

from krypton_ml.core.loader.module import load_module
from krypton_ml.core.models.cli_config import Model
from krypton_ml.core.runtime.hugging_face import HuggingFaceHandler


class KryptonCustomModel(ABC):
    @abstractmethod
    def predict(self, input: Dict[str, Any]) -> Dict[str, Any]:
        pass


class RegisteredModel(BaseModel):
    model_artifact: Any
    model_type: str
    name: str
    description: str
    tags: List[str]
    endpoint: str


class ModelInfoResponse(BaseModel):
    name: str
    description: str
    endpoint: str
    tags: List[str]


class ModelLoader(ABC):
    """Base class for model loading strategies"""

    @abstractmethod
    def load(self, model: Model) -> Any:
        """Load model artifact"""
        pass


class LangChainModelLoader(ModelLoader):
    def load(self, model: Model) -> Any:
        return load_module(model.module_path, model.callable)


class CustomModelLoader(ModelLoader):
    def load(self, model: Model) -> Any:
        model_class = load_module(model.module_path, model.callable)
        return model_class()


class HuggingFaceModelLoader(ModelLoader):
    def load(self, model: Model) -> Any:
        return HuggingFaceHandler(
            {
                "model_name": model.hf_model_name,
                "task": model.hf_task,
                "model_kwargs": model.hf_model_kwargs,
                "generation_kwargs": model.hf_generation_kwargs,
                "device": model.hf_device,
            }
        )
