---
search:
  boost: 5.0
---

# Slot: hasRequirementType

_The requirement type of whether this is preventive, detective, etc._

<div data-search-exclude markdown="1">

URI: [nexus:hasRequirementType](https://w3id.org/ai-atlas-nexus/hasRequirementType)
Alias: hasRequirementType

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Requirement](Requirement.md)                                     | A requirement representing a combination of obligation, permission, or prohib... | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |

## Properties

### Type and Range

| Property  | Value                                                                          |
| --------- | ------------------------------------------------------------------------------ |
| Range     | [AIUC1RequirementType](AIUC1RequirementType.md)                                |
| Domain    | [Any](Any.md)                                                                  |
| Domain Of | [ControlActivity](ControlActivity.md), [Requirement](Requirement.md)           |
| Slot URI  | [nexus:hasRequirementType](https://w3id.org/ai-atlas-nexus/hasRequirementType) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value             |
| ------------ | ------------------------ |
| self         | nexus:hasRequirementType |
| native       | nexus:hasRequirementType |

## LinkML Source

<details>
```yaml
name: hasRequirementType
description: The requirement type of whether this is preventive, detective, etc.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: Any
slot_uri: nexus:hasRequirementType
alias: hasRequirementType
domain_of:
- ControlActivity
- Requirement
range: AIUC1RequirementType

```
</details></div>
```
