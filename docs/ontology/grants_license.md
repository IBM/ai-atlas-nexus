---
search:
  boost: 5.0
---

# Slot: grants_license

_A relationship from a granting entity such as an Organization to a License instance._

<div data-search-exclude markdown="1">

URI: [nexus:grants_license](https://w3id.org/ai-atlas-nexus/grants_license)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                            | Description                                                                      | Modifies Slot |
| ------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| [Organization](Organization.md) | Any organizational entity such as a corporation, educational institution, con... | no            |
| [AiProvider](AiProvider.md)     | A provider under the AI Act is defined by Article 3(3) as a natural or legal ... | no            |
| [AiOffice](AiOffice.md)         | The EU AI Office (https://digital-strategy                                       | no            |

## Properties

### Type and Range

| Property  | Value                           |
| --------- | ------------------------------- |
| Range     | [License](License.md)           |
| Domain Of | [Organization](Organization.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value         |
| ------------ | -------------------- |
| self         | nexus:grants_license |
| native       | nexus:grants_license |

## LinkML Source

<details>
```yaml
name: grants_license
description: A relationship from a granting entity such as an Organization to a License
  instance.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
domain_of:
- Organization
range: License

```
</details></div>
```
