---
search:
  boost: 5.0
---

# Slot: refersToRisk

_Indicates the incident (subject) is a materialisation of the indicated risk (object)_

<div data-search-exclude markdown="1">

URI: [nexus:refersToRisk](https://w3id.org/ai-atlas-nexus/refersToRisk)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                                                           | Modifies Slot |
| ------------------------------- | --------------------------------------------------------------------- | ------------- |
| [RiskIncident](RiskIncident.md) | An event occuring or occured which is a realised or materialised risk | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [Risk](Risk.md)                 |
| Domain    | [RiskIncident](RiskIncident.md) |
| Domain Of | [RiskIncident](RiskIncident.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | nexus:refersToRisk |
| native       | nexus:refersToRisk |
| exact        | dpv:refersToRisk   |

## LinkML Source

<details>
```yaml
name: refersToRisk
description: Indicates the incident (subject) is a materialisation of the indicated
  risk (object)
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
exact_mappings:
- dpv:refersToRisk
rank: 1000
domain: RiskIncident
domain_of:
- RiskIncident
range: Risk
multivalued: true
inlined: false

```
</details></div>
```
