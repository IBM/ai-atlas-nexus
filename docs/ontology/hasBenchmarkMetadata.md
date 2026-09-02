---
search:
  boost: 5.0
---

# Slot: hasBenchmarkMetadata

_A relationship to a Benchmark Metadata Card which contains metadata about the benchmark._

<div data-search-exclude markdown="1">

URI: [nexus:hasBenchmarkMetadata](https://w3id.org/ai-atlas-nexus/hasBenchmarkMetadata)
Alias: hasBenchmarkMetadata

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                              | Description                                       | Modifies Slot |
| --------------------------------- | ------------------------------------------------- | ------------- |
| [Question](Question.md)           | An evaluation where a question has to be answered | no            |
| [AiEval](AiEval.md)               | An AI Evaluation, e                               | no            |
| [Questionnaire](Questionnaire.md) | A questionnaire groups questions                  | no            |

## Properties

### Type and Range

| Property  | Value                                             |
| --------- | ------------------------------------------------- |
| Range     | [BenchmarkMetadataCard](BenchmarkMetadataCard.md) |
| Domain    | [AiEval](AiEval.md)                               |
| Domain Of | [AiEval](AiEval.md)                               |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

<details>
<summary>Relationship Properties</summary>

| Property | Value                                 |
| -------- | ------------------------------------- |
| Inverse  | [describesAiEval](describesAiEval.md) |

</details>

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value               |
| ------------ | -------------------------- |
| self         | nexus:hasBenchmarkMetadata |
| native       | nexus:hasBenchmarkMetadata |

## LinkML Source

<details>
```yaml
name: hasBenchmarkMetadata
description: A relationship to a Benchmark Metadata Card which contains metadata about
  the benchmark.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: AiEval
alias: hasBenchmarkMetadata
domain_of:
- AiEval
inverse: describesAiEval
range: BenchmarkMetadataCard
multivalued: true
inlined: false

```
</details></div>
```
