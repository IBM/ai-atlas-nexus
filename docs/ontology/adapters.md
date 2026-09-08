---
search:
  boost: 5.0
---

# Slot: adapters

_A list of Adapters_

<div data-search-exclude markdown="1">

URI: [nexus:adapters](https://w3id.org/ai-atlas-nexus/adapters)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                      | Description                                                | Modifies Slot |
| ------------------------- | ---------------------------------------------------------- | ------------- |
| [Container](Container.md) | An umbrella object that holds the ontology class instances | no            |

## Properties

### Type and Range

| Property  | Value                     |
| --------- | ------------------------- |
| Range     | [Adapter](Adapter.md)     |
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

| Mapping Type | Mapped Value   |
| ------------ | -------------- |
| self         | nexus:adapters |
| native       | nexus:adapters |

## LinkML Source

<details>
```yaml
name: adapters
description: A list of Adapters
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: Container
domain_of:
- Container
range: Adapter
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
```
