# Slot: type

URI: [nexus:type](https://ibm.github.io/ai-atlas-nexus/ontology/type)
Alias: type

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                        | Description                                                                      | Modifies Slot |
| ------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Vocabulary](Vocabulary.md)                 | A collection of terms, with their definitions and relationships                  | no            |
| [Control](Control.md)                       | A measure that maintains and/or modifies                                         | no            |
| [Taxonomy](Taxonomy.md)                     | A hierachical taxonomy of concepts, with their definitions and relationships     | no            |
| [StakeholderGroup](StakeholderGroup.md)     | An AI system stakeholder grouping                                                | no            |
| [Group](Group.md)                           | Labelled groups of concepts                                                      | no            |
| [Entry](Entry.md)                           | An entry and its definitions                                                     | no            |
| [LLMQuestionPolicy](LLMQuestionPolicy.md)   | The policy guides how the language model should answer a diverse set of sensi... | no            |
| [CapabilityDomain](CapabilityDomain.md)     | A high-level domain of AI capabilities (e                                        | no            |
| [Policy](Policy.md)                         | A guidance document outlining any of: procedures, plans, principles, decision... | no            |
| [RiskIncident](RiskIncident.md)             | An event occuring or occured which is a realised or materialised risk            | no            |
| [Concept](Concept.md)                       | A concept                                                                        | no            |
| [Action](Action.md)                         | Action to remediate a risk                                                       | no            |
| [Risk](Risk.md)                             | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [Adapter](Adapter.md)                       | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [CapabilityConcept](CapabilityConcept.md)   | An umbrella term for referring to capability domains, groups, and individual ... | no            |
| [CapabilityTaxonomy](CapabilityTaxonomy.md) | A taxonomy of AI capabilities describing the abilities of AI systems             | no            |
| [RiskControl](RiskControl.md)               | A measure that maintains and/or modifies risk (and risk concepts)                | no            |
| [RiskConcept](RiskConcept.md)               | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [AiTask](AiTask.md)                         | A task, such as summarization and classification, performed by an AI             | no            |
| [RiskTaxonomy](RiskTaxonomy.md)             | A taxonomy of AI system related risks                                            | no            |
| [Capability](Capability.md)                 | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [Impact](Impact.md)                         |                                                                                  | no            |
| [CapabilityGroup](CapabilityGroup.md)       | A group of AI capabilities that are part of a capability taxonomy, organized ... | no            |
| [RiskGroup](RiskGroup.md)                   | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [Term](Term.md)                             | A term and its definitions                                                       | no            |
| [Principle](Principle.md)                   | A representation of values or norms that must be taken into consideration whe... | no            |
| [LLMIntrinsic](LLMIntrinsic.md)             | A capability that can be invoked through a well-defined API that is reasonabl... | no            |

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
range: string

```
</details>
```
