"""
A custom simple rules engine.
"""

import copy
from dataclasses import dataclass
from enum import Enum
from typing import Any


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

class PredicateOp(str, Enum):
    eq    = "eq"      # scalar string equality
    id_eq = "id_eq"   # equality on the instance's id slot


@dataclass
class Predicate:
    path: str         # dot-path into the subgraph, e.g. "deployment.env"
    op: PredicateOp
    value: str


@dataclass
class Action:
    target_path: str  # dot-path to the object to mutate ("" = root)
    attribute: str    # slot name to set
    value: Any


@dataclass
class Rule:
    id: str
    predicates: list[Predicate]
    actions: list[Action]
    priority: int = 0
    description: str = ""

def resolve_path(obj, path):
    """Walk the dot-separated path through nested objects or dicts.
    Args:
        obj: Any
        path: str
    Returns:
        Any | None
    """
    if not path:
        return obj
    current = obj
    for part in path.split("."):
        if current is None:
            return None
        current = current.get(part) if isinstance(current, dict) else getattr(current, part, None)
    return current


def set_at_path(obj, path, attribute, value):
    """
    Navigate to the path, then set attribute = value on the target node.
    Args:
        obj: Any
        path: str
        attribute: str
        value: Any
    Return:
        None
    """
    target = resolve_path(obj, path) if path else obj
    if target is None:
        raise ValueError(f"Path '{path}' resolved to None — cannot set {attribute}={value!r}")
    if isinstance(target, dict):
        target[attribute] = value
    else:
        setattr(target, attribute, value)


class RulesEngine:
    """
    Applies a priority-ordered list of rules to an instance and
    returns a derived copy of that instance.

    All predicates in a rule must match for the actions to fire.
    Rules are evaluated in descending priority order.
    """

    def __init__(self, rules: list[Rule]):
        self.rules = sorted(rules, key=lambda r: r.priority, reverse=True)

    def _eval_predicate(self, graph: Any, predicate: Predicate) -> bool:
        target = resolve_path(graph, predicate.path)
        if target is None:
            return False
        if predicate.op == PredicateOp.eq:
            return isinstance(target, str) and target == predicate.value
        if predicate.op == PredicateOp.id_eq:
            instance_id = getattr(target, "id", None) or getattr(target, "@id", None)
            return str(instance_id) == predicate.value
        return False

    def _rule_matches(self, graph: Any, rule: Rule) -> bool:
        return all(self._eval_predicate(graph, p) for p in rule.predicates)

    def apply(self, root: Any) -> Any:
        """Deep-copy *root*, apply matching rules, return derived subgraph."""
        derived = copy.deepcopy(root)
        for rule in self.rules:
            if self._rule_matches(derived, rule):
                for action in rule.actions:
                    set_at_path(derived, action.target_path, action.attribute, action.value)
        return derived

    def explain(self, root: Any) -> list[dict]:
        """Dry-run: return which rules would fire and which actions they would apply."""
        derived = copy.deepcopy(root)
        report = []
        for rule in self.rules:
            matched = self._rule_matches(derived, rule)
            entry = {
                "rule_id": rule.id,
                "description": rule.description,
                "priority": rule.priority,
                "matched": matched,
                "actions": [],
            }
            if matched:
                for action in rule.actions:
                    entry["actions"].append({
                        "target_path": action.target_path,
                        "attribute": action.attribute,
                        "value": action.value,
                    })
                    set_at_path(derived, action.target_path, action.attribute, action.value)
            report.append(entry)
        return report
