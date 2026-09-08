---
search:
  boost: 5.0
---

# Slot: hasVariant

_Indicates an incident that shares the same causative factors, produces similar harms, and involves the same intelligent systems as a known AI incident._

<div data-search-exclude markdown="1">

URI: [nexus:hasVariant](https://w3id.org/ai-atlas-nexus/hasVariant)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                                                           | Modifies Slot |
| ------------------------------- | --------------------------------------------------------------------- | ------------- |
| [RiskIncident](RiskIncident.md) | An event occuring or occured which is a realised or materialised risk | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [RiskIncident](RiskIncident.md) |
| Domain    | [RiskIncident](RiskIncident.md) |
| Domain Of | [RiskIncident](RiskIncident.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value     |
| ------------ | ---------------- |
| self         | nexus:hasVariant |
| native       | nexus:hasVariant |

## LinkML Source

<details>
```yaml
name: hasVariant
description: Indicates an incident that shares the same causative factors, produces
  similar harms, and involves the same intelligent systems as a known AI incident.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: RiskIncident
domain_of:
- RiskIncident
range: RiskIncident

```
</details></div>
```
