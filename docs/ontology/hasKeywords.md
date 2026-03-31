# Slot: hasKeywords

_A collection of keywords_

URI: [nexus:hasKeywords](https://ibm.github.io/ai-atlas-nexus/ontology/hasKeywords)
Alias: hasKeywords

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                          | Description                                                                      | Modifies Slot |
| ----------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Requirement](Requirement.md) | A requirement representing a combination of obligation, permission, or prohib... | no            |

## Properties

- Range: [String](String.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value      |
| ------------ | ----------------- |
| self         | nexus:hasKeywords |
| native       | nexus:hasKeywords |

## LinkML Source

<details>
```yaml
name: hasKeywords
description: A collection of keywords
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasKeywords
alias: hasKeywords
domain_of:
- Requirement
range: string
multivalued: true
inlined: false

```
</details>
```
