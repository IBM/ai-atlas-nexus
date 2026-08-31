from abc import ABC, abstractmethod
from typing import Any, List, Optional, Protocol

from ai_atlas_nexus.blocks.inference.base import InferenceEngine
from ai_atlas_nexus.blocks.risk_detector.generic import BatchSchema, DetectionRun


class Detector(Protocol):
    """The detector protocol

    `inference_engine` is declared read-only so that both shapes a decorator can wrap
    satisfy it: a `RiskDetector`, which sets it as an instance attribute, and another
    decorator, which exposes it as a property.
    """

    @property
    def inference_engine(self) -> InferenceEngine: ...

    def detect(self, usecases: List[str]) -> Any: ...

    def _run_inference(
        self, usecases: List[str], batch_schema: Optional[BatchSchema] = None
    ) -> DetectionRun[Any]: ...


class RiskDetectorDecorator(ABC):
    """Base for detectors that add one feature on top of another detector.

    Subclasses return a different type from `detect`.
    """

    def __init__(self, detector: Detector):
        """
        Args:
            detector: The detector to wrap.
        """
        self._detector = detector

    @property
    def detector(self) -> Detector:
        """The wrapped detector"""
        return self._detector

    @property
    def inference_engine(self) -> InferenceEngine:
        """The engine the wrapped detector runs on."""
        return self._detector.inference_engine

    @abstractmethod
    def detect(self, usecases: List[str]) -> Any:
        """Identify risks from usecases, adding this decorator's feature."""
        raise NotImplementedError

    def _run_inference(
        self, usecases: List[str], batch_schema: Optional[BatchSchema] = None
    ) -> DetectionRun[Any]:
        """Delegate to the wrapped detector.

        Decorators depend on `GenericRiskDetector._run_inference`: it returns the raw
        inference outputs that `detect` discards. A decorator needing to influence the
        inference itself overrides this, as `RiskDetectorWithExplanation` does to ask
        for a response schema carrying explanations.

        Args:
            usecases: List of usecase descriptions to analyze.
            batch_schema: Forwarded to the wrapped detector, overriding the batch
                response schema and its postprocessor.
        """
        return self._detector._run_inference(usecases, batch_schema=batch_schema)
