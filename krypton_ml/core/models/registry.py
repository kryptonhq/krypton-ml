from abc import abstractmethod, ABC
from typing import List, Any, Dict

from pydantic import BaseModel


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
