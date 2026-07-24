# Assisted by watsonx Code Assistant
import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch

from ai_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    TextGenerationInferenceOutput,
)
from ai_atlas_nexus.blocks.inference.vllm import VLLMInferenceEngine, _extract_logprobs
from ai_atlas_nexus.exceptions import InferenceError
from ai_atlas_nexus.metadata_base import InferenceEngineType


class TestExtractLogprobs(unittest.TestCase):
    """Test cases for _extract_logprobs helper function."""

    def test_extract_logprobs_with_valid_data(self):
        """Test extraction with valid logprobs data."""
        mock_logprob_obj = Mock()
        mock_logprob_obj.decoded_token = "test"
        mock_logprob_obj.logprob = -0.5

        logprobs = [{0: mock_logprob_obj}]
        result = _extract_logprobs(logprobs)

        self.assertIsNotNone(result)
        self.assertEqual(result["test"], -0.5)

    def test_extract_logprobs_with_empty_list(self):
        """Test extraction with empty logprobs."""
        result = _extract_logprobs([])
        self.assertIsNone(result)

    def test_extract_logprobs_with_none(self):
        """Test extraction with None."""
        result = _extract_logprobs(None)
        self.assertIsNone(result)

    def test_extract_logprobs_with_multiple_tokens(self):
        """Test extraction with multiple tokens."""
        mock_logprob_obj1 = Mock()
        mock_logprob_obj1.decoded_token = "hello"
        mock_logprob_obj1.logprob = -0.1

        mock_logprob_obj2 = Mock()
        mock_logprob_obj2.decoded_token = "world"
        mock_logprob_obj2.logprob = -0.2

        logprobs = [{0: mock_logprob_obj1}, {0: mock_logprob_obj2}]
        result = _extract_logprobs(logprobs)

        self.assertEqual(len(result), 2)
        self.assertEqual(result["hello"], -0.1)
        self.assertEqual(result["world"], -0.2)


class TestVLLMInferenceEngine(unittest.TestCase):
    """Test cases for VLLMInferenceEngine class."""


    @patch.dict("os.environ", {}, clear=True)
    def test_prepare_credentials_offline_mode(self):
        """Test credential preparation for offline mode (None credentials)."""
        with patch.object(
            VLLMInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = VLLMInferenceEngine.__new__(VLLMInferenceEngine)
            engine._inference_engine_type = InferenceEngineType.VLLM
            engine.model_name_or_path = "test-model"

            result = engine.prepare_credentials(None)

            self.assertIsNone(result)

    @patch("ai_atlas_nexus.blocks.inference.vllm.OpenAI")
    def test_create_client_with_credentials(self, mock_openai):
        """Test client creation with API credentials."""
        with patch.object(
            VLLMInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = VLLMInferenceEngine.__new__(VLLMInferenceEngine)
            engine.credentials = {"api_url": "http://localhost:8000", "api_key": "key"}
            engine.parameters = {}

            client = engine.create_client()

            mock_openai.assert_called_once()
            self.assertIsNotNone(client)


    def test_create_schema_format_with_response_format(self):
        """Test schema format creation with response_format."""
        with patch.object(
            VLLMInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = VLLMInferenceEngine.__new__(VLLMInferenceEngine)

            response_format = {"type": "object", "properties": {"name": {"type": "string"}}}
            result = engine._create_schema_format(response_format)

            self.assertEqual(result["type"], "json_schema")
            self.assertEqual(result["json_schema"]["name"], "JSON_schema")
            self.assertEqual(result["json_schema"]["schema"], response_format)

    def test_create_schema_format_without_response_format(self):
        """Test schema format creation without response_format."""
        with patch.object(
            VLLMInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = VLLMInferenceEngine.__new__(VLLMInferenceEngine)

            result = engine._create_schema_format(None)

            self.assertIsNone(result)

    def test_prepare_prediction_output_string(self):
        """Test prediction output preparation from string."""
        with patch.object(
            VLLMInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = VLLMInferenceEngine.__new__(VLLMInferenceEngine)
            engine.model_name_or_path = "test-model"
            engine._inference_engine_type = InferenceEngineType.VLLM

            result = engine._prepare_prediction_output("test response")

            self.assertEqual(type(result).__name__, "TextGenerationInferenceOutput")
            self.assertEqual(result.prediction, "test response")
            self.assertEqual(result.model_name_or_path, "test-model")

    def test_prepare_prediction_output_offline(self):
        """Test prediction output preparation in offline mode."""
        with patch.object(
            VLLMInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = VLLMInferenceEngine.__new__(VLLMInferenceEngine)
            engine.model_name_or_path = "test-model"
            engine._inference_engine_type = InferenceEngineType.VLLM

            # Mock offline response
            mock_output = Mock()
            mock_output.text = "generated text"
            mock_output.token_ids = [1, 2, 3]
            mock_output.finish_reason = "stop"
            mock_output.logprobs = None

            mock_response = Mock()
            mock_response.prompt = "test prompt"
            mock_response.outputs = [mock_output]

            result = engine._prepare_prediction_output(mock_response, offline=True)

            self.assertEqual(type(result).__name__, "TextGenerationInferenceOutput")
            self.assertEqual(result.prediction, "generated text")
            self.assertEqual(result.input_text, "test prompt")
            self.assertEqual(result.output_tokens, 3)
            self.assertEqual(result.stop_reason, "stop")

    def test_prepare_prediction_output_online(self):
        """Test prediction output preparation in online mode."""
        with patch.object(
            VLLMInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = VLLMInferenceEngine.__new__(VLLMInferenceEngine)
            engine.model_name_or_path = "test-model"
            engine._inference_engine_type = InferenceEngineType.VLLM

            # Mock online response
            mock_message = Mock()
            mock_message.content = "online response"

            mock_choice = Mock()
            mock_choice.message = mock_message
            mock_choice.finish_reason = "stop"
            mock_choice.logprobs = None

            mock_usage = Mock()
            mock_usage.total_tokens = 100
            mock_usage.completion_tokens = 50

            mock_response = Mock()
            mock_response.choices = [mock_choice]
            mock_response.usage = mock_usage

            result = engine._prepare_prediction_output(mock_response, offline=False)

            self.assertEqual(type(result).__name__, "TextGenerationInferenceOutput")
            self.assertEqual(result.prediction, "online response")
            self.assertEqual(result.input_tokens, 100)
            self.assertEqual(result.output_tokens, 50)
            self.assertEqual(result.stop_reason, "stop")



if __name__ == "__main__":
    unittest.main()
