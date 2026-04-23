# Slot: hasRule

_Specifying applicability or inclusion of a rule within specified context._

URI: [dpv:hasRule](https://w3id.org/dpv#hasRule)
Alias: hasRule

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Requirement](Requirement.md)                                     | A requirement representing a combination of obligation, permission, or prohib... | yes           |
| [Recommendation](Recommendation.md)                               | A rule describing a recommendation for performing an activity                    | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [Prohibition](Prohibition.md)                                     | A rule describing a prohibition to perform an activity                           | no            |
| [Rule](Rule.md)                                                   | A rule describing a process or control that directs or determines if and how ... | no            |
| [Obligation](Obligation.md)                                       | A rule describing an obligation for performing an activity                       | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [LLMQuestionPolicy](LLMQuestionPolicy.md)                         | The policy guides how the language model should answer a diverse set of sensi... | no            |
| [Permission](Permission.md)                                       | A rule describing a permission to perform an activity                            | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |

## Properties

### Type and Range

| Property  | Value                                                                                     |
| --------- | ----------------------------------------------------------------------------------------- |
| Range     | [Rule](Rule.md)                                                                           |
| Domain Of | [LLMQuestionPolicy](LLMQuestionPolicy.md), [Rule](Rule.md), [Requirement](Requirement.md) |
| Slot URI  | [dpv:hasRule](https://w3id.org/dpv#hasRule)                                               |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value  |
| ------------ | ------------- |
| self         | dpv:hasRule   |
| native       | nexus:hasRule |

## LinkML Source

<details>
```yaml
name: hasRule
description: Specifying applicability or inclusion of a rule within specified context.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: dpv:hasRule
alias: hasRule
domain_of:
- LLMQuestionPolicy
- Rule
- Requirement
range: Rule
multivalued: true
inlined: false

```
</details>
```
