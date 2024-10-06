import json
from typing import List

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from langchain.load.dump import dumps

from krypton_ml.core.models.cli_config import Model
from krypton_ml.core.models.registry import ModelInfoResponse
from krypton_ml.core.registry.model_registry import ModelRegistry

model_registry = ModelRegistry()


def load_model_endpoints(app: FastAPI, models: [Model]):
    for idx, model in enumerate(models):
        # Prepare the model key
        model_key = f"/{model.endpoint}"
        # Load the model into the model registry
        model_registry.load_model(model, model_key)

        @app.post(
            f"/{model.endpoint}",
            name=model.name,
            description=model.description,
            tags=model.tags,
        )
        async def invoke_model(request: Request, input: dict):
            # Get the model identifier from the request URL
            model_identifier = request.url.path
            # Invoke the model
            response = model_registry.invoke_model(model_identifier, input)

            json_string = dumps(response, ensure_ascii=False)
            return JSONResponse(content={"response": json.loads(json_string)})

        @app.get(
            "/registry/models",
            description="Get the list of registered models",
            response_model=List[ModelInfoResponse],
        )
        async def get_registered_models():
            return model_registry.get_registered_models()

    return app
