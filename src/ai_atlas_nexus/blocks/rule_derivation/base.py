from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuleMatch:
    """
    Evaluation result for a single rule against one instance.
    """
    rule_id: str
    description: str
    priority: int
    matched: bool
    derived_attributes: dict[str, Any] = field(default_factory=dict)


@dataclass
class RuleDerivationResult:
    """
    Aggregated result of applying all rules to one instance.
    """
    instance_id: str
    matches: list[RuleMatch]
    derived: dict[str, Any]

    @property
    def fired(self) -> list[RuleMatch]:
        return [m for m in self.matches if m.matched]


class RuleDeriverBase(ABC):

    @abstractmethod
    def derive(self, instance):
        """Derive with rules
        Args:
            instance: dict
        Returns:
            RuleDerivationResult
        """
        raise NotImplementedError

    @abstractmethod
    def explain(self, instance):
        """Explain with rules
        Args:
            instance: dict
        Returns:
            list[RuleMatch]
        """
        raise NotImplementedError
