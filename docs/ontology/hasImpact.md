---
search:
  boost: 5.0
---

# Slot: hasImpact

_Indicates impact(s) possible or arising as consequences from specified concept_

<div data-search-exclude markdown="1">

URI: [nexus:hasImpact](https://w3id.org/ai-atlas-nexus/hasImpact)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                                                           | Modifies Slot |
| ------------------------------- | --------------------------------------------------------------------- | ------------- |
| [RiskIncident](RiskIncident.md) | An event occuring or occured which is a realised or materialised risk | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [Impact](Impact.md)             |
| Domain    | [RiskConcept](RiskConcept.md)   |
| Domain Of | [RiskIncident](RiskIncident.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | nexus:hasImpact    |
| native       | nexus:hasImpact    |
| broad        | dpv:hasConsequence |

## LinkML Source

<details>
```yaml
name: hasImpact
description: Indicates impact(s) possible or arising as consequences from specified
  concept
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
broad_mappings:
- dpv:hasConsequence
rank: 1000
domain: RiskConcept
domain_of:
- RiskIncident
range: Impact

```
</details></div>
```
