---
search:
  boost: 5.0
---

# Slot: possessedByAi

_Indicates that this capability is possessed by a specific AI system or component. Inverse of hasCapability, allowing navigation from capabilities to AI systems. This enables queries like "which AI systems have this capability?"_

<div data-search-exclude markdown="1">

URI: [tech:hasCapability](https://w3id.org/dpv/tech#hasCapability)

<!-- no inheritance hierarchy -->

## Properties

### Type and Range

| Property | Value                                                         |
| -------- | ------------------------------------------------------------- |
| Range    | [BaseAi](BaseAi.md)                                           |
| Domain   | [Capability](Capability.md)                                   |
| Slot URI | [tech:hasCapability](https://w3id.org/dpv/tech#hasCapability) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

<details>
<summary>Relationship Properties</summary>

| Property | Value                             |
| -------- | --------------------------------- |
| Inverse  | [hasCapability](hasCapability.md) |

</details>

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value        |
| ------------ | ------------------- |
| self         | tech:hasCapability  |
| native       | nexus:possessedByAi |

## LinkML Source

<details>
```yaml
name: possessedByAi
description: Indicates that this capability is possessed by a specific AI system or
  component. Inverse of hasCapability, allowing navigation from capabilities to AI
  systems. This enables queries like "which AI systems have this capability?"
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: Capability
slot_uri: tech:hasCapability
inverse: hasCapability
range: BaseAi
multivalued: true
inlined: false

```
</details></div>
```
