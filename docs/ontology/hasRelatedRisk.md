---
search:
  boost: 5.0
---

# Slot: hasRelatedRisk

_A relationship where an entity relates to a risk_

<div data-search-exclude markdown="1">

URI: [nexus:hasRelatedRisk](https://w3id.org/ai-atlas-nexus/hasRelatedRisk)
Alias: hasRelatedRisk

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                              | Description                                                                      | Modifies Slot |
| ------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [LLMQuestionPolicy](LLMQuestionPolicy.md)         | The policy guides how the language model should answer a diverse set of sensi... | no            |
| [Action](Action.md)                               | Action to remediate a risk                                                       | yes           |
| [Questionnaire](Questionnaire.md)                 | A questionnaire groups questions                                                 | no            |
| [AiSystem](AiSystem.md)                           | A compound AI System composed of one or more AI capablities                      | yes           |
| [AiEval](AiEval.md)                               | An AI Evaluation, e                                                              | yes           |
| [Term](Term.md)                                   | A term and its definitions                                                       | no            |
| [AiAgent](AiAgent.md)                             | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [Question](Question.md)                           | An evaluation where a question has to be answered                                | no            |
| [EveryEvalAIResult](EveryEvalAIResult.md)         | An evaluation result from the Every Eval Ever dataset, capturing evaluation m... | yes           |
| [Adapter](Adapter.md)                             | Adapter-based methods add extra trainable parameters after the attention and ... | yes           |
| [LLMIntrinsic](LLMIntrinsic.md)                   | A capability that can be invoked through a well-defined API that is reasonabl... | yes           |
| [BenchmarkMetadataCard](BenchmarkMetadataCard.md) | Benchmark metadata cards offer a standardized way to document LLM benchmarks ... | yes           |

## Properties

### Type and Range

| Property  | Value                                                                                                                                                                                                                                                                               |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Range     | [Any](Any.md)                                                                                                                                                                                                                                                                       |
| Domain    | [Any](Any.md)                                                                                                                                                                                                                                                                       |
| Domain Of | [Term](Term.md), [LLMQuestionPolicy](LLMQuestionPolicy.md), [Action](Action.md), [AiSystem](AiSystem.md), [AiEval](AiEval.md), [EveryEvalAIResult](EveryEvalAIResult.md), [BenchmarkMetadataCard](BenchmarkMetadataCard.md), [Adapter](Adapter.md), [LLMIntrinsic](LLMIntrinsic.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | nexus:hasRelatedRisk |
| native       | nexus:hasRelatedRisk |

## LinkML Source

<details>
```yaml
name: hasRelatedRisk
description: A relationship where an entity relates to a risk
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: Any
alias: hasRelatedRisk
domain_of:
- Term
- LLMQuestionPolicy
- Action
- AiSystem
- AiEval
- EveryEvalAIResult
- BenchmarkMetadataCard
- Adapter
- LLMIntrinsic
range: Any
multivalued: true
inlined: false

```
</details></div>
```
