# Slot: isAppliedWithinDomain

_Specifies the domain an AI system is used within._

URI: [airo:isAppliedWithinDomain](https://w3id.org/airo#isAppliedWithinDomain)
Alias: isAppliedWithinDomain

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                                                      | Modifies Slot |
| ----------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiAgent](AiAgent.md)   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities                      | no            |

## Properties

- Range: [Domain](Domain.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

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
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: '[''AISystem'', ''AIComponent'']'
slot_uri: airo:isAppliedWithinDomain
alias: isAppliedWithinDomain
domain_of:
- AiSystem
range: Domain
multivalued: true
inlined: false

```
</details>
```
