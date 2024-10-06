from typing import List, Optional

from pydantic import BaseModel


class ModelOptions(BaseModel):
    debug: bool = False


class Model(BaseModel):
    name: str
    type: str
    module_path: str
    callable: str
    endpoint: str
    options: Optional[ModelOptions] = None
    tags: List[str] = []
    description: str = ""


class ServerConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    allow_origins: List[str] = []
    allow_credentials: bool = False
    allow_methods: List[str] = []
    allow_headers: List[str] = []
    debug: bool = False


class KryptonConfig(BaseModel):
    models: List[Model]
    server: Optional[ServerConfig]


class RootConfig(BaseModel):
    krypton: KryptonConfig
