---
search:
  boost: 5.0
---

# Slot: hasOutOfScopeUses

_Use cases where the benchmark is not designed to be applied and could give misleading results._

<div data-search-exclude markdown="1">

URI: [nexus:hasOutOfScopeUses](https://w3id.org/ai-atlas-nexus/hasOutOfScopeUses)

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

| Mapping Type | Mapped Value            |
| ------------ | ----------------------- |
| self         | nexus:hasOutOfScopeUses |
| native       | nexus:hasOutOfScopeUses |

## LinkML Source

<details>
```yaml
name: hasOutOfScopeUses
description: Use cases where the benchmark is not designed to be applied and could
  give misleading results.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- BenchmarkMetadataCard
range: string
multivalued: true

```
</details></div>
```
