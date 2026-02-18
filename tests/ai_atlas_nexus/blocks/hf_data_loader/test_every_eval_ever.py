"""
Tests for EveryEvalEverLoader HF data import
"""

import tempfile
from pathlib import Path
from unittest.mock import MagicMock


def get_loader():
    """Helper to get loader instance with mocked dataset"""
    from unittest.mock import patch
    with patch("datasets.load_dataset") as mock_load_dataset:
        mock_dataset = MagicMock()
        mock_dataset.__len__ = MagicMock(return_value=0)
        mock_load_dataset.return_value = mock_dataset

        from src.ai_atlas_nexus.blocks.hf_data_loader.every_eval_ever import (
            EveryEvalEverLoader,
        )
        return EveryEvalEverLoader()


class TestEveryEvalEverTransformation:
    """Test transformation logic of EveryEvalEverLoader"""

    def test_transform_record_minimal(self):
        """Test transforming a minimal evaluation record"""
        loader = get_loader()

        record = {
            "evaluation_id": "test-eval-123",
            "schema_version": "1.0",
            "evaluation_timestamp": "2026-02-13T00:00:00Z",
            "retrieved_timestamp": "1707000000",
        }

        result = loader.transform_record(record)

        assert result["id"] == "eee_test-eval-123"
        assert result["evaluation_id"] == "test-eval-123"
        assert result["schema_version"] == "1.0"
        assert "dateCreated" in result

    def test_transform_record_with_nested_data(self):
        """Test transforming a record with full nested structure"""
        loader = get_loader()

        record = {
            "evaluation_id": "gsm8k/meta-llama/Llama-3.1-8B",
            "schema_version": "1.0",
            "evaluation_timestamp": "2026-02-13T00:00:00Z",
            "retrieved_timestamp": "1707000000",
            "source_metadata": {
                "source_name": "Test Leaderboard",
                "source_type": "evaluation_run",
                "source_organization_name": "Test Org",
                "source_organization_url": "https://test.org",
                "evaluator_relationship": "first_party",
            },
            "model_info": {
                "name": "Llama 3.1 8B",
                "id": "meta-llama/Llama-3.1-8B",
            },
            "evaluation_results": [
                {
                    "evaluation_name": "GSM8K",
                    "source_data": {
                        "dataset_name": "gsm8k",
                        "source_type": "hf_dataset",
                        "hf_repo": "openai/gsm8k",
                        "hf_split": "test",
                    },
                    "metric_config": {
                        "lower_is_better": False,
                        "score_type": "continuous",
                        "min_score": 0.0,
                        "max_score": 100.0,
                    },
                    "score_details": {
                        "score": 75.2,
                    },
                }
            ],
        }

        result = loader.transform_record(record)

        # top-level fields
        assert result["id"] == "eee_gsm8k/meta-llama/Llama-3.1-8B"
        assert result["evaluation_id"] == "gsm8k/meta-llama/Llama-3.1-8B"

        # source metadata
        assert "hasSourceMetadata" in result
        assert result["hasSourceMetadata"]["source_name"] == "Test Leaderboard"
        assert result["hasSourceMetadata"]["evaluator_relationship"] == "first_party"

        # model info
        assert "hasModelInfo" in result
        assert result["hasModelInfo"]["model_name"] == "Llama 3.1 8B"
        assert result["hasModelInfo"]["model_id"] == "meta-llama/Llama-3.1-8B"

        # evaluation results
        assert "hasEvaluationResults" in result
        assert len(result["hasEvaluationResults"]) == 1

        eval_result = result["hasEvaluationResults"][0]
        assert eval_result["evaluation_name"] == "GSM8K"
        assert eval_result["hasSourceData"]["hf_repo"] == "openai/gsm8k"
        assert eval_result["hasMetricConfig"]["score_type"] == "continuous"
        assert eval_result["hasScoreDetails"]["score"] == 75.2

    def test_transform_record_missing_evaluation_id(self):
        """Test that record without evaluation_id is skipped"""
        loader = get_loader()

        record = {
            "schema_version": "1.0",
            # Missing evaluation_id
        }

        result = loader.transform_record(record)

        # Should return empty dict for invalid records
        assert result == {}

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

    def test_get_container_class_name(self):
        """Test container class name"""
        loader = get_loader()
        assert loader.get_container_class_name() == "Container"

    def test_get_entity_type_plural(self):
        """Test entity type plural name"""
        loader = get_loader()
        assert loader._get_entity_type_plural() == "everyevalaresults"

    def test_save_to_yaml(self):
        """Test saving transformed records to YAML"""
        loader = get_loader()

        records = [
            {
                "id": "test_1",
                "evaluation_id": "eval-1",
            },
            {
                "id": "test_2",
                "evaluation_id": "eval-2",
            },
        ]

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "test_output.yaml"
            loader.save_to_yaml(records, str(output_path))

            assert output_path.exists()
            content = output_path.read_text()

            # Check YAML structure
            assert "everyevalaresults:" in content
            assert "- id: test_1" in content
            assert "- id: test_2" in content
            assert "evaluation_id: eval-1" in content
            assert "evaluation_id: eval-2" in content
