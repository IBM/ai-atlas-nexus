# Risk Explanations with Flexible Types

## Overview

`identify_risks_from_usecases()` can return risks paired with explanations from
different sources. Use the `explanation_type` parameter to control which
explanations are included.

At the detector level this is a decorator rather than a flag:

```python
from ai_atlas_nexus.blocks.inference import ExplanationType
from ai_atlas_nexus.blocks.risk_detector import (
    GenericRiskDetector,
    RiskDetectorWithExplanation,
)

detector = RiskDetectorWithExplanation(
    GenericRiskDetector(...), ExplanationType.DESCRIPTION
)
result = detector.detect(["my AI system description"])
```

## Explanation Types

1. NONE (default)

- No explanations included, suitable for: Any model, all the inference engines

2. DESCRIPTION

- Includes risk description from the ontology (uses pre-existing risk metadata)
- Suitable for: Any model, all inference engines

3. REASONING

- Extracts model thinking/reasoning if available, requires the inference response to include `thinking` field
- Suitable for:
  - Ollama: Models with the think parameter enabled (think=True, "low", "medium", "high"), and whose reported capabilities include `thinking`
- Not suitable for the other engines yet, because none of them read reasoning back off
  the response into `thinking`:
  - WML: accepts `include_reasoning=True` and `reasoning_effort` on the request, but the
    response handler does not capture the reasoning, so `explanation` is `None`
  - RITS, VLLM, OpenAI: reasoning-capable models return the reasoning as
    `reasoning_content`, which is not captured yet, so `explanation` is `None`
  - HF: no reasoning output

4. SELF_EXPLANATION

- Extracts explanations from the model's structured response
- Requires model to generate JSON with {risk_name, explanation} pairs, so the model must reliably follow schema and produce well-formed explanations
- Suitable for:
  - Instruction-tuned models which can be capable of structured output (JSON schema compliance), for example: GPT-4, Claude, Granite 3.x series, Llama 3+ instruct, Mixtral instruct
  - Less suitable: Base models, smaller models (<7B), models without strong instruction-following

### `ExplanationType.NONE` (Default)

Returns a list of risks without explanations.

```python
risks = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=["my AI system"],
    inference_engine=engine,
)
# Result: List[List[Risk]]
```

### `ExplanationType.DESCRIPTION`

Includes the risk's description.

```python
result = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=["my AI system"],
    inference_engine=engine,
    explanation_type=ExplanationType.DESCRIPTION,
)
# Result: List[List[RiskWithExplanation]]

for risk_exp in result[0]:
    print(f"{risk_exp.risk.name}")
    print(f"  {risk_exp.explanation}")
    # Example:
    # Hallucination
    #   The model produces confidently stated but erroneous content
```

### `ExplanationType.REASONING`

Extracts the model's thinking/reasoning if available.

```python
result = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=["my AI system"],
    inference_engine=engine,
    explanation_type=ExplanationType.REASONING,
)
# Result: List[List[RiskWithExplanation]]

for risk_exp in result[0]:
    if risk_exp.explanation:
        print(f"{risk_exp.risk.name}:")
        print(f"  Model reasoning: {risk_exp.explanation}")
```

**Note**: Only models that support thinking/reasoning (e.g., Ollama with `think=True`) will populate this field. Others will have `None`.

**Known limitation**: Ollama is currently the only inference engine that populates
`TextGenerationInferenceOutput.thinking`. Reasoning-capable models on the
OpenAI-compatible engines (RITS, vLLM, OpenAI) return their reasoning as
`reasoning_content`, and WML accepts `include_reasoning` / `reasoning_effort` on the
request, but in neither case is the reasoning read back off the response. On those
engines `REASONING` therefore yields `explanation=None`. Use `SELF_EXPLANATION` instead
until this is addressed.

### `ExplanationType.SELF_EXPLANATION`

Surfaces the explanation the model emitted alongside its own answer.

- **Batch path (default, `batch_inference=True`).** The plain batch response schema uses one LLM call per usecase.
- **Per-risk path (`batch_inference=False`, or `use_dspy_prompt=True`).** That path uses
  the `AIRiskPresence` schema, so the
  model produces a rationale for each Yes/No decision and the decorator reads it
  directly.

```python
result = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=["my AI system"],
    inference_engine=engine,
    explanation_type=ExplanationType.SELF_EXPLANATION,
)
# Result: List[List[RiskWithExplanation]]

for risk_exp in result[0]:
    if risk_exp.explanation:
        print(f"{risk_exp.risk.name}:")
        print(f"  Explanation: {risk_exp.explanation}")
```

**Note**: Only models that honour the structure response schema will populate this
field. If a model returns something other than the requested JSON object, `explanation` comes back `None`.

## RiskWithExplanation Class

```python
@dataclass(kw_only=True)
class RiskWithExplanation:
    risk: Risk                      # The actual Risk object
    explanation: Optional[str]      # Explanation based on type
```

Access the wrapped risk:

```python
for risk_exp in result[0]:
    print(risk_exp.risk.name)          # Risk name
    print(risk_exp.risk.description)   # Risk description
    print(risk_exp.risk.id)            # Risk ID
    print(risk_exp.explanation)        # Type-specific explanation
```

## Combining with Metadata

Explanations work seamlessly with metadata tracking:

```python
result = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=["my AI system"],
    inference_engine=engine,
    return_metadata=True,
    explanation_type=ExplanationType.DESCRIPTION,
)
# result.data: List[List[RiskWithExplanation]]
# result.metadata: InferenceMetadata with tokens, stop_reasons, seed, etc.

for risk_exp in result.data[0]:
    print(f"{risk_exp.risk.name}: {risk_exp.explanation}")

print(f"Total tokens: {result.metadata.token_usage.total_tokens}")
print(f"Stop reasons: {result.metadata.stop_reason_summary}")
```

## Use Cases

### Educational Output

Show users why risks were detected:

```python
result = identify_risks_from_usecases(
    usecases=usecases,
    engine=engine,
    explanation_type=ExplanationType.REASONING,
)

for usecase_idx, usecase in enumerate(usecases):
    print(f"\nUsecase: {usecase}")
    for risk_exp in result[usecase_idx]:
        print(f"  • {risk_exp.risk.name}")
        print(f"    {risk_exp.explanation}")
```

### Debugging Model Reasoning

Understand the model's decision-making process:

```python
result = identify_risks_from_usecases(
    usecases=usecases,
    engine=engine,
    explanation_type=ExplanationType.REASONING,
)

for usecase_idx, usecase in enumerate(usecases):
    for risk_exp in result[usecase_idx]:
        if risk_exp.explanation:
            logger.debug(
                f"Risk '{risk_exp.risk.name}' detected for '{usecase}'",
                extra={"model_reasoning": risk_exp.explanation}
            )
```

### Lightweight Output

Use only descriptions, skip expensive reasoning:

```python
result = identify_risks_from_usecases(
    usecases=usecases,
    engine=engine,
    explanation_type=ExplanationType.DESCRIPTION,
)
# No LLM calls needed for explanations, uses existing Risk objects
```
