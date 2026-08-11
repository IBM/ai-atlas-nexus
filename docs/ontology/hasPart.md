---
search:
  boost: 5.0
---

# Slot: hasPart

_A relationship where an entity has another entity_

<div data-search-exclude markdown="1">

URI: [skos:member](http://www.w3.org/2004/02/skos/core#member)
Alias: hasPart

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                    | Description                                                                      | Modifies Slot |
| --------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [RiskControlGroup](RiskControlGroup.md) | A group of AI system related risk controls                                       | yes           |
| [RiskGroup](RiskGroup.md)               | A group of AI system related risks that are part of a risk taxonomy              | yes           |
| [Group](Group.md)                       | Labelled groups of concepts                                                      | no            |
| [AiTaskGroup](AiTaskGroup.md)           | A group of AI Tasks                                                              | yes           |
| [StakeholderGroup](StakeholderGroup.md) | An AI system stakeholder grouping                                                | no            |
| [AiTaskDomain](AiTaskDomain.md)         | A grouping of AI Tasks by domain                                                 | yes           |
| [CapabilityDomain](CapabilityDomain.md) | A high-level domain of AI capabilities (e                                        | yes           |
| [CapabilityGroup](CapabilityGroup.md)   | A group of AI capabilities that are part of a capability taxonomy, organized ... | yes           |

## Properties

### Type and Range

| Property  | Value                                                                                                                                                                                        |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Range     | [String](String.md)                                                                                                                                                                          |
| Domain Of | [Group](Group.md), [RiskControlGroup](RiskControlGroup.md), [RiskGroup](RiskGroup.md), [CapabilityGroup](CapabilityGroup.md), [AiTaskDomain](AiTaskDomain.md), [AiTaskGroup](AiTaskGroup.md) |
| Slot URI  | [skos:member](http://www.w3.org/2004/02/skos/core#member)                                                                                                                                    |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

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
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: skos:member
alias: hasPart
domain_of:
- Group
- RiskControlGroup
- RiskGroup
- CapabilityGroup
- AiTaskDomain
- AiTaskGroup
range: string
multivalued: true

```
</details></div>
```
