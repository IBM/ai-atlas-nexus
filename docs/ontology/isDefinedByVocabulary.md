# Slot: isDefinedByVocabulary

_A relationship where a term or a term group is defined by a vocabulary_

URI: [schema:isPartOf](http://schema.org/isPartOf)
Alias: isDefinedByVocabulary

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                              | Description                                                                      | Modifies Slot |
| --------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Principle](Principle.md)         | A representation of values or norms that must be taken into consideration whe... | no            |
| [LLMIntrinsic](LLMIntrinsic.md)   | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [Certification](Certification.md) | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [Entry](Entry.md)                 | An entry and its definitions                                                     | no            |
| [AiTask](AiTask.md)               | A task, such as summarization and classification, performed by an AI             | no            |
| [Term](Term.md)                   | A term and its definitions                                                       | no            |
| [Adapter](Adapter.md)             | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [Risk](Risk.md)                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [Capability](Capability.md)       | A specific AI capability or ability, such as reading comprehension, logical r... | no            |

## Properties

- Range: [Vocabulary](Vocabulary.md)

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
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
</details>
```
