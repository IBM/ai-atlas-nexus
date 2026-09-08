---
search:
  boost: 5.0
---

# Slot: hasDomains

_The specific domains or areas where the benchmark is applied (e.g., natural language processing, computer vision)._

<div data-search-exclude markdown="1">

URI: [nexus:hasDomains](https://w3id.org/ai-atlas-nexus/hasDomains)

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

| Mapping Type | Mapped Value     |
| ------------ | ---------------- |
| self         | nexus:hasDomains |
| native       | nexus:hasDomains |

## LinkML Source

<details>
```yaml
name: hasDomains
description: The specific domains or areas where the benchmark is applied (e.g., natural
  language processing, computer vision).
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
