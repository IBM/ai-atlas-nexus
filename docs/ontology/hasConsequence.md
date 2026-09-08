---
search:
  boost: 5.0
---

# Slot: hasConsequence

_Indicates consequence(s) possible or arising from specified concept_

<div data-search-exclude markdown="1">

URI: [nexus:hasConsequence](https://w3id.org/ai-atlas-nexus/hasConsequence)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                                                           | Modifies Slot |
| ------------------------------- | --------------------------------------------------------------------- | ------------- |
| [RiskIncident](RiskIncident.md) | An event occuring or occured which is a realised or materialised risk | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [Consequence](Consequence.md)   |
| Domain    | [RiskConcept](RiskConcept.md)   |
| Domain Of | [RiskIncident](RiskIncident.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | nexus:hasConsequence |
| native       | nexus:hasConsequence |

## LinkML Source

<details>
```yaml
name: hasConsequence
description: Indicates consequence(s) possible or arising from specified concept
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: RiskConcept
domain_of:
- RiskIncident
range: Consequence

```
</details></div>
```
