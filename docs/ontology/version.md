---
search:
  boost: 5.0
---

# Slot: version

_The version of the entity embodied by a specified resource._

<div data-search-exclude markdown="1">

URI: [schema:version](http://schema.org/version)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                                    | Description                                                                      | Modifies Slot |
| ------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [License](License.md)                                   | The general notion of a license which defines terms and grants permissions to... | no            |
| [Vocabulary](Vocabulary.md)                             | A collection of terms, with their definitions and relationships                  | no            |
| [Taxonomy](Taxonomy.md)                                 | A hierachical taxonomy of concepts, with their definitions and relationships     | no            |
| [RiskTaxonomy](RiskTaxonomy.md)                         | A taxonomy of AI system related risks                                            | no            |
| [RiskControlGroupTaxonomy](RiskControlGroupTaxonomy.md) | A taxonomy of AI system related risk controls groups                             | no            |
| [AiTaskTaxonomy](AiTaskTaxonomy.md)                     | A taxonomy of AI Tasks                                                           | no            |
| [CapabilityTaxonomy](CapabilityTaxonomy.md)             | A taxonomy of AI capabilities describing the abilities of AI systems             | no            |

## Properties

### Type and Range

| Property  | Value                                                                                                                                                                                                      |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Range     | [String](String.md)                                                                                                                                                                                        |
| Domain Of | [License](License.md), [Vocabulary](Vocabulary.md), [Taxonomy](Taxonomy.md), [RiskTaxonomy](RiskTaxonomy.md), [RiskControlGroupTaxonomy](RiskControlGroupTaxonomy.md), [AiTaskTaxonomy](AiTaskTaxonomy.md) |
| Slot URI  | [schema:version](http://schema.org/version)                                                                                                                                                                |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value   |
| ------------ | -------------- |
| self         | schema:version |
| native       | nexus:version  |

## LinkML Source

<details>
```yaml
name: version
description: The version of the entity embodied by a specified resource.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: schema:version
domain_of:
- License
- Vocabulary
- Taxonomy
- RiskTaxonomy
- RiskControlGroupTaxonomy
- AiTaskTaxonomy
range: string

```
</details></div>
```
