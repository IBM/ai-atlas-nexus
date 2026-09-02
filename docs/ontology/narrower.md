---
search:
  boost: 5.0
---

# Slot: narrower

_Related concepts that are narrower in scope or hierarchy._

<div data-search-exclude markdown="1">

URI: [skos:narrower](http://www.w3.org/2004/02/skos/core#narrower)
Alias: narrower

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                    | Description                                                                      | Modifies Slot |
| --------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [StakeholderGroup](StakeholderGroup.md) | An AI system stakeholder grouping                                                | no            |
| [CapabilityGroup](CapabilityGroup.md)   | A group of AI capabilities that are part of a capability taxonomy, organized ... | no            |
| [Group](Group.md)                       | Labelled groups of concepts                                                      | no            |
| [CapabilityDomain](CapabilityDomain.md) | A high-level domain of AI capabilities (e                                        | no            |
| [AiTaskGroup](AiTaskGroup.md)           | A group of AI Tasks                                                              | no            |
| [AiTaskDomain](AiTaskDomain.md)         | A grouping of AI Tasks by domain                                                 | no            |
| [RiskGroup](RiskGroup.md)               | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [RiskControlGroup](RiskControlGroup.md) | A group of AI system related risk controls                                       | no            |

## Properties

### Type and Range

| Property  | Value                                                         |
| --------- | ------------------------------------------------------------- |
| Range     | [String](String.md)                                           |
| Domain Of | [Group](Group.md)                                             |
| Slot URI  | [skos:narrower](http://www.w3.org/2004/02/skos/core#narrower) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

### Slot Characteristics

| Property | Value             |
| -------- | ----------------- |
| Owner    | [Group](Group.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value   |
| ------------ | -------------- |
| self         | skos:narrower  |
| native       | nexus:narrower |

## LinkML Source

<details>
```yaml
name: narrower
description: Related concepts that are narrower in scope or hierarchy.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: skos:narrower
alias: narrower
owner: Group
domain_of:
- Group
range: string
multivalued: true

```
</details></div>
```
