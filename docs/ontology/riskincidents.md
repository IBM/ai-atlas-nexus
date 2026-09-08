---
search:
  boost: 5.0
---

# Slot: riskincidents

_A list of AI risk incidents_

<div data-search-exclude markdown="1">

URI: [nexus:riskincidents](https://w3id.org/ai-atlas-nexus/riskincidents)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                      | Description                                                | Modifies Slot |
| ------------------------- | ---------------------------------------------------------- | ------------- |
| [Container](Container.md) | An umbrella object that holds the ontology class instances | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [RiskIncident](RiskIncident.md) |
| Domain Of | [Container](Container.md)       |

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

| Mapping Type | Mapped Value        |
| ------------ | ------------------- |
| self         | nexus:riskincidents |
| native       | nexus:riskincidents |

## LinkML Source

<details>
```yaml
name: riskincidents
description: A list of AI risk incidents
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: Container
domain_of:
- Container
range: RiskIncident
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
```
