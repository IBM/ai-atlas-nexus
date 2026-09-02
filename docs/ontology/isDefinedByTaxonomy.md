---
search:
  boost: 5.0
---

# Slot: isDefinedByTaxonomy

_A relationship where a concept or a concept group is defined by a taxonomy_

<div data-search-exclude markdown="1">

URI: [schema:isPartOf](http://schema.org/isPartOf)
Alias: isDefinedByTaxonomy

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Action](Action.md)                                               | Action to remediate a risk                                                       | no            |
| [Stakeholder](Stakeholder.md)                                     | Represents any individual, group or organization that can affect, be affected... | no            |
| [Principle](Principle.md)                                         | A representation of values or norms that must be taken into consideration whe... | no            |
| [AiTask](AiTask.md)                                               | A task, such as summarization and classification, performed by an AI             | no            |
| [Domain](Domain.md)                                               | An area, sector, or industry that is associated with economic activities         | no            |
| [Term](Term.md)                                                   | A term and its definitions                                                       | no            |
| [Impact](Impact.md)                                               |                                                                                  | no            |
| [Entry](Entry.md)                                                 | An entry and its definitions                                                     | no            |
| [Purpose](Purpose.md)                                             | The end goal for which an entity is used or an action is taken                   | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |
| [StakeholderGroup](StakeholderGroup.md)                           | An AI system stakeholder grouping                                                | no            |
| [Recommendation](Recommendation.md)                               | A rule describing a recommendation for performing an activity                    | no            |
| [Obligation](Obligation.md)                                       | A rule describing an obligation for performing an activity                       | no            |
| [Concept](Concept.md)                                             | A concept                                                                        | no            |
| [Requirement](Requirement.md)                                     | A requirement representing a combination of obligation, permission, or prohib... | no            |
| [CapabilityGroup](CapabilityGroup.md)                             | A group of AI capabilities that are part of a capability taxonomy, organized ... | no            |
| [Permission](Permission.md)                                       | A rule describing a permission to perform an activity                            | no            |
| [AIDeveloper](AIDeveloper.md)                                     | An organisation or entity that is concerned with the development of AI servic... | no            |
| [Certification](Certification.md)                                 | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |
| [RiskIncident](RiskIncident.md)                                   | An event occuring or occured which is a realised or materialised risk            | no            |
| [AiTaskDomain](AiTaskDomain.md)                                   | A grouping of AI Tasks by domain                                                 | no            |
| [CapabilityConcept](CapabilityConcept.md)                         | An umbrella term for referring to capability domains, groups, and individual ... | no            |
| [LLMIntrinsic](LLMIntrinsic.md)                                   | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [AIDeployer](AIDeployer.md)                                       | Any natural or legal person, public authority, agency or other body using an ... | no            |
| [RiskControlGroup](RiskControlGroup.md)                           | A group of AI system related risk controls                                       | no            |
| [Prohibition](Prohibition.md)                                     | A rule describing a prohibition to perform an activity                           | no            |
| [AIOperator](AIOperator.md)                                       | Refers to a provider, product manufacturer, deployer, authorised representati... | no            |
| [AIUser](AIUser.md)                                               | Individual or group that interacts with a system                                 | no            |
| [Capability](Capability.md)                                       | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [Policy](Policy.md)                                               | A guidance document outlining any of: procedures, plans, principles, decision... | no            |
| [LLMQuestionPolicy](LLMQuestionPolicy.md)                         | The policy guides how the language model should answer a diverse set of sensi... | no            |
| [LocalityOfUse](LocalityOfUse.md)                                 | The area, e                                                                      | no            |
| [RiskConcept](RiskConcept.md)                                     | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [AiSystem](AiSystem.md)                                           | A compound AI System composed of one or more AI capablities                      | no            |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [Risk](Risk.md)                                                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [RiskGroup](RiskGroup.md)                                         | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [AISubject](AISubject.md)                                         | An entity that is subject to or impacted by the use of AI                        | no            |
| [Group](Group.md)                                                 | Labelled groups of concepts                                                      | no            |
| [AiAgent](AiAgent.md)                                             | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AttributeConditionRule](AttributeConditionRule.md)               |                                                                                  | no            |
| [CapabilityDomain](CapabilityDomain.md)                           | A high-level domain of AI capabilities (e                                        | no            |
| [Adapter](Adapter.md)                                             | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [AiTaskGroup](AiTaskGroup.md)                                     | A group of AI Tasks                                                              | no            |
| [Rule](Rule.md)                                                   | A rule describing a process or control that directs or determines if and how ... | no            |
| [Control](Control.md)                                             | A measure that maintains and/or modifies                                         | no            |
| [RiskControl](RiskControl.md)                                     | A measure that maintains and/or modifies risk (and risk concepts)                | no            |

## Properties

### Type and Range

| Property  | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Range     | [Taxonomy](Taxonomy.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Domain Of | [Concept](Concept.md), [Control](Control.md), [Group](Group.md), [Entry](Entry.md), [Policy](Policy.md), [Rule](Rule.md), [RiskControlGroup](RiskControlGroup.md), [RiskGroup](RiskGroup.md), [Risk](Risk.md), [RiskControl](RiskControl.md), [Action](Action.md), [RiskIncident](RiskIncident.md), [CapabilityGroup](CapabilityGroup.md), [AiTaskDomain](AiTaskDomain.md), [AiTaskGroup](AiTaskGroup.md), [Stakeholder](Stakeholder.md), [StakeholderGroup](StakeholderGroup.md), [Requirement](Requirement.md) |
| Slot URI  | [schema:isPartOf](http://schema.org/isPartOf)                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value              |
| ------------ | ------------------------- |
| self         | schema:isPartOf           |
| native       | nexus:isDefinedByTaxonomy |

## LinkML Source

<details>
```yaml
name: isDefinedByTaxonomy
description: A relationship where a concept or a concept group is defined by a taxonomy
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: schema:isPartOf
alias: isDefinedByTaxonomy
domain_of:
- Concept
- Control
- Group
- Entry
- Policy
- Rule
- RiskControlGroup
- RiskGroup
- Risk
- RiskControl
- Action
- RiskIncident
- CapabilityGroup
- AiTaskDomain
- AiTaskGroup
- Stakeholder
- StakeholderGroup
- Requirement
range: Taxonomy

```
</details></div>
```
