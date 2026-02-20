# Slot: isDefinedByTaxonomy

_A relationship where a concept or a concept group is defined by a taxonomy_

URI: [schema:isPartOf](http://schema.org/isPartOf)
Alias: isDefinedByTaxonomy

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [RiskControl](RiskControl.md)                                     | A measure that maintains and/or modifies risk (and risk concepts)                | no            |
| [Entry](Entry.md)                                                 | An entry and its definitions                                                     | no            |
| [Term](Term.md)                                                   | A term and its definitions                                                       | no            |
| [Impact](Impact.md)                                               |                                                                                  | no            |
| [RiskIncident](RiskIncident.md)                                   | An event occuring or occured which is a realised or materialised risk            | no            |
| [Principle](Principle.md)                                         | A representation of values or norms that must be taken into consideration whe... | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |
| [LLMIntrinsic](LLMIntrinsic.md)                                   | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [Permission](Permission.md)                                       | A rule describing a permission to perform an activity                            | no            |
| [Policy](Policy.md)                                               | A guidance document outlining any of: procedures, plans, principles, decision... | no            |
| [Adapter](Adapter.md)                                             | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [CapabilityConcept](CapabilityConcept.md)                         | An umbrella term for referring to capability domains, groups, and individual ... | no            |
| [Group](Group.md)                                                 | Labelled groups of concepts                                                      | no            |
| [Rule](Rule.md)                                                   | A rule describing a process or control that directs or determines if and how ... | no            |
| [Action](Action.md)                                               | Action to remediate a risk                                                       | no            |
| [Recommendation](Recommendation.md)                               | A rule describing a recommendation for performing an activity                    | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [CapabilityGroup](CapabilityGroup.md)                             | A group of AI capabilities that are part of a capability taxonomy, organized ... | no            |
| [Control](Control.md)                                             | A measure that maintains and/or modifies                                         | no            |
| [Prohibition](Prohibition.md)                                     | A rule describing a prohibition to perform an activity                           | no            |
| [Certification](Certification.md)                                 | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [StakeholderGroup](StakeholderGroup.md)                           | An AI system stakeholder grouping                                                | no            |
| [LLMQuestionPolicy](LLMQuestionPolicy.md)                         | The policy guides how the language model should answer a diverse set of sensi... | no            |
| [Risk](Risk.md)                                                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [AiTask](AiTask.md)                                               | A task, such as summarization and classification, performed by an AI             | no            |
| [Capability](Capability.md)                                       | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [CapabilityDomain](CapabilityDomain.md)                           | A high-level domain of AI capabilities (e                                        | no            |
| [RiskConcept](RiskConcept.md)                                     | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [Stakeholder](Stakeholder.md)                                     | An AI system stakeholder for Responsible AI governance (e                        | no            |
| [Requirement](Requirement.md)                                     | A requirement representing a combination of obligation, permission, or prohib... | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |
| [Obligation](Obligation.md)                                       | A rule describing an obligation for performing an activity                       | no            |
| [Concept](Concept.md)                                             | A concept                                                                        | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [RiskGroup](RiskGroup.md)                                         | A group of AI system related risks that are part of a risk taxonomy              | no            |

## Properties

- Range: [Taxonomy](Taxonomy.md)

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
- RiskGroup
- Risk
- RiskControl
- Action
- RiskIncident
- CapabilityGroup
- StakeholderGroup
- Stakeholder
- Requirement
range: Taxonomy

```
</details>
```
