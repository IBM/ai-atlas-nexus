---
search:
  boost: 5.0
---

# Slot: isDefinedByVocabulary

_A relationship where a term or a term group is defined by a vocabulary_

<div data-search-exclude markdown="1">

URI: [schema:isPartOf](http://schema.org/isPartOf)
Alias: isDefinedByVocabulary

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                              | Description                                                                      | Modifies Slot |
| --------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Risk](Risk.md)                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [Capability](Capability.md)       | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [Adapter](Adapter.md)             | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [Purpose](Purpose.md)             | The end goal for which an entity is used or an action is taken                   | no            |
| [Principle](Principle.md)         | A representation of values or norms that must be taken into consideration whe... | no            |
| [AiTask](AiTask.md)               | A task, such as summarization and classification, performed by an AI             | no            |
| [Entry](Entry.md)                 | An entry and its definitions                                                     | no            |
| [LocalityOfUse](LocalityOfUse.md) | The area, e                                                                      | no            |
| [AiAgent](AiAgent.md)             | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [Domain](Domain.md)               | An area, sector, or industry that is associated with economic activities         | no            |
| [Certification](Certification.md) | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [AiSystem](AiSystem.md)           | A compound AI System composed of one or more AI capablities                      | no            |
| [LLMIntrinsic](LLMIntrinsic.md)   | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [Term](Term.md)                   | A term and its definitions                                                       | no            |

## Properties

### Type and Range

| Property  | Value                                                                                      |
| --------- | ------------------------------------------------------------------------------------------ |
| Range     | [Vocabulary](Vocabulary.md)                                                                |
| Domain Of | [Entry](Entry.md), [Term](Term.md), [Adapter](Adapter.md), [LLMIntrinsic](LLMIntrinsic.md) |
| Slot URI  | [schema:isPartOf](http://schema.org/isPartOf)                                              |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value                |
| ------------ | --------------------------- |
| self         | schema:isPartOf             |
| native       | nexus:isDefinedByVocabulary |

## LinkML Source

<details>
```yaml
name: isDefinedByVocabulary
description: A relationship where a term or a term group is defined by a vocabulary
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: schema:isPartOf
alias: isDefinedByVocabulary
domain_of:
- Entry
- Term
- Adapter
- LLMIntrinsic
range: Vocabulary

```
</details></div>
```
