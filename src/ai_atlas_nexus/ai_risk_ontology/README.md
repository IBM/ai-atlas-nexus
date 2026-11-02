# AI Risk ontology and risk taxonomy data

## Using LinkML for the schema and data representation

[LinkML](https://linkml.io/) is a flexible modeling language that allows you to author schemas in YAML that describe the structure of your data. Additionally, it is a framework for working with and validating data in a variety of formats (JSON, RDF, TSV), with generators for compiling LinkML schemas to other frameworks.

For these reasons LinkML is used to represent the AI risk ontology schema and the related data.

See the [LinkML documentation](https://linkml.io/linkml/index.html) for instructions how to install and use it.

## The ontology

The AI risk ontology tries to model AI systems from a risk point of view. It is based on [AIRO](https://w3id.org/airo), but goes beyond it by extending the risk concept to include existing AI risk taxonomies.

See the full documentation of the LinkML classes and slots in the [docs folder](https://github.com/IBM/ai-atlas-nexus/blob/main/docs/index.md).

## Persistent identifiers

The ontology is published under the persistent namespace `https://w3id.org/ai-atlas-nexus/`
(the `nexus:` prefix used by every module). The redirects are maintained at
[perma-id/w3id.org](https://github.com/perma-id/w3id.org/tree/master/ids/ai-atlas-nexus).

| Identifier | Resolves to |
| --- | --- |
| `https://w3id.org/ai-atlas-nexus/` and `https://w3id.org/ai-atlas-nexus/<Term>` | documentation page in a browser; RDF / SHACL / LinkML YAML via the `Accept` header |
| `https://w3id.org/ai-atlas-nexus/ai-risk-ontology.yaml` | the whole ontology as one self-contained LinkML schema (`project/linkml/ai-risk-ontology.merged.linkml.yaml`) |
| `https://w3id.org/ai-atlas-nexus/<module>.yaml`, e.g. `common.yaml` | the source module (`schema/<module>.yaml`) |
| `https://w3id.org/ai-atlas-nexus/schema/<path>.yaml` | any file of the schema source tree, including the modular root |
| `https://w3id.org/ai-atlas-nexus/ai-risk-ontology.owl.ttl` and `.shacl.ttl` | the `project/` artefacts |
| `https://w3id.org/ai-atlas-nexus/graph_export/<fmt>/<file>` | the exported knowledge graph |
| `https://w3id.org/ai-atlas-nexus/v<semver>/...` | any of the above pinned to a release tag |

The `project/` directory is regenerated with `make regenerate_project` (also run by the regenerate-on-merge workflow); do not edit content by hand. Only the artefacts this project already published are generated; JSON-LD, JSON Schema, ShEx, GraphQL, Protobuf, SQL DDL and the prefix map can each be enabled by removing a line from `.linkml/generators.yaml`.

### Importing the ontology from another LinkML schema

```yaml
prefixes:
  nexus: https://w3id.org/ai-atlas-nexus/
imports:
  - linkml:types
  - nexus:ai-risk-ontology
```

LinkML appends `.yaml` to the expanded CURIE and fetches the self-contained schema, so no
vendoring is needed. The modular root (`schema/ai-risk-ontology.yaml`) is meant for direct
loading (`SchemaView(url)`) and local development: its sibling-module imports are resolved
relative to the file that declares them, which LinkML does not do for schemas reached
through another schema's `imports:`.

## The risk taxonomy data

Included are 7 different risk taxonomies:

- the [IBM AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas)
- [IBM Granite Guardian](https://arxiv.org/abs/2412.07724)
- the [NIST AI Risk Management Framework](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- the [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- the [MIT AI Risk Repository](https://airisk.mit.edu/)
- the [AI Risk Taxonomy (AIR 2024)](https://arxiv.org/pdf/2406.17864)
- the [AILuminate Benchmark](https://arxiv.org/pdf/2503.05731)
- the [Unified Control Framework](https://arxiv.org/pdf/2503.05937v1) from Credo
