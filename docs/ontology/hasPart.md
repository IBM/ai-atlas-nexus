# Slot: hasPart

_A relationship where an entity has another entity_

URI: [skos:member](http://www.w3.org/2004/02/skos/core#member)
Alias: hasPart

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                    | Description                                                                      | Modifies Slot |
| --------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Group](Group.md)                       | Labelled groups of concepts                                                      | no            |
| [CapabilityGroup](CapabilityGroup.md)   | A group of AI capabilities that are part of a capability taxonomy, organized ... | yes           |
| [StakeholderGroup](StakeholderGroup.md) | An AI system stakeholder grouping                                                | no            |
| [RiskGroup](RiskGroup.md)               | A group of AI system related risks that are part of a risk taxonomy              | yes           |
| [CapabilityDomain](CapabilityDomain.md) | A high-level domain of AI capabilities (e                                        | yes           |

## Properties

- Range: [String](String.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value  |
| ------------ | ------------- |
| self         | skos:member   |
| native       | nexus:hasPart |

## LinkML Source

<details>
```yaml
name: hasPart
description: A relationship where an entity has another entity
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: skos:member
alias: hasPart
domain_of:
- Group
- RiskGroup
- CapabilityGroup
range: string
multivalued: true

```
</details>
```
