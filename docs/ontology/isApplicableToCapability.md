---
search:
  boost: 5.0
---

# Slot: isApplicableToCapability

_This evidence only applies to AI systems with this capability_

<div data-search-exclude markdown="1">

URI: [nexus:isApplicableToCapability](https://w3id.org/ai-atlas-nexus/isApplicableToCapability)
Alias: isApplicableToCapability

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |
| [Requirement](Requirement.md)                                     | A requirement representing a combination of obligation, permission, or prohib... | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |

## Properties

### Type and Range

| Property  | Value                                                                                      |
| --------- | ------------------------------------------------------------------------------------------ |
| Range     | [AiTask](AiTask.md)                                                                        |
| Domain    | [ControlActivity](ControlActivity.md)                                                      |
| Domain Of | [ControlActivity](ControlActivity.md), [Requirement](Requirement.md)                       |
| Slot URI  | [nexus:isApplicableToCapability](https://w3id.org/ai-atlas-nexus/isApplicableToCapability) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value                   |
| ------------ | ------------------------------ |
| self         | nexus:isApplicableToCapability |
| native       | nexus:isApplicableToCapability |

## LinkML Source

<details>
```yaml
name: isApplicableToCapability
description: This evidence only applies to AI systems with this capability
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: ControlActivity
slot_uri: nexus:isApplicableToCapability
alias: isApplicableToCapability
domain_of:
- ControlActivity
- Requirement
range: AiTask
multivalued: true
inlined: false

```
</details></div>
```
