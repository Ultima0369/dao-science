"""Auditable experience memory for Project Dao.Science.

Every recorded experience carries a context hash, decision, outcome, confidence,
and an audit log so that downstream retrieval is not just similarity-based but
also accountable. This maps the `` li-ru `` (practice-as-proof) methodology to a
reusable software component.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__all__ = ["ExperienceRecord", "AuditableMemory"]


@dataclass
class ExperienceRecord:
    """One auditable experience sample.

    Args:
        timestamp: ISO-8601 UTC timestamp of the event.
        context_hash: Stable identifier of the decision context.
        decision: Decision or policy label that was executed.
        outcome: Scalar outcome (e.g., reward, prediction error).
        confidence: Confidence weight in [0, 1].
        audit_log: Arbitrary structured metadata for later inspection.
    """

    timestamp: str
    context_hash: str
    decision: str
    outcome: float
    confidence: float
    audit_log: dict[str, Any] = field(default_factory=dict)


class AuditableMemory:
    """Memory indexed by context hash, with confidence-weighted audit."""

    def __init__(self) -> None:
        self._records: dict[str, list[ExperienceRecord]] = {}

    def store(self, record: ExperienceRecord) -> None:
        """Append a record under its context hash."""
        self._records.setdefault(record.context_hash, []).append(record)

    def retrieve(self, context_hash: str) -> list[ExperienceRecord]:
        """Return all records for the exact context hash."""
        return list(self._records.get(context_hash, []))

    def audit(self, context_hash: str) -> dict[str, Any]:
        """Return an audit summary for a context hash.

        Returns:
            A dictionary with ``applicability`` (mean confidence),
            ``mean_outcome`` (mean outcome), and ``count``. If no records
            exist, ``applicability`` is 0.0 and ``notes`` explains why.
        """
        records = self.retrieve(context_hash)
        if not records:
            return {"applicability": 0.0, "notes": "no history"}
        weights = [r.confidence for r in records]
        outcomes = [r.outcome for r in records]
        return {
            "applicability": sum(weights) / len(weights),
            "mean_outcome": sum(outcomes) / len(outcomes),
            "count": len(records),
        }

    def refresh_if_needed(
        self,
        context_hash: str,
        prediction_error: float,
        threshold: float = 1.0,
    ) -> bool:
        """Trigger a memory refresh when prediction error exceeds threshold.

        This is a policy hook: when surprise is large, the caller should
        re-evaluate the stored policy (e.g., decay old weights, sample
        counterfactuals, or flag the context for human review).

        Returns:
            True if a refresh was triggered.
        """
        if prediction_error <= threshold:
            return False
        # Stub for re-weighting / decay logic.
        return True
