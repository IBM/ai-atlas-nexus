import types
from typing import Any

from ai_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import (
    AttributeConditionRule,
)
from ai_atlas_nexus.blocks.rule_derivation.base import (
    RuleDerivationResult,
    RuleDeriverBase,
    RuleMatch,
)
from ai_atlas_nexus.blocks.rule_derivation.engine import (
    Action,
    Predicate,
    PredicateOp,
    Rule,
    RulesEngine,
)
from ai_atlas_nexus.toolkit.logging import configure_logger


logger = configure_logger(__name__)


def _get(obj: Any, key: str, default: Any = None) -> Any:
    """Unified attribute access for dicts and objects (Pydantic / SimpleNamespace)."""
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _to_namespace(instance: dict | Any, slots_to_normalize: set[str]) -> types.SimpleNamespace:
    """
    Convert an instance (dict or Pydantic/SimpleNamespace) to a SimpleNamespace.

    Multivalued slots that appear in rule predicates are flattened to their first
    element so the engine's eq predicate can perform scalar equality checks.
    """
    def _build(obj: Any) -> Any:
        if isinstance(obj, dict):
            ns = types.SimpleNamespace()
            for k, v in obj.items():
                setattr(ns, k, _build(v))
            return ns
        if isinstance(obj, list):
            return [_build(i) for i in obj]
        # Pydantic / dataclass objects: convert via their own field iteration
        if hasattr(obj, "model_fields"):
            ns = types.SimpleNamespace()
            for k in obj.model_fields:
                setattr(ns, k, _build(getattr(obj, k)))
            return ns
        return obj

    ns = _build(instance) if isinstance(instance, dict) else _build(
        {k: _get(instance, k) for k in (
            instance.keys() if isinstance(instance, dict)
            else vars(instance) if hasattr(instance, "__dict__")
            else {}
        )}
    )

    for slot in slots_to_normalize:
        val = getattr(ns, slot, None)
        if isinstance(val, list) and val:
            setattr(ns, slot, val[0])

    return ns


def _translate_attribute_condition_rules(raw_rules: list) -> list[Rule]:
    """
    Translate AttributeConditionRule records into Rule/Predicate/Action format.

    Accepts both raw dicts and Pydantic objects.

    Postconditions with dotted paths (e.g. hasRelatedRisk.isUsedWithinLocality)
    are simplified to top-level derived_<attr> attributes on the root so the
    engine's set_at_path can handle them without list iteration.
    """
    translated: list[Rule] = []
    for i, raw in enumerate(raw_rules):
        if _get(raw, "type") != type(AttributeConditionRule):
            continue

        precond = _get(_get(raw, "preconditions", {}), "slot_conditions", [])
        postcond = _get(_get(raw, "postconditions", {}), "slot_conditions", [])

        predicates = [
            Predicate(
                path=_get(sc, "slot_name"),
                op=PredicateOp.eq,
                value=_get(sc, "equals_string"),
            )
            for sc in precond
        ]

        actions = []
        for sc in postcond:
            slot_name = _get(sc, "slot_name")
            # Dotted paths target nested lists; map to a flat derived_ attribute on root.
            attr = slot_name.split(".")[-1] if "." in slot_name else slot_name
            actions.append(
                Action(
                    target_path="",
                    attribute=f"derived_{attr}",
                    value=_get(sc, "equals_string"),
                )
            )

        translated.append(
            Rule(
                id=_get(raw, "id"),
                description=_get(raw, "name", ""),
                priority=len(raw_rules) - i,
                predicates=predicates,
                actions=actions,
            )
        )

    logger.debug("Translated %d AttributeConditionRule(s)", len(translated))
    return translated


def _get_predicate_slots(rules: list[Rule]) -> set[str]:
    """Slot names used in rule predicates — candidates for list→scalar normalisation."""
    return {p.path for r in rules for p in r.predicates}


def _get_derived_attrs(rules: list[Rule]) -> set[str]:
    """Attribute names that rule actions will set on the derived instance."""
    return {a.attribute for r in rules for a in r.actions}


class RuleDeriver(RuleDeriverBase):
    """
    Applies AttributeConditionRules to AI system
    instances to derive locality-specific attributes (e.g. applicable controls).

    Accepts rules as raw dicts or Pydantic AttributeConditionRule
    objects. Works with both dict instances and Pydantic / SimpleNamespace objects.

    Example::

        rules = data["rules"]            # from hiring_usecase_data.yaml
        systems = [e for e in data["entries"] if e.get("type") == "AiSystem"]

        deriver = RuleDeriver(rules)
        for system in systems:
            result = deriver.derive(system)
            print(result.derived)        # {"derived_isUsedWithinLocality": "..."}
            print(result.fired)          # [RuleMatch(rule_id=..., matched=True, ...)]
    """

    def __init__(self, raw_rules: list):
        self._rules = _translate_attribute_condition_rules(raw_rules)
        self._engine = RulesEngine(self._rules)
        self._predicate_slots = _get_predicate_slots(self._rules)
        self._derived_attrs = _get_derived_attrs(self._rules)

    @property
    def rules(self) -> list[Rule]:
        return list(self._rules)

    @property
    def predicate_slots(self) -> set[str]:
        return set(self._predicate_slots)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def derive(self, instance: dict | Any) -> RuleDerivationResult:
        """
        Apply all rules to *instance* and return a RuleDerivationResult containing
        per-rule match outcomes and the merged dict of derived attributes.
        """
        root = _to_namespace(instance, self._predicate_slots)
        report = self._engine.explain(root)
        derived_ns = self._engine.apply(root)

        matches = [
            RuleMatch(
                rule_id=entry["rule_id"],
                description=entry["description"],
                priority=entry["priority"],
                matched=entry["matched"],
                derived_attributes={a["attribute"]: a["value"] for a in entry["actions"]},
            )
            for entry in report
        ]

        derived = {
            attr: getattr(derived_ns, attr)
            for attr in self._derived_attrs
            if getattr(derived_ns, attr, None) is not None
        }

        return RuleDerivationResult(
            instance_id=_get(instance, "id", ""),
            matches=matches,
            derived=derived,
        )

    def explain(self, instance: dict | Any) -> list[RuleMatch]:
        """Dry-run: return per-rule match outcomes without mutating anything."""
        root = _to_namespace(instance, self._predicate_slots)
        report = self._engine.explain(root)
        return [
            RuleMatch(
                rule_id=entry["rule_id"],
                description=entry["description"],
                priority=entry["priority"],
                matched=entry["matched"],
                derived_attributes={a["attribute"]: a["value"] for a in entry["actions"]},
            )
            for entry in report
        ]
