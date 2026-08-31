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
    OPENAI = "openai"
    BEDROCK = "bedrock"

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


@unique
class ExplanationType(str, Enum):
    """Types of explanations to include with detected risks."""

    NONE = "none"
    DESCRIPTION = "description"  # Risk description from ontology
    REASONING = "reasoning"  # Model's thinking/reasoning if available
    SELF_EXPLANATION = "self-explanation"  # Explanation from model's response itself
