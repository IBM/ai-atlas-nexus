---
type: Reference
id: https://w3id.org/ai-atlas-nexus/knowledge/references/owasp-agentic-skills-top10
title: OWASP Agentic Skills Top 10
description: The OWASP Agentic Skills Top 10, documenting ten security risks in reusable AI agent skills, encoded as a risk taxonomy in the knowledge graph.
version: "1.0 (2026 Edition)"
resource: https://owasp.org/www-project-agentic-skills-top-10/
generated:
  by: process:lokf-librarian
  at: "2026-09-02T16:35:47Z"
sources:
  - resource: https://github.com/IBM/ai-atlas-nexus/blob/main/src/ai_atlas_nexus/data/knowledge_graph/owasp_ast10_data.yaml
    title: owasp_ast10_data.yaml (RiskTaxonomy instance data)
  - resource: https://owasp.org/www-project-agentic-skills-top-10/assets/publications/ast10-top10-whitepaper-2.pdf
    title: OWASP Agentic Skills Top 10 Whitepaper (V1)
---

# Overview

The **OWASP Agentic Skills Top 10** (taxonomy id `owasp-ast10`) is encoded in `owasp_ast10_data.yaml`, with entries `AST01`-`AST10`. Per the data file, it "focuses on the skill layer, where instructions, code, dependencies, metadata, distribution channels, and runtime permissions combine to shape agent behavior" - distinct from the [OWASP Top 10 for Agentic Applications](owasp-agentic-applications.md), which covers agentic applications as a whole. A cross-taxonomy mapping to the IBM AI Risk Atlas ships alongside it as `mappings/owasp_ast10_to_ibm_risk_atlas_from_tsv_data.yaml`.
