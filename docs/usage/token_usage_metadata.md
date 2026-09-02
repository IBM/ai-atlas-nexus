# Token Usage Metadata Exposure

## Overview

`AIAtlasNexus.identify_risks_from_usecases()` exposes LLM
token usage metrics via an optional `return_metadata` parameter.

At the detector level this is a decorator rather than a flag: wrap any detector in
`RiskDetectorWithMetadata` to get the same information.

```python
from ai_atlas_nexus.blocks.risk_detector import (
    GenericRiskDetector,
    RiskDetectorWithMetadata,
)

detector = RiskDetectorWithMetadata(GenericRiskDetector(...))
result = detector.detect(["my AI system description"])
```

This enables monitoring and cost analysis of risk identification operations.

## Usage

### Basic API (Backward Compatible)

By default, the API returns a list of risks:

```python
risks = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=["my AI system description"],
    inference_engine=inference_engine,
    taxonomy="ibm-risk-atlas",
)
# risks: List[List[Risk]]
# Example: [[Risk(...), Risk(...)], ...]
```

### With Token Metadata

Pass `return_metadata=True` to receive a wrapped response with token usage, reported
both aggregated over the run and broken down per usecase:

```python
result = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=["my AI system description"],
    inference_engine=inference_engine,
    taxonomy="ibm-risk-atlas",
    return_metadata=True,
)
# result: DetectionResult[List[List[Risk]]]

# Access the risks data
risks = result.data
print(f"Identified risks: {[r.name for r in risks[0]]}")

# Access token usage metrics
print(f"Input tokens: {result.metadata.token_usage.input_tokens}")
print(f"Output tokens: {result.metadata.token_usage.output_tokens}")
print(f"Total tokens: {result.metadata.token_usage.total_tokens}")

# Model and inference info
print(f"Model: {result.metadata.model}")
print(f"Engine: {result.metadata.inference_engine}")
print(f"Number of LLM calls: {result.metadata.num_calls}")

# Reproducibility and prediction details
print(f"Seed: {result.metadata.seed}")  # None if calls used different seeds
print(f"Stop reasons: {result.metadata.stop_reason_summary}")  # e.g., {"eos": 99}
print(f"Has thinking: {result.metadata.has_thinking}")  # True if any call had thinking
```

### Per-Usecase Breakdown

`metadata.per_usecase` has one entry per usecase, in the order the usecases were
passed in and positionally aligned with `result.data`:

```python
result = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=["customer support chatbot", "loan approval model"],
    inference_engine=inference_engine,
    return_metadata=True,
)

for usecase, risks, usage in zip(usecases, result.data, result.metadata.per_usecase):
    print(f"{usecase}: {len(risks)} risks, {usage.token_usage.total_tokens} tokens "
          f"across {usage.num_calls} call(s)")
```

The per-usecase totals sum to the aggregate, so either view can be used without
double counting. An unreported count is `None` rather than 0, so default it before
doing arithmetic:

```python
assert sum(u.token_usage.input_tokens or 0 for u in result.metadata.per_usecase) == \
    (result.metadata.token_usage.input_tokens or 0)
```

How many calls each entry covers depends on the mode. With `batch_inference=True`
(the default) it is one call per usecase. With `batch_inference=False` or
`use_dspy_prompt=True` it is one call per risk per usecase, including the calls that
identified nothing — those still cost tokens.

Stop reasons, seeds and `has_thinking` are also reported per usecase. Note that
`seed` follows the same rule at both levels: it is only set if every call in that
scope used the same seed, so a usecase can report a seed while the run as a whole
reports `None`.

### With identify_risks_and_actions_from_usecases

The companion method also supports token metadata. It returns one entry per usecase
under `per_usecase`, each with that usecase's own `token_usage`, and the run totals at
the top level:

```python
result = ai_atlas_nexus.identify_risks_and_actions_from_usecases(
    usecases=["a support chatbot", "a loan approval model"],
    inference_engine=inference_engine,
    taxonomy="ibm-risk-atlas",
    return_metadata=True,
)

print(f"Total tokens used: {result['token_usage']['total_tokens']}")

for entry in result["per_usecase"]:
    usage = entry["token_usage"]
    print(f"{entry['usecase']}: {len(entry['risks'])} risks, "
          f"{usage['total_tokens']} tokens across {usage['num_calls']} call(s)")
```

Without `return_metadata=True` no `token_usage` key is present, at either level.

## Response Types

### DetectionResult[T]

Wraps detection results with metadata:

```python
@dataclass(kw_only=True)
class DetectionResult(Generic[T]):
    data: T  # List[List[Risk]], or List[List[RiskWithExplanation]] if explained
    metadata: InferenceMetadata
```

### InferenceMetadata

Contains inference information for the run, aggregated and per usecase:

```python
@dataclass(kw_only=True)
class InferenceMetadata:
    token_usage: TokenUsage           # Tokens aggregated over the whole run
    inference_engine: str              # Engine type (e.g., "WML")
    model: str                         # Model name/path
    num_calls: int                     # Total LLM calls made
    seed: Optional[int]                # Seed used (None if calls used different seeds)
    stop_reason_summary: Dict[str, int]  # Count of each stop reason (e.g., {"eos": 5})
    has_thinking: bool                 # Whether any call had thinking enabled
    per_usecase: List[UsecaseInferenceMetadata]  # One entry per usecase, in input order
```

### UsecaseInferenceMetadata

The same figures for a single usecase. The engine and model are not repeated, since
they are the same for every usecase in a run:

```python
@dataclass(kw_only=True)
class UsecaseInferenceMetadata:
    token_usage: TokenUsage            # Tokens for this usecase only
    num_calls: int                     # LLM calls made for this usecase
    seed: Optional[int]                # Seed used (None if this usecase's calls differed)
    stop_reason_summary: Dict[str, int]  # Count of each stop reason for this usecase
    has_thinking: bool                 # Whether any of this usecase's calls had thinking
```

### TokenUsage

Token metrics from the LLM:

```python
@dataclass(kw_only=True)
class TokenUsage:
    input_tokens: Optional[int]        # Tokens in the prompt
    output_tokens: Optional[int]       # Tokens in the response
    total_tokens: Optional[int]        # Sum of input + output
```

## Use Cases

### Cost Tracking

Monitor token consumption for cost analysis:

```python
result = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=usecases,
    inference_engine=inference_engine,
    return_metadata=True,
)

cost_per_1k_tokens = 0.001  # Example: $0.001 per 1000 tokens
total_tokens = result.metadata.token_usage.total_tokens
if total_tokens is None:
    print("This engine did not report token counts, so cost is unknown")
else:
    print(f"Cost of this operation: ${(total_tokens / 1000) * cost_per_1k_tokens:.4f}")
```

Or attribute cost to the usecase that incurred it, for chargeback or for finding
which usecases are expensive to analyze:

```python
for usecase, usage in zip(usecases, result.metadata.per_usecase):
    cost = ((usage.token_usage.total_tokens or 0) / 1000) * cost_per_1k_tokens
    print(f"{usecase}: ${cost:.4f}")
```

### Performance Analysis

Understand resource consumption patterns:

```python
result = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=usecases,
    inference_engine=inference_engine,
    return_metadata=True,
)

total_tokens = result.metadata.token_usage.total_tokens
if total_tokens is None or result.metadata.num_calls == 0:
    print("No token counts to average")
else:
    print(f"Average tokens per LLM call: {total_tokens / result.metadata.num_calls:.0f}")
```

### Reproducibility Tracking

Verify if runs are reproducible (same seed used):

```python
result = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=usecases,
    inference_engine=inference_engine,
    return_metadata=True,
)

if result.metadata.seed is not None:
    print(f"Run is reproducible with seed={result.metadata.seed}")
else:
    print("Run used different seeds, not reproducible")
```

### Stop Reason Analysis

Understand why the model stopped generating:

```python
result = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=usecases,
    inference_engine=inference_engine,
    return_metadata=True,
)

print(f"Stop reasons: {result.metadata.stop_reason_summary}")
# Example output: {"eos": 95, "max_tokens": 5}
# "eos" = natural end of sequence
# "max_tokens" = hit token limit
```

### Logging and Monitoring

Track usage over time:

```python
result = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=usecases,
    inference_engine=inference_engine,
    return_metadata=True,
)

logger.info(
    "Risk identification completed",
    extra={
        "model": result.metadata.model,
        "engine": result.metadata.inference_engine,
        "input_tokens": result.metadata.token_usage.input_tokens,
        "output_tokens": result.metadata.token_usage.output_tokens,
        "total_tokens": result.metadata.token_usage.total_tokens,
        "num_calls": result.metadata.num_calls,
        "seed": result.metadata.seed,
        "stop_reasons": result.metadata.stop_reason_summary,
        "has_thinking": result.metadata.has_thinking,
    }
)
```

## Supported Engines

Token metrics are aggregated across all supported inference engines
