# Slot: isPartOf

_A relationship where an entity is part of another entity_

URI: [schema:isPartOf](http://schema.org/isPartOf)
Alias: isPartOf

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                        | Description                                                                      | Modifies Slot |
| ------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [LLMIntrinsic](LLMIntrinsic.md)             | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [Term](Term.md)                             | A term and its definitions                                                       | no            |
| [AIUser](AIUser.md)                         | Individual or group that interacts with a system                                 | no            |
| [Risk](Risk.md)                             | The state of uncertainty associated with an AI system, that has the potential... | yes           |
| [Principle](Principle.md)                   | A representation of values or norms that must be taken into consideration whe... | no            |
| [CapabilityGroup](CapabilityGroup.md)       | A group of AI capabilities that are part of a capability taxonomy, organized ... | yes           |
| [AiTask](AiTask.md)                         | A task, such as summarization and classification, performed by an AI             | no            |
| [AIDeveloper](AIDeveloper.md)               | An organisation or entity that is concerned with the development of AI servic... | no            |
| [AIDeployer](AIDeployer.md)                 | Any natural or legal person, public authority, agency or other body using an ... | no            |
| [Entry](Entry.md)                           | An entry and its definitions                                                     | no            |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... | yes           |
| [AIOperator](AIOperator.md)                 | Refers to a provider, product manufacturer, deployer, authorised representati... | no            |
| [Certification](Certification.md)           | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [AiSystem](AiSystem.md)                     | A compound AI System composed of one or more AI capablities                      | no            |
| [AISubject](AISubject.md)                   | An entity that is subject to or impacted by the use of AI                        | no            |
| [Adapter](Adapter.md)                       | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [Capability](Capability.md)                 | A specific AI capability or ability, such as reading comprehension, logical r... | yes           |
| [Stakeholder](Stakeholder.md)               | Represents any individual, group or organization that can affect, be affected... | yes           |
| [AiAgent](AiAgent.md)                       | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |

## Properties

- Range: [String](String.md)

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: schema:isPartOf
alias: isPartOf
domain_of:
- Entry
- Risk
- LargeLanguageModel
- Stakeholder
- CapabilityGroup
range: string

```
</details>
```
