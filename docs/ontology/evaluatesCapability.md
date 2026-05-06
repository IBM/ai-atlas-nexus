# Slot: evaluatesCapability

_Indicates that this benchmark evaluates a specific capability_

URI: [nexus:evaluatesCapability](https://ibm.github.io/ai-atlas-nexus/ontology/evaluatesCapability)
Alias: evaluatesCapability

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

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: BenchmarkMetadataCard
alias: evaluatesCapability
inverse: evaluatedByBenchmark
range: Capability
multivalued: true
inlined: false

```
</details>
```
