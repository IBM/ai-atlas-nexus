# Change Log

## 2026-09-02
* **EU AI Act citation**: `references/eu-ai-act` now carries the canonical ELI URI
  (`http://data.europa.eu/eli/reg/2024/1689/oj`) as `sameAs` alongside the EUR-Lex
  landing page, with the body stating plainly that neither URL is recorded in this
  repository. A maintainer confirmed the citation, recorded as a `verified` event.
* **Audit corrections**: Verified every concept against the repository and fixed
  four. `datasets/ai-risk-ontology` gained the schema's declared `version` (0.5.0)
  and `license`, its EU AI Act link became `derivedFrom` (the schema encodes that
  vocabulary), and its body now states the root import closure precisely -
  `energy.yaml`/`eu_ai_act.yaml` enter via `ai_system.yaml`, while
  `semweb_context.yaml` is a CURIE map, not an import. `datasets/graph-export`
  distributions now name each export file exactly (Cypher, Sigma.js JSON, LaTeX)
  instead of their folders, and reference the regenerate-artifacts playbook.
  `glossary/cot-template` references that playbook too. The source map gained rows
  for the templates, mappings, datamodel/util, `CONTRIBUTING.md`, `LICENSE`, and
  `docs/concepts/IBM_AI_Risk_Atlas.md`, typed relations to the concepts it maps,
  and an accurate left-out list (toolkit, nav stubs, presentation assets).
* **Bootstrap discovery**: Replaced the scaffold's placeholder services with 23 real
  concepts scraped from the repository - 2 services (Python library, `ran-extension`
  CLI), 3 datasets (AI Risk Ontology schema, knowledge-graph instance data, graph
  export), 11 references (IBM AI Risk Atlas, Granite Guardian, MIT AI Risk
  Repository, NIST AI RMF GenAI Profile, AIR 2024, AILuminate, Credo UCF, OWASP
  LLM/Agentic Top 10s, EU AI Act, LinkML), 3 playbooks (knowledge-sources map,
  contributing a taxonomy, regenerate artifacts), 1 tutorial (Quickstart), 1
  glossary term (CoT template), and 2 organizations (AI Atlas Nexus Team, IBM).
  Recorded the scrape map in `playbooks/knowledge-sources.md`.
* **Initialization**: Scaffolded the LOKF bundle for AI Atlas Nexus with placeholder
  services. Real concepts to follow.
