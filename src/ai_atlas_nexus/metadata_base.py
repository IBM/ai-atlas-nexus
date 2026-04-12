# Standard
from enum import Enum, StrEnum, auto, unique


@unique
class InferenceEngineType(StrEnum):
    """Enum to contain possible values for inference engine types"""

    RITS = "rits"
    WML = "watsonx"
    VLLM = "vllm"
    OLLAMA = "ollama"
    HF = "hf"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.name, cls))

    def __str__(self):
        return self.name


@unique
class MappingMethod(str, Enum):
    """Enum to contain possible values for risk mapping methods"""

    SEMANTIC = "SEMANTIC"
    INFERENCE = "INFERENCE"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.name, cls))

    def __str__(self):
        return self.name


@unique
class BackendType(StrEnum):
    """LLM Inference backend types."""

    DEFAULT = auto()
    MELLEA = auto()
