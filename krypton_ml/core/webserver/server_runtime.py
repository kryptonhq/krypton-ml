import traceback

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from krypton_ml.core.models.cli_config import ServerConfig
from krypton_ml.core.webserver.log_middleware import LogMiddleware


def create_server_runtime(server_config: ServerConfig):
    app = FastAPI(title="Krypton ML Server", version="0.1.0")

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=server_config.allow_origins,
        allow_credentials=server_config.allow_credentials,
        allow_methods=server_config.allow_methods,
        allow_headers=server_config.allow_headers,
    )
    app.add_middleware(LogMiddleware)

    # Add a sample endpoint
    @app.get("/")
    async def root():
        return {"message": "Krpyton ML Server is running!"}

    # Health check endpoint
    @app.get("/health")
    async def health():
        return {"status": "ok"}

    # Error handling
    @app.exception_handler(Exception)
    async def generic_exception_handler(request, exc):
        exception_response = {
            "message": "An error occurred",
            "detail": str(exc),
        }
        if server_config.debug:
            exception_response["stack_trace"] = traceback.format_exc()

        return JSONResponse(
            status_code=500,
            content=exception_response,
        )

    return app
