# Slot: hasTasks

_The tasks or evaluations the benchmark is intended to assess._

URI: [nexus:hasTasks](https://ibm.github.io/ai-atlas-nexus/ontology/hasTasks)
Alias: hasTasks

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                              | Description                                                                      | Modifies Slot |
| ------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [BenchmarkMetadataCard](BenchmarkMetadataCard.md) | Benchmark metadata cards offer a standardized way to document LLM benchmarks ... | no            |
| [AiEval](AiEval.md)                               | An AI Evaluation, e                                                              | no            |
| [EveryEvalAIResult](EveryEvalAIResult.md)         | An evaluation result from the Every Eval Ever dataset, capturing evaluation m... | no            |
| [Questionnaire](Questionnaire.md)                 | A questionnaire groups questions                                                 | no            |
| [Question](Question.md)                           | An evaluation where a question has to be answered                                | no            |

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

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
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
</details>
```
