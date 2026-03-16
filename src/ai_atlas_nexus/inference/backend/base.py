from abc import ABC, abstractmethod
from typing import Any, Dict


class InferenceBackend(ABC):
    """Abstract base class for Inference backends."""

    @abstractmethod
    def initialize(
        self,
        inference_service: str,
        model_name_or_path: str,
        credentials: Dict[str, str],
        llm_parameters: Dict,
    ) -> Any:
        """Initialize Mellea backend with the provided inference service."""
        pass

    @abstractmethod
    def generate_text(self, **kwargs) -> str:
        """Generate a response from the backend."""
        pass

    @abstractmethod
    def generate_chat_response(self, **kwargs) -> str:
        """Generate a chat response from the backend."""
        pass
