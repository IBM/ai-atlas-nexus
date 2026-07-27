import json
import unittest
from unittest.mock import Mock, patch

from openai import (
    APIConnectionError,
    AuthenticationError,
    NotFoundError,
)

from ai_atlas_nexus.blocks.inference.openai import DEFAULT_OPENAI_API_URL, OpenAIInferenceEngine
from ai_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    TextGenerationInferenceOutput,
)
from ai_atlas_nexus.exceptions import InferenceError
from ai_atlas_nexus.metadata_base import InferenceEngineType


def _make_engine(**attrs) -> OpenAIInferenceEngine:
    """Return a bare OpenAIInferenceEngine instance with __init__ bypassed."""
    with patch.object(OpenAIInferenceEngine, "__init__", lambda self, *a, **kw: None):
        engine = OpenAIInferenceEngine.__new__(OpenAIInferenceEngine)
    for key, value in attrs.items():
        setattr(engine, key, value)
    return engine


class TestOpenAIInferenceEngine(unittest.TestCase):
    """Test cases for OpenAIInferenceEngine."""

    # prepare_credentials

    @patch.dict("os.environ", {}, clear=True)
    def test_prepare_credentials_missing_api_key(self):
        """Credential preparation fails without api_key."""
        engine = _make_engine(_inference_engine_type=InferenceEngineType.OPENAI)
        with self.assertRaises(AssertionError):
            engine.prepare_credentials({})

    @patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test"}, clear=True)
    def test_prepare_credentials_from_env(self):
        """Credential preparation reads api_key from env."""
        engine = _make_engine(_inference_engine_type=InferenceEngineType.OPENAI)
        creds = engine.prepare_credentials({})
        self.assertEqual(creds["api_key"], "sk-test")
        self.assertEqual(creds["api_url"], DEFAULT_OPENAI_API_URL)

    def test_prepare_credentials_from_dict(self):
        """Credential preparation reads api_key from passed dict."""
        engine = _make_engine(_inference_engine_type=InferenceEngineType.OPENAI)
        creds = engine.prepare_credentials(
            {"api_key": "sk-explicit", "api_url": "https://custom.openai.com/v1"}
        )
        self.assertEqual(creds["api_key"], "sk-explicit")
        self.assertEqual(creds["api_url"], "https://custom.openai.com/v1")

    # ping

    def test_ping_success(self):
        """Successful ping when models.list() does not raise."""
        mock_client = Mock()
        mock_client.models.list.return_value = Mock()
        engine = _make_engine(model_name_or_path="gpt-4o", client=mock_client)
        engine.ping()

    def test_ping_connection_error(self):
        """ping raises on APIConnectionError."""
        mock_client = Mock()
        mock_client.models.list.side_effect = APIConnectionError(request=Mock())
        engine = _make_engine(model_name_or_path="gpt-4o", client=mock_client)
        with self.assertRaises(Exception) as ctx:
            engine.ping()
        self.assertIn("Connection error", str(ctx.exception))

    def test_ping_not_found_treated_as_connection_error(self):
        """ping maps NotFoundError (bad base URL) to a connection error."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.headers = {}
        mock_client = Mock()
        mock_client.models.list.side_effect = NotFoundError(
            message="Not Found", response=mock_response, body={}
        )
        engine = _make_engine(model_name_or_path="gpt-5-mini", client=mock_client)
        with self.assertRaises(Exception) as ctx:
            engine.ping()
        self.assertIn("Connection error", str(ctx.exception))

    def test_ping_authentication_error(self):
        """ping raises on AuthenticationError."""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.headers = {}
        mock_client = Mock()
        mock_client.models.list.side_effect = AuthenticationError(
            message="invalid key", response=mock_response, body={}
        )
        engine = _make_engine(model_name_or_path="gpt-4o", client=mock_client)
        with self.assertRaises(Exception) as ctx:
            engine.ping()
        self.assertIn("Authentication failed", str(ctx.exception))

    # create_client — URL normalisation

    def test_create_client_normalises_url_without_v1(self):
        """api_url without /v1 suffix should have /v1 appended."""
        engine = _make_engine(
            credentials={"api_key": "sk-test", "api_url": "https://api.openai.com"}
        )
        with patch("ai_atlas_nexus.blocks.inference.openai.OpenAI") as mock_openai:
            engine.create_client()
            self.assertEqual(
                mock_openai.call_args.kwargs["base_url"], "https://api.openai.com/v1"
            )

    def test_create_client_keeps_existing_v1_suffix(self):
        """api_url that already ends with /v1 should not get a second /v1."""
        engine = _make_engine(
            credentials={"api_key": "sk-test", "api_url": "https://api.openai.com/v1"}
        )
        with patch("ai_atlas_nexus.blocks.inference.openai.OpenAI") as mock_openai:
            engine.create_client()
            self.assertEqual(
                mock_openai.call_args.kwargs["base_url"], "https://api.openai.com/v1"
            )

    def test_create_client_strips_trailing_slash(self):
        """Trailing slash in api_url should be stripped before /v1 is appended."""
        engine = _make_engine(
            credentials={"api_key": "sk-test", "api_url": "https://api.openai.com/"}
        )
        with patch("ai_atlas_nexus.blocks.inference.openai.OpenAI") as mock_openai:
            engine.create_client()
            self.assertEqual(
                mock_openai.call_args.kwargs["base_url"], "https://api.openai.com/v1"
            )

    # _prepare_chat_output

    def test_prepare_chat_output_string(self):
        """_prepare_chat_output from a plain string (postprocessed path)."""
        engine = _make_engine(
            model_name_or_path="gpt-4o",
            _inference_engine_type=InferenceEngineType.OPENAI,
        )
        result = engine._prepare_chat_output("hello world")
        self.assertIsInstance(result, TextGenerationInferenceOutput)
        self.assertEqual(result.prediction, "hello world")
        self.assertEqual(result.model_name_or_path, "gpt-4o")

    def test_prepare_chat_output_with_response_object(self):
        """_prepare_chat_output from an OpenAI response object."""
        engine = _make_engine(
            model_name_or_path="gpt-4o",
            _inference_engine_type=InferenceEngineType.OPENAI,
        )

        mock_message = Mock()
        mock_message.content = "generated text"
        mock_choice = Mock()
        mock_choice.message = mock_message
        mock_choice.finish_reason = "stop"
        mock_choice.logprobs = None
        mock_usage = Mock()
        mock_usage.total_tokens = 120
        mock_usage.completion_tokens = 40
        mock_response = Mock()
        mock_response.choices = [mock_choice]
        mock_response.usage = mock_usage

        result = engine._prepare_chat_output(mock_response)

        self.assertIsInstance(result, TextGenerationInferenceOutput)
        self.assertEqual(result.prediction, "generated text")
        self.assertEqual(result.input_tokens, 120)
        self.assertEqual(result.output_tokens, 40)
        self.assertEqual(result.stop_reason, "stop")
        self.assertIsNone(result.logprobs)

    def test_prepare_chat_output_with_logprobs(self):
        """_prepare_chat_output maps logprobs correctly."""
        engine = _make_engine(
            model_name_or_path="gpt-4o",
            _inference_engine_type=InferenceEngineType.OPENAI,
        )

        lp1, lp2 = Mock(), Mock()
        lp1.token, lp1.logprob = "foo", -0.5
        lp2.token, lp2.logprob = "bar", -1.2
        mock_logprobs = Mock()
        mock_logprobs.content = [lp1, lp2]
        mock_choice = Mock()
        mock_choice.message.content = "foo bar"
        mock_choice.finish_reason = "stop"
        mock_choice.logprobs = mock_logprobs
        mock_usage = Mock()
        mock_usage.total_tokens = 10
        mock_usage.completion_tokens = 2
        mock_response = Mock()
        mock_response.choices = [mock_choice]
        mock_response.usage = mock_usage

        result = engine._prepare_chat_output(mock_response)

        self.assertEqual(result.logprobs["foo"], -0.5)
        self.assertEqual(result.logprobs["bar"], -1.2)

    # _create_schema_format

    def test_create_schema_format_with_object_schema(self):
        """Object-type schemas pass through unwrapped."""
        engine = _make_engine()
        schema = {"type": "object", "properties": {"name": {"type": "string"}}}
        result = engine._create_schema_format(schema)
        self.assertEqual(result["type"], "json_schema")
        self.assertEqual(result["json_schema"]["name"], "openai_schema")
        self.assertEqual(result["json_schema"]["schema"], schema)

    def test_create_schema_format_wraps_root_array(self):
        """Root-array schemas are wrapped in an object so OpenAI accepts them."""
        engine = _make_engine()
        array_schema = {"type": "array", "items": {"enum": ["A", "B"]}}
        result = engine._create_schema_format(array_schema)
        outer = result["json_schema"]["schema"]
        self.assertEqual(outer["type"], "object")
        self.assertIn("items", outer["properties"])
        self.assertEqual(outer["properties"]["items"], array_schema)
        self.assertEqual(outer["required"], ["items"])

    def test_create_schema_format_none(self):
        """_create_schema_format returns None when no format given."""
        engine = _make_engine()
        self.assertIsNone(engine._create_schema_format(None))

    def test_prepare_chat_output_unwraps_array_envelope(self):
        """_prepare_chat_output unwraps the {"items": [...]} envelope."""
        engine = _make_engine(
            model_name_or_path="gpt-4o",
            _inference_engine_type=InferenceEngineType.OPENAI,
        )

        wrapped_content = json.dumps({"items": ["Risk A", "Risk B"]})
        mock_choice = Mock()
        mock_choice.message.content = wrapped_content
        mock_choice.finish_reason = "stop"
        mock_choice.logprobs = None
        mock_usage = Mock()
        mock_usage.total_tokens = 20
        mock_usage.completion_tokens = 5
        mock_response = Mock()
        mock_response.choices = [mock_choice]
        mock_response.usage = mock_usage

        result = engine._prepare_chat_output(mock_response)

        self.assertEqual(result.prediction, json.dumps(["Risk A", "Risk B"]))

    def test_prepare_chat_output_leaves_non_envelope_objects_intact(self):
        """_prepare_chat_output does NOT unwrap objects with multiple keys."""
        engine = _make_engine(
            model_name_or_path="gpt-4o",
            _inference_engine_type=InferenceEngineType.OPENAI,
        )

        multi_key = json.dumps({"items": ["A"], "extra": "value"})
        mock_choice = Mock()
        mock_choice.message.content = multi_key
        mock_choice.finish_reason = "stop"
        mock_choice.logprobs = None
        mock_usage = Mock()
        mock_usage.total_tokens = 10
        mock_usage.completion_tokens = 3
        mock_response = Mock()
        mock_response.choices = [mock_choice]
        mock_response.usage = mock_usage

        result = engine._prepare_chat_output(mock_response)

        self.assertEqual(result.prediction, multi_key)


if __name__ == "__main__":
    unittest.main()
