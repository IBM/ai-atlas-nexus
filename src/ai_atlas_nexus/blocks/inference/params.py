import dataclasses
from typing import Any, Dict, List, Literal, Optional, TypeAlias, Union

from openai.types.chat import ChatCompletionMessageParam
from pydantic import BaseModel
from typing_extensions import TypedDict

from ai_atlas_nexus.metadata_base import ExplanationType


class InferenceEngineCredentials(TypedDict):
    """Contains the prediction results and metadata for the inference.

    Args:
        api_url (str): API url of the hosted LLM server.

        api_key (str, optional) : API key to access services on the hosted LLM service.

        space_id (str, optional) : space id to use for the WML platform.

        project_id (str, optional) : project id to use for the WML platform.
    """

    api_url: str
    api_key: Optional[str] = None  # Optional for vLLM/Ollama server mode
    space_id: Optional[str] = None  # only used in WML engine
    project_id: Optional[str] = None  # only used in WML engine
    org_id: Optional[str] = None  # used in HF engine for org billing
    aws_access_key_id: Optional[str] = None  # only used in Bedrock engine
    aws_secret_access_key: Optional[str] = None  # only used in Bedrock engine
    region_name: Optional[str] = None  # only used in Bedrock engine


class RITSInferenceEngineParams(TypedDict):
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    max_completion_tokens: Optional[int] = None
    seed: Optional[int] = None
    stop: Union[Optional[str], List[str]] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    top_logprobs: Optional[int] = None
    logit_bias: Optional[Dict[str, int]] = None
    logprobs: Optional[bool] = True
    n: Optional[int] = None
    parallel_tool_calls: Optional[bool] = None
    service_tier: Optional[Literal["auto", "default"]] = None


class WMLInferenceEngineParams(TypedDict):
    frequency_penalty: Optional[float] = None
    logprobs: Optional[bool] = None
    top_logprobs: Optional[int] = None
    presence_penalty: Optional[float] = None
    response_format: Optional[dict] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    max_completion_tokens: Optional[int] = None
    time_limit: Optional[int] = None
    top_p: Optional[float] = None
    n: Optional[int] = None
    logit_bias: Optional[dict] = None
    seed: Optional[int] = None
    stop: Optional[list[str]] = None
    guided_choice: Optional[list[str]] = None
    guided_regex: Optional[str] = None
    guided_grammar: Optional[str] = None
    guided_json: Optional[dict] = None
    chat_template_kwargs: Optional[dict] = None
    reasoning_effort: Optional[Literal["low", "medium", "high"]] = None
    include_reasoning: Optional[bool] = None
    repetition_penalty: Optional[float] = None
    length_penalty: Optional[float] = None


class OllamaInferenceEngineParams(TypedDict):
    # load time options
    numa: Optional[bool] = None
    num_ctx: Optional[int] = None
    num_batch: Optional[int] = None
    num_gpu: Optional[int] = None
    main_gpu: Optional[int] = None
    low_vram: Optional[bool] = None
    f16_kv: Optional[bool] = None
    logits_all: Optional[bool] = None
    vocab_only: Optional[bool] = None
    use_mmap: Optional[bool] = None
    use_mlock: Optional[bool] = None
    embedding_only: Optional[bool] = None
    num_thread: Optional[int] = None

    # runtime options
    num_keep: Optional[int] = None
    seed: Optional[int] = None
    num_predict: Optional[int] = None
    top_k: Optional[int] = None
    top_p: Optional[float] = None
    tfs_z: Optional[float] = None
    typical_p: Optional[float] = None
    repeat_last_n: Optional[int] = None
    temperature: Optional[float] = None
    repeat_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    frequency_penalty: Optional[float] = None
    mirostat: Optional[int] = None
    mirostat_tau: Optional[float] = None
    mirostat_eta: Optional[float] = None
    penalize_newline: Optional[bool] = None
    stop: Optional[List[str]] = None

    # enable log probs
    logprobs: Optional[bool] = None
    top_logprobs: Optional[int] = None

    # enable or disable model thinking
    think: Optional[Union[bool, Literal["low", "medium", "high"]]] = False


class VLLMInferenceEngineParams(TypedDict):

    n: int = 1
    best_of: Optional[int] = None
    presence_penalty: float = 0.0
    frequency_penalty: float = 0.0
    repetition_penalty: float = 1.0
    temperature: float = 1.0
    top_p: float = 1.0
    top_k: int = -1
    min_p: float = 0.0
    seed: Optional[int] = None
    stop: Optional[Union[str, List[str]]] = None
    stop_token_ids: Optional[List[int]] = None
    bad_words: Optional[List[str]] = None
    ignore_eos: bool = False
    max_tokens: Optional[int] = None
    min_tokens: int = 0
    logprobs: Optional[int] = None
    prompt_logprobs: Optional[int] = None
    max_model_len: Optional[int] = None
    gpu_memory_utilization: Optional[float] = None


class HFInferenceEngineParams(TypedDict):
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    max_completion_tokens: Optional[int] = None
    seed: Optional[int] = None
    stop: Union[Optional[str], List[str]] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    top_logprobs: Optional[int] = None
    logit_bias: Optional[Dict[str, int]] = None
    logprobs: Optional[bool] = True
    n: Optional[int] = None

class AWSBedrockInferenceEngineParams(TypedDict):
    # Native Bedrock converse params (amazon.*, anthropic.*, etc.)
    maxTokens: Optional[int] = None
    topP: Optional[float] = None
    stopSequences: Optional[List[str]] = None
    temperature: Optional[float] = None
    # OpenAI-compatible params (openai.* models via invoke_model)
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    max_completion_tokens: Optional[int] = None
    max_tokens: Optional[int] = None
    seed: Optional[int] = None
    stop: Optional[List[str]] = None
    top_p: Optional[float] = None
    logprobs: Optional[bool] = None
    top_logprobs: Optional[int] = None
    logit_bias: Optional[Dict[str, int]] = None
    n: Optional[int] = None
    reasoning_effort: Optional[Literal["low", "medium", "high"]] = None
    verbosity: Optional[Literal["low", "medium", "high"]] = None
    service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] = None
    store: Optional[bool] = None
    metadata: Optional[Dict[str, str]] = None
    safety_identifier: Optional[str] = None
    prompt_cache_key: Optional[str] = None


class OpenAIInferenceEngineParams(TypedDict):
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    max_completion_tokens: Optional[int] = None
    seed: Optional[int] = None
    stop: Optional[list[str]] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    max_tokens: Optional[int] = None
    response_format: Optional[dict] = None
    top_logprobs: Optional[int] = None
    logit_bias: Optional[dict] = None
    logprobs: Optional[bool] = None
    n: Optional[int] = None
    reasoning_effort: Optional[Literal["low", "medium", "high"]] = None
    verbosity: Optional[Literal["low", "medium", "high"]] = None
    service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority"]] = None
    store: Optional[bool] = None
    metadata: Optional[dict[str, str]] = None
    safety_identifier: Optional[str] = None
    prompt_cache_key: Optional[str] = None


@dataclasses.dataclass(kw_only=True)
class TextGenerationInferenceOutput:
    """Contains the prediction results and metadata for the inference.

    Args:
        prediction (Any): model ouput

        input_tokens (int) : number of input tokens to the model.

        output_tokens (int) : number of output tokens to the model.

        stop_reason (str): stop reason for text generation, for example "eos" (end of string).

        seed (int): seed used by the model during generation.

        input_text (str): input to the model.

        logprobs (Dict[str, float]): Dict of prediction tokens to their Log probability

        model_name (str): the model_name as kept in the InferenceEngine.

        inference_engine (str): The label stating the type of the InferenceEngine.

        thinking: When thinking is enabled in ollama (think=True), the output will separate the model's thinking from the model's output.
    """

    prediction: Union[str, Dict[str, Any], List[Any]]
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    stop_reason: Optional[str] = None
    seed: Optional[int] = None
    input_text: Optional[str] = None
    logprobs: Optional[Dict[str, float]] = None
    model_name_or_path: Optional[str] = None
    inference_engine: Optional[str] = None
    thinking: Optional[str] = None


OpenAIChatCompletionMessageParam: TypeAlias = List[ChatCompletionMessageParam]

ValidChatCompletionMessageParam: TypeAlias = Union[
    str, OpenAIChatCompletionMessageParam
]

ValidListChatCompletionMessageParam: TypeAlias = Union[
    List[str], List[OpenAIChatCompletionMessageParam]
]


class MelleaInferenceParams(TypedDict, total=False):

    description: str
    format: type[BaseModel]
    tools: Optional[Any] = None
    prefix: Optional[str] = None
    grounding_context: Optional[dict[str, str]] = None
    requirements: Optional[list[str]] = None


ValidGenerateCompletionMessageParam: TypeAlias = Union[
    List[str], List[MelleaInferenceParams]
]


@dataclasses.dataclass(kw_only=True)
class TokenUsage:
    """Token usage metrics from one or more LLM inference calls.

    A count is None when the engine did not report it. `total_tokens` sums the counts
    that were reported.
    """

    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    total_tokens: Optional[int] = None

    def __post_init__(self) -> None:
        # Derive the total when a caller reports only the parts.
        if self.total_tokens is None and not (
            self.input_tokens is None and self.output_tokens is None
        ):
            self.total_tokens = (self.input_tokens or 0) + (self.output_tokens or 0)

    def __add__(self, other: "TokenUsage") -> "TokenUsage":
        def _add(left: Optional[int], right: Optional[int]) -> Optional[int]:
            if left is None and right is None:
                return None
            return (0 if left is None else left) + (0 if right is None else right)

        return TokenUsage(
            input_tokens=_add(self.input_tokens, other.input_tokens),
            output_tokens=_add(self.output_tokens, other.output_tokens),
            total_tokens=_add(self.total_tokens, other.total_tokens),
        )


@dataclasses.dataclass(kw_only=True)
class UsecaseInferenceMetadata:
    """Metadata from the inference calls made for a single usecase.
    """

    token_usage: TokenUsage
    num_calls: int
    seed: Optional[int] = None
    stop_reason_summary: Dict[str, int] = dataclasses.field(default_factory=dict)
    has_thinking: bool = False


@dataclasses.dataclass(kw_only=True)
class InferenceMetadata:
    """Metadata from the inference calls within a detection operation.

    The top-level fields aggregate every call in the run.
    `per_usecase` breaks the same figures down one entry per usecase.
    """

    token_usage: TokenUsage
    inference_engine: str
    model: str
    num_calls: int
    seed: Optional[int] = None
    stop_reason_summary: Dict[str, int] = dataclasses.field(default_factory=dict)
    has_thinking: bool = False
    per_usecase: List[UsecaseInferenceMetadata] = dataclasses.field(
        default_factory=list
    )
