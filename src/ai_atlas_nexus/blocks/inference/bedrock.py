import json
import os
from functools import partial
from typing import Dict, List, Union

import boto3
from dotenv import load_dotenv

from ai_atlas_nexus.blocks.inference.base import InferenceEngine
from ai_atlas_nexus.blocks.inference.params import (
    AWSBedrockInferenceEngineParams,
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

load_dotenv()

# Key used when wrapping a root-array schema in an object envelope so that
# Bedrock's converse API accepts it (it rejects bare array schemas).
_ARRAY_WRAP_KEY = "items"


class AWSBedrockInferenceEngine(InferenceEngine):
    """Inference engine for AWS Bedrock.

    Routes to the appropriate Bedrock endpoint based on the model ID:

    - ``openai.*`` models → ``invoke_model`` with a full OpenAI-compatible
      JSON body, supporting all OpenAI parameters (``seed``, ``reasoning_effort``, etc.).
    - All other models (``amazon.*``, ``anthropic.*``, etc.) → ``converse``,
      which only accepts ``maxTokens``, ``temperature``, ``topP``, ``stopSequences``
      in ``inferenceConfig``.

    Environment variables (all optional when passed directly in credentials):
        AWS_ACCESS_KEY_ID: AWS access key ID.
        AWS_SECRET_ACCESS_KEY: AWS secret access key.
        AWS_DEFAULT_REGION: AWS region (default: ``us-east-1``).
    """

    _inference_engine_type = InferenceEngineType.BEDROCK
    _inference_engine_parameter_class = AWSBedrockInferenceEngineParams

    # Expose so tests can introspect the same constant.
    _ARRAY_WRAP_KEY = _ARRAY_WRAP_KEY

    # Parameters accepted by Bedrock's converse inferenceConfig.
    _CONVERSE_CONFIG_KEYS = frozenset({"maxTokens", "temperature", "topP", "stopSequences"})

    def prepare_credentials(
        self, credentials: Union[Dict, InferenceEngineCredentials]
    ) -> InferenceEngineCredentials:
        aws_access_key_id = credentials.get(
            "aws_access_key_id", os.environ.get("AWS_ACCESS_KEY_ID", None)
        )
        assert aws_access_key_id, (
            f"Error while trying to run {self._inference_engine_type}. "
            "Please set the env variable: 'AWS_ACCESS_KEY_ID' or pass aws_access_key_id to credentials."
        )

        aws_secret_access_key = credentials.get(
            "aws_secret_access_key", os.environ.get("AWS_SECRET_ACCESS_KEY", None)
        )
        assert aws_secret_access_key, (
            f"Error while trying to run {self._inference_engine_type}. "
            "Please set the env variable: 'AWS_SECRET_ACCESS_KEY' or pass aws_secret_access_key to credentials."
        )

        region_name = credentials.get(
            "region_name", os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
        )

        return InferenceEngineCredentials(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )

    def _boto3_kwargs(self):
        return {
            "aws_access_key_id": self.credentials["aws_access_key_id"],
            "aws_secret_access_key": self.credentials["aws_secret_access_key"],
            "region_name": self.credentials["region_name"],
        }

    def create_client(self):
        return boto3.client("bedrock-runtime", **self._boto3_kwargs())

    def ping(self):
        try:
            sts = boto3.client("sts", **self._boto3_kwargs())
            sts.get_caller_identity()
        except Exception as exc:
            error_str = str(exc)
            if "InvalidClientTokenId" in error_str or "AuthFailure" in error_str:
                raise Exception(
                    "Authentication failed. Invalid AWS_ACCESS_KEY_ID or AWS_SECRET_ACCESS_KEY."
                )
            raise Exception(f"Connection error. Please check AWS credentials. {error_str}")

        bedrock = boto3.client("bedrock", **self._boto3_kwargs())
        available_models = [
            m["modelId"]
            for m in bedrock.list_foundation_models()["modelSummaries"]
        ]
        if self.model_name_or_path not in available_models:
            raise Exception(
                f"Model `{self.model_name_or_path}` not found. Available - {available_models}"
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
                    items=self._validate_generate_prompts(prompts),
                    desc=f"Inferring with {self._inference_engine_type}, backend - {self.backend._backend_type.upper()}",
                    concurrency_limit=self.concurrency_limit,
                    verbose=verbose,
                )
            ]
        except Exception as e:
            raise InferenceError(str(e))

    def generate_text(self, response_format, prompt):
        return self.generate_chat_response(response_format, messages=prompt)

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
                        partial(self.backend.generate_chat_response, response_format),
                    ),
                    items=self._validate_chat_messages(messages),
                    desc=f"Inferring with {self._inference_engine_type}, backend - {self.backend._backend_type.upper()}",
                    concurrency_limit=self.concurrency_limit,
                    verbose=verbose,
                )
            ]
        except Exception as e:
            raise InferenceError(str(e))

    def _is_openai_model(self):
        return self.model_name_or_path.startswith("openai.")

    def generate_chat_response(self, response_format, messages):
        if self._is_openai_model():
            return self._invoke_openai_model(messages)
        return self._invoke_converse(messages)

    def _invoke_openai_model(self, messages):
        """Call invoke_model with an OpenAI-compatible JSON body.

        Supports the full parameter set (seed, reasoning_effort, etc.).
        """
        openai_messages = self._to_openai_format(messages)
        body = {"model": self.model_name_or_path, "messages": openai_messages}
        body.update({k: v for k, v in self.parameters.items() if v is not None})

        response = self.client.invoke_model(
            modelId=self.model_name_or_path,
            body=json.dumps(body),
            contentType="application/json",
            accept="application/json",
        )
        return json.loads(response["body"].read())

    def _invoke_converse(self, messages):
        """Call converse for native Bedrock models (amazon.*, anthropic.*, etc.)."""
        kwargs = {
            "modelId": self.model_name_or_path,
            "messages": self._to_bedrock_format(messages),
        }
        inference_config = {
            k: v for k, v in self.parameters.items()
            if v is not None and k in self._CONVERSE_CONFIG_KEYS
        }
        if inference_config:
            kwargs["inferenceConfig"] = inference_config
        return self.client.converse(**kwargs)

    def _to_bedrock_format(self, messages):
        """Convert a string or openai-format message list to Bedrock converse format."""
        if isinstance(messages, str):
            return [{"role": "user", "content": [{"text": messages}]}]

        bedrock_messages = []
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            if isinstance(content, str):
                bedrock_messages.append({"role": role, "content": [{"text": content}]})
            elif isinstance(content, list):
                # openai multi-part content: extract text parts
                text_parts = [
                    part["text"] for part in content if part.get("type") == "text"
                ]
                bedrock_messages.append(
                    {"role": role, "content": [{"text": " ".join(text_parts)}]}
                )
        return bedrock_messages

    def _prepare_chat_output(self, response):
        if isinstance(response, str):
            prediction_data = {"prediction": response}
        elif "choices" in response:
            # OpenAI-compatible response (e.g. openai.* models on Bedrock)
            choice = response["choices"][0]
            content = choice["message"]["content"]
            usage = response.get("usage", {})
            prediction_data = {
                "prediction": content,
                "input_tokens": usage.get("prompt_tokens"),
                "output_tokens": usage.get("completion_tokens"),
                "stop_reason": choice.get("finish_reason"),
            }
        else:
            # Native Bedrock converse response (e.g. amazon.*, anthropic.*, etc.)
            content_blocks = response["output"]["message"]["content"]
            text_block = next((b for b in content_blocks if "text" in b), None)
            content = text_block["text"] if text_block else ""
            usage = response.get("usage", {})
            prediction_data = {
                "prediction": content,
                "input_tokens": usage.get("inputTokens"),
                "output_tokens": usage.get("outputTokens"),
                "stop_reason": response.get("stopReason"),
            }

        content = prediction_data["prediction"]
        if content:
            try:
                parsed = json.loads(content)
                if isinstance(parsed, dict) and list(parsed.keys()) == [self._ARRAY_WRAP_KEY]:
                    prediction_data["prediction"] = json.dumps(parsed[self._ARRAY_WRAP_KEY])
            except (json.JSONDecodeError, TypeError):
                pass

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
        return schema
