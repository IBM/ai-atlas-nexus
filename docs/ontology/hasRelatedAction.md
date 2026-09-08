---
search:
  boost: 5.0
---

# Slot: hasRelatedAction

_A relationship where an entity relates to an action_

<div data-search-exclude markdown="1">

URI: [nexus:hasRelatedAction](https://w3id.org/ai-atlas-nexus/hasRelatedAction)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name            | Description                                                                      | Modifies Slot |
| --------------- | -------------------------------------------------------------------------------- | ------------- |
| [Risk](Risk.md) | The state of uncertainty associated with an AI system, that has the potential... | no            |

## Properties

### Type and Range

| Property  | Value               |
| --------- | ------------------- |
| Range     | [Action](Action.md) |
| Domain Of | [Risk](Risk.md)     |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value           |
| ------------ | ---------------------- |
| self         | nexus:hasRelatedAction |
| native       | nexus:hasRelatedAction |

## LinkML Source

<details>
```yaml
name: hasRelatedAction
description: A relationship where an entity relates to an action
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- Risk
range: Action
multivalued: true
inlined: false

```
</details></div>
```
