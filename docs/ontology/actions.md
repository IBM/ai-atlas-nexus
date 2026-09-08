---
search:
  boost: 5.0
---

# Slot: actions

_A list of risk related actions_

<div data-search-exclude markdown="1">

URI: [nexus:actions](https://w3id.org/ai-atlas-nexus/actions)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                      | Description                                                | Modifies Slot |
| ------------------------- | ---------------------------------------------------------- | ------------- |
| [Container](Container.md) | An umbrella object that holds the ontology class instances | no            |

## Properties

### Type and Range

| Property  | Value                     |
| --------- | ------------------------- |
| Range     | [Action](Action.md)       |
| Domain Of | [Container](Container.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

### Slot Characteristics

| Property | Value                     |
| -------- | ------------------------- |
| Owner    | [Container](Container.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value  |
| ------------ | ------------- |
| self         | nexus:actions |
| native       | nexus:actions |

## LinkML Source

<details>
```yaml
name: actions
description: A list of risk related actions
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: Container
domain_of:
- Container
range: Action
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
```
