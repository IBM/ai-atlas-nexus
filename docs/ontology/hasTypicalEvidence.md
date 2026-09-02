---
search:
  boost: 5.0
---

# Slot: hasTypicalEvidence

_The evidence is usually found here_

<div data-search-exclude markdown="1">

URI: [nexus:hasTypicalEvidence](https://w3id.org/ai-atlas-nexus/hasTypicalEvidence)
Alias: hasTypicalEvidence

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

| Property  | Value                                                                          |
| --------- | ------------------------------------------------------------------------------ |
| Range     | [String](String.md)                                                            |
| Domain    | [ControlActivity](ControlActivity.md)                                          |
| Domain Of | [ControlActivity](ControlActivity.md)                                          |
| Slot URI  | [nexus:hasTypicalEvidence](https://w3id.org/ai-atlas-nexus/hasTypicalEvidence) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value             |
| ------------ | ------------------------ |
| self         | nexus:hasTypicalEvidence |
| native       | nexus:hasTypicalEvidence |

## LinkML Source

<details>
```yaml
name: hasTypicalEvidence
description: The evidence is usually found here
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: ControlActivity
slot_uri: nexus:hasTypicalEvidence
alias: hasTypicalEvidence
domain_of:
- ControlActivity
range: string
multivalued: false
inlined: false

```
</details></div>
```
