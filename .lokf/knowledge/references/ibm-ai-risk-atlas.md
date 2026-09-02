---
type: Reference
id: https://w3id.org/ai-atlas-nexus/knowledge/references/ibm-ai-risk-atlas
title: IBM AI Risk Atlas
description: IBM's educational taxonomy of risks associated with generative AI and foundation models, which AI Atlas Nexus builds on and encodes as a risk taxonomy.
resource: https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas
generated:
  by: process:lokf-librarian
  at: "2026-09-02T15:57:00Z"
sources:
  - resource: https://github.com/IBM/ai-atlas-nexus/blob/main/src/ai_atlas_nexus/data/knowledge_graph/risk_atlas_data.yaml
    title: risk_atlas_data.yaml (RiskTaxonomy instance data)
source:
  - https://w3id.org/ai-atlas-nexus/knowledge/org/ibm
---

# Overview

The **IBM AI Risk Atlas** is the taxonomy this project grew out of: AI Atlas Nexus "builds on the IBM AI Risk Atlas making this educational resource a nexus of governance assets and tooling" (repository README). It is encoded in the knowledge graph as `risk_atlas_data.yaml`, whose documentation entries also cite the IBM AI Ethics Board publication [Foundation models: Opportunities, risks and mitigations](https://www.ibm.com/downloads/documents/us-en/10a99803d8afd656). A concept page also exists in this repo's docs at `docs/concepts/IBM_AI_Risk_Atlas.md`.
