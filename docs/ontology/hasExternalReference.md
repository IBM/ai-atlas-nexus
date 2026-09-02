---
search:
  boost: 5.0
---

# Slot: hasExternalReference

_External references / additional resources related to this entity, such as articles, tools, or datasets. Distinct from hasDocumentation, which documents the entity itself. External references are not necessarily curated or vetted, and quality will vary._

<div data-search-exclude markdown="1">

URI: [nexus:hasExternalReference](https://w3id.org/ai-atlas-nexus/hasExternalReference)
Alias: hasExternalReference

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                              | Description                                                                      | Modifies Slot |
| --------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Capability](Capability.md)       | A specific AI capability or ability, such as reading comprehension, logical r... | no            |
| [Action](Action.md)               | Action to remediate a risk                                                       | no            |
| [AiTask](AiTask.md)               | A task, such as summarization and classification, performed by an AI             | no            |
| [Principle](Principle.md)         | A representation of values or norms that must be taken into consideration whe... | no            |
| [LocalityOfUse](LocalityOfUse.md) | The area, e                                                                      | no            |
| [AiSystem](AiSystem.md)           | A compound AI System composed of one or more AI capablities                      | no            |
| [Domain](Domain.md)               | An area, sector, or industry that is associated with economic activities         | no            |
| [Certification](Certification.md) | Certification mechanisms, seals, and marks for the purpose of demonstrating c... | no            |
| [Term](Term.md)                   | A term and its definitions                                                       | no            |
| [AiAgent](AiAgent.md)             | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [Risk](Risk.md)                   | The state of uncertainty associated with an AI system, that has the potential... | no            |
| [Entry](Entry.md)                 | An entry and its definitions                                                     | no            |
| [Purpose](Purpose.md)             | The end goal for which an entity is used or an action is taken                   | no            |
| [Adapter](Adapter.md)             | Adapter-based methods add extra trainable parameters after the attention and ... | no            |
| [LLMIntrinsic](LLMIntrinsic.md)   | A capability that can be invoked through a well-defined API that is reasonabl... | no            |
| [Control](Control.md)             | A measure that maintains and/or modifies                                         | no            |
| [RiskControl](RiskControl.md)     | A measure that maintains and/or modifies risk (and risk concepts)                | no            |

## Properties

### Type and Range

| Property  | Value                                                                              |
| --------- | ---------------------------------------------------------------------------------- |
| Range     | [Documentation](Documentation.md)                                                  |
| Domain Of | [Control](Control.md), [Entry](Entry.md)                                           |
| Slot URI  | [nexus:hasExternalReference](https://w3id.org/ai-atlas-nexus/hasExternalReference) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Aliases

- additional resources
- external_links

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value               |
| ------------ | -------------------------- |
| self         | nexus:hasExternalReference |
| native       | nexus:hasExternalReference |
| close        | rdfs:seeAlso               |

## LinkML Source

<details>
```yaml
name: hasExternalReference
description: External references / additional resources related to this entity, such
  as articles, tools, or datasets. Distinct from hasDocumentation, which documents
  the entity itself. External references are not necessarily curated or vetted, and
  quality will vary.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
aliases:
- additional resources
- external_links
close_mappings:
- rdfs:seeAlso
rank: 1000
slot_uri: nexus:hasExternalReference
alias: hasExternalReference
domain_of:
- Control
- Entry
range: Documentation
multivalued: true
inlined: false

```
</details></div>
```
