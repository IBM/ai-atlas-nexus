# Slot: isDefinedByTaxonomy

_A relationship where a concept or a concept group is defined by a taxonomy_

URI: [schema:isPartOf](http://schema.org/isPartOf)
Alias: isDefinedByTaxonomy

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AIUser](AIUser.md)                                               | Individual or group that interacts with a system                                 | no            |
| [Group](Group.md)                                                 | Labelled groups of concepts                                                      | no            |
| [Action](Action.md)                                               | Action to remediate a risk                                                       | no            |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [Rule](Rule.md)                                                   | A rule describing a process or control that directs or determines if and how ... | no            |
| [RiskIncident](RiskIncident.md)                                   | An event occuring or occured which is a realised or materialised risk            | no            |
| [RiskControlGroup](RiskControlGroup.md)                           | A group of AI system related risk controls                                       | no            |
| [Impact](Impact.md)                                               |                                                                                  | no            |
| [LLMQuestionPolicy](LLMQuestionPolicy.md)                         | The policy guides how the language model should answer a diverse set of sensi... | no            |
| [Capability](Capability.md)                                       | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [AiAgent](AiAgent.md)                                             | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [CapabilityGroup](CapabilityGroup.md)                             | A group of AI capabilities that are part of a capability taxonomy, organized ... | no            |
| [Recommendation](Recommendation.md)                               | A rule describing a recommendation for performing an activity                    | no            |
| [AIDeployer](AIDeployer.md)                                       | Any natural or legal person, public authority, agency or other body using an ... | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |
| [RiskControl](RiskControl.md)                                     | A measure that maintains and/or modifies risk (and risk concepts)                | no            |
| [RiskConcept](RiskConcept.md)                                     | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [StakeholderGroup](StakeholderGroup.md)                           | An AI system stakeholder grouping                                                | no            |
| [CapabilityDomain](CapabilityDomain.md)                           | A high-level domain of AI capabilities (e                                        | no            |
| [Principle](Principle.md)                                         | A representation of values or norms that must be taken into consideration whe... | no            |
| [Permission](Permission.md)                                       | A rule describing a permission to perform an activity                            | no            |
| [Risk](Risk.md)                                                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [CapabilityConcept](CapabilityConcept.md)                         | An umbrella term for referring to capability domains, groups, and individual ... | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [Requirement](Requirement.md)                                     | A requirement representing a combination of obligation, permission, or prohib... | no            |
| [AISubject](AISubject.md)                                         | An entity that is subject to or impacted by the use of AI                        | no            |
| [Term](Term.md)                                                   | A term and its definitions                                                       | no            |
| [Prohibition](Prohibition.md)                                     | A rule describing a prohibition to perform an activity                           | no            |
| [LLMIntrinsic](LLMIntrinsic.md)                                   | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [RiskGroup](RiskGroup.md)                                         | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [Entry](Entry.md)                                                 | An entry and its definitions                                                     | no            |
| [AIOperator](AIOperator.md)                                       | Refers to a provider, product manufacturer, deployer, authorised representati... | no            |
| [AiTask](AiTask.md)                                               | A task, such as summarization and classification, performed by an AI             | no            |
| [Adapter](Adapter.md)                                             | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [AIDeveloper](AIDeveloper.md)                                     | An organisation or entity that is concerned with the development of AI servic... | no            |
| [Stakeholder](Stakeholder.md)                                     | Represents any individual, group or organization that can affect, be affected... | no            |
| [Control](Control.md)                                             | A measure that maintains and/or modifies                                         | no            |
| [Certification](Certification.md)                                 | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [AiSystem](AiSystem.md)                                           | A compound AI System composed of one or more AI capablities                      | no            |
| [Obligation](Obligation.md)                                       | A rule describing an obligation for performing an activity                       | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [Concept](Concept.md)                                             | A concept                                                                        | no            |
| [Policy](Policy.md)                                               | A guidance document outlining any of: procedures, plans, principles, decision... | no            |

## Properties

### Type and Range

| Property  | Value                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Range     | [Taxonomy](Taxonomy.md)                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Domain Of | [Concept](Concept.md), [Control](Control.md), [Group](Group.md), [Entry](Entry.md), [Policy](Policy.md), [Rule](Rule.md), [RiskControlGroup](RiskControlGroup.md), [RiskGroup](RiskGroup.md), [Risk](Risk.md), [RiskControl](RiskControl.md), [Action](Action.md), [RiskIncident](RiskIncident.md), [Stakeholder](Stakeholder.md), [StakeholderGroup](StakeholderGroup.md), [CapabilityGroup](CapabilityGroup.md), [Requirement](Requirement.md) |
| Slot URI  | [schema:isPartOf](http://schema.org/isPartOf)                                                                                                                                                                                                                                                                                                                                                                                                    |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
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
- Stakeholder
- StakeholderGroup
- CapabilityGroup
- Requirement
range: Taxonomy

```
</details>
```
