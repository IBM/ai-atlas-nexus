# AI Risk ontology and risk taxonomy data

## Using LinkML for the schema and data representation

[LinkML](https://linkml.io/) is a flexible modeling language that allows you to author schemas in YAML that describe the structure of your data. Additionally, it is a framework for working with and validating data in a variety of formats (JSON, RDF, TSV), with generators for compiling LinkML schemas to other frameworks.

For these reasons LinkML is used to represent the AI risk ontology schema and the related data.

See the [LinkML documentation](https://linkml.io/linkml/index.html) for instructions how to install and use it.

## The ontology

The AI risk ontology tries to model AI systems from a risk point of view. It is based on [AIRO](https://w3id.org/airo), but goes beyond it by extending the risk concept to include existing AI risk taxonomies.

See the full documentation of the LinkML classes and slots in the [docs folder](https://github.com/IBM/ai-atlas-nexus/blob/main/docs/index.md).

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
