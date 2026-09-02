---
search:
  boost: 5.0
---

# Slot: isAppliedWithinDomain

_Specifies the domain an AI system is used within._

<div data-search-exclude markdown="1">

URI: [airo:isAppliedWithinDomain](https://w3id.org/airo#isAppliedWithinDomain)
Alias: isAppliedWithinDomain

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                                                      | Modifies Slot |
| ----------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiAgent](AiAgent.md)   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities                      | no            |

## Properties

### Type and Range

| Property  | Value                                                                     |
| --------- | ------------------------------------------------------------------------- |
| Range     | [Domain](Domain.md)                                                       |
| Domain Of | [AiSystem](AiSystem.md)                                                   |
| Slot URI  | [airo:isAppliedWithinDomain](https://w3id.org/airo#isAppliedWithinDomain) |

### Cardinality and Requirements

| Property    | Value |
| ----------- | ----- |
| Multivalued | Yes   |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value                |
| ------------ | --------------------------- |
| self         | airo:isAppliedWithinDomain  |
| native       | nexus:isAppliedWithinDomain |

## LinkML Source

<details>
```yaml
name: isAppliedWithinDomain
description: Specifies the domain an AI system is used within.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: airo:isAppliedWithinDomain
alias: isAppliedWithinDomain
domain_of:
- AiSystem
range: Domain
multivalued: true
inlined: false

```
</details></div>
```
