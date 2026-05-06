from ai_atlas_nexus.blocks.inference.backend.base import InferenceBackend
from ai_atlas_nexus.blocks.inference.backend.mellea import MelleaInferenceBackend
from ai_atlas_nexus.metadata_base import BackendType


class InferenceBackendFactory:

    @classmethod
    def create_backend(cls, backend: BackendType, *args, **kwargs) -> InferenceBackend:
        """Create an inference backend interface for the given backend type.

        Args:
            backend (BackendType): A backend interface to execute the LLM inference requests.

        Returns:
            InferenceBackend: Creates a new InferenceBackend.
        """
        if backend == BackendType.MELLEA:
            return MelleaInferenceBackend.initialize(*args, **kwargs)
