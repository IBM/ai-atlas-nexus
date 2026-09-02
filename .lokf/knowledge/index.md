---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/ai-atlas-nexus/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: AI Atlas Nexus Knowledge Bundle
description: AI Atlas Nexus provides tooling to help bring together disparate resources related to governance of foundation models.
license: https://www.apache.org/licenses/LICENSE-2.0
publisher:
  type: Organization
  id: https://w3id.org/ai-atlas-nexus/knowledge/org/ai-atlas-nexus-team
  name: AI Atlas Nexus Team
---

# AI Atlas Nexus Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for AI Atlas Nexus. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [AI Atlas Nexus Python Library](services/python-library.md) - the `ai-atlas-nexus` library and its `AIAtlasNexus` API.
* [ran-extension CLI](services/ran-extension-cli.md) - console script for installing AI Atlas Nexus extensions.

# Datasets

* [AI Risk Ontology (LinkML schema)](datasets/ai-risk-ontology.md) - the modular LinkML schema unifying risk and AI-model views.
* [AI Risk Knowledge Graph (LinkML instance data)](datasets/knowledge-graph.md) - YAML instance data curated from public taxonomies and frameworks.
* [Populated Graph Export](datasets/graph-export.md) - downloadable YAML/OWL/Cypher/JSON/LaTeX projections of the graph.

# References

* [IBM AI Risk Atlas](references/ibm-ai-risk-atlas.md) - the taxonomy AI Atlas Nexus builds on.
* [IBM Granite Guardian](references/granite-guardian.md) - safeguard-model risk dimensions.
* [MIT AI Risk Repository](references/mit-ai-risk-repository.md) - meta-review taxonomy, mitigations, and controls.
* [NIST AI RMF Generative AI Profile](references/nist-ai-rmf-genai-profile.md) - NIST AI 600-1 risks and actions.
* [The AI Risk Taxonomy (AIR 2024)](references/air-2024.md) - regulation/policy-derived risk taxonomy.
* [AILuminate Benchmark](references/ailuminate.md) - MLCommons risk and reliability benchmark.
* [Credo Unified Control Framework](references/credo-ucf.md) - unified AI governance controls.
* [OWASP Top 10 for LLM Applications](references/owasp-llm-top10.md) - LLM application risks (v2.0).
* [OWASP Top 10 for Agentic Applications](references/owasp-agentic-applications.md) - agentic application risks (2026).
* [OWASP Agentic Skills Top 10](references/owasp-agentic-skills-top10.md) - security risks in reusable AI agent skills.
* [EU AI Act](references/eu-ai-act.md) - EU regulation modelled as an ontology module.
* [LinkML](references/linkml.md) - the modelling framework the ontology is built with.

# Playbooks

* [Knowledge Sources Map](playbooks/knowledge-sources.md) - where this bundle's knowledge comes from and how to re-check it.
* [Contributing a Taxonomy or CoT Templates](playbooks/contributing-a-taxonomy.md) - add taxonomies, mappings, and CoT templates.
* [Regenerate Repository Artifacts](playbooks/regenerate-artifacts.md) - Makefile targets for regenerating generated outputs.

# Tutorials

* [AI Atlas Nexus Quickstart](tutorials/quickstart.md) - notebook overview of the library's functionality.

# Glossary

* [Chain of Thought (CoT) Template](glossary/cot-template.md) - prompt template for systematic reasoning and improved accuracy.

# Organizations

* [AI Atlas Nexus Team](org/ai-atlas-nexus-team.md) - maintainer team and bundle publisher.
* [IBM](org/ibm.md) - originator of the project and of several encoded taxonomies.
