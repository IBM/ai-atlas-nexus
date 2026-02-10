# Slot: belongsToDomain

_A relationship where a group belongs to a domain_

URI: [schema:isPartOf](http://schema.org/isPartOf)
Alias: belongsToDomain

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                    | Description                                                                      | Modifies Slot |
| --------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [StakeholderGroup](StakeholderGroup.md) | An AI system stakeholder grouping                                                | no            |
| [Group](Group.md)                       | Labelled groups of concepts                                                      | no            |
| [CapabilityDomain](CapabilityDomain.md) | A high-level domain of AI capabilities (e                                        | no            |
| [CapabilityGroup](CapabilityGroup.md)   | A group of AI capabilities that are part of a capability taxonomy, organized ... | yes           |
| [RiskGroup](RiskGroup.md)               | A group of AI system related risks that are part of a risk taxonomy              | no            |

## Properties

- Range: [Any](Any.md)

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value          |
| ------------ | --------------------- |
| self         | schema:isPartOf       |
| native       | nexus:belongsToDomain |

## LinkML Source

<details>
```yaml
name: belongsToDomain
description: A relationship where a group belongs to a domain
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: schema:isPartOf
alias: belongsToDomain
domain_of:
- Group
- CapabilityGroup
range: Any
multivalued: false
inlined: false

```
</details>
```
