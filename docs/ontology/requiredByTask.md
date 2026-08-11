---
search:
  boost: 5.0
---

# Slot: requiredByTask

_Indicates that this entry is required to perform a specific AI task._

<div data-search-exclude markdown="1">

URI: [nexus:requiredByTask](https://w3id.org/ai-atlas-nexus/requiredByTask)
Alias: requiredByTask

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                              | Description                                                                      | Modifies Slot |
| --------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Risk](Risk.md)                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [Capability](Capability.md)       | A specific AI capability or ability, such as reading comprehension, logical r... | yes           |
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

| Property  | Value                                          |
| --------- | ---------------------------------------------- |
| Range     | [Any](Any.md)                                  |
| Domain    | [Entry](Entry.md)                              |
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

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

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
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain: Entry
alias: requiredByTask
domain_of:
- Entry
- Capability
inverse: requiresCapability
range: Any
multivalued: true
inlined: false

```
</details></div>
```
