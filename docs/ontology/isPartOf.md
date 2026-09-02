---
search:
  boost: 5.0
---

# Slot: isPartOf

_A relationship where an entity is part of another entity_

<div data-search-exclude markdown="1">

URI: [schema:isPartOf](http://schema.org/isPartOf)
Alias: isPartOf

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                        | Description                                                                      | Modifies Slot |
| ------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Stakeholder](Stakeholder.md)               | Represents any individual, group or organization that can affect, be affected... | yes           |
| [AiTask](AiTask.md)                         | A task, such as summarization and classification, performed by an AI             | no            |
| [Principle](Principle.md)                   | A representation of values or norms that must be taken into consideration whe... | no            |
| [Domain](Domain.md)                         | An area, sector, or industry that is associated with economic activities         | no            |
| [Term](Term.md)                             | A term and its definitions                                                       | no            |
| [Entry](Entry.md)                           | An entry and its definitions                                                     | no            |
| [Purpose](Purpose.md)                       | The end goal for which an entity is used or an action is taken                   | no            |
| [AIDeveloper](AIDeveloper.md)               | An organisation or entity that is concerned with the development of AI servic... | no            |
| [CapabilityGroup](CapabilityGroup.md)       | A group of AI capabilities that are part of a capability taxonomy, organized ... | yes           |
| [Certification](Certification.md)           | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [LLMIntrinsic](LLMIntrinsic.md)             | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... | yes           |
| [AIDeployer](AIDeployer.md)                 | Any natural or legal person, public authority, agency or other body using an ... | no            |
| [AIOperator](AIOperator.md)                 | Refers to a provider, product manufacturer, deployer, authorised representati... | no            |
| [AIUser](AIUser.md)                         | Individual or group that interacts with a system                                 | no            |
| [Capability](Capability.md)                 | A specific AI capability or ability, such as reading comprehension, logical r... | yes           |
| [LocalityOfUse](LocalityOfUse.md)           | The area, e                                                                      | no            |
| [AiSystem](AiSystem.md)                     | A compound AI System composed of one or more AI capablities                      | no            |
| [Risk](Risk.md)                             | The state of uncertainty associated with an AI system, that has the potential... | yes           |
| [AISubject](AISubject.md)                   | An entity that is subject to or impacted by the use of AI                        | no            |
| [AiAgent](AiAgent.md)                       | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [Adapter](Adapter.md)                       | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [AiTaskGroup](AiTaskGroup.md)               | A group of AI Tasks                                                              | yes           |

## Properties

### Type and Range

| Property  | Value                                                                                                                                                                                |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Range     | [String](String.md)                                                                                                                                                                  |
| Domain Of | [Entry](Entry.md), [Risk](Risk.md), [CapabilityGroup](CapabilityGroup.md), [LargeLanguageModel](LargeLanguageModel.md), [AiTaskGroup](AiTaskGroup.md), [Stakeholder](Stakeholder.md) |
| Slot URI  | [schema:isPartOf](http://schema.org/isPartOf)                                                                                                                                        |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value    |
| ------------ | --------------- |
| self         | schema:isPartOf |
| native       | nexus:isPartOf  |

## LinkML Source

<details>
```yaml
name: isPartOf
description: A relationship where an entity is part of another entity
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: schema:isPartOf
alias: isPartOf
domain_of:
- Entry
- Risk
- CapabilityGroup
- LargeLanguageModel
- AiTaskGroup
- Stakeholder
range: string

```
</details></div>
```
