# Slot: hasControlApplication

_Which of the AIUC-1 ControlApplicationCategory this control activity (rule) belongs to_

URI: [nexus:hasControlApplication](https://ibm.github.io/ai-atlas-nexus/ontology/hasControlApplication)
Alias: hasControlApplication

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

- Range: [AIUC1ControlApplicationCategory](AIUC1ControlApplicationCategory.md)

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value                |
| ------------ | --------------------------- |
| self         | nexus:hasControlApplication |
| native       | nexus:hasControlApplication |

## LinkML Source

<details>
```yaml
name: hasControlApplication
description: Which of the AIUC-1 ControlApplicationCategory this control activity
  (rule) belongs to
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasControlApplication
alias: hasControlApplication
domain_of:
- ControlActivity
range: AIUC1ControlApplicationCategory

```
</details>
```
