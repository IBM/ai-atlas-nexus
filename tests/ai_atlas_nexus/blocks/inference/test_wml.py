# Assisted by watsonx Code Assistant
import unittest
from unittest.mock import MagicMock, Mock, patch

from ai_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    TextGenerationInferenceOutput,
)
from ai_atlas_nexus.blocks.inference.wml import WMLInferenceEngine
from ai_atlas_nexus.exceptions import InferenceError
from ai_atlas_nexus.metadata_base import InferenceEngineType


class TestWMLInferenceEngine(unittest.TestCase):
    """Test cases for WMLInferenceEngine class."""


    @patch.dict("os.environ", {}, clear=True)
    def test_prepare_credentials_missing_api_key(self):
        """Test credential preparation fails without api_key."""
        credentials = {
            "api_url": "https://us-south.ml.cloud.ibm.com",
            "space_id": "test-space-id",
        }

        with patch.object(
            WMLInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = WMLInferenceEngine.__new__(WMLInferenceEngine)
            engine._inference_engine_type = InferenceEngineType.WML

            with self.assertRaises(AssertionError):
                engine.prepare_credentials(credentials)

    @patch.dict("os.environ", {}, clear=True)
    def test_prepare_credentials_missing_api_url(self):
        """Test credential preparation fails without api_url."""
        credentials = {"api_key": "test-key", "space_id": "test-space-id"}

        with patch.object(
            WMLInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = WMLInferenceEngine.__new__(WMLInferenceEngine)
            engine._inference_engine_type = InferenceEngineType.WML

            with self.assertRaises(AssertionError):
                engine.prepare_credentials(credentials)

    @patch.dict("os.environ", {}, clear=True)
    def test_prepare_credentials_missing_space_and_project_id(self):
        """Test credential preparation fails without space_id or project_id."""
        credentials = {
            "api_key": "test-key",
            "api_url": "https://us-south.ml.cloud.ibm.com",
        }

        with patch.object(
            WMLInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = WMLInferenceEngine.__new__(WMLInferenceEngine)
            engine._inference_engine_type = InferenceEngineType.WML

            with self.assertRaises(ValueError) as ctx:
                engine.prepare_credentials(credentials)
            self.assertIn("space_id", str(ctx.exception))
            self.assertIn("project_id", str(ctx.exception))


    @patch("ai_atlas_nexus.blocks.inference.wml.configure_logger")
    @patch.dict("os.environ", {}, clear=True)
    def test_prepare_credentials_with_both_space_and_project_id(
        self, mock_logger_config
    ):
        """Test credential preparation warns when both space_id and project_id provided."""
        credentials = {
            "api_key": "test-key",
            "api_url": "https://us-south.ml.cloud.ibm.com",
            "space_id": "test-space-id",
            "project_id": "test-project-id",
        }

        mock_logger = Mock()
        mock_logger_config.return_value = mock_logger

        with patch.object(
            WMLInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = WMLInferenceEngine.__new__(WMLInferenceEngine)
            engine._inference_engine_type = InferenceEngineType.WML

            # Need to reinitialize logger module level variable
            import ai_atlas_nexus.blocks.inference.wml as wml_module

            wml_module.logger = mock_logger

            result = engine.prepare_credentials(credentials)

            # Verify warning was called
            mock_logger.warning.assert_called_once()
            self.assertIn("space_id", mock_logger.warning.call_args[0][0])


    def test_ping(self):
        """Test ping method (should pass as it's a no-op)."""
        with patch.object(
            WMLInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = WMLInferenceEngine.__new__(WMLInferenceEngine)

            # Should not raise exception
            engine.ping()

    def test_prepare_prediction_output_string(self):
        """Test prediction output preparation from string."""
        with patch.object(
            WMLInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = WMLInferenceEngine.__new__(WMLInferenceEngine)
            engine.model_name_or_path = "test-model"
            engine._inference_engine_type = InferenceEngineType.WML

            result = engine._prepare_prediction_output("test response")

            self.assertEqual(type(result).__name__, "TextGenerationInferenceOutput")
            self.assertEqual(result.prediction, "test response")
            self.assertEqual(result.model_name_or_path, "test-model")

    def test_prepare_prediction_output_generate_api_format(self):
        """Test prediction output preparation from generate API format."""
        with patch.object(
            WMLInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = WMLInferenceEngine.__new__(WMLInferenceEngine)
            engine.model_name_or_path = "test-model"
            engine._inference_engine_type = InferenceEngineType.WML

            response = {
                "results": [
                    {
                        "generated_text": "generated output",
                        "input_token_count": 10,
                        "generated_token_count": 20,
                        "stop_reason": "eos_token",
                    }
                ]
            }

            result = engine._prepare_prediction_output(response)

            self.assertEqual(type(result).__name__, "TextGenerationInferenceOutput")
            self.assertEqual(result.prediction, "generated output")
            self.assertEqual(result.input_tokens, 10)
            self.assertEqual(result.output_tokens, 20)
            self.assertEqual(result.stop_reason, "eos_token")

    def test_prepare_prediction_output_chat_api_format(self):
        """Test prediction output preparation from chat API format."""
        with patch.object(
            WMLInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = WMLInferenceEngine.__new__(WMLInferenceEngine)
            engine.model_name_or_path = "test-model"
            engine._inference_engine_type = InferenceEngineType.WML

            response = {
                "choices": [
                    {"message": {"content": "chat response"}, "finish_reason": "stop"}
                ],
                "usage": {"prompt_tokens": 15, "completion_tokens": 25},
            }

            result = engine._prepare_prediction_output(response)

            self.assertEqual(type(result).__name__, "TextGenerationInferenceOutput")
            self.assertEqual(result.prediction, "chat response")
            self.assertEqual(result.input_tokens, 15)
            self.assertEqual(result.output_tokens, 25)
            self.assertEqual(result.stop_reason, "stop")

    def test_prepare_prediction_output_chat_api_format_without_usage(self):
        """Test prediction output preparation from chat API format without usage."""
        with patch.object(
            WMLInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = WMLInferenceEngine.__new__(WMLInferenceEngine)
            engine.model_name_or_path = "test-model"
            engine._inference_engine_type = InferenceEngineType.WML

            response = {
                "choices": [
                    {"message": {"content": "chat response"}, "finish_reason": "stop"}
                ]
            }

            result = engine._prepare_prediction_output(response)

            self.assertEqual(type(result).__name__, "TextGenerationInferenceOutput")
            self.assertEqual(result.prediction, "chat response")
            self.assertIsNone(result.input_tokens)
            self.assertIsNone(result.output_tokens)
            self.assertEqual(result.stop_reason, "stop")

    def test_generate_text_delegates_to_chat(self):
        """Test that generate_text delegates to generate_chat_response."""
        with patch.object(
            WMLInferenceEngine, "__init__", lambda x, *args, **kwargs: None
        ):
            engine = WMLInferenceEngine.__new__(WMLInferenceEngine)

            mock_response = {"choices": [{"message": {"content": "response"}}]}

            with patch.object(
                engine, "generate_chat_response", return_value=mock_response
            ) as mock_gen_chat:
                response_format = {"type": "object"}
                prompt = "test prompt"

                result = engine.generate_text(response_format, prompt)

                mock_gen_chat.assert_called_once_with(
                    response_format, None, prompt
                )
                self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
