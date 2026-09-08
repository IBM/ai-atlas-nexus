---
search:
  boost: 5.0
---

# Slot: describesAiEval

_A relationship where a BenchmarkMetadataCard describes an AI evaluation (benchmark)._

<div data-search-exclude markdown="1">

URI: [nexus:describesAiEval](https://w3id.org/ai-atlas-nexus/describesAiEval)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                              | Description                                                                      | Modifies Slot |
| ------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [BenchmarkMetadataCard](BenchmarkMetadataCard.md) | Benchmark metadata cards offer a standardized way to document LLM benchmarks ... | no            |

## Properties

### Type and Range

| Property  | Value                                             |
| --------- | ------------------------------------------------- |
| Range     | [AiEval](AiEval.md)                               |
| Domain    | [BenchmarkMetadataCard](BenchmarkMetadataCard.md) |
| Domain Of | [BenchmarkMetadataCard](BenchmarkMetadataCard.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

<details>
<summary>Relationship Properties</summary>

| Property | Value                                           |
| -------- | ----------------------------------------------- |
| Inverse  | [hasBenchmarkMetadata](hasBenchmarkMetadata.md) |

</details>

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value          |
| ------------ | --------------------- |
| self         | nexus:describesAiEval |
| native       | nexus:describesAiEval |

## LinkML Source

<details>
```yaml
name: describesAiEval
description: A relationship where a BenchmarkMetadataCard describes an AI evaluation
  (benchmark).
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: BenchmarkMetadataCard
domain_of:
- BenchmarkMetadataCard
inverse: hasBenchmarkMetadata
range: AiEval
multivalued: true
inlined: false

```
</details></div>
```
