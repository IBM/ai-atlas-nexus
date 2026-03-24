# Slot: isComposedOf

_Relationship indicating the some entity is composed of other entities (including some of the same type)._

URI: [nexus:isComposedOf](https://ibm.github.io/ai-atlas-nexus/ontology/isComposedOf)
Alias: isComposedOf

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                    | Description                                                                      | Modifies Slot |
| ----------------------- | -------------------------------------------------------------------------------- | ------------- |
| [AiAgent](AiAgent.md)   | An artificial intelligence (AI) agent refers to a system or program that is c... | no            |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities                      | yes           |

## Properties

- Range: [String](String.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | nexus:isComposedOf |
| native       | nexus:isComposedOf |

## LinkML Source

<details>
```yaml
name: isComposedOf
description: Relationship indicating the some entity is composed of other entities
  (including some of the same type).
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
alias: isComposedOf
domain_of:
- AiSystem
range: string
multivalued: true
inlined: false

```
</details>
```
