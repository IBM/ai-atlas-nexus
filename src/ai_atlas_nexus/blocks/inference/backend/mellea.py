from typing import Any, Dict, Optional

from openai.types.chat import ChatCompletion
from pydantic import BaseModel

from ai_atlas_nexus.blocks.inference.backend.base import InferenceBackend
from ai_atlas_nexus.metadata_base import BackendType, InferenceEngineType


# Mellea operational defaults
LOOP_BUDGET = 3  # Repair loop budget for m.instruct() with RepairTemplateStrategy
AGENT_PREFIX = None


class MelleaInferenceBackend(InferenceBackend):
    """Mellea backend implementation."""

    _backend_type = BackendType.MELLEA

    def __init__(
        self,
        session,
        model_options: Optional[Dict] = None,
    ):
        """Creates a new Mellea backend.

        Args:
            session (MelleaSession): A Mellea session object that can be used as a context manager
            model_options (Dict, optional): Additional model options, which will upsert into the model/backend's defaults. Defaults to None.
        """
        self.session = session
        self.model_options = model_options

    @classmethod
    def initialize(
        cls,
        inference_engine_type: InferenceEngineType,
        model_name_or_path: str,
        credentials: Dict[str, str],
        llm_parameters: Dict,
    ):
        """Initialize Mellea backend with the provided inference service.

        Args:
            inference_service (str): _description_
            model_name_or_path (str): _description_
            credentials (Dict[str, str]): _description_
            llm_parameters (Dict): _description_

        Raises:
            ImportError: if mellea library is not installed.
            RuntimeError: if mellea failed to initialize.

        Returns:
            MelleaSession: A Mellea session object that can be used as a context manager
        """
        try:
            assert inference_engine_type in [
                InferenceEngineType.OLLAMA,
                InferenceEngineType.WML,
                InferenceEngineType.RITS,
            ], f"Mellea backend is not currently supported for {inference_engine_type.upper()} inference engine. Supported inference engines: OLLAMA, WML, RITS"

            # fix to replace `api_url` with `base_url` as it is widely used across the Mellea backends.
            credentials["base_url"] = credentials.pop("api_url", None)

            # Using OpenAI API for IBM RITS
            if inference_engine_type == InferenceEngineType.RITS:
                inference_engine_type = "openai"
                credentials.update(
                    {
                        "base_url": f"{credentials["base_url"]}/{model_name_or_path.split("/")[-1].lower().replace(".", "-")}/v1",
                        "default_headers": {"RITS_API_KEY": credentials.get("api_key")},
                    }
                )

            from mellea import start_session

            # create and start mellea session
            session = start_session(
                backend_name=inference_engine_type,
                model_id=model_name_or_path,
                **credentials,
            )

            return MelleaInferenceBackend(session=session, model_options=llm_parameters)

        except ImportError:
            raise ImportError(
                "Mellea is not installed. Install it with: pip install mellea"
            )
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Mellea backend: {str(e)}")

    def generate_text(
        self,
        format: type[BaseModel],
        description: str,
        prefix: Optional[str] = None,
        grounding_context: Optional[dict[str, str]] = None,
        requirements: Optional[list[str]] = None,
        **kwargs,
    ) -> str:
        """Generate a response using Mellea.

        Args:
            format (type[BaseModel]): If set, the BaseModel to use for constrained decoding. Defaults to None.
            description (str): The description of the instruction.
            prefix (str, optional): A prefix string or ContentBlock to use when generating the instruction. Defaults to None.
            grounding_context (dict[str, str], optional): A list of grounding contexts that the instruction can use. They can bind as variables using a (key: str, value: str | ContentBlock) tuple. Defaults to None.
            requirements (list[str], optional): A list of requirements that the instruction can be validated against. Defaults to None.

        Returns:
            str: a str response
        """
        from mellea.backends.openai import OpenAIBackend
        from mellea.stdlib.sampling import RepairTemplateStrategy

        if not hasattr(self, "session"):
            raise RuntimeError(
                "Mellea backend not initialized. Call initialize() first."
            )

        try:
            response_thunk = self.session.instruct(
                description=description,
                prefix=prefix or AGENT_PREFIX,
                grounding_context=grounding_context,
                requirements=requirements,
                format=format,
                strategy=RepairTemplateStrategy(loop_budget=LOOP_BUDGET),
                model_options=self.model_options,
            )

            if isinstance(self.session.backend, OpenAIBackend):
                return ChatCompletion(**response_thunk._meta["oai_chat_response"])
            elif "oai_chat_response" in response_thunk._meta:
                return {"choices": [response_thunk._meta["oai_chat_response"]]}
            else:
                return response_thunk._meta["chat_response"]

        except Exception as e:
            raise RuntimeError(f"Mellea text generation failed: {str(e)}")

    def generate_chat_response(
        self, format: type[BaseModel], tools: bool, messages: str
    ) -> str:
        """Generate a Mellea chat response. It is a lighter-weight alternative that sends a plain message with no requirements and no sampling strategy

        Args:
            format (type[BaseModel]): If set, the BaseModel to use for constrained decoding. Defaults to None.
            tools (bool): If true, tool calling is enabled in mellea. Default to False.
            messages (str): The description of the instruction.

        Returns:
            str: a str chat response
        """
        if not hasattr(self, "session"):
            raise RuntimeError(
                "Mellea backend not initialized. Call initialize() first."
            )

        try:
            if not isinstance(messages[0], str):
                raise Exception("Mellea chat input should always be a plain string.")

            response_thunk = self.session.chat(
                content=messages[0],
                format=format,
                model_options=self.model_options,
                tool_calls=bool(tools),
            )

            return response_thunk.content
        except Exception as e:
            raise RuntimeError(f"Mellea chat response failed: {str(e)}")
