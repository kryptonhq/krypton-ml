import json

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from langchain.load.dump import dumps
from krypton_ml.core.loader.module import load_module
from krypton_ml.core.models.cli_config import Model

model_registry = {}

def load_model_endpoints(app: FastAPI, models: [Model]):
    for idx, model in enumerate(models):
        lc_callable = load_module(model.module_path, model.callable)
        model_key = f"/{model.endpoint}"
        model_registry[model_key] = lc_callable

        @app.post(f"/{model.endpoint}", name=model.name, description=model.description, tags=model.tags)
        async def invoke_model(request: Request, input: dict):
            model_identifier = request.url.path
            response = model_registry[model_identifier].invoke(input)
            json_string = dumps(response, ensure_ascii=False)
            return JSONResponse(content={
                "response": json.loads(json_string)
            })

    return app
