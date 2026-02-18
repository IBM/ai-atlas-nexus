"""
Tests for AutoBenchmarkCardLoader HF data import
"""

import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch


def get_loader():
    """Helper to get loader instance with mocked dataset and AIAtlasNexus"""
    with patch("datasets.load_dataset") as mock_load_dataset, \
         patch("src.ai_atlas_nexus.blocks.hf_data_loader.auto_benchmark_card.AIAtlasNexus"):
        mock_dataset = MagicMock()
        mock_dataset.__len__ = MagicMock(return_value=0)
        mock_load_dataset.return_value = mock_dataset

        from src.ai_atlas_nexus.blocks.hf_data_loader.auto_benchmark_card import (
            AutoBenchmarkCardLoader,
        )
        return AutoBenchmarkCardLoader()


class TestAutoBenchmarkCardTransformation:
    """Test transformation logic of AutoBenchmarkCardLoader"""

    def test_transform_record_minimal(self):
        """Test transforming a minimal benchmark card record"""
        loader = get_loader()

        record = {
            "benchmark_card": {
                "benchmark_details": {
                    "name": "MMLU",
                    "overview": "Massive Multitask Language Understanding",
                    "data_type": "text",
                    "domains": ["general"],
                    "languages": ["English"],
                    "resources": ["https://github.com/hendrycks/test"],
                    "similar_benchmarks": [],
                },
                "data": {
                    "source": "Hendricks et al.",
                    "size": "15000",
                    "format": "Multiple choice",
                    "annotation": "Expert annotated",
                },
                "methodology": {
                    "methods": ["Multiple choice"],
                    "metrics": ["Accuracy"],
                    "calculation": "Fraction of correct answers",
                    "interpretation": "Higher is better",
                    "baseline_results": "50% random chance",
                    "validation": "Holdout test set",
                },
                "purpose_and_intended_users": {
                    "tasks": ["Question answering"],
                    "limitations": "English only",
                    "out_of_scope_uses": "Non-English languages",
                    "goal": "Test language understanding",
                    "audience": ["Researchers"],
                },
                "ethical_and_legal_considerations": {
                    "privacy_and_anonymity": "No personal data",
                    "consent_procedures": "N/A",
                    "compliance_with_regulations": "GDPR compliant",
                    "data_licensing": "CC-BY-4.0",
                },
                "possible_risks": [],
            }
        }

        result = loader.transform_record(record)

        assert result["id"] == "auto_benchmark_card_MMLU"
        assert result["name"] == "MMLU"
        assert result["description"] == "Massive Multitask Language Understanding"
        assert "dateCreated" in result
        assert result["hasDataType"] == ["text"]
        assert result["hasDomains"] == ["general"]
        assert result["hasLanguages"] == ["English"]

    def test_transform_record_missing_benchmark_card(self):
        """Test that record without benchmark_card field is skipped"""
        loader = get_loader()

        record = {
            "some_other_field": "value"
            # Missing benchmark_card
        }

        result = loader.transform_record(record)

        # Should return empty dict for invalid records
        assert result == {}

    def test_transform_record_with_nested_fields(self):
        """Test transforming record with nested field extraction"""
        loader = get_loader()

        record = {
            "benchmark_card": {
                "benchmark_details": {
                    "name": "SuperGLUE",
                    "overview": "General Language Understanding",
                    "data_type": "text",
                    "domains": ["NLP", "Understanding"],
                    "languages": ["English"],
                    "resources": [],
                    "similar_benchmarks": ["GLUE"],
                },
                "data": {
                    "source": "Wang et al.",
                    "size": "100k",
                    "format": "JSON",
                    "annotation": "Crowd sourced",
                },
                "methodology": {
                    "methods": ["Classification"],
                    "metrics": ["Macro F1", "Accuracy"],
                    "calculation": "Average across tasks",
                    "interpretation": "Higher better",
                    "baseline_results": "BERT baseline",
                    "validation": "Held-out test",
                },
                "purpose_and_intended_users": {
                    "tasks": ["Text classification", "Semantic similarity"],
                    "limitations": ["English only"],
                    "out_of_scope_uses": ["Non-English"],
                    "goal": "Test complex NLU",
                    "audience": ["Researchers", "Developers"],
                },
                "ethical_and_legal_considerations": {
                    "privacy_and_anonymity": "Anonymized",
                    "consent_procedures": "Yes",
                    "compliance_with_regulations": "Yes",
                    "data_licensing": "CC-BY-4.0",
                },
                "possible_risks": [],
            }
        }

        result = loader.transform_record(record)

        assert result["id"] == "auto_benchmark_card_SuperGLUE"
        assert result["hasMetrics"] == ["Macro F1", "Accuracy"]
        assert "NLP" in result["hasDomains"]
        assert "Text classification" in result["hasTasks"]

    def test_normalize_value_string(self):
        """Test normalizing string values"""
        loader = get_loader()
        assert loader._normalize_value("test") == ["test"]

    def test_normalize_value_list(self):
        """Test normalizing list values"""
        loader = get_loader()
        assert loader._normalize_value(["a", "b"]) == ["a", "b"]

    def test_normalize_value_dict(self):
        """Test normalizing dict values"""
        loader = get_loader()
        result = loader._normalize_value({"key1": "val1", "key2": "val2"})
        assert set(result) == {"val1", "val2"}

    def test_normalize_value_number(self):
        """Test normalizing numeric values"""
        loader = get_loader()
        assert loader._normalize_value(123) == ["123"]

    def test_get_nested_field(self):
        """Test extracting nested fields"""
        loader = get_loader()

        obj = {
            "level1": {
                "level2": "value"
            }
        }

        result = loader._get_nested_field(obj, "level1", "level2")
        assert result == "value"

    def test_get_container_class_name(self):
        """Test container class name"""
        loader = get_loader()
        assert loader.get_container_class_name() == "Container"

    def test_get_entity_type_plural(self):
        """Test entity type plural name"""
        loader = get_loader()
        assert loader._get_entity_type_plural() == "benchmarkmetadatacards"

    def test_save_to_yaml(self):
        """Test saving transformed records to YAML"""
        loader = get_loader()

        records = [
            {
                "id": "auto_benchmark_card_MMLU",
                "name": "MMLU",
            },
            {
                "id": "auto_benchmark_card_SuperGLUE",
                "name": "SuperGLUE",
            },
        ]

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "benchmarks.yaml"
            loader.save_to_yaml(records, str(output_path))

            assert output_path.exists()
            content = output_path.read_text()

            # Check YAML structure
            assert "benchmarkmetadatacards:" in content
            assert "- id: auto_benchmark_card_MMLU" in content
            assert "- id: auto_benchmark_card_SuperGLUE" in content
            assert "name: MMLU" in content
            assert "name: SuperGLUE" in content

    def test_transform_record_with_multiple_nested_fields(self):
        """Test handling multiple nested field extractions"""
        loader = get_loader()

        record = {
            "benchmark_card": {
                "benchmark_details": {
                    "name": "ARC",
                    "overview": "AI2 Reasoning Challenge",
                    "data_type": "text",
                    "domains": ["Reading comprehension"],
                    "languages": ["English"],
                    "resources": ["https://allenai.org/arc"],
                    "similar_benchmarks": ["RACE"],
                },
                "data": {
                    "source": "Clark et al.",
                    "size": "14k",
                    "format": "JSON",
                    "annotation": "Science questions",
                },
                "methodology": {
                    "methods": ["Multiple choice"],
                    "metrics": ["Accuracy"],
                    "calculation": "Fraction correct",
                    "interpretation": "0-1 scale",
                    "baseline_results": "Random ~25%",
                    "validation": "Held out test",
                },
                "purpose_and_intended_users": {
                    "tasks": ["Reading comprehension"],
                    "limitations": ["English", "Science domain"],
                    "out_of_scope_uses": ["Non-science"],
                    "goal": "Test reasoning",
                    "audience": ["Researchers"],
                },
                "ethical_and_legal_considerations": {
                    "privacy_and_anonymity": "Public data",
                    "consent_procedures": "N/A",
                    "compliance_with_regulations": "Open",
                    "data_licensing": "CC-BY-4.0",
                },
                "possible_risks": [],
            }
        }

        result = loader.transform_record(record)

        assert result["id"] == "auto_benchmark_card_ARC"
        assert result["name"] == "ARC"
        assert "Reading comprehension" in result["hasDomains"]
        assert "Accuracy" in result["hasMetrics"]
