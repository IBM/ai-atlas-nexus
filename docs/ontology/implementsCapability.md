# Slot: implementsCapability

_Indicates that this adapter implements a specific capability_

URI: [nexus:implementsCapability](https://ibm.github.io/ai-atlas-nexus/ontology/implementsCapability)
Alias: implementsCapability

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                  | Description                                                                      | Modifies Slot |
| --------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Adapter](Adapter.md) | Adapter-based methods add extra trainable parameters after the attention and ... | no            |

## Properties

- Range: [Capability](Capability.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value               |
| ------------ | -------------------------- |
| self         | nexus:implementsCapability |
| native       | nexus:implementsCapability |

## LinkML Source

<details>
```yaml
name: implementsCapability
description: Indicates that this adapter implements a specific capability
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
domain: Any
alias: implementsCapability
domain_of:
- Adapter
inverse: implementedByAdapter
range: Capability
multivalued: true
inlined: false

```
</details>
```
