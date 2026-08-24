"""Integration tests for the OWASP Agentic Skills Top 10 taxonomy."""

# Internal
from src.ai_atlas_nexus import AIAtlasNexus

# Unit Test Infrastructure
from tests.base import TestCaseBase


class TestOWASPAST10Integration(TestCaseBase):
    """Tests for the OWASP Agentic Skills Top 10 integration."""

    @classmethod
    def setUpClass(cls):
        """Load AI Atlas Nexus data."""
        cls.nexus = AIAtlasNexus()

    def test_taxonomy_and_documentation_loaded(self):
        """Verify the taxonomy and whitepaper record are loaded."""
        taxonomy = self.nexus.get_taxonomy_by_id("owasp-ast10")

        self.assertEqual(taxonomy.name, "OWASP Agentic Skills Top 10")
        self.assertEqual(taxonomy.version, "1.0 (2026 Edition)")
        self.assertEqual(taxonomy.hasLicense, "license-cc-by-sa-4.0")

        documents = [
            document
            for document in self.nexus.get_documents()
            if document.id
            == "owasp-agentic-skills-top-10-whitepaper-v1"
        ]

        self.assertEqual(len(documents), 1)
        self.assertEqual(
            documents[0].hasLicense,
            "license-cc-by-sa-4.0",
        )

    def test_all_ten_risks_loaded(self):
        """Verify all 10 OWASP AST10 risks are loaded."""
        risks = self.nexus.get_all_risks(taxonomy="owasp-ast10")

        expected_ids = {
            "ast01-malicious-skills",
            "ast02-supply-chain-compromise",
            "ast03-over-privileged-skills",
            "ast04-insecure-metadata",
            "ast05-untrusted-external-instructions",
            "ast06-weak-isolation",
            "ast07-update-drift",
            "ast08-poor-scanning",
            "ast09-no-governance",
            "ast10-cross-platform-reuse",
        }

        self.assertEqual({risk.id for risk in risks}, expected_ids)

    def test_mappings_are_bidirectional(self):
        """Verify at least 12 mappings and their inverse relationships."""
        risks = self.nexus.get_all_risks(taxonomy="owasp-ast10")

        mapping_count = sum(
            len(risk.related_mappings or [])
            for risk in risks
        )
        self.assertGreaterEqual(
            mapping_count,
            12,
            "Expected at least 12 mappings for OWASP AST10 risks",
        )

        for risk in risks:
            self.assertGreater(len(risk.related_mappings or []), 0)

            for target_id in risk.related_mappings:
                target = self.nexus.get_risk(id=target_id)

                self.assertIsNotNone(target)
                self.assertIn(
                    risk.id,
                    target.related_mappings or [],
                )
