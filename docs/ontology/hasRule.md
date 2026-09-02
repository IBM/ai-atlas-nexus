---
search:
  boost: 5.0
---

# Slot: hasRule

_Specifying applicability or inclusion of a rule within specified context._

<div data-search-exclude markdown="1">

URI: [dpv:hasRule](https://w3id.org/dpv#hasRule)
Alias: hasRule

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiTask](AiTask.md)                                               | A task, such as summarization and classification, performed by an AI             | no            |
| [Principle](Principle.md)                                         | A representation of values or norms that must be taken into consideration whe... | no            |
| [Domain](Domain.md)                                               | An area, sector, or industry that is associated with economic activities         | no            |
| [Term](Term.md)                                                   | A term and its definitions                                                       | no            |
| [Entry](Entry.md)                                                 | An entry and its definitions                                                     | no            |
| [Purpose](Purpose.md)                                             | The end goal for which an entity is used or an action is taken                   | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |
| [Recommendation](Recommendation.md)                               | A rule describing a recommendation for performing an activity                    | no            |
| [Obligation](Obligation.md)                                       | A rule describing an obligation for performing an activity                       | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |
| [Requirement](Requirement.md)                                     | A requirement representing a combination of obligation, permission, or prohib... | yes           |
| [Permission](Permission.md)                                       | A rule describing a permission to perform an activity                            | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [Certification](Certification.md)                                 | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [LLMIntrinsic](LLMIntrinsic.md)                                   | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [Prohibition](Prohibition.md)                                     | A rule describing a prohibition to perform an activity                           | no            |
| [Capability](Capability.md)                                       | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [LLMQuestionPolicy](LLMQuestionPolicy.md)                         | The policy guides how the language model should answer a diverse set of sensi... | no            |
| [LocalityOfUse](LocalityOfUse.md)                                 | The area, e                                                                      | no            |
| [AiSystem](AiSystem.md)                                           | A compound AI System composed of one or more AI capablities                      | no            |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [Risk](Risk.md)                                                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [AiAgent](AiAgent.md)                                             | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AttributeConditionRule](AttributeConditionRule.md)               |                                                                                  | no            |
| [Adapter](Adapter.md)                                             | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [Rule](Rule.md)                                                   | A rule describing a process or control that directs or determines if and how ... | no            |

## Properties

### Type and Range

| Property  | Value                                                                                                        |
| --------- | ------------------------------------------------------------------------------------------------------------ |
| Range     | [Rule](Rule.md)                                                                                              |
| Domain Of | [Entry](Entry.md), [LLMQuestionPolicy](LLMQuestionPolicy.md), [Rule](Rule.md), [Requirement](Requirement.md) |
| Slot URI  | [dpv:hasRule](https://w3id.org/dpv#hasRule)                                                                  |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

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
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: dpv:hasRule
alias: hasRule
domain_of:
- Entry
- LLMQuestionPolicy
- Rule
- Requirement
range: Rule
multivalued: true
inlined: false

```
</details></div>
```
