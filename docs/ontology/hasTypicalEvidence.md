# Slot: hasTypicalEvidence

_The evidence is usually found here_

URI: [nexus:hasTypicalEvidence](https://ibm.github.io/ai-atlas-nexus/ontology/hasTypicalEvidence)
Alias: hasTypicalEvidence

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

- Range: [String](String.md)

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasTypicalEvidence
alias: hasTypicalEvidence
domain_of:
- ControlActivity
range: string
multivalued: false
inlined: false

```
</details>
```
