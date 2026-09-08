---
search:
  boost: 5.0
---

# Slot: author

<div data-search-exclude markdown="1">

URI: [nexus:author](https://w3id.org/ai-atlas-nexus/author)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                              | Description                                                           | Modifies Slot |
| --------------------------------- | --------------------------------------------------------------------- | ------------- |
| [Documentation](Documentation.md) | Documented information about a concept or other topic(s) of interest  | no            |
| [RiskIncident](RiskIncident.md)   | An event occuring or occured which is a realised or materialised risk | no            |

## Properties

### Type and Range

| Property  | Value                                                              |
| --------- | ------------------------------------------------------------------ |
| Range     | [String](String.md)                                                |
| Domain Of | [Documentation](Documentation.md), [RiskIncident](RiskIncident.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

## Mappings

| Mapping Type | Mapped Value |
| ------------ | ------------ |
| self         | nexus:author |
| native       | nexus:author |

## LinkML Source

<details>
```yaml
name: author
domain_of:
- Documentation
- RiskIncident
range: string

```
</details></div>
```
