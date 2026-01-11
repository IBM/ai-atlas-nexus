import os
from typing import Dict, List, Optional, Union

from dotenv import load_dotenv

from ai_atlas_nexus.blocks.inference.base import InferenceEngine
from ai_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    OllamaInferenceEngineParams,
    OpenAIChatCompletionMessageParam,
    TextGenerationInferenceOutput,
)
from ai_atlas_nexus.blocks.inference.postprocessing import postprocess
from ai_atlas_nexus.exceptions import RiskInferenceError
from ai_atlas_nexus.metadata_base import InferenceEngineType
from ai_atlas_nexus.toolkit.job_utils import run_parallel
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
            logger.info(
                f"{self._inference_engine_type} inference engine will execute requests on the server at {api_url}."
            )

        return InferenceEngineCredentials(api_url=api_url)

    def create_client(self, credentials):
        from ollama import Client

        return Client(host=credentials["api_url"])

    def ping(self):
        if self.model_name_or_path not in [
            model.model for model in self.client.list().models
        ]:
            raise Exception(
                f"Model `{self.model_name_or_path}` not found. Please download it first."
            )

    def is_thinking_supported(self):
        if "thinking" in self.client.show(self.model_name_or_path).capabilities:
            return True
        else:
            raise Exception(
                f"`Model {self.model_name_or_path}` does not support thinking. Please pass `think=False` or use another model."
            )

    @postprocess
    def generate(
        self,
        prompts: List[str],
        response_format=None,
        postprocessors=None,
        verbose=True,
        **kwargs,
    ) -> List[TextGenerationInferenceOutput]:
        def generate_text(prompt: str):
            response = self.client.generate(
                model=self.model_name_or_path,
                prompt=prompt,
                format=response_format,
                logprobs=self.parameters.get("logprobs", None),
                top_logprobs=self.parameters.get("top_logprobs", None),
                options={
                    k: v
                    for k, v in self.parameters.items()
                    if (k != "logprobs" or k != "top_logprobs")
                },  # https://github.com/ollama/ollama/blob/main/docs/modelfile.mdx#valid-parameters-and-values
                think=self.think,
                **kwargs,
            )
            return self._prepare_prediction_output(response)

        try:
            return run_parallel(
                generate_text,
                prompts,
                f"Inferring with {self._inference_engine_type}",
                self.concurrency_limit,
                verbose=verbose,
            )
        except Exception as e:
            raise RiskInferenceError(str(e))

    @postprocess
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
        **kwargs,
    ) -> List[TextGenerationInferenceOutput]:

        def chat_response(messages):
            response = self.client.chat(
                model=self.model_name_or_path,
                messages=self._to_openai_format(messages),
                tools=tools,
                format=response_format,
                logprobs=self.parameters.get("logprobs", None),
                top_logprobs=self.parameters.get("top_logprobs", None),
                options={
                    k: v
                    for k, v in self.parameters.items()
                    if (k != "logprobs" or k != "top_logprobs")
                },  # https://github.com/ollama/ollama/blob/main/docs/modelfile.mdx#valid-parameters-and-values
                think=self.think,
                **kwargs,
            )
            return self._prepare_prediction_output(response)

        try:
            return run_parallel(
                chat_response,
                messages,
                f"Inferring with {self._inference_engine_type}",
                self.concurrency_limit,
                verbose=verbose,
            )
        except Exception as e:
            raise RiskInferenceError(str(e))

    def _prepare_prediction_output(self, response):
        return TextGenerationInferenceOutput(
            prediction=(
                response.message.content
                if hasattr(response, "message")
                else response.response
            ),
            input_tokens=response.prompt_eval_count,
            output_tokens=response.eval_count,
            stop_reason=response.done_reason,
            thinking=response.thinking if hasattr(response, "thinking") else None,
            model_name_or_path=self.model_name_or_path,
            logprobs=(
                {output.token: output.logprob for output in response.logprobs}
                if response.logprobs
                else None
            ),
            inference_engine=str(self._inference_engine_type),
        )
