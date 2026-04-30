import itertools
import json
import os
from importlib.metadata import version
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import yaml
from jinja2 import Template
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import YAMLDumper
from sssom_schema import Mapping

from ai_atlas_nexus.blocks.atlas_explorer.explorer import AtlasExplorer
from ai_atlas_nexus.exceptions import RiskInferenceError, handle_exception


# workaround for txtai
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"
os.environ["OMP_NUM_THREADS"] = "1"

from ai_atlas_nexus import AiTask, Taxonomy
from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import (
    Action,
    Adapter,
    AiEval,
    BenchmarkMetadataCard,
    Dataset,
    Documentation,
    LLMIntrinsic,
    LLMQuestionPolicy,
    Policy,
    Principle,
    Risk,
    RiskControl,
    RiskIncident,
    RiskTaxonomy,
    Rule,
    Stakeholder,
)
from ai_atlas_nexus.blocks.inference import InferenceEngine
from ai_atlas_nexus.blocks.prompt_builder import (
    FewShotPromptBuilder,
    ZeroShotPromptBuilder,
)
from ai_atlas_nexus.blocks.prompt_response_schema import (
    AITaskList,
    DomainType,
    QuestionnaireOutput,
)
from ai_atlas_nexus.blocks.prompt_templates import (
    AI_TASKS_TEMPLATE,
    QUESTIONNAIRE_COT_TEMPLATE,
)
from ai_atlas_nexus.blocks.risk_categorization.severity import RiskSeverityCategorizer
from ai_atlas_nexus.blocks.risk_detector import GenericRiskDetector
from ai_atlas_nexus.blocks.risk_mapping import RiskMapper
from ai_atlas_nexus.data import load_resource
from ai_atlas_nexus.extension import Extension
from ai_atlas_nexus.metadata_base import BackendType, MappingMethod
from ai_atlas_nexus.toolkit.data_utils import load_yamls_to_container
from ai_atlas_nexus.toolkit.error_utils import type_check, value_check
from ai_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)
RISK_IDENTIFICATION_COT = load_resource("risk_generation_cot.json")


class AIAtlasNexus:
    """A AIAtlasNexus object"""

    # Load the schema
    directory = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(
        directory,
        "ai_risk_ontology/schema/ai-risk-ontology.yaml",
    )
    schema_view = SchemaView(yaml.safe_load(fn))

    def __init__(self, base_dir: Optional[str] = None):
        """Create a new AIAtlasNexus object

        Args:
            base_dir: str
                (Optional) add an alternative source of data
        """
        if base_dir is not None:
            if type(base_dir) != str:
                raise ValueError(
                    "Base directory must be a string",
                    base_dir,
                )
            if not os.path.isdir(base_dir):
                logger.error(
                    f"Directory %s does not exist.",
                    base_dir,
                )
                raise FileNotFoundError(
                    "Base directory is not found",
                    base_dir,
                )

        ontology = load_yamls_to_container(base_dir)
        self._ontology = ontology
        self._atlas_explorer = AtlasExplorer(ontology)
        logger.info(
            f"Created AIAtlasNexus instance. Base_dir: %s",
            base_dir,
        )

    def export(cls, export_path):
        """Export AIAtlasNexus configuration to file.

        Args:
            export_path: str
                The path to the directory where the artifact will be exported to.

        """
        if not os.path.isdir(export_path):
            logger.error(
                f"Directory %s does not exist.",
                export_path,
            )
            raise FileNotFoundError(
                "Export directory is not found",
                export_path,
            )

        export_file_path = os.path.join(export_path, "ai-risk-ontology.yaml")

        with open(
            export_file_path,
            "+tw",
            encoding="utf-8",
        ) as output_file:
            print(
                YAMLDumper().dumps(cls._ontology),
                file=output_file,
            )
            output_file.close()

    @classmethod
    def get_schema(cls):
        """Get schema

        Returns:
            schema
        """
        return cls.schema_view

    @classmethod
    def get_version(cls):
        """Get library version

        Returns:
            dict: Version number
        """
        response = {"version": version("ai_atlas_nexus")}
        return response

    def get_all_classes(cls):
        """
        Get all the available classes

        Returns:
            List[str]
                List of classes
        """
        classes: List[str] = cls._atlas_explorer.get_all_classes()
        return classes

    def get_all(cls, class_name, taxonomy=None, vocabulary=None):
        """
        Get all the instances of a specified class.

        Args:
            class_name: str
                Name of the class (the collection key in data)
            taxonomy: Optional[Union[str, List[str]]]
                (Optional) The string id for a taxonomy or list of taxonomy ids
            vocabulary:
                (Optional) The string id for a vocabulary

        Returns:
            List[Dict[str, Any]]
                List of instances
        """
        value_check(
            "<RAN0948RVB6E>",
            class_name,
            "Please provide a class_name",
        )
        instances: list[Any] = cls._atlas_explorer.get_all(
            class_name, taxonomy, vocabulary
        )
        return instances

    def get_by_id(cls, class_name, identifier):
        """
        Get a single instance by its identifier.

        Args:
            class_name: str
                Name of the class (the collection key in data)
            identifier: str
                Value of the identifier field

        Returns:
            Optional[Dict[str, Any]]
                The matching instance or None
        """
        instance = cls._atlas_explorer.get_by_id(class_name, identifier)
        return instance

    def get_by_attribute(cls, class_name, attribute, value):
        """
        Get a single instance by its identifier.

        Args:
            class_name: str
                Name of the class (the collection key in data)
            attribute: str
                Attribute name to filter by
            value: Any
                Value to match

        Returns:
            Optional[Dict[str, Any]]
                The matching instance or None
        """
        instance = cls._atlas_explorer.get_by_attribute(class_name, attribute, value)
        return instance

    def query(cls, class_name, **kwargs):
        """
        Query instances using keyword arguments.

        Args:
            class_name: Union[str | list]:
                Name of the class (the collection key in data)
            **kwargs:
                The attribute-value pairs to filter by

        Returns:
            List[Dict[str, Any]]
                List of matching instances
        """
        return cls._atlas_explorer.query(class_name, **kwargs)

    def get_all_risks(cls, taxonomy=None):
        """Get all risk definitions from the LinkML

        Args:
            taxonomy: Optional[Union[str, List[str]]]
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            list[Risk]
                Result containing a list of AI risks
        """
        type_check(
            "<RANEACF44A7E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        risk_instances = cls._atlas_explorer.get_all("risks", taxonomy=taxonomy)
        return risk_instances

    def get_risk(
        cls,
        tag=None,
        id=None,
        name=None,
        taxonomy=None,
    ):
        """Get risk definition from the LinkML, filtered by risk atlas id, tag, name

        Args:
            id: (Optional) str
                The string ID identifying the risk
            tag: (Optional) str
                The string tag identifying the risk
            name: (Optional) str
                The string name identifying the risk
            taxonomy: Optional[Union[str, List[str]]]
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            Risk
                Result containing a list of AI risks
        """
        type_check(
            "<RAND62C1B3AE>",
            Union[str, List],
            allow_none=True,
            tag=tag,
            id=id,
            name=name,
            taxonomy=taxonomy,
        )
        value_check(
            "<RAN14D4D967E>",
            tag or id or name,
            "Please provide tag, id, or name",
        )

        risk: Risk | None = cls._atlas_explorer.query(
            "risks",
            tag=tag,
            id=id,
            name=name,
            taxonomy=taxonomy,
        )
        if risk and len(risk) > 0:
            risk = risk[0]
        else:
            risk = None
        return risk

    def get_related_risks(
        cls,
        risk=None,
        tag=None,
        id=None,
        name=None,
        taxonomy=None,
    ):
        """Get related risks from the LinkML, filtered by risk id, tag, or name

        Args:
            risk: (Optional) Risk
                The risk
            id: (Optional) str
                The string ID identifying the risk
            tag: (Optional) str
                The string tag identifying the risk
            name: (Optional) str
                The string name identifying the risk
            taxonomy: Optional[Union[str, List[str]]]
                (Optional) The string label for a taxonomy or list of strings
        Returns:
            List[str]
                Result containing a list of AI risk IDs
        """
        type_check(
            "<RAN283B72CAE>",
            Risk,
            allow_none=True,
            risk=risk,
        )
        type_check(
            "<RANC9FDCC45E>",
            Union[str | List],
            allow_none=True,
            tag=tag,
            id=id,
            name=name,
            taxonomy=taxonomy,
        )
        value_check(
            "<RAN0748ECB7E>",
            risk or tag or id or name,
            "Please provide tag, id, or name",
        )

        if id:
            risk = cls.get_risk(id=id)
        elif tag:
            risk = cls.get_risk(tag=tag)

        # just get all the related risks from the risk, these should have been added during lifting
        options = [
            risk.close_mappings or [],
            risk.exact_mappings or [],
            risk.broad_mappings or [],
            risk.narrow_mappings or [],
            risk.related_mappings or [],
        ]
        related_risk_ids = [x for x_list in options for x in x_list]
        related_risk_instances = [
            risk_instance
            for risk_instance in [cls.get_risk(id=x) for x in related_risk_ids]
            if risk_instance is not None
        ]
        return related_risk_instances

    def get_related_actions(
        cls,
        risk=None,
        tag=None,
        id=None,
        name=None,
        taxonomy=None,
    ):
        """Get actions for a risk definition from the LinkML.  The risk is identified by risk id, tag, or name

        Args:
            risk: (Optional) Risk
                The risk
            id: (Optional) str
                The string ID identifying the risk
            tag: (Optional) str
                The string tag identifying the risk
            name: (Optional) str
                The string name identifying the risk
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            Risk
                Result containing a list of AI actions
        """
        type_check(
            "<RANEDB39EABE>",
            Risk,
            allow_none=True,
            risk=risk,
        )
        type_check(
            "<RANC49E332BE>",
            str,
            allow_none=True,
            tag=tag,
            id=id,
            name=name,
            taxonomy=taxonomy,
        )
        value_check(
            "<RAN7154EE0FE>",
            risk or tag or id or name,
            "Please provide risk, tag, id, or name",
        )

        if id:
            risk = cls.get_risk(id=id)
        elif tag:
            risk = cls.get_risk(tag=tag)
        elif name:
            risk = cls.get_risk(name=name)

        related_action_ids = risk.hasRelatedAction
        if related_action_ids:
            return [
                cls._atlas_explorer.get_by_id(class_name="actions", identifier=x)
                for x in related_action_ids
            ]
        else:
            return []
        return related_action_instances

    def get_all_actions(cls, taxonomy: Optional[Union[str, List[str]]] = None):
        """Get all action definitions from the LinkML

        Args:
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            list[Action]
                Result containing a list of AI actions
        """
        type_check(
            "<RAN1C9A35ADE>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        action_instances: list[Action] = cls._atlas_explorer.get_all(
            "actions", taxonomy=taxonomy
        )
        return action_instances

    def get_action_by_id(cls, id, taxonomy: Optional[Union[str, List[str]]] = None):
        """Get an action definition from the LinkML, filtered by action id

        Args:
            id: str
                The string id identifying the action
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            Action
                Result containing an action
        """
        type_check(
            "<RAN66203B1FE>",
            str,
            allow_none=False,
            id=id,
        )
        type_check(
            "<RAN869039B6E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        action: Action | None = cls._atlas_explorer.get_by_id(
            class_name="actions", identifier=id
        )
        return action

    def get_related_risk_controls(
        cls,
        risk=None,
        tag=None,
        id=None,
        name=None,
        taxonomy=None,
    ):
        """Get related risk controls for a risk definition from the LinkML.  The risk is identified by risk id, tag, or name

        Args:
            risk: (Optional) Risk
                The risk
            id: (Optional) str
                The string ID identifying the risk
            tag: (Optional) str
                The string tag identifying the risk
            name: (Optional) str
                The string name identifying the risk
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            Risk
                Result containing a list of AI actions
        """
        type_check(
            "<RAN4E03158FE>",
            Risk,
            allow_none=True,
            risk=risk,
        )
        type_check(
            "<RAN55784808E>",
            str,
            allow_none=True,
            tag=tag,
            id=id,
            name=name,
            taxonomy=taxonomy,
        )
        value_check(
            "<RAN5DCADG95E>",
            risk or tag or id or name,
            "Please provide risk, tag, id, or name",
        )

        if id:
            risk = cls.get_risk(id=id)
        elif tag:
            risk = cls.get_risk(tag=tag)
        elif name:
            risk = cls.get_risk(name=name)

        risk_controls = [
            cls._atlas_explorer.get_by_id(class_name="riskcontrols", identifier=x)
            for x in risk.isDetectedBy or []
        ]
        return risk_controls

    def get_all_risk_controls(cls, taxonomy: Optional[Union[str, List[str]]] = None):
        """Get all risk control definitions from the LinkML

        Args:
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            list[RiskControl]
                Result containing a list of RiskControls
        """
        type_check(
            "<RAN129A1692E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        risk_control_instances: list[RiskControl] = cls._atlas_explorer.get_all(
            "riskcontrols", taxonomy=taxonomy
        )
        return risk_control_instances

    def get_risk_control(
        cls, id=None, taxonomy: Optional[Union[str, List[str]]] = None
    ):
        """Get an action definition from the LinkML, filtered by risk control id

        Args:
            id: str
                The string id identifying the risk control
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            Action
                Result containing a risk control.
        """
        type_check(
            "<RAN9785FFE3E>",
            str,
            allow_none=False,
            id=id,
        )
        type_check(
            "<RAN5A157049E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        risk_control: RiskControl | None = cls._atlas_explorer.get_by_id(
            class_name="riskcontrols", identifier=id
        )
        return risk_control

    @handle_exception(exceptions=[RiskInferenceError])
    def identify_risks_from_usecases(
        cls,
        usecases: List[str],
        inference_engine: InferenceEngine,
        taxonomy: str | list[str] | List[str] | None = None,
        cot_examples: Optional[Dict[str, List]] = None,
        max_risk: Optional[int] = None,
        zero_shot_only: bool = False,
        batch_inference: bool = True,
        use_dspy_prompt: bool = False,
    ) -> List[List[Risk]]:
        """Identify potential risks from a usecase description

        Args:
            usecases (List[str]):
                A List of strings describing AI usecases
            inference_engine (InferenceEngine):
                An LLM inference engine to infer risks from the usecases.
            taxonomy (str, optional):
                The string label for a taxonomy. If not specified, the system will use "ibm-risk-atlas" as the default taxonomy.
            cot_examples (Dict[str, List], optional):
                If the user wants to improve risk identification via a Few-shot approach, `cot_examples` can be
                provided with the desired taxonomy as key. Please follow the example template at src/ai_atlas_nexus/data/templates/risk_generation_cot.json.
                If the `cot_examples` is omitted, the API default to a Zero-Shot approach.
            max_risk (int, optional):
                The maximum number of risks to extract. Pass None to allow the inference engine to determine the number of risks. Defaults to None.
            zero_shot_only (bool): If enabled, this flag allows the system to perform Zero Shot Risk identification, and the field `cot_examples` will be ignored.
            batch_inference (bool): Whether to run risk inference service in batch mode or at each risk level. Defaults to True.
            use_dspy_prompt (bool): Use per-risk DSPy optmized prompt instructions for risk identification. When enabled, `batch_inference` flag is ignored.
        Returns:
            List[List[Risk]]:
                Result containing a list of risks
        """
        type_check(
            "<RANE02D314BE>",
            List,
            allow_none=False,
            usecases=usecases,
        )
        type_check(
            "<RANE023914BE>",
            InferenceEngine,
            allow_none=False,
            inference_engine=inference_engine,
        )
        type_check(
            "<RANB72CAE6EE>",
            Union[str, list, List, None],
            allow_none=True,
            taxonomy=taxonomy,
        )
        type_check(
            "<RAN80975498E>",
            int,
            allow_none=True,
            max_risk=max_risk,
        )
        value_check(
            "<RAN4717CF18E>",
            all([isinstance(usecase, str) for usecase in usecases]),
            "Usecases must be a list of string.",
        )

        # if not providing taxonomy, set to IBM AI risk atlas
        taxonomies = []

        if taxonomy is None:
            logger.warning(
                f"<RAN47375G12W>",
                f"Taxonomy was not provided, defaulting to ibm-risk-atlas.",
            )
            taxonomies = ["ibm-risk-atlas"]
        elif isinstance(taxonomy, str):
            taxonomies.append(taxonomy)
        else:
            taxonomies = taxonomy

        if taxonomy is None:
            logger.warning(
                f"<RAN47375G12W>",
                f"Taxonomy was not provided, defaulting to ibm-risk-atlas.",
            )

        combined_processed_examples = None
        combined_risks = []

        for tx in taxonomies:

            if tx == "ibm-attack-risk-atlas":
                risks = [
                    risk
                    for risk in cls._atlas_explorer.get_all(
                        "risks", taxonomy="ibm-risk-atlas"
                    )
                    if risk.tag.endswith("-attack")
                ]
            else:
                risks = cls._atlas_explorer.get_all("risks", taxonomy=tx)

            combined_risks.extend(risks)

            if len(taxonomies) > 1:
                logger.debug(
                    f"When there is more than one taxonomy given, `zero_shot_only` flag is enabled.",
                )
                zero_shot_only = True

            if zero_shot_only:
                logger.debug(
                    f"The `zero_shot_only` flag is enabled. The system will use the Zero shot method. Any provided `cot_examples` will be disregarded.",
                )
            else:
                # For the given taxonomy type, check if the user has provided 'cot_examples'. If not,
                # retrieve the default cot examples from the master. If no examples exist in the master,
                # set it as None. The CoT examples include risk-related questions that have been synthetically generated for this task.
                processed_examples = (
                    cot_examples and cot_examples.get(tx, None)
                ) or RISK_IDENTIFICATION_COT.get(tx, None)
                if (
                    combined_processed_examples
                    and type(combined_processed_examples) == list
                ):
                    combined_processed_examples.append(processed_examples)
                else:
                    combined_processed_examples = processed_examples

        if combined_processed_examples is None:
            logger.warning(
                f"<RAN47275F12W> Chain of Thought (CoT) examples were not provided, or do not exist in the master for this taxonomy. The API will use the Zero shot method. To improve the accuracy of risk identification, please provide CoT examples in `cot_examples` when calling this API. You may also consider raising an issue to permanently add these examples to the AI Atlas Nexus master."
            )

        risk_detector = GenericRiskDetector(
            risks=combined_risks,
            inference_engine=inference_engine,
            cot_examples=combined_processed_examples,
            max_risk=max_risk,
            batch_inference=batch_inference,
            use_dspy_prompt=use_dspy_prompt,
        )

        return risk_detector.detect(usecases)

    @handle_exception(exceptions=[RiskInferenceError])
    def identify_risks_and_actions_from_usecases(
        cls,
        usecases: List[str],
        inference_engine: InferenceEngine,
        taxonomy: str | list[str] | List[str] | None = None,
        cot_examples: Optional[Dict[str, List]] = None,
        max_risk: Optional[int] = None,
        zero_shot_only: bool = False,
    ):
        """Identify potential risks from a usecase description

        Args:
            usecases (List[str]):
                A List of strings describing AI usecases
            inference_engine (InferenceEngine):
                An LLM inference engine to infer risks from the usecases.
            taxonomy (str | list[str] | List[str] | None = None):
                The string label for a taxonomy. If not specified, the system will use "ibm-risk-atlas" as the default taxonomy.
            cot_examples (Dict[str, List], optional):
                If the user wants to improve risk identification via a Few-shot approach, `cot_examples` can be
                provided with the desired taxonomy as key. Please follow the example template at src/ai_atlas_nexus/data/templates/risk_generation_cot.json.
                If the `cot_examples` is omitted, the API default to a Zero-Shot approach.
            max_risk (int, optional):
                The maximum number of risks to extract. Pass None to allow the inference engine to determine the number of risks. Defaults to None.
            zero_shot_only (bool): If enabled, this flag allows the system to perform Zero Shot Risk identification, and the field `cot_examples` will be ignored.
        Returns:
            List[List[Risk]]:
                Result containing a list of risks
        """
        type_check(
            "<RANE053314BE>",
            List,
            allow_none=False,
            usecases=usecases,
        )
        type_check(
            "<RANE023614CE>",
            InferenceEngine,
            allow_none=False,
            inference_engine=inference_engine,
        )
        type_check(
            "<RANB72CPE6BE>",
            Union[str, list, List, None],
            allow_none=True,
            taxonomy=taxonomy,
        )
        type_check(
            "<RAND098498E>",
            int,
            allow_none=True,
            max_risk=max_risk,
        )
        value_check(
            "<RAN6717CP18E>",
            all([isinstance(usecase, str) for usecase in usecases]),
            "Usecases must be a list of string.",
        )

        risks = cls.identify_risks_from_usecases(
            usecases, inference_engine, taxonomy, cot_examples, max_risk, zero_shot_only
        )[0]
        control_ids = []
        actions = []
        detectors = []

        for risk in risks:
            if risk.hasRelatedAction:
                risk_actions = (
                    risk.hasRelatedAction
                    if isinstance(risk.hasRelatedAction, list)
                    else [risk.hasRelatedAction]
                )
                actions.extend(risk_actions)

            if risk.isDetectedBy:
                risk_detections = (
                    risk.isDetectedBy
                    if isinstance(risk.isDetectedBy, list)
                    else [risk.isDetectedBy]
                )
                detectors.extend(risk_detections)

            mappings = list(
                itertools.chain(
                    risk.related_mappings or [],
                    risk.broad_mappings or [],
                    risk.close_mappings or [],
                    risk.exact_mappings or [],
                    risk.hasRelatedAction or [],
                    risk.isDetectedBy or [],
                )
            )

            control_ids.extend(
                cls._atlas_explorer.filter_ids_by_type(
                    ids=mappings, disallowed_types=["Risk"]
                )
            )
            control_ids = list(set(control_ids))

        summary_1 = {
            "risk_ids": [risk.id for risk in risks],
            "action_ids": actions,
            "detector_ids": detectors,
        }
        summary_2 = cls._atlas_explorer.arrange_ids_by_type(control_ids)
        summary = summary_1 | summary_2

        result = {
            "usecases": usecases,
            "model": inference_engine.model_name_or_path,
            "taxonomy": taxonomy,
            "summary": summary,
            "risks": risks,
            "mixed_control_items": [
                cls._atlas_explorer.get_by_id(None, identifier=item)
                for item in control_ids
            ],
        }
        return result

    def get_all_taxonomies(cls):
        """Get all taxonomy definitions from the LinkML

        Returns:
            List[Taxonomy]
                Result containing a list of taxonomies
        """
        taxonomy_instances: list[RiskTaxonomy] = cls._atlas_explorer.get_all(
            "taxonomies"
        )
        return taxonomy_instances

    def get_taxonomy_by_id(cls, id):
        """Get taxonomy definitions from the LinkML filtered by taxonomy id

        Args:
            id: str
                The string id for a taxonomy

        Returns:
            Taxonomy
                An AI taxonomy
        """
        type_check(
            "<RANBFB574E3E>",
            str,
            allow_none=False,
            id=id,
        )

        taxonomy: RiskTaxonomy | None = cls._atlas_explorer.get_by_id(
            class_name="taxonomies", identifier=id
        )
        return taxonomy

    def generate_zero_shot_risk_questionnaire_output(
        cls,
        usecase: str,
        risk_questionnaire: List[Dict[str, str]],
        inference_engine: InferenceEngine,
        verbose=True,
    ):
        """Get prediction using the zero shot approach.

        Args:
            usecase (str): A string describing an AI usecase
            risk_questionnaire: List[Dict[str, str]]: A risk questionnaire
                Check example below.
                ```
                [
                    "In which environment is the system used?",
                ]
                ```
            inference_engine (InferenceEngine):
                An LLM inference engine to predict the output based on the given use case.

        Returns:
            List[str]: List of LLM predictions.
        """
        type_check(
            "<RANF7EFFADAE>",
            InferenceEngine,
            allow_none=False,
            inference_engine=inference_engine,
        )
        type_check(
            "<RANB9FDEA04E>",
            str,
            allow_none=False,
            usecase=usecase,
        )
        type_check(
            "<RANF7256EC3E>",
            List,
            allow_none=False,
            questions=risk_questionnaire,
        )
        value_check(
            "<RANC49F00D3E>",
            inference_engine and risk_questionnaire,
            "Please provide questions and inference_engine",
        )

        # Extract only questions
        risk_questionnaire = [
            question_data["question"] for question_data in risk_questionnaire
        ]

        # Prepare zero shots inference prompts
        prompts = [
            ZeroShotPromptBuilder(
                QUESTIONNAIRE_COT_TEMPLATE,
            ).build(usecase=usecase, question=question)
            for question in risk_questionnaire
        ]

        # Invoke inference service
        return inference_engine.generate(
            prompts,
            response_format=QuestionnaireOutput,
            postprocessors=["json_object"],
            verbose=verbose,
        )

    def generate_few_shot_risk_questionnaire_output(
        cls,
        usecase: str,
        risk_questionnaire: List[Dict[str, Any]],
        inference_engine: InferenceEngine,
        verbose=True,
    ):
        """Get prediction using the few shot (Chain of Thought) examples.

        Args:
            usecase (str): A string describing an AI usecase
            risk_questionnaire (List[Dict]): Chain of Thought data for risk questionnaire.
                Each question is associated with a list of example intents and
                corresponding answers. Check example JSON below.
                ```
                [
                    {
                        "question": "In which environment is the system used?",
                        "examples": [
                            "intent": "Find patterns in healthcare insurance claims",
                            "answer": "Insurance Claims Processing or Risk Management or Data Analytics",
                            "explanation": "The system might be used by an insurance company's claims processing department to analyze and identify patterns in healthcare insurance claims."
                        ]
                    }
                ]
            inference_engine (InferenceEngine):
                An LLM inference engine to predict the output based on the given use case.
            filter_cot_data_by (Dict[str, str]):
                A dictionary to filter CoT examples with key as CoT field and value as filter string.
                ```

        Returns:
            List[str]: List of LLM predictions.
        """
        type_check(
            "<RAN19989483E>",
            InferenceEngine,
            allow_none=False,
            inference_engine=inference_engine,
        )
        type_check(
            "<RAN17812927E>",
            str,
            allow_none=False,
            usecase=usecase,
        )
        type_check(
            "<RAN46376875E>",
            List,
            allow_none=False,
            questions=risk_questionnaire,
        )
        value_check(
            "<RAN59638961E>",
            inference_engine and risk_questionnaire,
            "Please provide risk_questionnaire_cot and inference_engine",
        )

        assert (
            risk_questionnaire and len(risk_questionnaire) > 0
        ), "`Chain of Thought (risk_questionnaire_cot)` data cannot be None or empty."

        # Prepare few shots inference prompts from CoT Data
        prompts = [
            FewShotPromptBuilder(QUESTIONNAIRE_COT_TEMPLATE).build(
                cot_examples=question_data["cot_examples"],
                usecase=usecase,
                question=question_data["question"],
            )
            for question_data in risk_questionnaire
        ]

        # Invoke inference service
        return inference_engine.generate(
            prompts,
            response_format=QuestionnaireOutput,
            postprocessors=["json_object"],
            verbose=verbose,
        )

    def identify_ai_tasks_from_usecases(
        cls, usecases: List[str], inference_engine: InferenceEngine, verbose=True
    ) -> List[List[str]]:
        """Identify potential risks from a usecase description

        Args:
            usecases (List[str]):
                A List of strings describing AI usecases
            inference_engine (InferenceEngine):
                An LLM inference engine to identify AI tasks from usecases.
            verbose (bool, optional): prints detailed output during the inference process. Defaults to True.

        Returns:
            List[List[str]]:
                Result containing a list of AI tasks
        """
        type_check(
            "<RAN3B9CD886E>",
            InferenceEngine,
            allow_none=False,
            inference_engine=inference_engine,
        )
        type_check("<RAN4CDA6852E>", List, allow_none=False, usecases=usecases)
        value_check(
            "<RAN0E435F50E>",
            inference_engine and usecases,
            "Please provide usecases and inference_engine",
        )

        # Load HF tasks from the template dir
        hf_ai_tasks = [
            {"task_label": task.name, "task_description": task.description}
            for task in cls.get_all(class_name="aitasks", taxonomy="hf-ml-tasks")
        ]

        prompts = [
            (
                {
                    "description": "Classify the given use case into one or more AI Tasks that describes it best. Use the AI tasks definitions to make your decision. Provide a brief explanation for choosing a particular AI Task.",
                    "prefix": "You are an AI Task Classifier. You are clear and deterministic in your response. You always give classification label based on a plausible explanation. Study and understand the JSON below containing a list of AI task and its description.",
                    "requirements": [
                        "Give one or more AI tasks that best describes the use case",
                        "Provide a brief, plausible explanation for your choice",
                        "Be clear and deterministic in your classification",
                        "The AI task should only be from the AI Task Definitions. Do not include any other task type.",
                    ],
                    "grounding_context": {
                        "Use case": usecase,
                        "AI Task Definitions": json.dumps(hf_ai_tasks, indent=2),
                    },
                }
                if inference_engine.backend._backend_type == BackendType.MELLEA
                else Template(AI_TASKS_TEMPLATE).render(
                    usecase=usecase,
                    hf_ai_tasks=hf_ai_tasks,
                    limit=len(hf_ai_tasks),
                )
            )
            for usecase in usecases
        ]

        # Invoke inference service
        return inference_engine.generate(
            prompts=prompts,
            response_format=AITaskList,
            postprocessors=["json_object"],
            verbose=verbose,
        )

    def generate_proposed_mappings(
        cls,
        new_risks: List[Risk],
        existing_risks: List[Risk],
        inference_engine: InferenceEngine,
        new_prefix: str,
        mapping_method: MappingMethod = MappingMethod.SEMANTIC,
    ) -> List[Mapping]:
        """Identify mappings between a new set of risks and risks that exist in the Risk Atlas

        Args:
            new_risks: List[Risk]
                A new set of risks
            existing_risks: List[Risk]
                Secondary list, this should be the list of existing risks in RAN
            inference_engine: (Optional)Union[InferenceEngine | None]:
                An LLM inference engine to infer risks from the use cases.
            new_prefix: str
                The CURIE prefix for the new list of risks
            mapping_method: MappingMethod
                The possible values for type of risk mapping method

        Returns:
            List[Mapping]
                Result containing a list of mappings
        """
        type_check(
            "<RAN28959363E>",
            InferenceEngine,
            allow_none=True,
            inference_engine=inference_engine,
        )
        value_check(
            "<RAN85167315E>",
            new_risks and existing_risks,
            "Please provide new_risks and existing_risks",
        )
        value_check(
            "<RAN49187395E>",
            len(new_risks) > 0 and len(existing_risks) > 0,
            "The new and existing risks must not be empty",
        )
        risk_mapper = RiskMapper(
            new_risks=new_risks,
            existing_risks=existing_risks,
            inference_engine=inference_engine,
            new_prefix=new_prefix,
            mapping_method=mapping_method,
        )

        return risk_mapper.generate(
            new_risks=new_risks,
            existing_risks=existing_risks,
            inference_engine=inference_engine,
            new_prefix=new_prefix,
            mapping_method=mapping_method,
        )

    def get_risk_incidents(cls, taxonomy: Optional[Union[str, List[str]]] = None):
        """Get risk incident instances, optionally filtered by taxonomy

        Args:
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            List[RiskIncident]
                Result containing a list of AI Risk Incidents
        """
        type_check(
            "<RAN04811131E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        risk_incident_instances: List[RiskIncident] = cls._atlas_explorer.get_all(
            "riskincidents", taxonomy=taxonomy
        )
        return risk_incident_instances

    def get_risk_incident(
        cls, id=None, taxonomy: Optional[Union[str, List[str]]] = None
    ):
        """Get an risk incident instance filtered by risk incident id

        Args:
            id: str
                The string id identifying the risk incident
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            RiskIncident
                Result containing a risk incident.
        """
        type_check(
            "<RAN97353068E>",
            str,
            allow_none=False,
            id=id,
        )
        type_check(
            "<RAN38198685E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        risk_incident: RiskIncident | None = cls._atlas_explorer.get_by_id(
            class_name="riskincidents", identifier=id
        )
        return risk_incident

    def get_related_risk_incidents(
        cls,
        risk=None,
        risk_id=None,
        taxonomy=None,
    ):
        """Get related risk incident filtered by risk id

        Args:
            risk: (Optional) Risk
                The risk
            risk_id: (Optional) str
                The string ID identifying the risk
            taxonomy: str
                (Optional) The string label for a taxonomy
        Returns:
            List[RiskIncident]
                Result containing a list of AI risk incidents
        """
        type_check(
            "<RAN40791379E>",
            Risk,
            allow_none=True,
            risk=risk,
        )
        type_check(
            "<RANC9FDCC45E>",
            str,
            allow_none=True,
            risk_id=risk_id,
            taxonomy=taxonomy,
        )
        value_check(
            "<RAN79007538E>",
            risk or risk_id,
            "Please provide risk or id",
        )

        if risk_id:
            risk = cls.get_risk(id=risk_id)

        related_risk_incidents = cls._atlas_explorer.query(
            "riskincidents",
            refersToRisk=risk.id,
            taxonomy=taxonomy,
        )
        return related_risk_incidents

    def get_all_evaluations(cls, taxonomy: Optional[Union[str, List[str]]] = None):
        """Get all evaluation definitions from the LinkML

        Args:
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            list[AiEval]
                Result containing a list of AiEval
        """
        type_check(
            "<RAN18094995E>", Union[str, List], allow_none=True, taxonomy=taxonomy
        )

        evaluation_instances: list[AiEval] = cls._atlas_explorer.get_all(
            "evaluations", taxonomy=taxonomy
        )
        return evaluation_instances

    def get_evaluation(cls, id=None, taxonomy: Optional[Union[str, List[str]]] = None):
        """Get an evaluation definition from the LinkML, filtered by id

        Args:
            id: str
                The string id identifying the evaluation
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            Action
                Result containing an evaluation.
        """
        type_check("<RAN84465757E>", str, allow_none=False, id=id)
        type_check(
            "<RAN29906222E>", Union[str, List], allow_none=True, taxonomy=taxonomy
        )

        evaluation: AiEval | None = cls._atlas_explorer.get_by_id(
            class_name="evaluations", identifier=id
        )
        return evaluation

    def get_related_evaluations(
        cls, risk=None, risk_id=None, taxonomy: Optional[Union[str, List[str]]] = None
    ):
        """Get related evaluations filtered by risk id

        Args:
            risk: (Optional) Risk
                The risk
            risk_id: (Optional) str
                The string ID identifying the risk
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels
        Returns:
            List[AiEval]
                Result containing a list of AI evaluations
        """
        type_check("<RAN04616807E>", Risk, allow_none=True, risk=risk)
        type_check(
            "<RAN05640166E>",
            Union[str, List],
            allow_none=True,
            risk_id=risk_id,
            taxonomy=taxonomy,
        )
        value_check(
            "<RAN39630388E>",
            risk or risk_id,
            "Please provide risk or id",
        )

        if risk_id:
            risk = cls.get_risk(id=risk_id)

        related_evaluations = cls._atlas_explorer.query(
            "evaluations", hasRelatedRisk=risk.id, taxonomy=taxonomy
        )
        return related_evaluations

    def get_benchmark_metadata_cards(
        cls, risk=None, risk_id=None, taxonomy: Optional[Union[str, List[str]]] = None
    ):
        """Get all benchmark metadata definitions from the LinkML

        Args:
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            list[BenchmarkMetadataCard]
                Result containing a list of BenchmarkMetadataCards
        """
        type_check(
            "<RAN07894687E>",
            Union[str, List],
            allow_none=True,
            risk_id=risk_id,
            taxonomy=taxonomy,
        )
        type_check("<RAN30190075E>", Risk, allow_none=True, risk=risk)

        benchmark_metatdata_card_instances: list[BenchmarkMetadataCard] = (
            cls._atlas_explorer.get_all("benchmarkmetadatacards", taxonomy=taxonomy)
        )
        return benchmark_metatdata_card_instances

    def get_benchmark_metadata_card(cls, id=str):
        """Get an benchmark_metadata_card definition from the LinkML, filtered by id

        Args:
            id: str
                The string id identifying the benchmark_metadata_card
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            BenchmarkMetadataCard
                Result containing a benchmark_metadata_card.
        """
        type_check(
            "<RAN30946549E>",
            str,
            allow_none=False,
            id=id,
        )

        benchmark_metadata_card: BenchmarkMetadataCard | None = (
            cls._atlas_explorer.get_by_id(
                class_name="benchmarkmetadatacards", identifier=id
            )
        )
        return benchmark_metadata_card

    def get_documents(cls, taxonomy: Optional[Union[str, List[str]]] = None):
        """Get all document definitions from the LinkML

        Args:
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            list[Documentation]
                Result containing a list of Documentation
        """
        type_check(
            "<RAN61770043E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        document_instances: list[Documentation] = cls._atlas_explorer.get_all(
            "documents", taxonomy=taxonomy
        )
        return document_instances

    def get_document(cls, id=str):
        """Get a document definition from the LinkML, filtered by id

        Args:
            id: str
                The string id identifying the documentation entry
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            Documentation
                Result containing a document.
        """
        type_check(
            "<RAN12472418E>",
            str,
            allow_none=False,
            id=id,
        )

        document: Documentation | None = cls._atlas_explorer.get_by_id(
            "documents", identifier=id
        )
        return document

    def get_datasets(cls, taxonomy: Optional[Union[str, List[str]]] = None):
        """Get all dataset definitions from the LinkML

        Args:
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            list[Dataset]
                Result containing a list of Dataset entries
        """
        type_check(
            "<RAN61770043E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        dataset_instances: list[Dataset] = cls._atlas_explorer.get_all(
            "datasets", taxonomy=taxonomy
        )
        return dataset_instances

    def get_dataset(cls, id=str):
        """Get a dataset definition from the LinkML, filtered by id

        Args:
            id: str
                The string id identifying the dataset entry
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            Dataset
                Result containing a dataset.
        """
        type_check(
            "<RAN12472418E>",
            str,
            allow_none=False,
            id=id,
        )

        dataset: Dataset | None = cls._atlas_explorer.get_by_id(
            "datasets", identifier=id
        )
        return dataset

    def get_stakeholders(cls, taxonomy: Optional[Union[str, List[str]]] = None):
        """Get all stakeholder definitions from the LinkML

        Args:
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            list[Stakeholder]
                Result containing a list of Stakeholder entries
        """
        type_check(
            "<RAN61770043E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        stakeholder_instances: list[Stakeholder] = cls._atlas_explorer.get_all(
            "stakeholders", taxonomy=taxonomy
        )
        return stakeholder_instances

    def get_stakeholder(cls, id=str):
        """Get a stakeholder definition from the LinkML, filtered by id

        Args:
            id: str
                The string id identifying the stakeholder entry
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            Stakeholder
                Result containing a stakeholder.
        """
        type_check(
            "<RAN12472418E>",
            str,
            allow_none=False,
            id=id,
        )

        stakeholder: Stakeholder | None = cls._atlas_explorer.get_by_id(
            "stakeholders", identifier=id
        )
        return stakeholder

    def get_intrinsics(cls, taxonomy: Optional[Union[str, List[str]]] = None):
        """Get all intrinsic definitions from the LinkML

        Args:
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            list[LLMIntrinsic]
                Result containing a list of LLMIntrinsic entries
        """
        type_check(
            "<RAN61770043E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        intrinsic_instances: list[LLMIntrinsic] = cls._atlas_explorer.get_all(
            "llmintrinsics", taxonomy=taxonomy
        )
        return intrinsic_instances

    def get_intrinsic(cls, id=str):
        """Get an intrinsic definition from the LinkML, filtered by id

        Args:
            id: str
                The string id identifying the intrinsic entry
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            LLMIntrinsic
                Result containing a intrinsic.
        """
        type_check(
            "<RAN12472418E>",
            str,
            allow_none=False,
            id=id,
        )

        intrinsic: LLMIntrinsic | None = cls._atlas_explorer.get_by_id(
            "llmintrinsics", identifier=id
        )
        return intrinsic

    def get_related_intrinsics(
        cls,
        risk=None,
        tag=None,
        risk_id=None,
        aitask=None,
        aitask_id=None,
        task_id=None,
        name=None,
        taxonomy=None,
    ):
        """Get related intrinsics for a risk definition from the LinkML.  The risk is identified by risk id, tag, or name

        Args:
            risk: (Optional) Risk
                The risk
            risk_id: (Optional) str
                The string ID identifying the risk
            aitask: (Optional) str
                The aitask
            aitask_id: (Optional) str
                The string ID identifying the ai task
            tag: (Optional) str
                The string tag identifying the risk
            name: (Optional) str
                The string name identifying the risk
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            List
                Result containing a list of Intrinsics
        """
        type_check(
            "<RAN4E03158FE>",
            Risk,
            allow_none=True,
            risk=risk,
        )
        type_check(
            "<RAN4E93178FE>",
            AiTask,
            allow_none=True,
            aitask=aitask,
        )
        type_check(
            "<RAN55784808E>",
            str,
            allow_none=True,
            tag=tag,
            risk_id=risk_id,
            aitask_id=aitask_id,
            name=name,
            taxonomy=taxonomy,
        )
        value_check(
            "<RAN5DCADF94E>",
            risk or tag or aitask or aitask_id or risk_id or name,
            "Please provide risk, tag, aitask, aitask_id, risk_id, or name",
        )

        if aitask or aitask_id:
            if aitask_id:
                aitask = cls.get_by_id(class_name="aitasks", identifier=aitask_id)

            related_llmintrinsics = []
            capability_ids = (
                cls._atlas_explorer.get_attribute(
                    class_name="aitasks",
                    identifier=aitask.id,
                    attribute="requiresCapability",
                )
                or []
            )
            for cap in capability_ids:
                related_llmintrinsics += cls._atlas_explorer.query(
                    "llmintrinsics", c=cap.id, taxonomy=taxonomy
                )
        else:
            if risk_id:
                risk = cls.get_risk(id=risk_id)
            elif tag:
                risk = cls.get_risk(tag=tag)
            elif name:
                risk = cls.get_risk(name=name)

            related_llmintrinsics = cls._atlas_explorer.query(
                "llmintrinsics", hasRelatedRisk=risk.id, taxonomy=taxonomy
            )

        return related_llmintrinsics

    def get_adapters(cls, taxonomy: Optional[Union[str, List[str]]] = None):
        """Get all adapter definitions from the LinkML

        Args:
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            list[Adapter]
                Result containing a list of Adapter entries
        """
        type_check(
            "<RAN61770043E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        adapter_instances: list[Adapter] = cls._atlas_explorer.get_all(
            "adapters", taxonomy
        )
        return adapter_instances

    def get_adapter(cls, id=str):
        """Get an adapter definition from the LinkML, filtered by id

        Args:
            id: str
                The string id identifying the stakeholder entry
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            Adapter
                Result containing a adapter.
        """
        type_check(
            "<RAN12472418E>",
            str,
            allow_none=False,
            id=id,
        )

        adapter: Adapter | None = cls._atlas_explorer.get_by_id(
            "adapters", identifier=id
        )
        return adapter

    def get_llm_question_policies(
        cls, taxonomy: Optional[Union[str, List[str]]] = None
    ):
        """Get all LLM Quesiton Policy definitions from the LinkML

        Args:
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            list[LLMQuestionPolicy]
                Result containing a list of LLMQuestionPolicy entries
        """
        type_check(
            "<RAN61796043E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        llm_question_policy_instances: list[LLMQuestionPolicy] = (
            cls._atlas_explorer.get_all("llmquestionpolicies", taxonomy)
        )
        return llm_question_policy_instances

    def get_llm_question_policy(cls, id=str):
        """Get an LLM Question Policy definition from the LinkML, filtered by id

        Args:
            id: str
                The string id identifying the LLM question policy entry
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            LLMQuestionPolicy
                Result containing an LLM Question Policy.
        """
        type_check(
            "<RAN32462418E>",
            str,
            allow_none=False,
            id=id,
        )

        llm_question_policy: LLMQuestionPolicy | None = cls._atlas_explorer.get_by_id(
            "llmquestionPolicies", identifier=id
        )
        return llm_question_policy

    def get_principles(
        cls, taxonomy: Optional[Union[str, List[str]]] = None, document=None
    ):
        """Get all Principle definitions from the LinkML

        Args:
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels
            document: str
                (Optional) The string label for a document


        Returns:
            list[Principle]
                Result containing a list of Principle entries
        """
        type_check(
            "<RAN61573043E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )
        type_check(
            "<RAN62577043E>",
            str,
            allow_none=True,
            document=document,
        )

        principle_instances: list[Principle] = cls._atlas_explorer.get_all(
            "principles", taxonomy=taxonomy, document=document
        )
        return principle_instances

    def get_principle(cls, id=str):
        """Get a Principle definition from the LinkML, filtered by id

        Args:
            id: str
                The string id identifying the Principle entry

        Returns:
            Principle
                Result containing a Principle.
        """
        type_check(
            "<RAN97462678E>",
            str,
            allow_none=False,
            id=id,
        )

        principle: Principle | None = cls._atlas_explorer.get_by_id(
            "principles", identifier=id
        )
        return principle

    def get_instances(
        cls, target_class, taxonomy: Optional[Union[str, List[str]]] = None
    ):
        """Get all instance definitions from the LinkML

        Args:
            target_class: str
                (Optional) The string label for a target class
            taxonomy: str or list of str
                (Optional) The string label for a taxonomy or list of taxonomy labels

        Returns:
            list[Any]
                Result containing a list of instance entries
        """
        type_check(
            "<RAN92358069E>",
            str,
            allow_none=False,
            target_class=id,
        )
        type_check(
            "<RAN61877043E>",
            Union[str, List],
            allow_none=True,
            taxonomy=taxonomy,
        )

        instances: list[Any] = cls._atlas_explorer.get_instances(target_class, taxonomy)
        return instances

    def identify_domain_from_usecases(
        cls, usecases: List[str], inference_engine: InferenceEngine, verbose=True
    ) -> List[List[str]]:
        """Identify potential risks from a usecase description

        Args:
            usecases (List[str]):
                A List of strings describing AI usecases
            inference_engine (InferenceEngine):
                An LLM inference engine to identify AI tasks from usecases.
            verbose (bool, optional): prints detailed output during the inference process. Defaults to True.

        Returns:
            List[List[str]]:
                Result containing a list of AI tasks
        """
        type_check(
            "<RAN3B9CD886E>",
            InferenceEngine,
            allow_none=False,
            inference_engine=inference_engine,
        )
        type_check(
            "<RAN4CDA6852E>",
            List,
            allow_none=False,
            usecases=usecases,
        )
        value_check(
            "<RAN0E435F50E>",
            inference_engine and usecases,
            "Please provide usecases and inference_engine",
        )

        # Load risk questionnaire CoT from the template dir
        risk_questionnaire = load_resource("risk_questionnaire_cot.json")

        # Retrieve domain question data
        domain_ques_data = risk_questionnaire[0]

        # Load ai domain defintions from the template dir
        AI_DOMAIN_DEFINITONS = load_resource("ai_domain_defintions.json")

        prompts = [
            (
                {
                    "description": "Classify the given use case into one of the AI Domains that describes it best. Use the AI domain definitions to make your decision. Provide a brief explanation for choosing a particular AI Domain. If no suitable domain exists, classify it as 'Other'",
                    "prefix": "You are an AI Domain Classifier. You are clear and deterministic in your response. You always give classification label based on a plausible explanation.",
                    "requirements": [
                        "Give the AI domain that best describes the use case",
                        "Provide a brief, plausible explanation for your choice",
                        "Be clear and deterministic in your classification",
                        "The AI domain should only be from the AI Domain Definitions. Do not include any other domain type.",
                    ],
                    "grounding_context": {
                        "Use case": usecase,
                        "AI Domain Definitions": json.dumps(
                            AI_DOMAIN_DEFINITONS, indent=2
                        ),
                    },
                }
                if inference_engine.backend._backend_type == BackendType.MELLEA
                else FewShotPromptBuilder(
                    prompt_template=QUESTIONNAIRE_COT_TEMPLATE,
                ).build(
                    cot_examples=domain_ques_data["cot_examples"],
                    usecase=usecase,
                    question=domain_ques_data["question"],
                )
            )
            for usecase in usecases
        ]

        # Invoke inference service
        return inference_engine.generate(
            prompts=prompts,
            response_format=DomainType,
            postprocessors=["json_object"],
            verbose=verbose,
        )

    def categorize_risk_severity(
        self,
        usecases: List[str],
        inference_engine: InferenceEngine,
    ):
        """Determine the severity of risks based on the use case description.
        Args:
            usecases (List[str]):
                A List of strings describing AI usecases
            inference_engine (InferenceEngine):
                An LLM inference engine
        Returns:
            results (List[Dict]):
                Results detailing risk categorization by usecase.
        """
        type_check(
            "<RAN75727859E>",
            InferenceEngine,
            allow_none=False,
            inference_engine=inference_engine,
        )
        type_check(
            "<RAN68734549E>",
            List,
            allow_none=False,
            usecases=usecases,
        )
        value_check(
            "<RAN30508300E>",
            inference_engine and usecases,
            "Please provide usecases and inference_engine",
        )

        # Create Risk Severity instance
        risk_severity = RiskSeverityCategorizer(inference_engine)

        # Load risk questionnaire from the template dir
        risk_questionnaire = load_resource("risk_questionnaire_cot.json")

        # Collecting required parameters for categorizing risk severity per usecase
        results = []
        for usecase in usecases:
            domains = self.identify_domain_from_usecases(
                [usecase], inference_engine=inference_engine, verbose=False
            )
            # Get AI Domain of the usecase
            domain_predictions = [domain.prediction["answer"] for domain in domains]
            domain = domain_predictions[0] if len(domain_predictions) == 1 else None

            # Using a risk questionnaire to identify key attributes necessary for
            # constituting an AI system from the usecase.
            #
            # (Q4) AI User that interacts with the AI system
            # (Q5) Intended purpose of the AI System
            # (Q6) The capability of an AI system to do what it is designed to do
            # (Q7) AI Subject impacted by the AI System
            predictions = [
                response.prediction["answer"]
                for response in self.generate_few_shot_risk_questionnaire_output(
                    usecase,
                    list(
                        filter(
                            lambda question: question["no"] in ["Q4", "Q5", "Q6", "Q7"],
                            risk_questionnaire,
                        )
                    ),
                    inference_engine=inference_engine,
                    verbose=False,
                )
            ]

            # Extracting predictions
            if len(predictions) == 4:
                ai_user = predictions[0]
                purpose = predictions[1]
                capability = predictions[2]
                ai_subject = predictions[3]
            else:
                raise Exception(
                    "Unable to retrieve all the required attributes from the usecase. Please try again."
                )

            # Calling the risk categorization API with the required attributes.
            results.append(
                risk_severity.categorize(
                    domain, purpose, capability, ai_user, ai_subject
                )
            )

        return results

    def run_ares_evaluation(
        cls, risks: List[Risk], inference_engine: InferenceEngine, target: Dict
    ) -> None:
        """Submit potential attack risks for ARES red-teaming evaluation.
        This API needs the `ran-ares-integration` extension. Please install this extension via
        `ran-extension install ran-ares-integration`. Refer `Readme` file for further information
        on `ai-atlas-nexus` extensions.

        Args:
            risks (List[Risk]):
                A List of attack risks
            inference_engine (InferenceEngine):
                An instance of the LLM inference engine
            target (Dict):
                A target AI model to perform the ARES red-teaming evaluation

        Returns:
            None
        """
        logger.info(
            f"Risks submitted for ARES evluation: {json.dumps([risk.name for risk in risks], indent=2)}"
        )

        # Load RAN-ARES extension
        ares_extension = Extension.load(
            "ran-ares-integration", inference_engine, target=target
        )

        # Run extension on the given risks
        for risk in risks:
            ares_extension.run(risk)
