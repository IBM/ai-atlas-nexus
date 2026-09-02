---
search:
  boost: 5.0
---

# Slot: belongsToDomain

_A relationship where a group belongs to a domain_

<div data-search-exclude markdown="1">

URI: [schema:isPartOf](http://schema.org/isPartOf)
Alias: belongsToDomain

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                    | Description                                                                      | Modifies Slot |
| --------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [StakeholderGroup](StakeholderGroup.md) | An AI system stakeholder grouping                                                | no            |
| [CapabilityGroup](CapabilityGroup.md)   | A group of AI capabilities that are part of a capability taxonomy, organized ... | yes           |
| [Group](Group.md)                       | Labelled groups of concepts                                                      | no            |
| [CapabilityDomain](CapabilityDomain.md) | A high-level domain of AI capabilities (e                                        | no            |
| [AiTaskGroup](AiTaskGroup.md)           | A group of AI Tasks                                                              | no            |
| [AiTaskDomain](AiTaskDomain.md)         | A grouping of AI Tasks by domain                                                 | no            |
| [RiskGroup](RiskGroup.md)               | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [RiskControlGroup](RiskControlGroup.md) | A group of AI system related risk controls                                       | no            |

## Properties

### Type and Range

| Property  | Value                                                    |
| --------- | -------------------------------------------------------- |
| Range     | [Any](Any.md)                                            |
| Domain Of | [Group](Group.md), [CapabilityGroup](CapabilityGroup.md) |
| Slot URI  | [schema:isPartOf](http://schema.org/isPartOf)            |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

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
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
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
</details></div>
```
