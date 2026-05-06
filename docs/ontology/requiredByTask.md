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
| [AiAgent](AiAgent.md)             | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [Term](Term.md)                   | A term and its definitions                                                       | no            |
| [Certification](Certification.md) | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [LLMIntrinsic](LLMIntrinsic.md)   | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [AiSystem](AiSystem.md)           | A compound AI System composed of one or more AI capablities                      | no            |
| [Capability](Capability.md)       | A specific AI capability or ability, such as reading comprehension, logical r... | yes           |
| [Principle](Principle.md)         | A representation of values or norms that must be taken into consideration whe... | no            |
| [Risk](Risk.md)                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [Entry](Entry.md)                 | An entry and its definitions                                                     | no            |

## Properties

### Type and Range

| Property  | Value                                          |
| --------- | ---------------------------------------------- |
| Range     | [AiTask](AiTask.md)                            |
| Domain Of | [Entry](Entry.md), [Capability](Capability.md) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

<details>
<summary>Relationship Properties</summary>

| Property | Value                                       |
| -------- | ------------------------------------------- |
| Inverse  | [requiresCapability](requiresCapability.md) |

</details>

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
