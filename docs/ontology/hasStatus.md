---
search:
  boost: 5.0
---

# Slot: hasStatus

_Indicates the status of specified concept_

<div data-search-exclude markdown="1">

URI: [nexus:hasStatus](https://w3id.org/ai-atlas-nexus/hasStatus)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                                                           | Modifies Slot |
| ------------------------------- | --------------------------------------------------------------------- | ------------- |
| [RiskIncident](RiskIncident.md) | An event occuring or occured which is a realised or materialised risk | no            |

## Properties

### Type and Range

| Property  | Value                               |
| --------- | ----------------------------------- |
| Range     | [IncidentStatus](IncidentStatus.md) |
| Domain    | [RiskConcept](RiskConcept.md)       |
| Domain Of | [RiskIncident](RiskIncident.md)     |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value    |
| ------------ | --------------- |
| self         | nexus:hasStatus |
| native       | nexus:hasStatus |

## LinkML Source

<details>
```yaml
name: hasStatus
description: Indicates the status of specified concept
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: RiskConcept
domain_of:
- RiskIncident
range: IncidentStatus

```
</details></div>
```
