---
search:
  boost: 10.0
---

# Class: SourceData

_Information about the data source used in evaluation_

<div data-search-exclude markdown="1">

URI: [nexus:sourcedata](https://w3id.org/ai-atlas-nexus/sourcedata)

```mermaid
 classDiagram
    class SourceData
    click SourceData href "../SourceData/"
      Entity <|-- SourceData
        click Entity href "../Entity/"

      SourceData : broad_mappings





        SourceData --> "*" Any : broad_mappings
        click Any href "../Any/"



      SourceData : close_mappings





        SourceData --> "*" Any : close_mappings
        click Any href "../Any/"



      SourceData : dataset_name

      SourceData : dateCreated

      SourceData : dateModified

      SourceData : description

      SourceData : exact_mappings





        SourceData --> "*" Any : exact_mappings
        click Any href "../Any/"



      SourceData : hasLifecycleStatus





        SourceData --> "0..1" LifecycleStatus : hasLifecycleStatus
        click LifecycleStatus href "../LifecycleStatus/"



      SourceData : hf_repo

      SourceData : hf_split

      SourceData : id

      SourceData : isCategorizedAs





        SourceData --> "*" Any : isCategorizedAs
        click Any href "../Any/"



      SourceData : name

      SourceData : narrow_mappings





        SourceData --> "*" Any : narrow_mappings
        click Any href "../Any/"



      SourceData : notes

      SourceData : related_mappings





        SourceData --> "*" Any : related_mappings
        click Any href "../Any/"



      SourceData : source_type

      SourceData : url


```

## Inheritance

- [Entity](Entity.md)
  - **SourceData**

## Class Properties

| Property  | Value                                                          |
| --------- | -------------------------------------------------------------- |
| Class URI | [nexus:sourcedata](https://w3id.org/ai-atlas-nexus/sourcedata) |

## Slots

| Name                                        | Cardinality and Range                            | Description                                                                      | Inheritance         |
| ------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------- | ------------------- |
| [dataset_name](dataset_name.md)             | 0..1 <br/> [String](String.md)                   | Name of the dataset                                                              | direct              |
| [source_type](source_type.md)               | 0..1 <br/> [String](String.md)                   | Type of data source (e                                                           | direct              |
| [hf_repo](hf_repo.md)                       | 0..1 <br/> [String](String.md)                   | HuggingFace repository                                                           | direct              |
| [hf_split](hf_split.md)                     | 0..1 <br/> [String](String.md)                   | HuggingFace dataset split                                                        | direct              |
| [id](id.md)                                 | 1 <br/> [String](String.md)                      | A unique identifier to this instance of the model element                        | [Entity](Entity.md) |
| [name](name.md)                             | 0..1 <br/> [String](String.md)                   | A text name of this instance                                                     | [Entity](Entity.md) |
| [description](description.md)               | 0..1 <br/> [String](String.md)                   | The description of an entity                                                     | [Entity](Entity.md) |
| [url](url.md)                               | 0..1 <br/> [Uri](Uri.md)                         | An optional URL associated with this instance                                    | [Entity](Entity.md) |
| [dateCreated](dateCreated.md)               | 0..1 <br/> [Date](Date.md)                       | The date on which the entity was created                                         | [Entity](Entity.md) |
| [dateModified](dateModified.md)             | 0..1 <br/> [Date](Date.md)                       | The date on which the entity was most recently modified                          | [Entity](Entity.md) |
| [exact_mappings](exact_mappings.md)         | \* <br/> [Any](Any.md)                           | The property is used to link two concepts, indicating a high degree of confid... | [Entity](Entity.md) |
| [close_mappings](close_mappings.md)         | \* <br/> [Any](Any.md)                           | The property is used to link two concepts that are sufficiently similar that ... | [Entity](Entity.md) |
| [related_mappings](related_mappings.md)     | \* <br/> [Any](Any.md)                           | The property skos:relatedMatch is used to state an associative mapping link b... | [Entity](Entity.md) |
| [narrow_mappings](narrow_mappings.md)       | \* <br/> [Any](Any.md)                           | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [broad_mappings](broad_mappings.md)         | \* <br/> [Any](Any.md)                           | The property is used to state a hierarchical mapping link between two concept... | [Entity](Entity.md) |
| [isCategorizedAs](isCategorizedAs.md)       | \* <br/> [Any](Any.md)                           | A relationship where an entity has been deemed to be categorized                 | [Entity](Entity.md) |
| [hasLifecycleStatus](hasLifecycleStatus.md) | 0..1 <br/> [LifecycleStatus](LifecycleStatus.md) | The editorial / publication lifecycle state of this entity                       | [Entity](Entity.md) |
| [notes](notes.md)                           | \* <br/> [String](String.md)                     | Free-text editorial notes, source breadcrumbs, or build-time provenance that ... | [Entity](Entity.md) |

## Usages

| used by                                             | used in                           | type  | used                        |
| --------------------------------------------------- | --------------------------------- | ----- | --------------------------- |
| [EvaluationResultRecord](EvaluationResultRecord.md) | [hasSourceData](hasSourceData.md) | range | [SourceData](SourceData.md) |

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value     |
| ------------ | ---------------- |
| self         | nexus:sourcedata |
| native       | nexus:SourceData |

## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SourceData
description: Information about the data source used in evaluation
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entity
attributes:
  dataset_name:
    name: dataset_name
    description: Name of the dataset
    from_schema: https://w3id.org/ai-atlas-nexus/ai_eval
    rank: 1000
    domain_of:
    - SourceData
    range: string
  source_type:
    name: source_type
    description: Type of data source (e.g., hf_dataset)
    from_schema: https://w3id.org/ai-atlas-nexus/ai_eval
    domain_of:
    - SourceMetadata
    - SourceData
    range: string
  hf_repo:
    name: hf_repo
    description: HuggingFace repository
    from_schema: https://w3id.org/ai-atlas-nexus/ai_eval
    rank: 1000
    domain_of:
    - SourceData
    range: string
  hf_split:
    name: hf_split
    description: HuggingFace dataset split
    from_schema: https://w3id.org/ai-atlas-nexus/ai_eval
    rank: 1000
    domain_of:
    - SourceData
    range: string
class_uri: nexus:sourcedata

````
</details>

### Induced

<details>
```yaml
name: SourceData
description: Information about the data source used in evaluation
from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
is_a: Entity
attributes:
  dataset_name:
    name: dataset_name
    description: Name of the dataset
    from_schema: https://w3id.org/ai-atlas-nexus/ai_eval
    rank: 1000
    owner: SourceData
    domain_of:
    - SourceData
    range: string
  source_type:
    name: source_type
    description: Type of data source (e.g., hf_dataset)
    from_schema: https://w3id.org/ai-atlas-nexus/ai_eval
    owner: SourceData
    domain_of:
    - SourceMetadata
    - SourceData
    range: string
  hf_repo:
    name: hf_repo
    description: HuggingFace repository
    from_schema: https://w3id.org/ai-atlas-nexus/ai_eval
    rank: 1000
    owner: SourceData
    domain_of:
    - SourceData
    range: string
  hf_split:
    name: hf_split
    description: HuggingFace dataset split
    from_schema: https://w3id.org/ai-atlas-nexus/ai_eval
    rank: 1000
    owner: SourceData
    domain_of:
    - SourceData
    range: string
  id:
    name: id
    description: A unique identifier to this instance of the model element. Example
      identifiers include UUID, URI, URN, etc.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    owner: SourceData
    domain_of:
    - Entity
    range: string
    required: true
  name:
    name: name
    description: A text name of this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:name
    owner: SourceData
    domain_of:
    - Entity
    - BenchmarkMetadataCard
    range: string
  description:
    name: description
    description: The description of an entity
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:description
    owner: SourceData
    domain_of:
    - Entity
    range: string
  url:
    name: url
    description: An optional URL associated with this instance.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:url
    owner: SourceData
    domain_of:
    - Entity
    range: uri
  dateCreated:
    name: dateCreated
    description: The date on which the entity was created.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateCreated
    owner: SourceData
    domain_of:
    - Entity
    range: date
    required: false
  dateModified:
    name: dateModified
    description: The date on which the entity was most recently modified.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: schema:dateModified
    owner: SourceData
    domain_of:
    - Entity
    range: date
    required: false
  exact_mappings:
    name: exact_mappings
    description: The property is used to link two concepts, indicating a high degree
      of confidence that the concepts can be used interchangeably across a wide range
      of information retrieval applications
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:exactMatch
    owner: SourceData
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  close_mappings:
    name: close_mappings
    description: The property is used to link two concepts that are sufficiently similar
      that they can be used interchangeably in some information retrieval applications.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:closeMatch
    owner: SourceData
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  related_mappings:
    name: related_mappings
    description: The property skos:relatedMatch is used to state an associative mapping
      link between two concepts.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:relatedMatch
    owner: SourceData
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  narrow_mappings:
    name: narrow_mappings
    description: The property is used to state a hierarchical mapping link between
      two concepts, indicating that the concept linked to, is a narrower concept than
      the originating concept.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:narrowMatch
    owner: SourceData
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  broad_mappings:
    name: broad_mappings
    description: The property is used to state a hierarchical mapping link between
      two concepts, indicating that the concept linked to, is a broader concept than
      the originating concept.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:broadMatch
    owner: SourceData
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  isCategorizedAs:
    name: isCategorizedAs
    description: A relationship where an entity has been deemed to be categorized
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: nexus:isCategorizedAs
    owner: SourceData
    domain_of:
    - Entity
    range: Any
    multivalued: true
    inlined: false
  hasLifecycleStatus:
    name: hasLifecycleStatus
    description: The editorial / publication lifecycle state of this entity. Distinct
      from AiLifecyclePhase, which describes an AI system's runtime evolution rather
      than the editorial workflow of a catalogued entry.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    aliases:
    - lifecycle_status
    - doc_status
    rank: 1000
    slot_uri: adms:status
    owner: SourceData
    domain_of:
    - Entity
    range: LifecycleStatus
  notes:
    name: notes
    description: Free-text editorial notes, source breadcrumbs, or build-time provenance
      that do not belong in the user-facing description. Opaque to consumers.
    from_schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology
    rank: 1000
    slot_uri: skos:note
    owner: SourceData
    domain_of:
    - Entity
    range: string
    recommended: false
    multivalued: true
class_uri: nexus:sourcedata

````

</details></div>
