import json
import os
import re
from functools import partial
from typing import Dict, List, Union

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

# Key used when wrapping a root-array schema in an object envelope for the
# OpenAI-compatible response_format field.
_ARRAY_WRAP_KEY = "items"


class AWSBedrockInferenceEngine(InferenceEngine):
    """Inference engine for AWS Bedrock (openai.* models via invoke_model).

    Supports ``openai.*`` models using ``invoke_model`` with a full OpenAI-compatible JSON body,
    supporting all OpenAI parameters (``seed``, ``reasoning_effort``, etc.).

    Environment variables (all optional when passed directly in credentials):
        AWS_ACCESS_KEY_ID: AWS access key ID.
        AWS_SECRET_ACCESS_KEY: AWS secret access key.
        AWS_DEFAULT_REGION: AWS region (default: ``us-east-1``).
    """

    _inference_engine_type = InferenceEngineType.BEDROCK
    _inference_engine_parameter_class = AWSBedrockInferenceEngineParams

    # Expose so tests can introspect the same constant.
    _ARRAY_WRAP_KEY = _ARRAY_WRAP_KEY

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
        import boto3
        return boto3.client("bedrock-runtime", **self._boto3_kwargs())

    def ping(self):
        import boto3
        import botocore.exceptions
        try:
            sts = boto3.client("sts", **self._boto3_kwargs())
            sts.get_caller_identity()
        except botocore.exceptions.ClientError as exc:
            raise Exception(
                f"Authentication failed. Invalid AWS_ACCESS_KEY_ID or AWS_SECRET_ACCESS_KEY - {exc}"
            )
        except botocore.exceptions.NoCredentialsError as exc:
            raise Exception(
                f"Authentication failed. AWS credentials not found - {exc}"
            )
        except botocore.exceptions.EndpointConnectionError as exc:
            raise Exception(f"Connection error - {exc}")

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
        """Delegate to the chat API — intentionally, not as a shortcut.

        `generate()` and `chat()` converge on the same
        `generate_chat_response` call because Bedrock doesn't expose a
        second, independent completion endpoint for the model families
        this engine supports: `converse` (native models) and the
        OpenAI-compatible `invoke_model` body (`openai.*` models) are both
        chat-shaped APIs, and AWS recommends `converse` over the legacy,
        per-model `invoke_model` payload precisely because it unifies
        single-turn and multi-turn requests behind one structure. A
        "generate" call here is simply a `converse`/`invoke_model` call
        with one user-role message and no history — there is no distinct
        Bedrock "generate" operation left to implement separately.
        """
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
    ) -> List[TextGenerationInferenceOutput]:
        try:
            return [
                self._prepare_chat_output(response)
                for response in run_parallel(
                    func=partial(
                        unwrap_arguments_and_call_func,
                        partial(self.backend.generate_chat_response, response_format, tools),
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
        if not self.model_name_or_path.startswith("openai."):
            raise NotImplementedError(
                f"Model `{self.model_name_or_path}` is not supported by the Bedrock inference engine. "
                "Only openai.* models are currently supported."
            )
        schema = self._create_schema_format(self.format(response_format))
        return self._invoke_openai_model(messages, schema, tools)

    def _invoke_openai_model(self, messages, schema=None, tools=None):
        """Call invoke_model with an OpenAI-compatible JSON body.

        Supports the full parameter set (seed, reasoning_effort, etc.).
        """
        openai_messages = self._to_openai_format(messages)
        body = {"model": self.model_name_or_path, "messages": openai_messages}
        body.update({k: v for k, v in self.parameters.items() if v is not None})
        if schema is not None:
            body["response_format"] = schema
        if tools is not None:
            body["tools"] = tools
        response = self.client.invoke_model(
            modelId=self.model_name_or_path,
            body=json.dumps(body),
            contentType="application/json",
            accept="application/json",
        )
        return json.loads(response["body"].read())

    def _prepare_chat_output(self, response):
        if isinstance(response, str):
            prediction_data = {"prediction": response}
        elif "choices" in response:
            # OpenAI-compatible response
            choice = response["choices"][0]
            content = choice["message"]["content"]
            usage = response.get("usage", {})
            prediction_data = {
                "prediction": content,
                "input_tokens": usage.get("prompt_tokens"),
                "output_tokens": usage.get("completion_tokens"),
                "stop_reason": choice.get("finish_reason"),
                "seed": getattr(self, "parameters", {}).get("seed"),
            }
        else:
            raise ValueError(f"Unexpected response format from Bedrock: {response}")
        content = prediction_data["prediction"]
        if content:
            # If the model returned noise around the JSON (e.g. a Python list-repr or
            # a <reasoning> prefix), extract the first {...} block before parsing.
            parsed = None
            try:
                parsed = json.loads(content)
            except (json.JSONDecodeError, TypeError):
                m = re.search(r"\{.*\}", content, flags=re.DOTALL)
                if m:
                    try:
                        parsed = json.loads(m.group(0))
                    except (json.JSONDecodeError, TypeError):
                        pass
            if isinstance(parsed, dict) and list(parsed.keys()) == [self._ARRAY_WRAP_KEY]:
                prediction_data["prediction"] = json.dumps(parsed[self._ARRAY_WRAP_KEY])
            elif parsed is not None and not isinstance(parsed, str):
                prediction_data["prediction"] = json.dumps(parsed)

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
                "name": "Bedrock_Schema",
                "schema": schema,
                "strict": True,
            },
        }
