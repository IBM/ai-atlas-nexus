---
search:
  boost: 5.0
---

# Slot: type

<div data-search-exclude markdown="1">

URI: [nexus:type](https://w3id.org/ai-atlas-nexus/type)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Vocabulary](Vocabulary.md)                                       | A collection of terms, with their definitions and relationships                  | no            |
| [Taxonomy](Taxonomy.md)                                           | A hierachical taxonomy of concepts, with their definitions and relationships     | no            |
| [Concept](Concept.md)                                             | A concept                                                                        | no            |
| [Control](Control.md)                                             | A measure that maintains and/or modifies                                         | no            |
| [Group](Group.md)                                                 | Labelled groups of concepts                                                      | no            |
| [Entry](Entry.md)                                                 | An entry and its definitions                                                     | no            |
| [Term](Term.md)                                                   | A term and its definitions                                                       | no            |
| [Principle](Principle.md)                                         | A representation of values or norms that must be taken into consideration whe... | no            |
| [Policy](Policy.md)                                               | A guidance document outlining any of: procedures, plans, principles, decision... | no            |
| [LLMQuestionPolicy](LLMQuestionPolicy.md)                         | The policy guides how the language model should answer a diverse set of sensi... | no            |
| [Rule](Rule.md)                                                   | A rule describing a process or control that directs or determines if and how ... | no            |
| [AttributeConditionRule](AttributeConditionRule.md)               |                                                                                  | no            |
| [Permission](Permission.md)                                       | A rule describing a permission to perform an activity                            | no            |
| [Prohibition](Prohibition.md)                                     | A rule describing a prohibition to perform an activity                           | no            |
| [Obligation](Obligation.md)                                       | A rule describing an obligation for performing an activity                       | no            |
| [Recommendation](Recommendation.md)                               | A rule describing a recommendation for performing an activity                    | no            |
| [Certification](Certification.md)                                 | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [LocalityOfUse](LocalityOfUse.md)                                 | The area, e                                                                      | no            |
| [RiskTaxonomy](RiskTaxonomy.md)                                   | A taxonomy of AI system related risks                                            | no            |
| [RiskControlGroupTaxonomy](RiskControlGroupTaxonomy.md)           | A taxonomy of AI system related risk controls groups                             | no            |
| [RiskControlGroup](RiskControlGroup.md)                           | A group of AI system related risk controls                                       | no            |
| [RiskGroup](RiskGroup.md)                                         | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [Risk](Risk.md)                                                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [RiskConcept](RiskConcept.md)                                     | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [RiskControl](RiskControl.md)                                     | A measure that maintains and/or modifies risk (and risk concepts)                | no            |
| [Action](Action.md)                                               | Action to remediate a risk                                                       | no            |
| [RiskIncident](RiskIncident.md)                                   | An event occuring or occured which is a realised or materialised risk            | no            |
| [Impact](Impact.md)                                               |                                                                                  | no            |
| [CapabilityTaxonomy](CapabilityTaxonomy.md)                       | A taxonomy of AI capabilities describing the abilities of AI systems             | no            |
| [CapabilityConcept](CapabilityConcept.md)                         | An umbrella term for referring to capability domains, groups, and individual ... | no            |
| [CapabilityDomain](CapabilityDomain.md)                           | A high-level domain of AI capabilities (e                                        | no            |
| [CapabilityGroup](CapabilityGroup.md)                             | A group of AI capabilities that are part of a capability taxonomy, organized ... | no            |
| [Capability](Capability.md)                                       | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [AiSystem](AiSystem.md)                                           | A compound AI System composed of one or more AI capablities                      | no            |
| [AiAgent](AiAgent.md)                                             | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AiTask](AiTask.md)                                               | A task, such as summarization and classification, performed by an AI             | no            |
| [AiTaskTaxonomy](AiTaskTaxonomy.md)                               | A taxonomy of AI Tasks                                                           | no            |
| [AiTaskDomain](AiTaskDomain.md)                                   | A grouping of AI Tasks by domain                                                 | no            |
| [AiTaskGroup](AiTaskGroup.md)                                     | A group of AI Tasks                                                              | no            |
| [Purpose](Purpose.md)                                             | The end goal for which an entity is used or an action is taken                   | no            |
| [Domain](Domain.md)                                               | An area, sector, or industry that is associated with economic activities         | no            |
| [StakeholderGroup](StakeholderGroup.md)                           | An AI system stakeholder grouping                                                | no            |
| [BenchmarkMetadataCard](BenchmarkMetadataCard.md)                 | Benchmark metadata cards offer a standardized way to document LLM benchmarks ... | no            |
| [Adapter](Adapter.md)                                             | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [LLMIntrinsic](LLMIntrinsic.md)                                   | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |
| [Requirement](Requirement.md)                                     | A requirement representing a combination of obligation, permission, or prohib... | no            |

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
