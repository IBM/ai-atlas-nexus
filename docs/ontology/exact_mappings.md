---
search:
  boost: 5.0
---

# Slot: exact_mappings

_The property is used to link two concepts, indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications_

<div data-search-exclude markdown="1">

URI: [skos:exactMatch](http://www.w3.org/2004/02/skos/core#exactMatch)
Alias: exact_mappings

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                              | Description                                                                      | Modifies Slot |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiTask](AiTask.md)                                               | A task, such as summarization and classification, performed by an AI             | no            |
| [Taxonomy](Taxonomy.md)                                           | A hierachical taxonomy of concepts, with their definitions and relationships     | no            |
| [Term](Term.md)                                                   | A term and its definitions                                                       | no            |
| [Modality](Modality.md)                                           | A modality supported by an Ai component                                          | no            |
| [Question](Question.md)                                           | An evaluation where a question has to be answered                                | no            |
| [IncidentConcludedclass](IncidentConcludedclass.md)               |                                                                                  | no            |
| [Purpose](Purpose.md)                                             | The end goal for which an entity is used or an action is taken                   | no            |
| [IncidentHaltedclass](IncidentHaltedclass.md)                     |                                                                                  | no            |
| [ScoreDetails](ScoreDetails.md)                                   | Details about evaluation scores                                                  | no            |
| [AIDeveloper](AIDeveloper.md)                                     | An organisation or entity that is concerned with the development of AI servic... | no            |
| [Concept](Concept.md)                                             | A concept                                                                        | no            |
| [ControlActivityProhibition](ControlActivityProhibition.md)       | A control activity (rule) describing a prohibition to perform an activity        | no            |
| [AiTaskDomain](AiTaskDomain.md)                                   | A grouping of AI Tasks by domain                                                 | no            |
| [Prohibition](Prohibition.md)                                     | A rule describing a prohibition to perform an activity                           | no            |
| [Entity](Entity.md)                                               | A generic grouping for any identifiable entity                                   | no            |
| [Capability](Capability.md)                                       | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [LLMQuestionPolicy](LLMQuestionPolicy.md)                         | The policy guides how the language model should answer a diverse set of sensi... | no            |
| [AIComponent](AIComponent.md)                                     | Component (element) of an AI system                                              | no            |
| [AiModel](AiModel.md)                                             | A base AI Model class                                                            | no            |
| [ControlActivityPermission](ControlActivityPermission.md)         | A control activity (rule) describing a permission to perform an activity         | no            |
| [EveryEvalAIResult](EveryEvalAIResult.md)                         | An evaluation result from the Every Eval Ever dataset, capturing evaluation m... | no            |
| [CapabilityDomain](CapabilityDomain.md)                           | A high-level domain of AI capabilities (e                                        | no            |
| [BenchmarkMetadataCard](BenchmarkMetadataCard.md)                 | Benchmark metadata cards offer a standardized way to document LLM benchmarks ... | no            |
| [Action](Action.md)                                               | Action to remediate a risk                                                       | no            |
| [Stakeholder](Stakeholder.md)                                     | Represents any individual, group or organization that can affect, be affected... | no            |
| [Principle](Principle.md)                                         | A representation of values or norms that must be taken into consideration whe... | no            |
| [Domain](Domain.md)                                               | An area, sector, or industry that is associated with economic activities         | no            |
| [MetricConfig](MetricConfig.md)                                   | Configuration for evaluation metrics                                             | no            |
| [Impact](Impact.md)                                               |                                                                                  | no            |
| [Severity](Severity.md)                                           |                                                                                  | no            |
| [StakeholderGroup](StakeholderGroup.md)                           | An AI system stakeholder grouping                                                | no            |
| [AiTaskTaxonomy](AiTaskTaxonomy.md)                               | A taxonomy of AI Tasks                                                           | no            |
| [Obligation](Obligation.md)                                       | A rule describing an obligation for performing an activity                       | no            |
| [ControlActivityObligation](ControlActivityObligation.md)         | A control activity (rule) describing an obligation for performing an activity    | no            |
| [CapabilityConcept](CapabilityConcept.md)                         | An umbrella term for referring to capability domains, groups, and individual ... | no            |
| [LLMIntrinsic](LLMIntrinsic.md)                                   | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [IncidentStatus](IncidentStatus.md)                               |                                                                                  | no            |
| [AIUser](AIUser.md)                                               | Individual or group that interacts with a system                                 | no            |
| [LocalityOfUse](LocalityOfUse.md)                                 | The area, e                                                                      | no            |
| [AiSystem](AiSystem.md)                                           | A compound AI System composed of one or more AI capablities                      | no            |
| [AISubject](AISubject.md)                                         | An entity that is subject to or impacted by the use of AI                        | no            |
| [Likelihood](Likelihood.md)                                       |                                                                                  | no            |
| [AiEvalResult](AiEvalResult.md)                                   | The result of an evaluation for a specific AI model                              | no            |
| [AiModelValidation](AiModelValidation.md)                         | AI model validation steps that have been performed after the model training t... | no            |
| [AiTaskGroup](AiTaskGroup.md)                                     | A group of AI Tasks                                                              | no            |
| [LargeLanguageModelFamily](LargeLanguageModelFamily.md)           | A large language model family is a set of models that are provided by the sam... | no            |
| [Rule](Rule.md)                                                   | A rule describing a process or control that directs or determines if and how ... | no            |
| [RiskControl](RiskControl.md)                                     | A measure that maintains and/or modifies risk (and risk concepts)                | no            |
| [Input](Input.md)                                                 | Input for which the system or component generates output                         | no            |
| [Vocabulary](Vocabulary.md)                                       | A collection of terms, with their definitions and relationships                  | no            |
| [IncidentMitigatedclass](IncidentMitigatedclass.md)               |                                                                                  | no            |
| [EvaluationResultRecord](EvaluationResultRecord.md)               | A single evaluation result record                                                | no            |
| [CapabilityTaxonomy](CapabilityTaxonomy.md)                       | A taxonomy of AI capabilities describing the abilities of AI systems             | no            |
| [IncidentOngoingclass](IncidentOngoingclass.md)                   |                                                                                  | no            |
| [BaseAi](BaseAi.md)                                               | Any type of AI, be it a LLM, RL agent, SVM, etc                                  | no            |
| [Entry](Entry.md)                                                 | An entry and its definitions                                                     | no            |
| [ControlActivity](ControlActivity.md)                             | An obligation, permission, or prohibition for AI system assurance                | no            |
| [ModelInfo](ModelInfo.md)                                         | Information about the AI model being evaluated                                   | no            |
| [ControlActivityRecommendation](ControlActivityRecommendation.md) | A control activity (rule) describing a recommendation for performing an activ... | no            |
| [Requirement](Requirement.md)                                     | A requirement representing a combination of obligation, permission, or prohib... | no            |
| [CapabilityGroup](CapabilityGroup.md)                             | A group of AI capabilities that are part of a capability taxonomy, organized ... | no            |
| [Certification](Certification.md)                                 | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [RiskIncident](RiskIncident.md)                                   | An event occuring or occured which is a realised or materialised risk            | no            |
| [LargeLanguageModel](LargeLanguageModel.md)                       | A large language model (LLM) is an AI model which supports a range of languag... | no            |
| [AIDeployer](AIDeployer.md)                                       | Any natural or legal person, public authority, agency or other body using an ... | no            |
| [AIOperator](AIOperator.md)                                       | Refers to a provider, product manufacturer, deployer, authorised representati... | no            |
| [Questionnaire](Questionnaire.md)                                 | A questionnaire groups questions                                                 | no            |
| [RiskConcept](RiskConcept.md)                                     | An umbrella term for referring to risk, risk source, consequence and impact      | no            |
| [AiEval](AiEval.md)                                               | An AI Evaluation, e                                                              | no            |
| [AiProvider](AiProvider.md)                                       | A provider under the AI Act is defined by Article 3(3) as a natural or legal ... | no            |
| [Risk](Risk.md)                                                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [IncidentNearMissclass](IncidentNearMissclass.md)                 |                                                                                  | no            |
| [RiskGroup](RiskGroup.md)                                         | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [Documentation](Documentation.md)                                 | Documented information about a concept or other topic(s) of interest             | no            |
| [AiAgent](AiAgent.md)                                             | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AttributeConditionRule](AttributeConditionRule.md)               |                                                                                  | no            |
| [Adapter](Adapter.md)                                             | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [SourceMetadata](SourceMetadata.md)                               | Metadata about the source of an evaluation                                       | no            |
| [Control](Control.md)                                             | A measure that maintains and/or modifies                                         | no            |
| [Consequence](Consequence.md)                                     |                                                                                  | no            |
| [License](License.md)                                             | The general notion of a license which defines terms and grants permissions to... | no            |
| [DataPreprocessing](DataPreprocessing.md)                         | Data transformations, such as PI filtering, performed to ensure high quality ... | no            |
| [Recommendation](Recommendation.md)                               | A rule describing a recommendation for performing an activity                    | no            |
| [Permission](Permission.md)                                       | A rule describing a permission to perform an activity                            | no            |
| [Dataset](Dataset.md)                                             | A body of structured information describing some topic(s) of interest            | no            |
| [Organization](Organization.md)                                   | Any organizational entity such as a corporation, educational institution, con... | no            |
| [AiOffice](AiOffice.md)                                           | The EU AI Office (https://digital-strategy                                       | no            |
| [RiskControlGroup](RiskControlGroup.md)                           | A group of AI system related risk controls                                       | no            |
| [Policy](Policy.md)                                               | A guidance document outlining any of: procedures, plans, principles, decision... | no            |
| [RiskControlGroupTaxonomy](RiskControlGroupTaxonomy.md)           | A taxonomy of AI system related risk controls groups                             | no            |
| [AiLifecyclePhase](AiLifecyclePhase.md)                           | A Phase of AI lifecycle which indicates evolution of the system from concepti... | no            |
| [RiskTaxonomy](RiskTaxonomy.md)                                   | A taxonomy of AI system related risks                                            | no            |
| [Group](Group.md)                                                 | Labelled groups of concepts                                                      | no            |
| [SourceData](SourceData.md)                                       | Information about the data source used in evaluation                             | no            |

## Properties

### Type and Range

| Property  | Value                                                             |
| --------- | ----------------------------------------------------------------- |
| Range     | [Any](Any.md)                                                     |
| Domain Of | [Entity](Entity.md)                                               |
| Slot URI  | [skos:exactMatch](http://www.w3.org/2004/02/skos/core#exactMatch) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | skos:exactMatch      |
| native       | nexus:exact_mappings |

## LinkML Source

<details>
```yaml
name: exact_mappings
description: The property is used to link two concepts, indicating a high degree of
  confidence that the concepts can be used interchangeably across a wide range of
  information retrieval applications
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: skos:exactMatch
alias: exact_mappings
domain_of:
- Entity
range: Any
multivalued: true
inlined: false

```
</details></div>
```
