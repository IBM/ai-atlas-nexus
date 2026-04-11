from ai_atlas_nexus.blocks.inference import (
    OllamaInferenceEngine,
    RITSInferenceEngine,
    VLLMInferenceEngine,
    WMLInferenceEngine,
)
from ai_atlas_nexus.blocks.inference.params import (
    InferenceEngineCredentials,
    OllamaInferenceEngineParams,
    RITSInferenceEngineParams,
    VLLMInferenceEngineParams,
    WMLInferenceEngineParams,
)
from ai_atlas_nexus.data import load_resource
from ai_atlas_nexus.library import AIAtlasNexus


inference_engine = WMLInferenceEngine(
    model_name_or_path="ibm/granite-4-h-small",
    credentials={
        "api_key": "uG5JqNBXskpMtA87jCmRcsSSdXgsge2Lc69ovE3D5_j2",
        "api_url": "https://us-south.ml.cloud.ibm.com",
        "project_id": "b9b8fd74-ee51-4386-b754-316a7e1e4d12",
    },
    parameters=WMLInferenceEngineParams(
        max_new_tokens=1000, decoding_method="greedy", repetition_penalty=1
    ),
)
# inference_engine = RITSInferenceEngine(
#     model_name_or_path="ibm-granite/granite-3.3-8b-instruct",
#     credentials={
#         "api_key": "cbc683b3a1a7c52d2a73008b785d2811",
#         "api_url": "https://inference-3scale-apicast-production.apps.rits.fmaas.res.ibm.com",
#     },
#     parameters=RITSInferenceEngineParams(max_completion_tokens=1000, temperature=0),
#     backend="mellea",
# )

ai_atlas_nexus = AIAtlasNexus()

usecase = "Generate personalized, relevant responses, recommendations, and summaries of claims for customers to support agents to enhance their interactions with customers."

domains = ai_atlas_nexus.identify_domain_from_usecases(
    usecases=[usecase],
    inference_engine=inference_engine,
)

print(domains[0].prediction)
