# Slot: hasPurpose

_Indicates the purpose of an entity, e.g. AI system, components._

URI: [airo:hasPurpose](https://w3id.org/airo#hasPurpose)
Alias: hasPurpose

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                                                      | Modifies Slot |
| ----------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiAgent](AiAgent.md)   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities                      | no            |

## Properties

- Range: [Purpose](Purpose.md)

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value     |
| ------------ | ---------------- |
| self         | airo:hasPurpose  |
| native       | nexus:hasPurpose |

## LinkML Source

<details>
```yaml
name: hasPurpose
description: Indicates the purpose of an entity, e.g. AI system, components.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: airo:hasPurpose
alias: hasPurpose
domain_of:
- AiSystem
range: Purpose

```
</details>
```
