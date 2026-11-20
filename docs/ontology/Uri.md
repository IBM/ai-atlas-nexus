---

search:
boost: 1.0
---# Type: Uri

_a complete URI_

<div data-search-exclude markdown="1">

URI: [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI)

## Type Properties

| Property       | Value                                                 |
| -------------- | ----------------------------------------------------- |
| Base           | `URI`                                                 |
| Type URI       | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Representation | `str`                                                 |

## Comments

- in RDF serializations a slot with range of uri is treated as a literal or type xsd:anyURI unless it is an identifier or a reference to an identifier, in which case it is translated directly to a node

## Notes

- If you are authoring schemas in LinkML YAML, the type is referenced with the lower case "uri".

## Identifier and Mapping Information

### Schema Source

- from schema: https://w3id.org/ai-atlas-nexus/ai-risk-ontology

## Mappings

| Mapping Type | Mapped Value |
| ------------ | ------------ |
| self         | xsd:anyURI   |
| native       | nexus:Uri    |
| close        | schema:URL   |

</div>
