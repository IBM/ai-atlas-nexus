from abc import ABC, abstractmethod
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, TypeAdapter, ValidationError

from ai_atlas_nexus.blocks.inference.backend import InferenceBackendFactory
from ai_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    MelleaInferenceParams,
    OllamaInferenceEngineParams,
    OpenAIChatCompletionMessageParam,
    RITSInferenceEngineParams,
    TextGenerationInferenceOutput,
    VLLMInferenceEngineParams,
    WMLInferenceEngineParams,
)
from ai_atlas_nexus.metadata_base import BackendType, InferenceEngineType
from ai_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)


class InferenceEngine(ABC):

    _backend_type = BackendType.DEFAULT

    def __init__(
        self,
        model_name_or_path: str,
        credentials: Optional[Union[Dict, InferenceEngineCredentials]] = None,
        parameters: Optional[
            Union[
                RITSInferenceEngineParams,
                WMLInferenceEngineParams,
                OllamaInferenceEngineParams,
                VLLMInferenceEngineParams,
            ]
        ] = None,
        backend: Optional[Literal["default", "mellea"]] = "default",
        concurrency_limit: int = 10,
    ):
        """Create an instance of the InferenceEngine using the `model_name_or_path` and chosen LLM service.

        Args:
            model_name_or_path (str): model name or path as per the LLM model service
            credentials (Optional[Union[Dict, InferenceEngineCredentials]], optional): credentials for the inference engine instance. Defaults to None.
            parameters (Optional[ Union[ RITSInferenceEngineParams, WMLInferenceEngineParams, OllamaInferenceEngineParams, VLLMInferenceEngineParams, ] ], optional): parameters to use during request generation. Defaults to None.
            concurrency_limit (int, optional): No of parallel calls to be made to the LLM service. Defaults to 10.
        """

        self.model_name_or_path = model_name_or_path
        self.credentials = self.prepare_credentials(credentials or {})
        self.parameters = self._check_if_parameters_are_valid(parameters or {})
        self.concurrency_limit = concurrency_limit

        # Create inference client
        self.client = self.create_client()

        # Health check
        try:
            self.ping()
        except Exception as e:
            raise Exception(
                f"Failed to create `{self.__class__.__name__}`. Reason: {str(e)}"
            )

        if backend == BackendType.DEFAULT:
            self.backend = self
        else:
            assert self._inference_engine_type in [
                InferenceEngineType.OLLAMA,
                InferenceEngineType.WML,
                InferenceEngineType.RITS,
            ], f"[{backend}] backend is not currently supported for {self._inference_engine_type}. Supported inference engines: OLLAMA, WML, RITS"

            # Create inference backend
            self.backend = InferenceBackendFactory.create_backend(
                BackendType(backend),
                self._inference_engine_type,
                self.model_name_or_path,
                self.credentials,
                self.parameters,
            )

        logger.info(
            f"✓ Created {self._inference_engine_type} inference engine for model: {model_name_or_path}, backend - {backend.upper()}"
        )

    def _check_if_parameters_are_valid(self, parameters):
        if parameters:
            invalid_params = []
            for param_key, _ in parameters.items():
                if param_key not in list(
                    self._inference_engine_parameter_class.__annotations__
                ):
                    invalid_params.append(param_key)

            if len(invalid_params) > 0:
                raise Exception(
                    f"Invalid parameters found: {invalid_params}. {self._inference_engine_type} inference engine only supports {list(self._inference_engine_parameter_class.__annotations__)}"
                )

        return parameters

    def _to_openai_format(self, messages: Union[OpenAIChatCompletionMessageParam, str]):
        if isinstance(messages, str):
            return [{"role": "user", "content": messages}]

        try:
            if TypeAdapter(OpenAIChatCompletionMessageParam).validate_python(messages):
                return messages
        except:
            raise Exception(
                f"Invalid input message format. Please use openai format or plain str."
            )

    def _validate_chat_messages(self, messages):
        try:
            if isinstance(messages, str) or TypeAdapter(
                OpenAIChatCompletionMessageParam
            ).validate_python(messages):
                return [messages]
        except ValidationError:
            try:
                if isinstance(messages[0], str) or TypeAdapter(
                    OpenAIChatCompletionMessageParam
                ).validate_python(messages[0]):
                    return messages
            except ValidationError:
                raise Exception(
                    "Input should be of valid type: str, List[str], OpenAIChatCompletionMessageParam, List[OpenAIChatCompletionMessageParam]"
                )

    def ping(self):
        # Implement inference engine specific ping in their respective class.
        pass

    def format(self, response_format: Union[Dict, BaseModel]):
        if response_format is None:
            return None
        elif isinstance(response_format, Dict):
            return response_format
        elif isinstance(response_format, type(BaseModel)):
            return response_format.model_json_schema()
        else:
            raise Exception(f"Invalid response format type: {response_format}")

    @abstractmethod
    def prepare_credentials(
        self,
        credentials: Union[Dict, InferenceEngineCredentials],
    ) -> InferenceEngineCredentials:
        raise NotImplementedError

    @abstractmethod
    def create_client(self, credentials: InferenceEngineCredentials) -> Any:
        raise NotImplementedError

    @abstractmethod
    def generate(
        self,
        prompts: Union[List[str], List[MelleaInferenceParams]],
        response_format=None,
        postprocessors: List[str] = None,
        verbose=True,
    ) -> List[TextGenerationInferenceOutput]:
        raise NotImplementedError

    @abstractmethod
    def chat(
        self,
        messages: Union[
            str,
            List[str],
            OpenAIChatCompletionMessageParam,
            List[OpenAIChatCompletionMessageParam],
        ],
        tools=None,
        response_format=None,
        postprocessors: List[str] = None,
        verbose=True,
    ) -> List[TextGenerationInferenceOutput]:
        raise NotImplementedError
