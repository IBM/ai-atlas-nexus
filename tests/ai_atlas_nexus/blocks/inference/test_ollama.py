# Assisted by watsonx Code Assistant
import asyncio
import unittest
from unittest.mock import AsyncMock, MagicMock, Mock, call, patch

from ai_atlas_nexus.blocks.inference.ollama import OllamaInferenceEngine
from ai_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    TextGenerationInferenceOutput,
)
from ai_atlas_nexus.exceptions import InferenceError
from ai_atlas_nexus.metadata_base import InferenceEngineType


class TestOllamaInferenceEngine(unittest.TestCase):
    """Test cases for OllamaInferenceEngine class."""


    @patch.dict("os.environ", {}, clear=True)
    def test_prepare_credentials_missing_api_url(self):
        """Test credential preparation fails without api_url."""
        credentials = {}

        with patch.object(
            OllamaInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = OllamaInferenceEngine.__new__(OllamaInferenceEngine)
            engine._inference_engine_type = InferenceEngineType.OLLAMA

            with self.assertRaises(AssertionError):
                engine.prepare_credentials(credentials)


    def test_ping_success(self):
        """Test successful ping."""
        with patch.object(
            OllamaInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = OllamaInferenceEngine.__new__(OllamaInferenceEngine)
            engine.model_name_or_path = "llama2"
            engine.credentials = {"api_url": "http://localhost:11434"}
            engine.auto_download_model = False

            # Mock client methods
            mock_model = Mock()
            mock_model.model = "llama2"

            mock_list_response = Mock()
            mock_list_response.models = [mock_model]

            mock_client = Mock()
            mock_client.ps.return_value = None
            mock_client.list.return_value = mock_list_response

            engine.client = mock_client
            engine.parameters = {}

            # Should not raise exception
            engine.ping()

    def test_ping_connection_error(self):
        """Test ping with connection error."""
        with patch.object(
            OllamaInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = OllamaInferenceEngine.__new__(OllamaInferenceEngine)
            engine.credentials = {"api_url": "http://localhost:11434"}

            mock_client = Mock()
            mock_client.ps.side_effect = ConnectionError("Connection refused")

            engine.client = mock_client

            with self.assertRaises(Exception) as ctx:
                engine.ping()
            self.assertIn("not running", str(ctx.exception))

    def test_ping_model_not_found_auto_download_disabled(self):
        """Test ping when model not found and auto_download disabled."""
        with patch.object(
            OllamaInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = OllamaInferenceEngine.__new__(OllamaInferenceEngine)
            engine.model_name_or_path = "missing-model"
            engine.credentials = {"api_url": "http://localhost:11434"}
            engine.auto_download_model = False

            mock_list_response = Mock()
            mock_list_response.models = []

            mock_client = Mock()
            mock_client.ps.return_value = None
            mock_client.list.return_value = mock_list_response

            engine.client = mock_client
            engine.parameters = {}

            with self.assertRaises(Exception) as ctx:
                engine.ping()
            self.assertIn("not found", str(ctx.exception))

    def test_ping_model_not_found_auto_download_enabled(self):
        """Test ping when model not found and auto_download enabled."""
        with patch.object(
            OllamaInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = OllamaInferenceEngine.__new__(OllamaInferenceEngine)
            engine.model_name_or_path = "llama2"
            engine.credentials = {"api_url": "http://localhost:11434"}
            engine.auto_download_model = True

            mock_list_response = Mock()
            mock_list_response.models = []

            mock_client = Mock()
            mock_client.ps.return_value = None
            mock_client.list.return_value = mock_list_response

            engine.client = mock_client
            engine.parameters = {}

            with patch.object(engine, "_pull_model") as mock_pull:
                engine.ping()
                mock_pull.assert_called_once_with("llama2")

    def test_ping_thinking_parameter_unsupported_model(self):
        """Test ping with thinking parameter on unsupported model."""
        with patch.object(
            OllamaInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = OllamaInferenceEngine.__new__(OllamaInferenceEngine)
            engine.model_name_or_path = "llama2"
            engine.credentials = {"api_url": "http://localhost:11434"}
            engine.auto_download_model = False
            engine.parameters = {"think": True}

            mock_model = Mock()
            mock_model.model = "llama2"

            mock_list_response = Mock()
            mock_list_response.models = [mock_model]

            mock_show_response = Mock()
            mock_show_response.capabilities = []

            mock_client = Mock()
            mock_client.ps.return_value = None
            mock_client.list.return_value = mock_list_response
            mock_client.show.return_value = mock_show_response

            engine.client = mock_client

            with self.assertRaises(Exception) as ctx:
                engine.ping()
            self.assertIn("does not support thinking", str(ctx.exception))

    def test_pull_model_success(self):
        """Test successful model pull."""
        with patch.object(
            OllamaInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = OllamaInferenceEngine.__new__(OllamaInferenceEngine)

            mock_progress = Mock()
            mock_progress.status = "downloading"
            mock_progress.completed = 50
            mock_progress.total = 100

            mock_client = Mock()
            mock_client.pull.return_value = [mock_progress]

            engine.client = mock_client

            # Should not raise exception
            with patch("builtins.print"):
                engine._pull_model("llama2")

    def test_pull_model_failure(self):
        """Test model pull failure."""
        with patch.object(
            OllamaInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = OllamaInferenceEngine.__new__(OllamaInferenceEngine)

            mock_client = Mock()
            mock_client.pull.side_effect = Exception("Network error")

            engine.client = mock_client

            with self.assertRaises(Exception) as ctx:
                engine._pull_model("llama2")
            self.assertIn("Error pulling model", str(ctx.exception))

    def test_prepare_prediction_output_string(self):
        """Test prediction output preparation from string."""
        with patch.object(
            OllamaInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = OllamaInferenceEngine.__new__(OllamaInferenceEngine)
            engine.model_name_or_path = "llama2"
            engine._inference_engine_type = InferenceEngineType.OLLAMA

            result = engine._prepare_prediction_output("test response")

            self.assertEqual(type(result).__name__, "TextGenerationInferenceOutput")
            self.assertEqual(result.prediction, "test response")
            self.assertEqual(result.model_name_or_path, "llama2")

    def test_prepare_prediction_output_with_response_field(self):
        """Test prediction output preparation with response field."""
        with patch.object(
            OllamaInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = OllamaInferenceEngine.__new__(OllamaInferenceEngine)
            engine.model_name_or_path = "llama2"
            engine._inference_engine_type = InferenceEngineType.OLLAMA

            mock_response = Mock()
            mock_response.response = "generated text"
            mock_response.prompt_eval_count = 10
            mock_response.eval_count = 20
            mock_response.done_reason = "stop"
            mock_response.thinking = None
            mock_response.logprobs = None

            result = engine._prepare_prediction_output(mock_response)

            self.assertEqual(type(result).__name__, "TextGenerationInferenceOutput")
            self.assertEqual(result.prediction, "generated text")
            self.assertEqual(result.input_tokens, 10)
            self.assertEqual(result.output_tokens, 20)
            self.assertEqual(result.stop_reason, "stop")


    def test_prepare_prediction_output_with_logprobs(self):
        """Test prediction output preparation with logprobs."""
        with patch.object(
            OllamaInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = OllamaInferenceEngine.__new__(OllamaInferenceEngine)
            engine.model_name_or_path = "llama2"
            engine._inference_engine_type = InferenceEngineType.OLLAMA

            mock_logprob1 = Mock()
            mock_logprob1.token = "hello"
            mock_logprob1.logprob = -0.1

            mock_logprob2 = Mock()
            mock_logprob2.token = "world"
            mock_logprob2.logprob = -0.2

            mock_response = Mock()
            mock_response.response = "hello world"
            mock_response.prompt_eval_count = 5
            mock_response.eval_count = 10
            mock_response.done_reason = "stop"
            mock_response.thinking = None
            mock_response.logprobs = [mock_logprob1, mock_logprob2]

            result = engine._prepare_prediction_output(mock_response)

            self.assertEqual(type(result).__name__, "TextGenerationInferenceOutput")
            self.assertEqual(result.logprobs["hello"], -0.1)
            self.assertEqual(result.logprobs["world"], -0.2)


if __name__ == "__main__":
    unittest.main()
