---
search:
  boost: 5.0
---

# Slot: isProvidedBy

_A relationship to the Organization instance that provides this instance._

<div data-search-exclude markdown="1">

URI: [schema:provider](http://schema.org/provider)
Alias: isProvidedBy

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                  | Description                                                           | Modifies Slot |
| --------------------- | --------------------------------------------------------------------- | ------------- |
| [Dataset](Dataset.md) | A body of structured information describing some topic(s) of interest | no            |

## Properties

### Type and Range

| Property  | Value                                         |
| --------- | --------------------------------------------- |
| Range     | [Organization](Organization.md)               |
| Domain Of | [Dataset](Dataset.md)                         |
| Slot URI  | [schema:provider](http://schema.org/provider) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value       |
| ------------ | ------------------ |
| self         | schema:provider    |
| native       | nexus:isProvidedBy |

## LinkML Source

<details>
```yaml
name: isProvidedBy
description: A relationship to the Organization instance that provides this instance.
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
rank: 1000
slot_uri: schema:provider
alias: isProvidedBy
domain_of:
- Dataset
range: Organization

```
</details></div>
```
