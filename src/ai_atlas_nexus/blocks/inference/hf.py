import os
from typing import Dict, List, Union

import httpx
from dotenv import load_dotenv
from openai import BadRequestError, NotFoundError

from ai_atlas_nexus.blocks.inference.base import InferenceEngine
from ai_atlas_nexus.blocks.inference.params import (
    HFInferenceEngineParams,
    InferenceEngineCredentials,
    OpenAIChatCompletionMessageParam,
    TextGenerationInferenceOutput,
)
from ai_atlas_nexus.blocks.inference.postprocessing import postprocess
from ai_atlas_nexus.exceptions import RiskInferenceError
from ai_atlas_nexus.metadata_base import InferenceEngineType
from ai_atlas_nexus.toolkit.job_utils import run_parallel


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

    def create_client(self, credentials):
        from openai import OpenAI

        default_headers = {}
        if credentials.get("org_id"):
            default_headers["X-HF-Bill-To"] = credentials["org_id"]

        return OpenAI(
            api_key=credentials["api_key"],
            base_url=credentials["api_url"],
            default_headers=default_headers,
            timeout=httpx.Timeout(None, connect=5.0),
        )

    def ping(self):
        # HF router may not support model listing; a lightweight
        # completions call would be expensive.  Accept silently.
        try:
            self.client.models.list()
        except NotFoundError:
            pass

    @postprocess
    def generate(
        self,
        prompts: List[str],
        response_format=None,
        postprocessors=None,
        verbose=True,
    ) -> List[TextGenerationInferenceOutput]:
        return self.chat(prompts, response_format, postprocessors, verbose)

    @postprocess
    def chat(
        self,
        messages: Union[
            List[OpenAIChatCompletionMessageParam],
            List[str],
        ],
        response_format=None,
        postprocessors=None,
        verbose=True,
    ) -> TextGenerationInferenceOutput:

        def chat_response(messages):
            response = self.client.chat.completions.create(
                messages=self._to_openai_format(messages),
                model=self.model_name_or_path,
                response_format=self._create_schema_format(response_format),
                **self.parameters,
            )
            return self._prepare_chat_output(response)

        try:
            return run_parallel(
                chat_response,
                messages,
                f"Inferring with {self._inference_engine_type}",
                self.concurrency_limit,
                verbose=verbose,
            )
        except BadRequestError as e:
            msg = e.body.get("message", str(e)) if isinstance(e.body, dict) else str(e)
            raise RiskInferenceError(msg)
        except Exception as e:
            raise RiskInferenceError(str(e))

    def _prepare_chat_output(self, response):
        return TextGenerationInferenceOutput(
            prediction=response.choices[0].message.content,
            input_tokens=response.usage.total_tokens,
            output_tokens=response.usage.completion_tokens,
            stop_reason=response.choices[0].finish_reason,
            model_name_or_path=self.model_name_or_path,
            logprobs=(
                {
                    output.token: output.logprob
                    for output in response.choices[0].logprobs.content
                }
                if response.choices[0].logprobs
                else None
            ),
            inference_engine=str(self._inference_engine_type),
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
