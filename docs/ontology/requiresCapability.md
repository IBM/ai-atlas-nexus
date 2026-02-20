# Slot: requiresCapability

_Indicates that this entry requires a specific capability_

URI: [nexus:requiresCapability](https://ibm.github.io/ai-atlas-nexus/ontology/requiresCapability)
Alias: requiresCapability

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                        | Description                                                                      | Modifies Slot |
| ------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Principle](Principle.md)                   | A representation of values or norms that must be taken into consideration whe... | no            |
| [LLMIntrinsic](LLMIntrinsic.md)             | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [Certification](Certification.md)           | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [Entry](Entry.md)                           | An entry and its definitions                                                     | no            |
| [AiTask](AiTask.md)                         | A task, such as summarization and classification, performed by an AI             | no            |
| [Term](Term.md)                             | A term and its definitions                                                       | no            |
| [Adapter](Adapter.md)                       | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [Risk](Risk.md)                             | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... | no            |
| [Capability](Capability.md)                 | A specific AI capability or ability, such as reading comprehension, logical r... | no            |

## Properties

- Range: [Capability](Capability.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value             |
| ------------ | ------------------------ |
| self         | nexus:requiresCapability |
| native       | nexus:requiresCapability |

## LinkML Source

<details>
```yaml
name: requiresCapability
description: Indicates that this entry requires a specific capability
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: Any
alias: requiresCapability
domain_of:
- Entry
- LargeLanguageModel
- AiTask
- Adapter
inverse: requiredByTask
range: Capability
multivalued: true
inlined: false

```
</details>
```
