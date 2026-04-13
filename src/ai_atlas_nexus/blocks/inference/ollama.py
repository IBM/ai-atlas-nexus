import os
from functools import partial
from typing import Any, Dict, List, Literal, Union

from dotenv import load_dotenv

from ai_atlas_nexus.blocks.inference.base import InferenceEngine
from ai_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    MelleaInferenceParams,
    OllamaInferenceEngineParams,
    OpenAIChatCompletionMessageParam,
    TextGenerationInferenceOutput,
)
from ai_atlas_nexus.blocks.inference.postprocessing import postprocess
from ai_atlas_nexus.exceptions import RiskInferenceError
from ai_atlas_nexus.metadata_base import InferenceEngineType
from ai_atlas_nexus.toolkit.job_utils import (
    run_parallel,
    unwrap_arguments_and_call_func,
)
from ai_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)

# load .env file to environment
load_dotenv()


class OllamaInferenceEngine(InferenceEngine):

    _inference_engine_type = InferenceEngineType.OLLAMA
    _inference_engine_parameter_class = OllamaInferenceEngineParams

    def prepare_credentials(
        self, credentials: Union[Dict, InferenceEngineCredentials]
    ) -> InferenceEngineCredentials:
        api_url = credentials.get(
            "api_url",
            os.environ.get(f"{self._inference_engine_type}_API_URL", None),
        )
        assert api_url, (
            f"Error while trying to run {self._inference_engine_type}. "
            f"Please pass api_url to credentials or set the env variable: '{self._inference_engine_type}_API_URL'"
        )

        if api_url:
            logger.debug(
                f"{self._inference_engine_type} inference engine will execute requests on the server at {api_url}."
            )

        return InferenceEngineCredentials(api_url=api_url)

    def create_client(self):
        from ollama import Client

        return Client(host=self.credentials["api_url"])

    def ping(self):
        try:
            self.client.ps()
        except ConnectionError:
            raise Exception(
                f"Ollama server not running at {self.credentials["api_url"]}"
            )

        if self.model_name_or_path not in [
            model.model for model in self.client.list().models
        ]:
            raise Exception(
                f"Model `{self.model_name_or_path}` not found. Please download it first."
            )

        if "think" in self.parameters and self.parameters["think"]:
            if not "thinking" in self.client.show(self.model_name_or_path).capabilities:
                raise Exception(
                    f"`Model {self.model_name_or_path}` does not support thinking. Please pass `think=False` or pass a supported model."
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
                self._prepare_prediction_output(response)
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
        return self.client.generate(
            model=self.model_name_or_path,
            prompt=prompt,
            format=self.format(response_format),
            logprobs=self.parameters.get("logprobs", None),
            top_logprobs=self.parameters.get("top_logprobs", None),
            think=self.parameters.get("think", None),
            options={
                k: v
                for k, v in self.parameters.items()
                if (k not in ["logprobs", "top_logprobs", "think"])
            },  # https://github.com/ollama/ollama/blob/main/docs/modelfile.mdx#valid-parameters-and-values
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
        verbose: bool = True,
    ) -> TextGenerationInferenceOutput:
        try:
            return [
                self._prepare_prediction_output(response)
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

    def generate_chat_response(
        self, response_format, tools, messages
    ) -> List[TextGenerationInferenceOutput]:
        return self.client.chat(
            model=self.model_name_or_path,
            messages=self._to_openai_format(messages),
            tools=tools,
            format=self.format(response_format),
            logprobs=self.parameters.get("logprobs", None),
            top_logprobs=self.parameters.get("top_logprobs", None),
            think=self.parameters.get("think", None),
            options={
                k: v
                for k, v in self.parameters.items()
                if (k not in ["logprobs", "top_logprobs", "think"])
            },  # https://github.com/ollama/ollama/blob/main/docs/modelfile.mdx#valid-parameters-and-values
        )

    def _prepare_prediction_output(self, response):
        if isinstance(response, str):
            prediction_data = {"prediction": response}
        else:
            prediction_data = {
                "prediction": getattr(
                    response,
                    "response",
                    getattr(getattr(response, "message", response), "content", None),
                ),
                "input_tokens": getattr(response, "prompt_eval_count", None),
                "output_tokens": getattr(response, "eval_count", None),
                "stop_reason": getattr(response, "done_reason", None),
                "thinking": getattr(
                    response,
                    "thinking",
                    getattr(getattr(response, "message", response), "thinking", None),
                ),
                "logprobs": (
                    {output.token: output.logprob for output in response.logprobs}
                    if hasattr(response, "logprobs") and response.logprobs
                    else None
                ),
            }
        return TextGenerationInferenceOutput(
            model_name_or_path=self.model_name_or_path,
            inference_engine=str(self._inference_engine_type),
            **prediction_data,
        )
