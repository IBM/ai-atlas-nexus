# Slot: hasStakeholder

_Indicates stakeholders of an AI system or component._

URI: [airo:hasStakeholder](https://w3id.org/airo#hasStakeholder)
Alias: hasStakeholder

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                                                      | Modifies Slot |
| ----------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiAgent](AiAgent.md)   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities                      | no            |

## Properties

- Range: [Stakeholder](Stakeholder.md)

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | airo:hasStakeholder  |
| native       | nexus:hasStakeholder |

## LinkML Source

<details>
```yaml
name: hasStakeholder
description: Indicates stakeholders of an AI system or component.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: '[''airo:AISystem'', ''airo:AIComponent'']'
slot_uri: airo:hasStakeholder
alias: hasStakeholder
domain_of:
- AiSystem
range: Stakeholder

```
</details>
```
