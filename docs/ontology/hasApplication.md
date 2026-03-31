# Slot: hasApplication

_The application category, Optional or Mandatory._

URI: [nexus:hasApplication](https://ibm.github.io/ai-atlas-nexus/ontology/hasApplication)
Alias: hasApplication

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                          | Description                                                                      | Modifies Slot |
| ----------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Requirement](Requirement.md) | A requirement representing a combination of obligation, permission, or prohib... | no            |

## Properties

- Range: [AIUC1ApplicationCategory](AIUC1ApplicationCategory.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | nexus:hasApplication |
| native       | nexus:hasApplication |

## LinkML Source

<details>
```yaml
name: hasApplication
description: The application category, Optional or Mandatory.
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: nexus:hasApplication
alias: hasApplication
domain_of:
- Requirement
range: AIUC1ApplicationCategory
multivalued: true
inlined: false

```
</details>
```
