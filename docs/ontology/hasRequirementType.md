# Slot: hasRequirementType

_The requirement type of whether this is preventive, detective, etc._

URI: [nexus:hasRequirementType](https://ibm.github.io/ai-atlas-nexus/ontology/hasRequirementType)
Alias: hasRequirementType

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [Requirement](Requirement.md)                                     | A requirement representing a combination of obligation, permission, or prohib... | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |

## Properties

- Range: [AIUC1RequirementType](AIUC1RequirementType.md)

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasRequirementType
alias: hasRequirementType
domain_of:
- ControlActivity
- Requirement
range: AIUC1RequirementType

```
</details>
```
