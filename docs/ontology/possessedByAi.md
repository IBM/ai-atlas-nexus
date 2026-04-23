# Slot: possessedByAi

_Indicates that this capability is possessed by a specific AI system or component. Inverse of hasCapability, allowing navigation from capabilities to AI systems. This enables queries like "which AI systems have this capability?"_

URI: [tech:hasCapability](https://w3id.org/dpv/tech#hasCapability)
Alias: possessedByAi

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

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: Capability
slot_uri: tech:hasCapability
alias: possessedByAi
inverse: hasCapability
range: BaseAi
multivalued: true
inlined: false

```
</details>
```
