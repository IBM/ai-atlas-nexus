---
search:
  boost: 5.0
---

# Slot: hasSeverity

_Indicates the severity associated with a concept_

<div data-search-exclude markdown="1">

URI: [nexus:hasSeverity](https://w3id.org/ai-atlas-nexus/hasSeverity)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                                                           | Modifies Slot |
| ------------------------------- | --------------------------------------------------------------------- | ------------- |
| [RiskIncident](RiskIncident.md) | An event occuring or occured which is a realised or materialised risk | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [Severity](Severity.md)         |
| Domain    | [RiskConcept](RiskConcept.md)   |
| Domain Of | [RiskIncident](RiskIncident.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value      |
| ------------ | ----------------- |
| self         | nexus:hasSeverity |
| native       | nexus:hasSeverity |

## LinkML Source

<details>
```yaml
name: hasSeverity
description: Indicates the severity associated with a concept
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: RiskConcept
domain_of:
- RiskIncident
range: Severity

```
</details></div>
```
