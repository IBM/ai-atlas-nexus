# Slot: controls

_A list of AI controls_

URI: [nexus:controls](https://ibm.github.io/ai-atlas-nexus/ontology/controls)
Alias: controls

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                      | Description                                                | Modifies Slot |
| ------------------------- | ---------------------------------------------------------- | ------------- |
| [Container](Container.md) | An umbrella object that holds the ontology class instances | no            |

## Properties

- Range: [Control](Control.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value   |
| ------------ | -------------- |
| self         | nexus:controls |
| native       | nexus:controls |

## LinkML Source

<details>
```yaml
name: controls
description: A list of AI controls
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
alias: controls
owner: Container
domain_of:
- Container
range: Control
multivalued: true
inlined: true
inlined_as_list: true

```
</details>
```
