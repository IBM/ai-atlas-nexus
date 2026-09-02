---
search:
  boost: 5.0
---

# Slot: hasLicense

_Indicates licenses associated with a resource_

<div data-search-exclude markdown="1">

URI: [airo:hasLicense](https://w3id.org/airo#hasLicense)
Alias: hasLicense

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                    | Description                                                                      | Modifies Slot |
| ------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Documentation](Documentation.md)                       | Documented information about a concept or other topic(s) of interest             | no            |
| [Vocabulary](Vocabulary.md)                             | A collection of terms, with their definitions and relationships                  | no            |
| [AiTaskTaxonomy](AiTaskTaxonomy.md)                     | A taxonomy of AI Tasks                                                           | no            |
| [Questionnaire](Questionnaire.md)                       | A questionnaire groups questions                                                 | no            |
| [RiskTaxonomy](RiskTaxonomy.md)                         | A taxonomy of AI system related risks                                            | no            |
| [AiModel](AiModel.md)                                   | A base AI Model class                                                            | no            |
| [AiSystem](AiSystem.md)                                 | A compound AI System composed of one or more AI capablities                      | no            |
| [Taxonomy](Taxonomy.md)                                 | A hierachical taxonomy of concepts, with their definitions and relationships     | no            |
| [AiEval](AiEval.md)                                     | An AI Evaluation, e                                                              | no            |
| [Dataset](Dataset.md)                                   | A body of structured information describing some topic(s) of interest            | no            |
| [CapabilityTaxonomy](CapabilityTaxonomy.md)             | A taxonomy of AI capabilities describing the abilities of AI systems             | no            |
| [AiAgent](AiAgent.md)                                   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [Question](Question.md)                                 | An evaluation where a question has to be answered                                | no            |
| [BaseAi](BaseAi.md)                                     | Any type of AI, be it a LLM, RL agent, SVM, etc                                  | no            |
| [Adapter](Adapter.md)                                   | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [BenchmarkMetadataCard](BenchmarkMetadataCard.md)       | Benchmark metadata cards offer a standardized way to document LLM benchmarks ... | no            |
| [LargeLanguageModel](LargeLanguageModel.md)             | A large language model (LLM) is an AI model which supports a range of languag... | no            |
| [RiskControlGroupTaxonomy](RiskControlGroupTaxonomy.md) | A taxonomy of AI system related risk controls groups                             | no            |

## Properties

### Type and Range

| Property  | Value                                                                                                                                                                                                                                                                                                                                                             |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Range     | [License](License.md)                                                                                                                                                                                                                                                                                                                                             |
| Domain Of | [Dataset](Dataset.md), [Documentation](Documentation.md), [Vocabulary](Vocabulary.md), [Taxonomy](Taxonomy.md), [RiskTaxonomy](RiskTaxonomy.md), [RiskControlGroupTaxonomy](RiskControlGroupTaxonomy.md), [BaseAi](BaseAi.md), [AiTaskTaxonomy](AiTaskTaxonomy.md), [AiEval](AiEval.md), [BenchmarkMetadataCard](BenchmarkMetadataCard.md), [Adapter](Adapter.md) |
| Slot URI  | [airo:hasLicense](https://w3id.org/airo#hasLicense)                                                                                                                                                                                                                                                                                                               |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value     |
| ------------ | ---------------- |
| self         | airo:hasLicense  |
| native       | nexus:hasLicense |

## LinkML Source

<details>
```yaml
name: hasLicense
description: Indicates licenses associated with a resource
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: airo:hasLicense
alias: hasLicense
domain_of:
- Dataset
- Documentation
- Vocabulary
- Taxonomy
- RiskTaxonomy
- RiskControlGroupTaxonomy
- BaseAi
- AiTaskTaxonomy
- AiEval
- BenchmarkMetadataCard
- Adapter
range: License

```
</details></div>
```
