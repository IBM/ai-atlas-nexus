---
search:
  boost: 5.0
---

# Slot: hasRequirement

_This requirement this rule belongs to_

<div data-search-exclude markdown="1">

URI: [nexus:hasRequirement](https://w3id.org/ai-atlas-nexus/hasRequirement)
Alias: hasRequirement

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |

## Properties

### Type and Range

| Property  | Value                                                                  |
| --------- | ---------------------------------------------------------------------- |
| Range     | [Requirement](Requirement.md)                                          |
| Domain    | [ControlActivity](ControlActivity.md)                                  |
| Domain Of | [ControlActivity](ControlActivity.md)                                  |
| Slot URI  | [nexus:hasRequirement](https://w3id.org/ai-atlas-nexus/hasRequirement) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | nexus:hasRequirement |
| native       | nexus:hasRequirement |

## LinkML Source

<details>
```yaml
name: hasRequirement
description: This requirement this rule belongs to
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: ControlActivity
slot_uri: nexus:hasRequirement
alias: hasRequirement
domain_of:
- ControlActivity
range: Requirement
multivalued: false
inlined: false

```
</details></div>
```
