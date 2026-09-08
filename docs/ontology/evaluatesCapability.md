---
search:
  boost: 5.0
---

# Slot: evaluatesCapability

_Indicates that this benchmark evaluates a specific capability_

<div data-search-exclude markdown="1">

URI: [nexus:evaluatesCapability](https://w3id.org/ai-atlas-nexus/evaluatesCapability)

<!-- no inheritance hierarchy -->

## Properties

### Type and Range

| Property | Value                                             |
| -------- | ------------------------------------------------- |
| Range    | [Capability](Capability.md)                       |
| Domain   | [BenchmarkMetadataCard](BenchmarkMetadataCard.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

<details>
<summary>Relationship Properties</summary>

| Property | Value                                           |
| -------- | ----------------------------------------------- |
| Inverse  | [evaluatedByBenchmark](evaluatedByBenchmark.md) |

</details>

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value              |
| ------------ | ------------------------- |
| self         | nexus:evaluatesCapability |
| native       | nexus:evaluatesCapability |

## LinkML Source

<details>
```yaml
name: evaluatesCapability
description: Indicates that this benchmark evaluates a specific capability
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: BenchmarkMetadataCard
inverse: evaluatedByBenchmark
range: Capability
multivalued: true
inlined: false

```
</details></div>
```
