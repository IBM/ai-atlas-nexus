---
search:
  boost: 5.0
---

# Slot: hasTasks

_The tasks or evaluations the benchmark is intended to assess._

<div data-search-exclude markdown="1">

URI: [nexus:hasTasks](https://w3id.org/ai-atlas-nexus/hasTasks)
Alias: hasTasks

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                              | Description                                                                      | Modifies Slot |
| ------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiEval](AiEval.md)                               | An AI Evaluation, e                                                              | no            |
| [Questionnaire](Questionnaire.md)                 | A questionnaire groups questions                                                 | no            |
| [Question](Question.md)                           | An evaluation where a question has to be answered                                | no            |
| [EveryEvalAIResult](EveryEvalAIResult.md)         | An evaluation result from the Every Eval Ever dataset, capturing evaluation m... | no            |
| [BenchmarkMetadataCard](BenchmarkMetadataCard.md) | Benchmark metadata cards offer a standardized way to document LLM benchmarks ... | no            |

## Properties

### Type and Range

| Property  | Value                                                                                                             |
| --------- | ----------------------------------------------------------------------------------------------------------------- |
| Range     | [String](String.md)                                                                                               |
| Domain Of | [AiEval](AiEval.md), [EveryEvalAIResult](EveryEvalAIResult.md), [BenchmarkMetadataCard](BenchmarkMetadataCard.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value   |
| ------------ | -------------- |
| self         | nexus:hasTasks |
| native       | nexus:hasTasks |

## LinkML Source

<details>
```yaml
name: hasTasks
description: The tasks or evaluations the benchmark is intended to assess.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
alias: hasTasks
domain_of:
- AiEval
- EveryEvalAIResult
- BenchmarkMetadataCard
range: string
multivalued: true
inlined: false

```
</details></div>
```
