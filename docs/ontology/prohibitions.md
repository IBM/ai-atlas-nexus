---
search:
  boost: 5.0
---

# Slot: prohibitions

_A list of prohibitions_

<div data-search-exclude markdown="1">

URI: [nexus:prohibitions](https://w3id.org/ai-atlas-nexus/prohibitions)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                      | Description                                                | Modifies Slot |
| ------------------------- | ---------------------------------------------------------- | ------------- |
| [Container](Container.md) | An umbrella object that holds the ontology class instances | no            |

## Properties

### Type and Range

| Property  | Value                         |
| --------- | ----------------------------- |
| Range     | [Prohibition](Prohibition.md) |
| Domain Of | [Container](Container.md)     |

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

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | nexus:prohibitions |
| native       | nexus:prohibitions |

## LinkML Source

<details>
```yaml
name: prohibitions
description: A list of prohibitions
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: Container
domain_of:
- Container
range: Prohibition
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
```
