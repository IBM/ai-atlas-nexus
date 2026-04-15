# Slot: requiredByTask

_Indicates that this entry is required to perform a specific AI task._

URI: [nexus:requiredByTask](https://ibm.github.io/ai-atlas-nexus/ontology/requiredByTask)
Alias: requiredByTask

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                              | Description                                                                      | Modifies Slot |
| --------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Adapter](Adapter.md)             | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [AiTask](AiTask.md)               | A task, such as summarization and classification, performed by an AI             | no            |
| [LLMIntrinsic](LLMIntrinsic.md)   | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [Capability](Capability.md)       | A specific AI capability or ability, such as reading comprehension, logical r... | yes           |
| [Term](Term.md)                   | A term and its definitions                                                       | no            |
| [Entry](Entry.md)                 | An entry and its definitions                                                     | no            |
| [Risk](Risk.md)                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [Certification](Certification.md) | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [Principle](Principle.md)         | A representation of values or norms that must be taken into consideration whe... | no            |
| [AiSystem](AiSystem.md)           | A compound AI System composed of one or more AI capablities                      | no            |
| [AiAgent](AiAgent.md)             | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |

## Properties

- Range: [AiTask](AiTask.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | nexus:requiredByTask |
| native       | nexus:requiredByTask |

## LinkML Source

<details>
```yaml
name: requiredByTask
description: Indicates that this entry is required to perform a specific AI task.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
alias: requiredByTask
domain_of:
- Entry
- Capability
inverse: requiresCapability
range: AiTask
multivalued: true
inlined: false

```
</details>
```
