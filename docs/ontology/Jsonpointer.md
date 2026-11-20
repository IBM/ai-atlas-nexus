---

search:
boost: 1.0
---# Type: Jsonpointer

_A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form._

<div data-search-exclude markdown="1">

URI: [xsd:string](http://www.w3.org/2001/XMLSchema#string)

## Type Properties

| Property       | Value                                                 |
| -------------- | ----------------------------------------------------- |
| Base           | `str`                                                 |
| Type URI       | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Representation | `str`                                                 |

## Notes

- If you are authoring schemas in LinkML YAML, the type is referenced with the lower case "jsonpointer".

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value      |
| ------------ | ----------------- |
| self         | xsd:string        |
| native       | nexus:Jsonpointer |

</div>
