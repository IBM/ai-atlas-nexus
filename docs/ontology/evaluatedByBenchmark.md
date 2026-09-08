---
search:
  boost: 5.0
---

# Slot: evaluatedByBenchmark

_Indicates that this capability is evaluated by a specific benchmark_

<div data-search-exclude markdown="1">

URI: [nexus:evaluatedByBenchmark](https://w3id.org/ai-atlas-nexus/evaluatedByBenchmark)

<!-- no inheritance hierarchy -->

## Properties

### Type and Range

| Property | Value                                             |
| -------- | ------------------------------------------------- |
| Range    | [BenchmarkMetadataCard](BenchmarkMetadataCard.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

<details>
<summary>Relationship Properties</summary>

| Property | Value                                         |
| -------- | --------------------------------------------- |
| Inverse  | [evaluatesCapability](evaluatesCapability.md) |

</details>

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value               |
| ------------ | -------------------------- |
| self         | nexus:evaluatedByBenchmark |
| native       | nexus:evaluatedByBenchmark |

## LinkML Source

<details>
```yaml
name: evaluatedByBenchmark
description: Indicates that this capability is evaluated by a specific benchmark
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
inverse: evaluatesCapability
range: BenchmarkMetadataCard
multivalued: true
inlined: false

```
</details></div>
```
