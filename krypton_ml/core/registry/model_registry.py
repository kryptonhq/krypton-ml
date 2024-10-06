from typing import Dict, Any

from krypton_ml.core.loader.module import load_module
from krypton_ml.core.models.cli_config import Model
from krypton_ml.core.models.registry import RegisteredModel


class ModelRegistry:
    def __init__(self):
        self.model_registry: Dict[str, RegisteredModel] = {}

    def load_model(self, model: Model, model_key: str):
        """
        Load a model into the model registry
        :param model: Model object from the CLI config
        :param model_key: Key to store the model in the registry
        :return: None
        """
        model_callable = load_module(model.module_path, model.callable)
        if model.type == "langchain":
            model_artifact = model_callable
        elif model.type == "custom":
            # Initialize the model so that the model is ready to be invoked
            model_artifact = model_callable()
        else:
            raise ValueError(f"Unsupported model type: {model.type}")

        self.model_registry[model_key] = RegisteredModel(
            model_artifact=model_artifact,
            model_type=model.type,
            name=model.name,
            description=model.description,
            tags=model.tags,
        )

    def invoke_model(self, model_key: str, input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Invoke a model from the model registry
        :param model_key: Key of the model to invoke
        :param input: Dict[str, Any] Input to the model
        :return: Dict[str, Any] Response from the model
        """
        if model_key not in self.model_registry:
            raise KeyError(f"Model with key {model_key} not found in registry")

        model_info = self.model_registry[model_key]
        model = model_info.model_artifact
        model_type = model_info.model_type

        if model_type == "langchain":
            return model.invoke(input)
        elif model_type == "custom":
            return model.predict(input)
        else:
            raise ValueError(f"Unsupported model type: {model_type}")