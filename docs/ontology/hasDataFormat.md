---
search:
  boost: 5.0
---

# Slot: hasDataFormat

_The structure and modality of the data (e.g., sentence pairs, question-answer format, tabular data)._

<div data-search-exclude markdown="1">

URI: [nexus:hasDataFormat](https://w3id.org/ai-atlas-nexus/hasDataFormat)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                              | Description                                                                      | Modifies Slot |
| ------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [EveryEvalAIResult](EveryEvalAIResult.md)         | An evaluation result from the Every Eval Ever dataset, capturing evaluation m... | no            |
| [BenchmarkMetadataCard](BenchmarkMetadataCard.md) | Benchmark metadata cards offer a standardized way to document LLM benchmarks ... | no            |

## Properties

### Type and Range

| Property  | Value                                                                                        |
| --------- | -------------------------------------------------------------------------------------------- |
| Range     | [String](String.md)                                                                          |
| Domain Of | [EveryEvalAIResult](EveryEvalAIResult.md), [BenchmarkMetadataCard](BenchmarkMetadataCard.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value        |
| ------------ | ------------------- |
| self         | nexus:hasDataFormat |
| native       | nexus:hasDataFormat |

## LinkML Source

<details>
```yaml
name: hasDataFormat
description: The structure and modality of the data (e.g., sentence pairs, question-answer
  format, tabular data).
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- EveryEvalAIResult
- BenchmarkMetadataCard
range: string
multivalued: true

```
</details></div>
```
