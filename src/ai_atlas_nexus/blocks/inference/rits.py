import os
from functools import partial
from typing import Dict, List, Union

import httpx
import pydantic
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
    RITSInferenceEngineParams,
    TextGenerationInferenceOutput,
)
from ai_atlas_nexus.blocks.inference.postprocessing import postprocess
from ai_atlas_nexus.exceptions import RiskInferenceError
from ai_atlas_nexus.metadata_base import InferenceEngineType
from ai_atlas_nexus.toolkit.job_utils import (
    run_parallel,
    unwrap_arguments_and_call_func,
)


# load .env file to environment
load_dotenv()


class RITSInferenceEngine(InferenceEngine):

    _inference_engine_type = InferenceEngineType.RITS
    _inference_engine_parameter_class = RITSInferenceEngineParams

    def prepare_credentials(
        self, credentials: Union[Dict, InferenceEngineCredentials]
    ) -> InferenceEngineCredentials:
        api_key = credentials.get(
            "api_key", os.environ.get(f"{self._inference_engine_type}_API_KEY", None)
        )
        assert api_key, (
            f"Error while trying to run {self._inference_engine_type}. "
            f"Please set the env variable: '{self._inference_engine_type}_API_KEY' or pass api_key to credentials."
        )

        api_url = credentials.get(
            "api_url", os.environ.get(f"{self._inference_engine_type}_API_URL", None)
        )
        assert api_url, (
            f"Error while trying to run {self._inference_engine_type}. "
            f"Please set the env variable: '{self._inference_engine_type}_API_URL' or pass api_url to credentials."
        )

        return InferenceEngineCredentials(api_key=api_key, api_url=api_url)

    def create_client(self):
        model_name_for_endpoint = (
            self.model_name_or_path.split("/")[-1].lower().replace(".", "-")
        )
        return OpenAI(
            api_key=self.credentials["api_key"],
            base_url=f"{self.credentials['api_url']}/{model_name_for_endpoint}/v1",
            default_headers={"RITS_API_KEY": self.credentials["api_key"]},
            timeout=httpx.Timeout(None, connect=1.0),
        )

    def ping(self):
        try:
            self.client.models.list()
        except APIConnectionError:
            raise Exception("Connection error. Please check RITS API URL.")
        except PermissionDeniedError:
            raise Exception("RITS authentication failed. Invalid RITS API KEY.")
        except NotFoundError:
            raise Exception(f"Model `{self.model_name_or_path}` not available.")

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
        except Exception as e:
            raise RiskInferenceError(str(e))

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
        except Exception as e:
            raise RiskInferenceError(str(e))

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
                    "name": "RITS_schema",
                    "schema": response_format,
                },
            }
        else:
            return None
