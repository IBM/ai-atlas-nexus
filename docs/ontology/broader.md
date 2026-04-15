# Slot: broader

URI: [skos:narrower](http://www.w3.org/2004/02/skos/core#narrower)
Alias: broader

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                    | Description                                                                      | Modifies Slot |
| --------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [RiskControlGroup](RiskControlGroup.md) | A group of AI system related risk controls                                       | no            |
| [Group](Group.md)                       | Labelled groups of concepts                                                      | no            |
| [RiskGroup](RiskGroup.md)               | A group of AI system related risks that are part of a risk taxonomy              | no            |
| [CapabilityDomain](CapabilityDomain.md) | A high-level domain of AI capabilities (e                                        | no            |
| [StakeholderGroup](StakeholderGroup.md) | An AI system stakeholder grouping                                                | no            |
| [CapabilityGroup](CapabilityGroup.md)   | A group of AI capabilities that are part of a capability taxonomy, organized ... | no            |

## Properties

- Range: [String](String.md)

- Multivalued: True

## Identifier and Mapping Information

### Schema Source

- from schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value  |
| ------------ | ------------- |
| self         | skos:narrower |
| native       | nexus:broader |

## LinkML Source

<details>
```yaml
name: broader
from_schema: https://ibm.github.io/ai-atlas-nexus/ontology/ai-risk-ontology
rank: 1000
slot_uri: skos:narrower
alias: broader
owner: Group
domain_of:
- Group
range: string
multivalued: true

```
</details>
```
