# Slot: hasRequirement

_This requirement this rule belongs to_

URI: [nexus:hasRequirement](https://ibm.github.io/ai-atlas-nexus/ontology/hasRequirement)
Alias: hasRequirement

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |

## Properties

- Range: [Requirement](Requirement.md)

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasRequirement
alias: hasRequirement
domain_of:
- ControlActivity
range: Requirement
multivalued: false
inlined: false

```
</details>
```
