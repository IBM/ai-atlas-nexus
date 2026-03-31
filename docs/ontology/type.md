# Slot: type

URI: [nexus:type](https://ibm.github.io/ai-atlas-nexus/ontology/type)
Alias: type

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Action](Action.md)                                               | Action to remediate a risk                                                       | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |
| [Obligation](Obligation.md)                                       | A rule describing an obligation for performing an activity                       | no            |
| [Vocabulary](Vocabulary.md)                                       | A collection of terms, with their definitions and relationships                  | no            |
| [LLMIntrinsic](LLMIntrinsic.md)                                   | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [Term](Term.md)                                                   | A term and its definitions                                                       | no            |
| [Permission](Permission.md)                                       | A rule describing a permission to perform an activity                            | no            |
| [Risk](Risk.md)                                                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [Impact](Impact.md)                                               |                                                                                  | no            |
| [Principle](Principle.md)                                         | A representation of values or norms that must be taken into consideration whe... | no            |
| [CapabilityGroup](CapabilityGroup.md)                             | A group of AI capabilities that are part of a capability taxonomy, organized ... | no            |
| [RiskConcept](RiskConcept.md)                                     | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [AiTask](AiTask.md)                                               | A task, such as summarization and classification, performed by an AI             | no            |
| [Group](Group.md)                                                 | Labelled groups of concepts                                                      | no            |
| [Concept](Concept.md)                                             | A concept                                                                        | no            |
| [Entry](Entry.md)                                                 | An entry and its definitions                                                     | no            |
| [Recommendation](Recommendation.md)                               | A rule describing a recommendation for performing an activity                    | no            |
| [RiskControl](RiskControl.md)                                     | A measure that maintains and/or modifies risk (and risk concepts)                | no            |
| [CapabilityDomain](CapabilityDomain.md)                           | A high-level domain of AI capabilities (e                                        | no            |
| [RiskControlGroupTaxonomy](RiskControlGroupTaxonomy.md)           | A taxonomy of AI system related risk controls groups                             | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [RiskControlGroup](RiskControlGroup.md)                           | A group of AI system related risk controls                                       | no            |
| [Rule](Rule.md)                                                   | A rule describing a process or control that directs or determines if and how ... | no            |
| [RiskGroup](RiskGroup.md)                                         | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [Certification](Certification.md)                                 | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [Control](Control.md)                                             | A measure that maintains and/or modifies                                         | no            |
| [AiSystem](AiSystem.md)                                           | A compound AI System composed of one or more AI capablities                      | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |
| [StakeholderGroup](StakeholderGroup.md)                           | An AI system stakeholder grouping                                                | no            |
| [Requirement](Requirement.md)                                     | A requirement representing a combination of obligation, permission, or prohib... | no            |
| [CapabilityTaxonomy](CapabilityTaxonomy.md)                       | A taxonomy of AI capabilities describing the abilities of AI systems             | no            |
| [Policy](Policy.md)                                               | A guidance document outlining any of: procedures, plans, principles, decision... | no            |
| [LLMQuestionPolicy](LLMQuestionPolicy.md)                         | The policy guides how the language model should answer a diverse set of sensi... | no            |
| [Adapter](Adapter.md)                                             | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [Prohibition](Prohibition.md)                                     | A rule describing a prohibition to perform an activity                           | no            |
| [Capability](Capability.md)                                       | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [RiskTaxonomy](RiskTaxonomy.md)                                   | A taxonomy of AI system related risks                                            | no            |
| [Taxonomy](Taxonomy.md)                                           | A hierachical taxonomy of concepts, with their definitions and relationships     | no            |
| [RiskIncident](RiskIncident.md)                                   | An event occuring or occured which is a realised or materialised risk            | no            |
| [CapabilityConcept](CapabilityConcept.md)                         | An umbrella term for referring to capability domains, groups, and individual ... | no            |
| [AiAgent](AiAgent.md)                                             | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |

## Properties

- Range: [String](String.md)

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
- ControlActivity
- ControlActivityPermission
- ControlActivityProhibition
- ControlActivityObligation
- ControlActivityRecommendation
- Requirement
range: string

```
</details>
```
