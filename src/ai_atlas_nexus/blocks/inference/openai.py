import json
import os
from functools import partial
from typing import Dict, List, Union

import httpx
from dotenv import load_dotenv
from openai import (
    APIConnectionError,
    AuthenticationError,
    NotFoundError,
    OpenAI,
    PermissionDeniedError,
)

from ai_atlas_nexus.blocks.inference.base import InferenceEngine
from ai_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    MelleaInferenceParams,
    OpenAIChatCompletionMessageParam,
    OpenAIInferenceEngineParams,
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

load_dotenv()

DEFAULT_OPENAI_API_URL = "https://api.openai.com/v1"


class OpenAIInferenceEngine(InferenceEngine):
    """Inference engine for the OpenAI API.

    Uses the standard OpenAI Chat Completions endpoint.

    Environment variables:
        OPENAI_API_KEY: OpenAI API key (required).
        OPENAI_API_URL: API base URL (default: https://api.openai.com/v1).
    """

    _inference_engine_type = InferenceEngineType.OPENAI
    _inference_engine_parameter_class = OpenAIInferenceEngineParams

    # Key used when wrapping a root-array schema in an object envelope so that
    # OpenAI's structured-output API accepts it (it rejects bare array schemas).
    _ARRAY_WRAP_KEY = "items"

    def prepare_credentials(
        self, credentials: Union[Dict, InferenceEngineCredentials]
    ) -> InferenceEngineCredentials:
        api_key = credentials.get("api_key", os.environ.get("OPENAI_API_KEY", None))
        assert api_key, (
            f"Error while trying to run {self._inference_engine_type}. "
            f"Please set the env variable: 'OPENAI_API_KEY' or pass api_key to credentials."
        )

        api_url = credentials.get(
            "api_url", os.environ.get("OPENAI_API_URL", DEFAULT_OPENAI_API_URL)
        )

        return InferenceEngineCredentials(api_key=api_key, api_url=api_url)

    def create_client(self):
        api_url = self.credentials["api_url"].rstrip("/")
        if not api_url.endswith("/v1"):
            api_url = f"{api_url}/v1"
        return OpenAI(
            api_key=self.credentials["api_key"],
            base_url=api_url,
            timeout=httpx.Timeout(None, connect=5.0),
        )

    def ping(self):
        try:
            available_models = [model.id for model in self.client.models.list().data]
            if self.model_name_or_path not in available_models:
                raise Exception(
                    f"Model `{self.model_name_or_path}` not found. Available - {available_models}"
                )
        except APIConnectionError:
            raise Exception("Connection error. Please check OPENAI_API_URL.")
        except (AuthenticationError, PermissionDeniedError):
            raise Exception("Authentication failed. Invalid OPENAI_API_KEY.")
        except NotFoundError:
            raise Exception("Connection error. Please check OPENAI_API_URL.")

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
                    items=self._validate_generate_prompts(prompts),
                    desc=f"Inferring with {self._inference_engine_type}, backend - {self.backend._backend_type.upper()}",
                    concurrency_limit=self.concurrency_limit,
                    verbose=verbose,
                )
            ]
        except Exception as e:
            raise InferenceError(str(e))

    def generate_text(self, response_format, prompt):
        return self.generate_chat_response(response_format, tools=None, messages=prompt)

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
            content = response.choices[0].message.content
            if content:
                try:
                    parsed = json.loads(content)
                    if isinstance(parsed, dict) and list(parsed.keys()) == [self._ARRAY_WRAP_KEY]:
                        content = json.dumps(parsed[self._ARRAY_WRAP_KEY])
                except (json.JSONDecodeError, TypeError):
                    pass

            prediction_data = {
                "prediction": content,
                "input_tokens": response.usage.prompt_tokens,
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
        if not response_format:
            return None
        schema = response_format
        if schema.get("type") == "array":
            schema = {
                "type": "object",
                "properties": {self._ARRAY_WRAP_KEY: response_format},
                "required": [self._ARRAY_WRAP_KEY],
            }
        return {
            "type": "json_schema",
            "json_schema": {
                "name": "openai_schema",
                "schema": schema,
            },
        }
