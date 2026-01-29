# Slot: implementedByAdapter

_Indicates that this capability is implemented by a specific adapter. This relationship distinguishes the abstract capability (what can be done) from the technical implementation mechanism (how it is added/extended via adapters)._

\_\_

URI: [nexus:implementedByAdapter](https://ibm.github.io/ai-atlas-nexus/ontology/implementedByAdapter)
Alias: implementedByAdapter

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                                                                      | Modifies Slot |
| ------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Capability](Capability.md)     | A specific AI capability or ability, such as reading comprehension, logical r... | yes           |
| [Term](Term.md)                 | A term and its definitions                                                       | no            |
| [Principle](Principle.md)       | A representation of values or norms that must be taken into consideration whe... | no            |
| [LLMIntrinsic](LLMIntrinsic.md) | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [AiTask](AiTask.md)             | A task, such as summarization and classification, performed by an AI             | no            |
| [Risk](Risk.md)                 | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [Entry](Entry.md)               | An entry and its definitions                                                     | no            |
| [Adapter](Adapter.md)           | Adapter-based methods add extra trainable parameters after the attention and ... | no            |

## Properties

- Range: [Adapter](Adapter.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value               |
| ------------ | -------------------------- |
| self         | nexus:implementedByAdapter |
| native       | nexus:implementedByAdapter |

## LinkML Source

<details>
```yaml
name: implementedByAdapter
description: 'Indicates that this capability is implemented by a specific adapter.
  This relationship distinguishes the abstract capability (what can be done) from
  the technical implementation mechanism (how it is added/extended via adapters).

'
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: Any
alias: implementedByAdapter
domain_of:

- Entry
- Capability
  inverse: implementsCapability
  range: Adapter
  multivalued: true
  inlined: false

```
</details>
```
