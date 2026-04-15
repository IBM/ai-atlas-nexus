# Slot: isUsedWithinLocality

_Specifies the domain an AI system is used within._

URI: [airo:isUsedWithinLocality](https://w3id.org/airo#isUsedWithinLocality)
Alias: isUsedWithinLocality

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                                                      | Modifies Slot |
| ----------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiAgent](AiAgent.md)   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities                      | no            |

## Properties

- Range: [LocalityOfUse](LocalityOfUse.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value               |
| ------------ | -------------------------- |
| self         | airo:isUsedWithinLocality  |
| native       | nexus:isUsedWithinLocality |

## LinkML Source

<details>
```yaml
name: isUsedWithinLocality
description: Specifies the domain an AI system is used within.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: '[''AISystem'', ''AIComponent'']'
slot_uri: airo:isUsedWithinLocality
alias: isUsedWithinLocality
domain_of:
- AiSystem
range: LocalityOfUse
multivalued: true
inlined: false

```
</details>
```
