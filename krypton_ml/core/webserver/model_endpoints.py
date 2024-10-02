from fastapi import FastAPI

from krypton_ml.core.loader.module import load_module
from krypton_ml.core.models.cli_config import Model

model_registry = {}

def load_model_endpoints(app: FastAPI, models: [Model]):
    for idx, model in enumerate(models):

        lc_callable = load_module(model.module_path, model.callable)
        model_registry[model.name] = lc_callable

        @app.post(f"/{model.endpoint}", name=model.name, description=model.description, tags=model.tags)
        async def invoke_model(input: dict):
            response = model_registry[model.name](input)
            return response

    return app
