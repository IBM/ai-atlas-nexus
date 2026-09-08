---
search:
  boost: 5.0
---

# Slot: permissions

_A list of Permissions_

<div data-search-exclude markdown="1">

URI: [nexus:permissions](https://w3id.org/ai-atlas-nexus/permissions)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                      | Description                                                | Modifies Slot |
| ------------------------- | ---------------------------------------------------------- | ------------- |
| [Container](Container.md) | An umbrella object that holds the ontology class instances | no            |

## Properties

### Type and Range

| Property  | Value                       |
| --------- | --------------------------- |
| Range     | [Permission](Permission.md) |
| Domain Of | [Container](Container.md)   |

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

| Mapping Type | Mapped Value      |
| ------------ | ----------------- |
| self         | nexus:permissions |
| native       | nexus:permissions |

## LinkML Source

<details>
```yaml
name: permissions
description: A list of Permissions
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: Container
domain_of:
- Container
range: Permission
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
```
