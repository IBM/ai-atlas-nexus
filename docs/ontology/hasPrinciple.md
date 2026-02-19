# Slot: hasPrinciple

_Which of the AIUC-1 principles this requirement belongs to_

URI: [dpv:isPartOf](https://w3id.org/dpv#isPartOf)
Alias: hasPrinciple

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                          | Description                                                                      | Modifies Slot |
| ----------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Requirement](Requirement.md) | A requirement representing a combination of obligation, permission, or prohib... | no            |

## Properties

- Range: [Principle](Principle.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | dpv:isPartOf       |
| native       | nexus:hasPrinciple |

## LinkML Source

<details>
```yaml
name: hasPrinciple
description: Which of the AIUC-1 principles this requirement belongs to
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: dpv:isPartOf
alias: hasPrinciple
domain_of:
- Requirement
range: Principle
multivalued: true
inlined: false

```
</details>
```
