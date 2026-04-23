import os
from functools import partial
from typing import Dict, List, Union

import httpx
from dotenv import load_dotenv
from openai import (
    APIConnectionError,
    AuthenticationError,
    NotFoundError,
    PermissionDeniedError,
)

from ai_atlas_nexus.blocks.inference.base import InferenceEngine
from ai_atlas_nexus.blocks.inference.params import (
    HFInferenceEngineParams,
    InferenceEngineCredentials,
    MelleaInferenceParams,
    OpenAIChatCompletionMessageParam,
    TextGenerationInferenceOutput,
)
from ai_atlas_nexus.blocks.inference.postprocessing import postprocess
from ai_atlas_nexus.exceptions import InferenceError
from ai_atlas_nexus.metadata_base import InferenceEngineType
from ai_atlas_nexus.toolkit.job_utils import (
    run_parallel,
    unwrap_arguments_and_call_func,
)
from ai_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)

# load .env file to environment
load_dotenv()

DEFAULT_HF_API_URL = "https://router.huggingface.co/v1"


class HFInferenceEngine(InferenceEngine):
    """Inference engine for HuggingFace Inference Providers.

    Uses the OpenAI-compatible API exposed by HuggingFace's inference router.
    Supports org-level billing via the ``X-HF-Bill-To`` header.

    Environment variables:
        HF_TOKEN: HuggingFace API token (required).
        HF_API_URL: API base URL (default: https://router.huggingface.co/v1).
        HF_ORG: Organization to bill (optional, sets X-HF-Bill-To header).
    """

    _inference_engine_type = InferenceEngineType.HF
    _inference_engine_parameter_class = HFInferenceEngineParams

    def prepare_credentials(
        self, credentials: Union[Dict, InferenceEngineCredentials]
    ) -> InferenceEngineCredentials:
        api_key = credentials.get(
            "api_key", os.environ.get("HF_TOKEN", None)
        )
        assert api_key, (
            f"Error while trying to run {self._inference_engine_type}. "
            f"Please set the env variable: 'HF_TOKEN' or pass api_key to credentials."
        )

        api_url = credentials.get(
            "api_url", os.environ.get("HF_API_URL", DEFAULT_HF_API_URL)
        )

        org_id = credentials.get(
            "org_id", os.environ.get("HF_ORG", None)
        )

        return InferenceEngineCredentials(
            api_key=api_key, api_url=api_url, org_id=org_id
        )

    def create_client(self):
        from openai import OpenAI

        default_headers = {}
        if self.credentials.get("org_id"):
            default_headers["X-HF-Bill-To"] = self.credentials["org_id"]

        return OpenAI(
            api_key=self.credentials["api_key"],
            base_url=self.credentials["api_url"],
            default_headers=default_headers,
            timeout=httpx.Timeout(None, connect=5.0),
        )

    def ping(self):

        try:
            available_models = [model.id for model in self.client.models.list().data]
        except (NotFoundError, APIConnectionError):
            raise Exception("Connection error. Please check HF API URL.")
        except (AuthenticationError, PermissionDeniedError):
            raise Exception("Authentication failed. Invalid HF_TOKEN.")

        if self.model_name_or_path not in available_models:
            raise Exception(
                f"Model `{self.model_name_or_path}` not found or not available for inference on HuggingFace."
            )

    @postprocess
    def generate(
        self,
        prompts: Union[List[str], List[MelleaInferenceParams]],
        response_format=None,
        postprocessors: List[str] = None,
        verbose=True,
    ) -> List[TextGenerationInferenceOutput]:
        try:
            return [
                self._prepare_chat_output(response)
                for response in run_parallel(
                    func=partial(
                        unwrap_arguments_and_call_func,
                        partial(self.backend.generate_text, response_format),
                    ),
                    items=prompts,
                    desc=f"Inferring with {self._inference_engine_type}, backend - {self.backend._backend_type.upper()}",
                    concurrency_limit=self.concurrency_limit,
                    verbose=verbose,
                )
            ]
        except (AuthenticationError, PermissionDeniedError) as e:
            raise InferenceError("Authentication failed. Invalid HF_TOKEN.")
        except Exception as e:
            raise InferenceError(str(e))

    def generate_text(self, response_format, prompt):
        return self.client.chat.completions.create(
            messages=self._to_openai_format(prompt),
            model=self.model_name_or_path,
            response_format=self._create_schema_format(self.format(response_format)),
            **self.parameters,
        )

    @postprocess
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
    ) -> TextGenerationInferenceOutput:
        try:
            return [
                self._prepare_chat_output(response)
                for response in run_parallel(
                    func=partial(
                        unwrap_arguments_and_call_func,
                        partial(
                            self.backend.generate_chat_response, response_format, tools
                        ),
                    ),
                    items=self._validate_chat_messages(messages),
                    desc=f"Inferring with {self._inference_engine_type}, backend - {self.backend._backend_type.upper()}",
                    concurrency_limit=self.concurrency_limit,
                    verbose=verbose,
                )
            ]
        except (AuthenticationError, PermissionDeniedError) as e:
            raise InferenceError("Authentication failed. Invalid HF_TOKEN.")
        except Exception as e:
            raise InferenceError(str(e))

    def generate_chat_response(self, response_format, tools, messages):
        return self.client.chat.completions.create(
            messages=self._to_openai_format(messages),
            model=self.model_name_or_path,
            tools=tools,
            response_format=self._create_schema_format(self.format(response_format)),
            **self.parameters,
        )

    def _prepare_chat_output(self, response):
        if isinstance(response, str):
            prediction_data = {"prediction": response}
        else:
            prediction_data = {
                "prediction": response.choices[0].message.content,
                "input_tokens": response.usage.total_tokens,
                "output_tokens": response.usage.completion_tokens,
                "stop_reason": response.choices[0].finish_reason,
                "logprobs": (
                    {
                        output.token: output.logprob
                        for output in response.choices[0].logprobs.content
                    }
                    if response.choices[0].logprobs
                    else None
                ),
            }

        return TextGenerationInferenceOutput(
            model_name_or_path=self.model_name_or_path,
            inference_engine=str(self._inference_engine_type),
            **prediction_data,
        )

    def _create_schema_format(self, response_format):
        if response_format:
            return {
                "type": "json_schema",
                "json_schema": {
                    "name": "response_schema",
                    "schema": response_format,
                },
            }
        else:
            return None
