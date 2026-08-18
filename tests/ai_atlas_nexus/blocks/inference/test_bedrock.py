import json
import unittest
from unittest.mock import Mock, patch

from ai_atlas_nexus.blocks.inference.bedrock import AWSBedrockInferenceEngine
from ai_atlas_nexus.blocks.inference.params import TextGenerationInferenceOutput
from ai_atlas_nexus.metadata_base import InferenceEngineType


def _make_engine(**attrs) -> AWSBedrockInferenceEngine:
    """Return a bare AWSBedrockInferenceEngine instance with __init__ bypassed."""
    with patch.object(AWSBedrockInferenceEngine, "__init__", lambda self, *a, **kw: None):
        engine = AWSBedrockInferenceEngine.__new__(AWSBedrockInferenceEngine)
    for key, value in attrs.items():
        setattr(engine, key, value)
    return engine


def _mock_response(content, *, input_tokens=10, output_tokens=3, stop_reason="end_turn"):
    """Build a minimal Bedrock converse response mock."""
    return {
        "output": {"message": {"content": [{"text": content}]}},
        "usage": {"inputTokens": input_tokens, "outputTokens": output_tokens},
        "stopReason": stop_reason,
    }


class TestAWSBedrockInferenceEngine(unittest.TestCase):
    """Test cases for AWSBedrockInferenceEngine."""

    # prepare_credentials

    @patch.dict("os.environ", {}, clear=True)
    def test_prepare_credentials_missing_access_key_id(self):
        """Credential preparation fails without aws_access_key_id."""
        engine = _make_engine(_inference_engine_type=InferenceEngineType.BEDROCK)
        with self.assertRaises(AssertionError):
            engine.prepare_credentials({})

    @patch.dict("os.environ", {"AWS_ACCESS_KEY_ID": "AKIATEST"}, clear=True)
    def test_prepare_credentials_missing_secret_key(self):
        """Credential preparation fails when aws_secret_access_key is missing."""
        engine = _make_engine(_inference_engine_type=InferenceEngineType.BEDROCK)
        with self.assertRaises(AssertionError):
            engine.prepare_credentials({})

    @patch.dict(
        "os.environ",
        {
            "AWS_ACCESS_KEY_ID": "AKIATEST",
            "AWS_SECRET_ACCESS_KEY": "secret",
            "AWS_DEFAULT_REGION": "eu-west-1",
        },
        clear=True,
    )
    def test_prepare_credentials_from_env(self):
        """Credential preparation reads all values from env variables."""
        engine = _make_engine(_inference_engine_type=InferenceEngineType.BEDROCK)
        creds = engine.prepare_credentials({})
        self.assertEqual(creds["aws_access_key_id"], "AKIATEST")
        self.assertEqual(creds["aws_secret_access_key"], "secret")
        self.assertEqual(creds["region_name"], "eu-west-1")

    def test_prepare_credentials_from_dict(self):
        """Credential preparation reads values from passed dict."""
        engine = _make_engine(_inference_engine_type=InferenceEngineType.BEDROCK)
        creds = engine.prepare_credentials(
            {
                "aws_access_key_id": "AKIAEXPLICIT",
                "aws_secret_access_key": "s3cr3t",
                "region_name": "ap-southeast-1",
            }
        )
        self.assertEqual(creds["aws_access_key_id"], "AKIAEXPLICIT")
        self.assertEqual(creds["aws_secret_access_key"], "s3cr3t")
        self.assertEqual(creds["region_name"], "ap-southeast-1")

    @patch.dict(
        "os.environ",
        {"AWS_ACCESS_KEY_ID": "AKIA", "AWS_SECRET_ACCESS_KEY": "s"},
        clear=True,
    )
    def test_prepare_credentials_default_region(self):
        """region_name defaults to us-east-1 when not set."""
        engine = _make_engine(_inference_engine_type=InferenceEngineType.BEDROCK)
        creds = engine.prepare_credentials({})
        self.assertEqual(creds["region_name"], "us-east-1")

    # create_client

    def test_create_client_builds_boto3_client(self):
        """create_client calls boto3.client with the correct arguments."""
        engine = _make_engine(
            credentials={
                "aws_access_key_id": "AKIA",
                "aws_secret_access_key": "s3cr3t",
                "region_name": "us-east-1",
            }
        )
        with patch("ai_atlas_nexus.blocks.inference.bedrock.boto3") as mock_boto3:
            engine.create_client()
            mock_boto3.client.assert_called_once_with(
                "bedrock-runtime",
                aws_access_key_id="AKIA",
                aws_secret_access_key="s3cr3t",
                region_name="us-east-1",
            )

    # ping

    def _mock_boto3_for_ping(self, mock_boto3, model_id, sts_side_effect=None):
        """Configure boto3.client mock for ping(): first call = STS, second = bedrock mgmt."""
        mock_sts = Mock()
        if sts_side_effect:
            mock_sts.get_caller_identity.side_effect = sts_side_effect
        else:
            mock_sts.get_caller_identity.return_value = {"UserId": "test"}

        mock_bedrock_mgmt = Mock()
        mock_bedrock_mgmt.list_foundation_models.return_value = {
            "modelSummaries": [{"modelId": model_id}]
        }

        mock_boto3.client.side_effect = [mock_sts, mock_bedrock_mgmt]

    def test_ping_success(self):
        """Successful ping when credentials are valid and model is available."""
        engine = _make_engine(
            model_name_or_path="amazon.nova-pro-v1:0",
            credentials={
                "aws_access_key_id": "AKIA",
                "aws_secret_access_key": "s",
                "region_name": "us-east-1",
            }
        )
        with patch("ai_atlas_nexus.blocks.inference.bedrock.boto3") as mock_boto3:
            self._mock_boto3_for_ping(mock_boto3, "amazon.nova-pro-v1:0")
            engine.ping()  # should not raise

    def test_ping_invalid_credentials(self):
        """ping raises on invalid AWS credentials."""
        engine = _make_engine(
            model_name_or_path="amazon.nova-pro-v1:0",
            credentials={
                "aws_access_key_id": "BAD",
                "aws_secret_access_key": "BAD",
                "region_name": "us-east-1",
            }
        )
        with patch("ai_atlas_nexus.blocks.inference.bedrock.boto3") as mock_boto3:
            self._mock_boto3_for_ping(
                mock_boto3, "amazon.nova-pro-v1:0",
                sts_side_effect=Exception("InvalidClientTokenId"),
            )
            with self.assertRaises(Exception) as ctx:
                engine.ping()
        self.assertIn("Authentication failed", str(ctx.exception))

    def test_ping_model_not_found(self):
        """ping raises when model is not in the available list."""
        engine = _make_engine(
            model_name_or_path="amazon.nova-fake-v9:0",
            credentials={
                "aws_access_key_id": "AKIA",
                "aws_secret_access_key": "s",
                "region_name": "us-east-1",
            }
        )
        with patch("ai_atlas_nexus.blocks.inference.bedrock.boto3") as mock_boto3:
            self._mock_boto3_for_ping(mock_boto3, "amazon.nova-pro-v1:0")
            with self.assertRaises(Exception) as ctx:
                engine.ping()
        self.assertIn("amazon.nova-fake-v9:0", str(ctx.exception))
        self.assertIn("not found", str(ctx.exception))

    def test_ping_connection_error(self):
        """ping raises a connection error when STS cannot be reached."""
        engine = _make_engine(
            model_name_or_path="amazon.nova-pro-v1:0",
            credentials={
                "aws_access_key_id": "AKIA",
                "aws_secret_access_key": "s",
                "region_name": "us-east-1",
            }
        )
        with patch("ai_atlas_nexus.blocks.inference.bedrock.boto3") as mock_boto3:
            self._mock_boto3_for_ping(
                mock_boto3, "amazon.nova-pro-v1:0",
                sts_side_effect=Exception("Could not connect to endpoint"),
            )
            with self.assertRaises(Exception) as ctx:
                engine.ping()
        self.assertIn("Connection error", str(ctx.exception))

    # _to_bedrock_format

    def test_to_bedrock_format_string(self):
        """Plain strings are wrapped as user messages."""
        engine = _make_engine()
        result = engine._to_bedrock_format("hello")
        self.assertEqual(result, [{"role": "user", "content": [{"text": "hello"}]}])

    def test_to_bedrock_format_openai_messages(self):
        """OpenAI-style message dicts are converted to Bedrock format."""
        engine = _make_engine()
        messages = [
            {"role": "user", "content": "What is risk?"},
            {"role": "assistant", "content": "Risk is ..."},
        ]
        result = engine._to_bedrock_format(messages)
        self.assertEqual(result[0]["role"], "user")
        self.assertEqual(result[0]["content"][0]["text"], "What is risk?")
        self.assertEqual(result[1]["role"], "assistant")
        self.assertEqual(result[1]["content"][0]["text"], "Risk is ...")

    # _prepare_chat_output

    def test_prepare_chat_output_with_response_dict(self):
        """_prepare_chat_output extracts prediction, token counts, and stop reason."""
        engine = _make_engine(
            model_name_or_path="amazon.nova-pro-v1:0",
            _inference_engine_type=InferenceEngineType.BEDROCK,
        )
        result = engine._prepare_chat_output(
            _mock_response("generated text", input_tokens=120, output_tokens=40)
        )
        self.assertIsInstance(result, TextGenerationInferenceOutput)
        self.assertEqual(result.prediction, "generated text")
        self.assertEqual(result.input_tokens, 120)
        self.assertEqual(result.output_tokens, 40)
        self.assertEqual(result.stop_reason, "end_turn")

    def test_prepare_chat_output_unwraps_array_envelope(self):
        """_prepare_chat_output unwraps the {"items": [...]} envelope."""
        engine = _make_engine(
            model_name_or_path="amazon.nova-pro-v1:0",
            _inference_engine_type=InferenceEngineType.BEDROCK,
        )
        wrapped = json.dumps({"items": ["Risk A", "Risk B"]})
        result = engine._prepare_chat_output(_mock_response(wrapped))
        self.assertEqual(result.prediction, json.dumps(["Risk A", "Risk B"]))

    def test_prepare_chat_output_leaves_non_envelope_objects_intact(self):
        """_prepare_chat_output does NOT unwrap objects with multiple keys."""
        engine = _make_engine(
            model_name_or_path="amazon.nova-pro-v1:0",
            _inference_engine_type=InferenceEngineType.BEDROCK,
        )
        multi_key = json.dumps({"items": ["A"], "extra": "value"})
        result = engine._prepare_chat_output(_mock_response(multi_key))
        self.assertEqual(result.prediction, multi_key)

    # _create_schema_format

    def test_create_schema_format_with_object_schema(self):
        """Object-type schemas pass through unwrapped."""
        engine = _make_engine()
        schema = {"type": "object", "properties": {"name": {"type": "string"}}}
        result = engine._create_schema_format(schema)
        self.assertEqual(result, schema)

    def test_create_schema_format_wraps_root_array(self):
        """Root-array schemas are wrapped in an object."""
        engine = _make_engine()
        array_schema = {"type": "array", "items": {"enum": ["A", "B"]}}
        result = engine._create_schema_format(array_schema)
        self.assertEqual(result["type"], "object")
        self.assertIn("items", result["properties"])
        self.assertEqual(result["properties"]["items"], array_schema)
        self.assertEqual(result["required"], ["items"])

    def test_create_schema_format_none(self):
        """_create_schema_format returns None when no format given."""
        engine = _make_engine()
        self.assertIsNone(engine._create_schema_format(None))


if __name__ == "__main__":
    unittest.main()
