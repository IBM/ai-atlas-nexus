---
search:
  boost: 5.0
---

# Slot: hasAnnotation

_The process used to annotate or label the dataset, including who or what performed the annotations (e.g., human annotators, automated processes)._

<div data-search-exclude markdown="1">

URI: [nexus:hasAnnotation](https://w3id.org/ai-atlas-nexus/hasAnnotation)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                              | Description                                                                      | Modifies Slot |
| ------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [BenchmarkMetadataCard](BenchmarkMetadataCard.md) | Benchmark metadata cards offer a standardized way to document LLM benchmarks ... | no            |

## Properties

### Type and Range

| Property  | Value                                             |
| --------- | ------------------------------------------------- |
| Range     | [String](String.md)                               |
| Domain Of | [BenchmarkMetadataCard](BenchmarkMetadataCard.md) |

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
| self         | nexus:hasAnnotation |
| native       | nexus:hasAnnotation |

## LinkML Source

<details>
```yaml
name: hasAnnotation
description: The process used to annotate or label the dataset, including who or what
  performed the annotations (e.g., human annotators, automated processes).
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- BenchmarkMetadataCard
range: string
multivalued: true

```
</details></div>
```
