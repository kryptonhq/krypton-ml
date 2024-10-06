from pydantic_yaml import parse_yaml_raw_as

from krypton_ml.core.models.cli_config import RootConfig


def load_config(config: str) -> RootConfig:
    return parse_yaml_raw_as(RootConfig, open(config).read())
