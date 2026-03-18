import os
from functools import partial
from typing import Any, Dict, List, Optional, Union

from dotenv import load_dotenv

from ai_atlas_nexus.blocks.inference.base import InferenceEngine
from ai_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    OpenAIChatCompletionMessageParam,
    TextGenerationInferenceOutput,
    WMLInferenceEngineParams,
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


class WMLInferenceEngine(InferenceEngine):

    _inference_engine_type = InferenceEngineType.WML
    _inference_engine_parameter_class = WMLInferenceEngineParams

    def prepare_credentials(
        self, credentials: Union[Dict, InferenceEngineCredentials]
    ) -> InferenceEngineCredentials:
        api_key = credentials.get(
            "api_key", os.environ.get(f"{self._inference_engine_type}_API_KEY", None)
        )
        assert api_key, (
            f"Error while trying to create {self._inference_engine_type}. "
            f"Please set the env variable: '{self._inference_engine_type}_API_KEY' or pass api_key to credentials."
        )

        api_url = credentials.get(
            "api_url", os.environ.get(f"{self._inference_engine_type}_API_URL", None)
        )
        assert api_url, (
            f"Error while trying to create {self._inference_engine_type}. "
            f"Please set the env variable: '{self._inference_engine_type}_API_URL' or pass api_url to credentials."
        )

        space_id = credentials.get(
            "space_id",
            os.environ.get(f"{self._inference_engine_type}_SPACE_ID", None),
        )

        project_id = credentials.get(
            "project_id",
            os.environ.get(f"{self._inference_engine_type}_PROJECT_ID", None),
        )

        if not (space_id or project_id):
            raise ValueError(
                "Error while trying to create {self._inference_engine_type} inference engine. "
                "Either 'space_id' or 'project_id' need to be specified when using WMLInferenceEngine. "
                f"Please set the env variable: '{self._inference_engine_type}_SPACE_ID'/'{self._inference_engine_type}_PROJECT_ID' "
                "or pass space_id/project_id to credentials.",
            )
        elif space_id and project_id:
            logger.warning(
                "Either 'space_id' or 'project_id' need to be "
                "specified, however, both were found. 'WMLInferenceEngine' "
                "will use space_id by default."
            )

        return InferenceEngineCredentials(
            api_key=api_key, api_url=api_url, space_id=space_id, project_id=project_id
        )

    def create_client(self):
        from ibm_watsonx_ai import APIClient
        from ibm_watsonx_ai.foundation_models import ModelInference

        client = APIClient(
            {
                "url": self.credentials["api_url"],
                "apikey": self.credentials["api_key"],
            }
        )
        if self.credentials["space_id"]:
            client.set.default_space(self.credentials["space_id"])
        else:
            client.set.default_project(self.credentials["project_id"])

        # self.parameters.update(
        #     {"response_format": self._create_schema_format(response_format)}
        # )
        return ModelInference(
            model_id=self.model_name_or_path, api_client=client, params=self.parameters
        )

    def ping(self):
        # ping is handled by the APIClient class internally.
        pass

    @postprocess
    def generate(
        self,
        prompts: List[str],
        response_format=None,
        postprocessors=None,
        verbose=True,
    ) -> List[TextGenerationInferenceOutput]:
        responses = []

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

    def generate_text(
        self, response_format, prompt: str
    ) -> List[TextGenerationInferenceOutput]:
        for response in self.client.generate(
            prompt=[prompt],
            params=self.parameters,
            concurrency_limit=self.concurrency_limit,
        ):
            return response

    @postprocess
    def chat(
        self,
        messages: Union[OpenAIChatCompletionMessageParam, str],
        tools=None,
        response_format=None,
        postprocessors=None,
        verbose=True,
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
                    items=[messages],
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
            messages=self._to_openai_format(messages),
            params=self.parameters,
        )

    def _prepare_prediction_output(
        self, response
    ) -> List[TextGenerationInferenceOutput]:
        _CHAT_API = True if "choices" in response else False
        if _CHAT_API:
            prediction_data = {
                "prediction": response["choices"][0]["message"]["content"],
                "input_tokens": response["usage"]["prompt_tokens"],
                "output_tokens": response["usage"]["completion_tokens"],
                "stop_reason": response["choices"][0]["finish_reason"],
            }
        else:
            prediction_data = {
                "prediction": response["results"][0]["generated_text"],
                "input_tokens": response["results"][0]["input_token_count"],
                "output_tokens": response["results"][0]["generated_token_count"],
                "stop_reason": response["results"][0]["stop_reason"],
            }

        return TextGenerationInferenceOutput(
            model_name_or_path=self.model_name_or_path,
            inference_engine=str(self._inference_engine_type),
            **prediction_data,
        )
