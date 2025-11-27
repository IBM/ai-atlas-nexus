from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

import pydantic
import requests

from ai_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    OllamaInferenceEngineParams,
    OpenAIChatCompletionMessageParam,
    RITSInferenceEngineParams,
    TextGenerationInferenceOutput,
    VLLMInferenceEngineParams,
    WMLInferenceEngineParams,
)
from ai_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)


class InferenceEngine(ABC):

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
        think: Optional[bool] = None,
        concurrency_limit: int = 10,
    ):
        """Create an instance of the InferenceEngine using the `model_name_or_path` and chosen LLM service.

        Args:
            model_name_or_path (str): model name or path as per the LLM model service
            credentials (Optional[Union[Dict, InferenceEngineCredentials]], optional): credentials for the inference engine instance. Defaults to None.
            parameters (Optional[ Union[ RITSInferenceEngineParams, WMLInferenceEngineParams, OllamaInferenceEngineParams, VLLMInferenceEngineParams, ] ], optional): parameters to use during request generation. Defaults to None.
            think (Optional[bool], optional): enable or disable model thinking. Currently, only supported in Ollama. Defaults to None.
            concurrency_limit (int, optional): No of parallel calls to be made to the LLM service. Defaults to 10.
        """

        self.model_name_or_path = model_name_or_path
        self.credentials = self.prepare_credentials(credentials or {})
        self.parameters = self._check_if_parameters_are_valid(parameters or {})
        self.think = think
        self.concurrency_limit = concurrency_limit

        # Create inference client
        self.client = self.create_client(self.credentials)

        # Health check
        try:
            self.ping()
        except Exception as e:
            raise Exception(
                f"Failed to create `{self.__class__.__name__}`. Reason: {str(e)} Given API credentials: {self.credentials}"
            )

        # Verify whether the inference engine and the model type support `thinking`.
        if think:
            self.is_thinking_supported()

        logger.info(f"Created {self._inference_engine_type} inference engine.")

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

    def _to_openai_format(self, prompt: Union[OpenAIChatCompletionMessageParam, str]):
        if isinstance(prompt, str):
            return [{"role": "user", "content": prompt}]
        elif pydantic.TypeAdapter(OpenAIChatCompletionMessageParam).validate_python(
            prompt
        ):
            return prompt
        else:
            raise Exception(
                f"Invalid input format: {prompt}. Please use openai format or plain str."
            )

    def ping(self):
        # Implement inference engine specific ping in their respective class.
        pass

    def is_thinking_supported(self):
        raise Exception(
            f"Currently, model thinking (think=True) is only supported in OllamaInferenceEngine."
        )

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
        prompts: List[str],
        response_format=None,
        postprocessors=None,
        verbose=True,
    ) -> List[TextGenerationInferenceOutput]:
        raise NotImplementedError

    @abstractmethod
    def chat(
        self,
        messages: Union[
            List[OpenAIChatCompletionMessageParam],
            List[str],
        ],
        tools=None,
        response_format=None,
        postprocessors=None,
        verbose=True,
    ) -> List[TextGenerationInferenceOutput]:
        raise NotImplementedError
