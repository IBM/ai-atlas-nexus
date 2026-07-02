import os
from functools import partial
from typing import Dict, List, Union

from dotenv import load_dotenv
from openai import OpenAI

from ai_atlas_nexus.blocks.inference.base import InferenceEngine
from ai_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    MelleaInferenceParams,
    OpenAIChatCompletionMessageParam,
    TextGenerationInferenceOutput,
    VLLMInferenceEngineParams,
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


def _extract_logprobs(logprobs):
    """Extract logprobs from vllm response format into a simple token->logprob dict."""
    if not logprobs:
        return None

    result = {}
    for prob in logprobs:
        logprob_obj = list(prob.values())[0]
        result[logprob_obj.decoded_token] = logprob_obj.logprob
    return result


class VLLMInferenceEngine(InferenceEngine):

    _inference_engine_type = InferenceEngineType.VLLM
    _inference_engine_parameter_class = VLLMInferenceEngineParams

    def prepare_credentials(
        self, credentials: Union[Dict, InferenceEngineCredentials]
    ) -> InferenceEngineCredentials:
        api_url = None
        if credentials:
            api_url = credentials.get(
                "api_url",
                os.environ.get(f"{self._inference_engine_type}_API_URL", None),
            )
            assert api_url, (
                f"To run {self._inference_engine_type} in offline mode, passed `credentials` must be None. To run in server mode, "
                f"pass only the `api_url` to credentials or set the env variable: '{self._inference_engine_type}_API_URL'"
            )

            logger.info(
                f"Detected {self._inference_engine_type} api url. {self._inference_engine_type} engine will execute requests on the server at {api_url}."
            )

            api_key = credentials.get(
                "api_key",
                os.environ.get(f"{self._inference_engine_type}_API_KEY", None),
            )

            return InferenceEngineCredentials(api_url=api_url, api_key=api_key)
        else:
            logger.info(
                f"Running {self._inference_engine_type} in offline mode. The model `{self.model_name_or_path}` will be downloaded if not available offline."
            )
            return None

    def create_client(self):
        if self.credentials:
            return OpenAI(
                api_key=(
                    self.credentials["api_key"] if self.credentials["api_key"] else "-"
                ),
                base_url=f"{self.credentials['api_url']}/v1",
            )
        else:
            from vllm import LLM

            return LLM(
                model=self.model_name_or_path,
                trust_remote_code=True,
                gpu_memory_utilization=self.parameters.pop(
                    "gpu_memory_utilization", 0.92
                ),
                max_model_len=self.parameters.pop("max_model_len", None),
            )

    def ping(self):
        if isinstance(self.client, OpenAI) and self.model_name_or_path not in [
            model.id for model in self.client.models.list().data
        ]:
            raise Exception(
                f"Model `{self.model_name_or_path}` not found. Please download it first."
            )

    @postprocess
    def generate(
        self,
        prompts: Union[List[str], List[MelleaInferenceParams]],
        response_format=None,
        postprocessors: List[str] = None,
        verbose=True,
    ):
        try:
            if isinstance(self.client, OpenAI):
                return [
                    self._prepare_prediction_output(response, offline=False)
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
            else:
                from vllm import SamplingParams
                from vllm.sampling_params import StructuredOutputsParams

                if response_format:
                    self.parameters.update(
                        {
                            "structured_outputs": StructuredOutputsParams(
                                json=self.format(response_format)
                            )
                        }
                    )
                return [
                    self._prepare_prediction_output(response)
                    for response in self.client.generate(
                        prompts=prompts,
                        sampling_params=SamplingParams(**self.parameters),
                        use_tqdm=verbose,
                    )
                ]
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
    ):
        try:
            if isinstance(self.client, OpenAI):
                return [
                    self._prepare_prediction_output(response, offline=False)
                    for response in run_parallel(
                        func=partial(
                            unwrap_arguments_and_call_func,
                            partial(
                                self.backend.generate_chat_response,
                                response_format,
                                tools,
                            ),
                        ),
                        items=self._validate_chat_messages(messages),
                        desc=f"Inferring with {self._inference_engine_type}, backend - {self.backend._backend_type.upper()}",
                        concurrency_limit=self.concurrency_limit,
                        verbose=verbose,
                    )
                ]
            else:
                from vllm import SamplingParams
                from vllm.sampling_params import StructuredOutputsParams

                if response_format:
                    self.parameters.update(
                        {
                            "structured_outputs": StructuredOutputsParams(
                                json=self.format(response_format)
                            )
                        }
                    )
                return [
                    self._prepare_prediction_output(response)
                    for response in self.client.chat(
                        messages=[
                            self._to_openai_format(message) for message in messages
                        ],
                        sampling_params=SamplingParams(**self.parameters),
                        use_tqdm=verbose,
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

    def _prepare_prediction_output(self, response, offline=True):
        if isinstance(response, str):
            prediction_data = {"prediction": response}
        elif offline:
            prediction_data = {
                "prediction": response.outputs[0].text,
                "input_text": response.prompt,
                "output_tokens": len(response.outputs[0].token_ids),
                "stop_reason": response.outputs[0].finish_reason,
                "logprobs": _extract_logprobs(response.outputs[0].logprobs),
            }
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
                    "name": "JSON_schema",
                    "schema": response_format,
                },
            }
        else:
            return None
