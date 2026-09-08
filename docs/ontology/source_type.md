---
search:
  boost: 5.0
---

# Slot: source_type

<div data-search-exclude markdown="1">

URI: [nexus:source_type](https://w3id.org/ai-atlas-nexus/source_type)

<!-- no inheritance hierarchy -->

## Applicable Classes

| Name                                | Description                                          | Modifies Slot |
| ----------------------------------- | ---------------------------------------------------- | ------------- |
| [SourceMetadata](SourceMetadata.md) | Metadata about the source of an evaluation           | no            |
| [SourceData](SourceData.md)         | Information about the data source used in evaluation | no            |

## Properties

### Type and Range

| Property  | Value                                                            |
| --------- | ---------------------------------------------------------------- |
| Range     | [String](String.md)                                              |
| Domain Of | [SourceMetadata](SourceMetadata.md), [SourceData](SourceData.md) |

### Cardinality and Requirements

| Property | Value |
| -------- | ----- |

## Identifier and Mapping Information

## Mappings

| Mapping Type | Mapped Value      |
| ------------ | ----------------- |
| self         | nexus:source_type |
| native       | nexus:source_type |

## LinkML Source

<details>
```yaml
name: source_type
domain_of:
- SourceMetadata
- SourceData
range: string

```
</details></div>
```
