import typer
import uvicorn

from krypton_ml.core.loader.config import load_config
from krypton_ml.core.models.cli_config import RootConfig
from krypton_ml.core.utils.logger import logger
from krypton_ml.core.webserver.model_endpoints import load_model_endpoints
from krypton_ml.core.webserver.server_runtime import create_server_runtime

app = typer.Typer()


@app.command()
def main(config: str = typer.Argument(help="The config file")):
    parsed_config: RootConfig = load_config(config)
    app = create_server_runtime(parsed_config.krypton.server)
    app = load_model_endpoints(app, parsed_config.krypton.models)

    logger.info("Starting Krypton ML Server")
    uvicorn.run(
        app,
        host=parsed_config.krypton.server.host,
        port=parsed_config.krypton.server.port,
        log_config=None,
    )


if __name__ == "__main__":
    app()
