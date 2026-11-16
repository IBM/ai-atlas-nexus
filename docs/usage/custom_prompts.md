# Custom risk identification prompts

`AIAtlasNexus.identify_risks_from_usecases()` accepts a `prompt_template`: a
[Jinja](https://jinja.palletsprojects.com/) template that replaces the built-in
risk identification prompt.

```python
template = """You are a security reviewer. Known risks:
{{ risks }}

Which of these apply to the usecase? Answer with an array of the 'category' labels.
Usecase: {{ usecase }}
Risks: """

risks = ai_atlas_nexus.identify_risks_from_usecases(
    usecases=["my AI system description"],
    inference_engine=engine,
    prompt_template=template,
)
```

`identify_risks_and_actions_from_usecases()` and `GenericRiskDetector` take the same parameter.

## Template variables

| Mode                               | Variables                                                                          |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| Batch (default)                    | `usecase`, `risks` (JSON list of category/description), `max_risk`, `cot_examples` |
| Per-risk (`batch_inference=False`) | `usecase`, `risk_name`, `risk_description`, `cot_examples`                         |

The template must contain `{{ usecase }}`, and must be valid Jinja. Otherwise a
`ValueError` is raised when the detector is created.

## Response format

Only the prompt is replaced. The response is still parsed as before, so the prompt
must ask for the output the parser expects:

- Batch: an array of risk labels (names from the taxonomy).
- Per-risk: an answer starting with Yes or No.
- Batch with `explanation_type=SELF_EXPLANATION`: JSON of the form
  `{"risks": [{"risk_name": "...", "explanation": "..."}]}`.

## Precedence

A custom `prompt_template` takes precedence over `use_dspy_prompt`, with a warning.
Few-shot examples are passed to the template as `cot_examples`; the template
decides whether to render them.
