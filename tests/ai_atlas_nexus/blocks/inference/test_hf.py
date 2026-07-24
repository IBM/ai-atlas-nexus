# Assisted by watsonx Code Assistant
import unittest
from unittest.mock import MagicMock, Mock, patch

from ai_atlas_nexus.blocks.inference.hf import DEFAULT_HF_API_URL, HFInferenceEngine
from ai_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    TextGenerationInferenceOutput,
)
from ai_atlas_nexus.exceptions import InferenceError
from ai_atlas_nexus.metadata_base import InferenceEngineType


class TestHFInferenceEngine(unittest.TestCase):
    """Test cases for HFInferenceEngine class."""


    @patch.dict("os.environ", {}, clear=True)
    def test_prepare_credentials_missing_api_key(self):
        """Test credential preparation fails without api_key."""
        credentials = {}

        with patch.object(
            HFInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = HFInferenceEngine.__new__(HFInferenceEngine)
            engine._inference_engine_type = InferenceEngineType.HF

            with self.assertRaises(AssertionError):
                engine.prepare_credentials(credentials)



    def test_ping_success(self):
        """Test successful ping with valid model."""
        with patch.object(
            HFInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = HFInferenceEngine.__new__(HFInferenceEngine)
            engine.model_name_or_path = "meta-llama/Llama-3.3-70B-Instruct"

            mock_model = Mock()
            mock_model.id = "meta-llama/Llama-3.3-70B-Instruct"

            mock_models_list = Mock()
            mock_models_list.data = [mock_model]

            mock_client = Mock()
            mock_client.models.list.return_value = mock_models_list

            engine.client = mock_client

            # Should not raise exception
            engine.ping()

    def test_ping_model_not_found(self):
        """Test ping when model not found."""
        with patch.object(
            HFInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = HFInferenceEngine.__new__(HFInferenceEngine)
            engine.model_name_or_path = "missing-model"

            mock_models_list = Mock()
            mock_models_list.data = []

            mock_client = Mock()
            mock_client.models.list.return_value = mock_models_list

            engine.client = mock_client

            with self.assertRaises(Exception) as ctx:
                engine.ping()
            self.assertIn("not found", str(ctx.exception))


    def test_prepare_chat_output_string(self):
        """Test chat output preparation from string."""
        with patch.object(
            HFInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = HFInferenceEngine.__new__(HFInferenceEngine)
            engine.model_name_or_path = "test-model"
            engine._inference_engine_type = InferenceEngineType.HF

            result = engine._prepare_chat_output("test response")

            self.assertEqual(type(result).__name__, "TextGenerationInferenceOutput")
            self.assertEqual(result.prediction, "test response")
            self.assertEqual(result.model_name_or_path, "test-model")

    def test_prepare_chat_output_with_response_object(self):
        """Test chat output preparation from response object."""
        with patch.object(
            HFInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = HFInferenceEngine.__new__(HFInferenceEngine)
            engine.model_name_or_path = "test-model"
            engine._inference_engine_type = InferenceEngineType.HF

            mock_message = Mock()
            mock_message.content = "generated response"

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

            result = engine._prepare_chat_output(mock_response)

            self.assertEqual(type(result).__name__, "TextGenerationInferenceOutput")
            self.assertEqual(result.prediction, "generated response")
            self.assertEqual(result.input_tokens, 100)
            self.assertEqual(result.output_tokens, 50)
            self.assertEqual(result.stop_reason, "stop")

    def test_prepare_chat_output_with_logprobs(self):
        """Test chat output preparation with logprobs."""
        with patch.object(
            HFInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = HFInferenceEngine.__new__(HFInferenceEngine)
            engine.model_name_or_path = "test-model"
            engine._inference_engine_type = InferenceEngineType.HF

            mock_logprob1 = Mock()
            mock_logprob1.token = "hello"
            mock_logprob1.logprob = -0.1

            mock_logprob2 = Mock()
            mock_logprob2.token = "world"
            mock_logprob2.logprob = -0.2

            mock_logprobs = Mock()
            mock_logprobs.content = [mock_logprob1, mock_logprob2]

            mock_message = Mock()
            mock_message.content = "hello world"

            mock_choice = Mock()
            mock_choice.message = mock_message
            mock_choice.finish_reason = "stop"
            mock_choice.logprobs = mock_logprobs

            mock_usage = Mock()
            mock_usage.total_tokens = 10
            mock_usage.completion_tokens = 5

            mock_response = Mock()
            mock_response.choices = [mock_choice]
            mock_response.usage = mock_usage

            result = engine._prepare_chat_output(mock_response)

            self.assertEqual(type(result).__name__, "TextGenerationInferenceOutput")
            self.assertEqual(result.logprobs["hello"], -0.1)
            self.assertEqual(result.logprobs["world"], -0.2)

    def test_create_schema_format_with_response_format(self):
        """Test schema format creation with response_format."""
        with patch.object(
            HFInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = HFInferenceEngine.__new__(HFInferenceEngine)

            response_format = {"type": "object", "properties": {"name": {"type": "string"}}}
            result = engine._create_schema_format(response_format)

            self.assertEqual(result["type"], "json_schema")
            self.assertEqual(result["json_schema"]["name"], "response_schema")
            self.assertEqual(result["json_schema"]["schema"], response_format)

    def test_create_schema_format_without_response_format(self):
        """Test schema format creation without response_format."""
        with patch.object(
            HFInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = HFInferenceEngine.__new__(HFInferenceEngine)

            result = engine._create_schema_format(None)

            self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
