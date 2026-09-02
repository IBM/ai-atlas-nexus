---
search:
  boost: 5.0
---

# Slot: hasEvidenceCategory

_The evidence category, ie Technical Implementation, Operational Practices, etc._

<div data-search-exclude markdown="1">

URI: [nexus:hasEvidenceCategory](https://w3id.org/ai-atlas-nexus/hasEvidenceCategory)
Alias: hasEvidenceCategory

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |

## Properties

### Type and Range

| Property  | Value                                                                            |
| --------- | -------------------------------------------------------------------------------- |
| Range     | [AIUC1EvidenceCategory](AIUC1EvidenceCategory.md)                                |
| Domain    | [ControlActivity](ControlActivity.md)                                            |
| Domain Of | [ControlActivity](ControlActivity.md)                                            |
| Slot URI  | [nexus:hasEvidenceCategory](https://w3id.org/ai-atlas-nexus/hasEvidenceCategory) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value              |
| ------------ | ------------------------- |
| self         | nexus:hasEvidenceCategory |
| native       | nexus:hasEvidenceCategory |

## LinkML Source

<details>
```yaml
name: hasEvidenceCategory
description: The evidence category, ie Technical Implementation, Operational Practices,
  etc.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: ControlActivity
slot_uri: nexus:hasEvidenceCategory
alias: hasEvidenceCategory
domain_of:
- ControlActivity
range: AIUC1EvidenceCategory
multivalued: true
inlined: false

```
</details></div>
```
