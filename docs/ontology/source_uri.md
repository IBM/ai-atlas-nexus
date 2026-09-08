---
search:
  boost: 5.0
---

# Slot: source_uri

_The uri of the incident_

<div data-search-exclude markdown="1">

URI: [nexus:source_uri](https://w3id.org/ai-atlas-nexus/source_uri)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                                                           | Modifies Slot |
| ------------------------------- | --------------------------------------------------------------------- | ------------- |
| [RiskIncident](RiskIncident.md) | An event occuring or occured which is a realised or materialised risk | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [String](String.md)             |
| Domain Of | [RiskIncident](RiskIncident.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

### Slot Characteristics

| Property | Value                           |
| -------- | ------------------------------- |
| Owner    | [RiskIncident](RiskIncident.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value     |
| ------------ | ---------------- |
| self         | nexus:source_uri |
| native       | nexus:source_uri |

## LinkML Source

<details>
```yaml
name: source_uri
description: The uri of the incident
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
owner: RiskIncident
domain_of:
- RiskIncident
range: string

```
</details></div>
```
