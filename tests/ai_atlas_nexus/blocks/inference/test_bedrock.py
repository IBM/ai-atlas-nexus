import json
import unittest
from unittest.mock import Mock, patch

import botocore.exceptions

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


def _mock_openai_response(content, *, input_tokens=10, output_tokens=3, stop_reason="stop"):
    """Build a minimal OpenAI-compatible response mock."""
    return {
        "choices": [{"message": {"content": content}, "finish_reason": stop_reason}],
        "usage": {"prompt_tokens": input_tokens, "completion_tokens": output_tokens},
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
        with patch("boto3.client") as mock_client:
            engine.create_client()
            mock_client.assert_called_once_with(
                "bedrock-runtime",
                aws_access_key_id="AKIA",
                aws_secret_access_key="s3cr3t",
                region_name="us-east-1",
            )

    # ping

    def _mock_boto3_for_ping(self, mock_client, model_id, sts_side_effect=None):
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

        mock_client.side_effect = [mock_sts, mock_bedrock_mgmt]

    def test_ping_success(self):
        """Successful ping when credentials are valid and model is available."""
        engine = _make_engine(
            model_name_or_path="openai.gpt-4o-mini",
            credentials={
                "aws_access_key_id": "AKIA",
                "aws_secret_access_key": "s",
                "region_name": "us-east-1",
            }
        )
        with patch("boto3.client") as mock_client:
            self._mock_boto3_for_ping(mock_client, "openai.gpt-4o-mini")
            engine.ping()  # should not raise

    def test_ping_invalid_credentials(self):
        """ping raises on invalid AWS credentials."""
        engine = _make_engine(
            model_name_or_path="openai.gpt-4o-mini",
            credentials={
                "aws_access_key_id": "BAD",
                "aws_secret_access_key": "BAD",
                "region_name": "us-east-1",
            }
        )
        with patch("boto3.client") as mock_client:
            self._mock_boto3_for_ping(
                mock_client, "openai.gpt-4o-mini",
                sts_side_effect=botocore.exceptions.ClientError(
                    {"Error": {"Code": "InvalidClientTokenId", "Message": "invalid token"}},
                    "GetCallerIdentity",
                ),
            )
            with self.assertRaises(Exception) as ctx:
                engine.ping()
        self.assertIn("Authentication failed", str(ctx.exception))

    def test_ping_model_not_found(self):
        """ping raises when model is not in the available list."""
        engine = _make_engine(
            model_name_or_path="openai.gpt-fake",
            credentials={
                "aws_access_key_id": "AKIA",
                "aws_secret_access_key": "s",
                "region_name": "us-east-1",
            }
        )
        with patch("boto3.client") as mock_client:
            self._mock_boto3_for_ping(mock_client, "openai.gpt-4o-mini")
            with self.assertRaises(Exception) as ctx:
                engine.ping()
        self.assertIn("openai.gpt-fake", str(ctx.exception))
        self.assertIn("not found", str(ctx.exception))

    def test_ping_connection_error(self):
        """ping raises a connection error when STS cannot be reached."""
        engine = _make_engine(
            model_name_or_path="openai.gpt-4o-mini",
            credentials={
                "aws_access_key_id": "AKIA",
                "aws_secret_access_key": "s",
                "region_name": "us-east-1",
            }
        )
        with patch("boto3.client") as mock_client:
            self._mock_boto3_for_ping(
                mock_client, "openai.gpt-4o-mini",
                sts_side_effect=botocore.exceptions.EndpointConnectionError(
                    endpoint_url="https://sts.us-east-1.amazonaws.com"
                ),
            )
            with self.assertRaises(Exception) as ctx:
                engine.ping()
        self.assertIn("Connection error", str(ctx.exception))

    # _prepare_chat_output

    def test_prepare_chat_output_with_openai_response(self):
        """_prepare_chat_output extracts prediction, token counts, stop reason, and seed."""
        engine = _make_engine(
            model_name_or_path="openai.gpt-4o-mini",
            _inference_engine_type=InferenceEngineType.BEDROCK,
            parameters={"seed": 42, "temperature": 0.7},
        )
        result = engine._prepare_chat_output(
            _mock_openai_response("generated text", input_tokens=120, output_tokens=40)
        )
        self.assertIsInstance(result, TextGenerationInferenceOutput)
        self.assertEqual(result.prediction, "generated text")
        self.assertEqual(result.input_tokens, 120)
        self.assertEqual(result.output_tokens, 40)
        self.assertEqual(result.stop_reason, "stop")
        self.assertEqual(result.seed, 42)

    def test_prepare_chat_output_unwraps_array_envelope(self):
        """_prepare_chat_output unwraps the {"items": [...]} envelope."""
        engine = _make_engine(
            model_name_or_path="openai.gpt-4o-mini",
            _inference_engine_type=InferenceEngineType.BEDROCK,
            parameters={},
        )
        wrapped = json.dumps({"items": ["Risk A", "Risk B"]})
        result = engine._prepare_chat_output(_mock_openai_response(wrapped))
        self.assertEqual(result.prediction, json.dumps(["Risk A", "Risk B"]))

    def test_prepare_chat_output_leaves_non_envelope_objects_intact(self):
        """_prepare_chat_output does NOT unwrap objects with multiple keys."""
        engine = _make_engine(
            model_name_or_path="openai.gpt-4o-mini",
            _inference_engine_type=InferenceEngineType.BEDROCK,
            parameters={},
        )
        multi_key = json.dumps({"items": ["A"], "extra": "value"})
        result = engine._prepare_chat_output(_mock_openai_response(multi_key))
        self.assertEqual(result.prediction, multi_key)

    def test_prepare_chat_output_raises_on_unknown_response_format(self):
        """_prepare_chat_output raises ValueError for unrecognised response shapes."""
        engine = _make_engine(
            model_name_or_path="openai.gpt-4o-mini",
            _inference_engine_type=InferenceEngineType.BEDROCK,
            parameters={},
        )
        with self.assertRaises(ValueError, msg="Unexpected response format from Bedrock"):
            engine._prepare_chat_output({"unknown_key": "value"})

    # _create_schema_format

    def test_create_schema_format_with_object_schema(self):
        """Object-type schemas are wrapped in the json_schema envelope."""
        engine = _make_engine()
        schema = {"type": "object", "properties": {"name": {"type": "string"}}}
        result = engine._create_schema_format(schema)
        self.assertEqual(result["type"], "json_schema")
        self.assertEqual(result["json_schema"]["name"], "Bedrock_Schema")
        self.assertEqual(result["json_schema"]["schema"], schema)
        self.assertTrue(result["json_schema"]["strict"])

    def test_create_schema_format_wraps_root_array(self):
        """Root-array schemas are wrapped in an object, then the json_schema envelope."""
        engine = _make_engine()
        array_schema = {"type": "array", "items": {"enum": ["A", "B"]}}
        result = engine._create_schema_format(array_schema)
        self.assertEqual(result["type"], "json_schema")
        inner = result["json_schema"]["schema"]
        self.assertEqual(inner["type"], "object")
        self.assertIn("items", inner["properties"])
        self.assertEqual(inner["properties"]["items"], array_schema)
        self.assertEqual(inner["required"], ["items"])

    def test_create_schema_format_none(self):
        """_create_schema_format returns None when no format given."""
        engine = _make_engine()
        self.assertIsNone(engine._create_schema_format(None))

    # _invoke_openai_model

    def _make_openai_engine(self, model_id="openai.gpt-4o-mini", parameters=None):
        """Helper: engine with a mock client for _invoke_openai_model tests."""
        engine = _make_engine(
            model_name_or_path=model_id,
            parameters=parameters or {},
        )
        engine.client = Mock()
        engine.client.invoke_model.return_value = {
            "body": Mock(read=lambda: json.dumps(_mock_openai_response("ok")).encode())
        }
        return engine

    def test_invoke_openai_model_sends_correct_body(self):
        """_invoke_openai_model includes model, messages, parameters, schema, and tools in the body."""
        engine = self._make_openai_engine(parameters={"max_tokens": 100, "temperature": 0.5})
        messages = [{"role": "user", "content": "hello"}]
        engine._invoke_openai_model(messages)
        call_kwargs = engine.client.invoke_model.call_args[1]
        body = json.loads(call_kwargs["body"])
        self.assertEqual(body["model"], "openai.gpt-4o-mini")
        self.assertEqual(body["messages"], messages)
        self.assertEqual(body["max_tokens"], 100)
        self.assertEqual(body["temperature"], 0.5)

    def test_invoke_openai_model_omits_none_params(self):
        """Parameters with None values are not included in the body."""
        engine = self._make_openai_engine(parameters={"max_tokens": None, "temperature": 0.7})
        engine._invoke_openai_model([{"role": "user", "content": "hi"}])
        body = json.loads(engine.client.invoke_model.call_args[1]["body"])
        self.assertNotIn("max_tokens", body)
        self.assertEqual(body["temperature"], 0.7)

    def test_invoke_openai_model_includes_schema_and_tools(self):
        """schema and tools are forwarded as response_format and tools in the body."""
        engine = self._make_openai_engine()
        schema = {"type": "json_schema", "json_schema": {"name": "S", "schema": {}, "strict": True}}
        tools = [{"type": "function", "function": {"name": "f"}}]
        engine._invoke_openai_model([{"role": "user", "content": "hi"}], schema=schema, tools=tools)
        body = json.loads(engine.client.invoke_model.call_args[1]["body"])
        self.assertEqual(body["response_format"], schema)
        self.assertEqual(body["tools"], tools)

    def test_invoke_openai_model_omits_none_schema_and_tools(self):
        """response_format and tools keys are absent from the body when not provided."""
        engine = self._make_openai_engine()
        engine._invoke_openai_model([{"role": "user", "content": "hi"}])
        body = json.loads(engine.client.invoke_model.call_args[1]["body"])
        self.assertNotIn("response_format", body)
        self.assertNotIn("tools", body)


if __name__ == "__main__":
    unittest.main()
