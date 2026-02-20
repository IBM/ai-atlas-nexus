# Slot: hasDocumentation

_Indicates documentation associated with an entity._

URI: [airo:hasDocumentation](https://w3id.org/airo#hasDocumentation)
Alias: hasDocumentation

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                    | Description                                                                      | Modifies Slot |
| ------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Question](Question.md)                                 | An evaluation where a question has to be answered                                | no            |
| [RiskControl](RiskControl.md)                           | A measure that maintains and/or modifies risk (and risk concepts)                | no            |
| [Entry](Entry.md)                                       | An entry and its definitions                                                     | no            |
| [Term](Term.md)                                         | A term and its definitions                                                       | no            |
| [LargeLanguageModel](LargeLanguageModel.md)             | A large language model (LLM) is an AI model which supports a range of languag... | no            |
| [Impact](Impact.md)                                     |                                                                                  | no            |
| [AiEval](AiEval.md)                                     | An AI Evaluation, e                                                              | no            |
| [RiskIncident](RiskIncident.md)                         | An event occuring or occured which is a realised or materialised risk            | no            |
| [Taxonomy](Taxonomy.md)                                 | A hierachical taxonomy of concepts, with their definitions and relationships     | no            |
| [Principle](Principle.md)                               | A representation of values or norms that must be taken into consideration whe... | no            |
| [LLMIntrinsic](LLMIntrinsic.md)                         | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [Dataset](Dataset.md)                                   | A body of structured information describing some topic(s) of interest            | no            |
| [Adapter](Adapter.md)                                   | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [CapabilityConcept](CapabilityConcept.md)               | An umbrella term for referring to capability domains, groups, and individual ... | no            |
| [AiSystem](AiSystem.md)                                 | A compound AI System composed of one or more AI capablities                      | no            |
| [Group](Group.md)                                       | Labelled groups of concepts                                                      | no            |
| [Questionnaire](Questionnaire.md)                       | A questionnaire groups questions                                                 | no            |
| [Action](Action.md)                                     | Action to remediate a risk                                                       | no            |
| [Vocabulary](Vocabulary.md)                             | A collection of terms, with their definitions and relationships                  | no            |
| [CapabilityGroup](CapabilityGroup.md)                   | A group of AI capabilities that are part of a capability taxonomy, organized ... | no            |
| [Certification](Certification.md)                       | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [AiTask](AiTask.md)                                     | A task, such as summarization and classification, performed by an AI             | no            |
| [StakeholderGroup](StakeholderGroup.md)                 | An AI system stakeholder grouping                                                | no            |
| [Risk](Risk.md)                                         | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [Capability](Capability.md)                             | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [BenchmarkMetadataCard](BenchmarkMetadataCard.md)       | Benchmark metadata cards offer a standardized way to document LLM benchmarks ... | no            |
| [CapabilityDomain](CapabilityDomain.md)                 | A high-level domain of AI capabilities (e                                        | no            |
| [AiAgent](AiAgent.md)                                   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [RiskConcept](RiskConcept.md)                           | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [BaseAi](BaseAi.md)                                     | Any type of AI, be it a LLM, RL agent, SVM, etc                                  | no            |
| [LargeLanguageModelFamily](LargeLanguageModelFamily.md) | A large language model family is a set of models that are provided by the sam... | no            |
| [Concept](Concept.md)                                   | A concept                                                                        | no            |
| [AiModel](AiModel.md)                                   | A base AI Model class                                                            | no            |
| [RiskGroup](RiskGroup.md)                               | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [CapabilityTaxonomy](CapabilityTaxonomy.md)             | A taxonomy of AI capabilities describing the abilities of AI systems             | no            |
| [RiskTaxonomy](RiskTaxonomy.md)                         | A taxonomy of AI system related risks                                            | no            |

## Properties

- Range: [Documentation](Documentation.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value           |
| ------------ | ---------------------- |
| self         | airo:hasDocumentation  |
| native       | nexus:hasDocumentation |

## LinkML Source

<details>
```yaml
name: hasDocumentation
description: Indicates documentation associated with an entity.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: airo:hasDocumentation
alias: hasDocumentation
domain_of:
- Dataset
- Vocabulary
- Taxonomy
- Concept
- Group
- Entry
- Term
- Principle
- RiskTaxonomy
- Action
- BaseAi
- LargeLanguageModelFamily
- AiEval
- BenchmarkMetadataCard
- Adapter
- LLMIntrinsic
range: Documentation
multivalued: true
inlined: false

```
</details>
```
