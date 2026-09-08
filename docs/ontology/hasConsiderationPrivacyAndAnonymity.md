---
search:
  boost: 5.0
---

# Slot: hasConsiderationPrivacyAndAnonymity

_How any personal or sensitive data is handled and whether any anonymization techniques are applied._

<div data-search-exclude markdown="1">

URI: [nexus:hasConsiderationPrivacyAndAnonymity](https://w3id.org/ai-atlas-nexus/hasConsiderationPrivacyAndAnonymity)

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

| Mapping Type | Mapped Value                              |
| ------------ | ----------------------------------------- |
| self         | nexus:hasConsiderationPrivacyAndAnonymity |
| native       | nexus:hasConsiderationPrivacyAndAnonymity |

## LinkML Source

<details>
```yaml
name: hasConsiderationPrivacyAndAnonymity
description: How any personal or sensitive data is handled and whether any anonymization
  techniques are applied.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- BenchmarkMetadataCard
range: string
multivalued: true

```
</details></div>
```
