from typing import Any, Dict, List, Optional, TypedDict

from pydantic import BaseModel

from ai_atlas_nexus.inference.backend.base import InferenceBackend
from ai_atlas_nexus.metadata_base import BackendType


# Mellea operational defaults
LOOP_BUDGET = 3  # Repair loop budget for m.instruct() with RepairTemplateStrategy
AGENT_PREFIX = None


class MelleaOllamaChatResponseWrapper:

    def __init__(self, response):
        self.message = response


class MelleaWMLChatResponseWrapper(TypedDict):

    choices: List[Dict]
    usage: Dict


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
        inference_service: str,
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
            from mellea import start_session

            # fix to replace `api_url` with `base_url` as it is widely used across the Mellea backends.
            credentials["base_url"] = credentials.pop("api_url")

            # create and start mellea session
            session = start_session(
                backend_name=inference_service,
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
            description (str): The description of the instruction.
            prefix (str, optional): A prefix string or ContentBlock to use when generating the instruction. Defaults to None.
            grounding_context (dict[str, str], optional): A list of grounding contexts that the instruction can use. They can bind as variables using a (key: str, value: str | ContentBlock) tuple. Defaults to None.
            requirements (list[str], optional): A list of requirements that the instruction can be validated against. Defaults to None.
            format (type[BaseModel]): If set, the BaseModel to use for constrained decoding. Defaults to None.

        Returns:
            str: a str response
        """
        from mellea.backends.watsonx import WatsonxAIBackend
        from mellea.stdlib.sampling import RepairTemplateStrategy

        if not hasattr(self, "session"):
            raise RuntimeError(
                "Mellea backend not initialized. Call create_client() first."
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

            if isinstance(self.session.backend, WatsonxAIBackend):
                return MelleaWMLChatResponseWrapper(
                    choices=[response_thunk._meta["oai_chat_response"]],
                    usage={"prompt_tokens": None, "completion_tokens": None},
                )
            return response_thunk._meta["chat_response"]

        except Exception as e:
            raise RuntimeError(f"Mellea generation failed: {str(e)}")

    def generate_chat_response(
        self, format: type[BaseModel], tools: Any, description: str
    ) -> str:
        """Generate a chat response using Mellea.

        Args:
            messages (str): The description of the instruction.
            format (type[BaseModel]): If set, the BaseModel to use for constrained decoding. Defaults to None.

        Returns:
            str: a str chat response
        """
        from mellea.backends.watsonx import WatsonxAIBackend

        if not hasattr(self, "session"):
            raise RuntimeError(
                "Mellea backend not initialized. Call create_client() first."
            )
        if not isinstance(description, str):
            raise RuntimeError("Mellea chat backend only supports str as a prompt.")

        try:
            response_thunk = self.session.chat(
                content=description,
                format=format,
                model_options=self.model_options,
                tool_calls=bool(tools),
            )

            if isinstance(self.session.backend, WatsonxAIBackend):
                return MelleaWMLChatResponseWrapper(
                    choices=[
                        {
                            "message": {"content": response_thunk.content},
                            "finish_reason": None,
                        }
                    ],
                    usage={"prompt_tokens": None, "completion_tokens": None},
                )
            return MelleaOllamaChatResponseWrapper(message=response_thunk)

        except Exception as e:
            raise RuntimeError(f"Mellea generation failed: {str(e)}")
