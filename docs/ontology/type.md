---
search:
  boost: 5.0
---

# Slot: type

<div data-search-exclude markdown="1">

URI: [nexus:type](https://w3id.org/ai-atlas-nexus/type)
Alias: type

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [CapabilityTaxonomy](CapabilityTaxonomy.md)                       | A taxonomy of AI capabilities describing the abilities of AI systems             | no            |
| [Capability](Capability.md)                                       | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [RiskControlGroup](RiskControlGroup.md)                           | A group of AI system related risk controls                                       | no            |
| [RiskGroup](RiskGroup.md)                                         | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [AiTaskGroup](AiTaskGroup.md)                                     | A group of AI Tasks                                                              | no            |
| [StakeholderGroup](StakeholderGroup.md)                           | An AI system stakeholder grouping                                                | no            |
| [RiskConcept](RiskConcept.md)                                     | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [AiTaskDomain](AiTaskDomain.md)                                   | A grouping of AI Tasks by domain                                                 | no            |
| [CapabilityDomain](CapabilityDomain.md)                           | A high-level domain of AI capabilities (e                                        | no            |
| [RiskIncident](RiskIncident.md)                                   | An event occuring or occured which is a realised or materialised risk            | no            |
| [Certification](Certification.md)                                 | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |
| [Requirement](Requirement.md)                                     | A requirement representing a combination of obligation, permission, or prohib... | no            |
| [AiTaskTaxonomy](AiTaskTaxonomy.md)                               | A taxonomy of AI Tasks                                                           | no            |
| [Adapter](Adapter.md)                                             | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [Purpose](Purpose.md)                                             | The end goal for which an entity is used or an action is taken                   | no            |
| [Principle](Principle.md)                                         | A representation of values or norms that must be taken into consideration whe... | no            |
| [RiskControlGroupTaxonomy](RiskControlGroupTaxonomy.md)           | A taxonomy of AI system related risk controls groups                             | no            |
| [RiskTaxonomy](RiskTaxonomy.md)                                   | A taxonomy of AI system related risks                                            | no            |
| [AiAgent](AiAgent.md)                                             | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [Domain](Domain.md)                                               | An area, sector, or industry that is associated with economic activities         | no            |
| [Vocabulary](Vocabulary.md)                                       | A collection of terms, with their definitions and relationships                  | no            |
| [AiSystem](AiSystem.md)                                           | A compound AI System composed of one or more AI capablities                      | no            |
| [Risk](Risk.md)                                                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [LLMIntrinsic](LLMIntrinsic.md)                                   | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [RiskControl](RiskControl.md)                                     | A measure that maintains and/or modifies risk (and risk concepts)                | no            |
| [Recommendation](Recommendation.md)                               | A rule describing a recommendation for performing an activity                    | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |
| [Prohibition](Prohibition.md)                                     | A rule describing a prohibition to perform an activity                           | no            |
| [Entry](Entry.md)                                                 | An entry and its definitions                                                     | no            |
| [Permission](Permission.md)                                       | A rule describing a permission to perform an activity                            | no            |
| [Policy](Policy.md)                                               | A guidance document outlining any of: procedures, plans, principles, decision... | no            |
| [LLMQuestionPolicy](LLMQuestionPolicy.md)                         | The policy guides how the language model should answer a diverse set of sensi... | no            |
| [Concept](Concept.md)                                             | A concept                                                                        | no            |
| [BenchmarkMetadataCard](BenchmarkMetadataCard.md)                 | Benchmark metadata cards offer a standardized way to document LLM benchmarks ... | no            |
| [Action](Action.md)                                               | Action to remediate a risk                                                       | no            |
| [Impact](Impact.md)                                               |                                                                                  | no            |
| [Term](Term.md)                                                   | A term and its definitions                                                       | no            |
| [Taxonomy](Taxonomy.md)                                           | A hierachical taxonomy of concepts, with their definitions and relationships     | no            |
| [Group](Group.md)                                                 | Labelled groups of concepts                                                      | no            |
| [AiTask](AiTask.md)                                               | A task, such as summarization and classification, performed by an AI             | no            |
| [Control](Control.md)                                             | A measure that maintains and/or modifies                                         | no            |
| [LocalityOfUse](LocalityOfUse.md)                                 | The area, e                                                                      | no            |
| [Rule](Rule.md)                                                   | A rule describing a process or control that directs or determines if and how ... | no            |
| [Obligation](Obligation.md)                                       | A rule describing an obligation for performing an activity                       | no            |
| [AttributeConditionRule](AttributeConditionRule.md)               |                                                                                  | no            |
| [CapabilityConcept](CapabilityConcept.md)                         | An umbrella term for referring to capability domains, groups, and individual ... | no            |
| [CapabilityGroup](CapabilityGroup.md)                             | A group of AI capabilities that are part of a capability taxonomy, organized ... | no            |

## Properties

### Type and Range

| Property  | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Range     | [String](String.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Domain Of | [Vocabulary](Vocabulary.md), [Taxonomy](Taxonomy.md), [Concept](Concept.md), [Control](Control.md), [Group](Group.md), [Entry](Entry.md), [Policy](Policy.md), [Rule](Rule.md), [Permission](Permission.md), [Prohibition](Prohibition.md), [Obligation](Obligation.md), [Recommendation](Recommendation.md), [Certification](Certification.md), [BenchmarkMetadataCard](BenchmarkMetadataCard.md), [ControlActivity](ControlActivity.md), [ControlActivityPermission](ControlActivityPermission.md), [ControlActivityProhibition](ControlActivityProhibition.md), [ControlActivityObligation](ControlActivityObligation.md), [ControlActivityRecommendation](ControlActivityRecommendation.md), [Requirement](Requirement.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

## Mappings

| Mapping Type | Mapped Value |
| ------------ | ------------ |
| self         | nexus:type   |
| native       | nexus:type   |

## LinkML Source

<details>
```yaml
name: type
alias: type
domain_of:
- Vocabulary
- Taxonomy
- Concept
- Control
- Group
- Entry
- Policy
- Rule
- Permission
- Prohibition
- Obligation
- Recommendation
- Certification
- BenchmarkMetadataCard
- ControlActivity
- ControlActivityPermission
- ControlActivityProhibition
- ControlActivityObligation
- ControlActivityRecommendation
- Requirement
range: string

```
</details></div>
```
