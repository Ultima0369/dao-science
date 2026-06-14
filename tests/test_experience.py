"""Unit tests for dao_science.experience auditable memory."""
from __future__ import annotations

import pytest

from dao_science.experience import AuditableMemory, ExperienceRecord


def _record(context: str, outcome: float, confidence: float) -> ExperienceRecord:
    return ExperienceRecord(
        timestamp="2026-06-14T00:00:00Z",
        context_hash=context,
        decision="policy-a",
        outcome=outcome,
        confidence=confidence,
    )


def test_store_and_retrieve():
    memory = AuditableMemory()
    memory.store(_record("ctx-1", 1.0, 0.9))
    assert len(memory.retrieve("ctx-1")) == 1
    assert len(memory.retrieve("ctx-missing")) == 0


def test_audit_computes_mean_confidence_and_outcome():
    memory = AuditableMemory()
    memory.store(_record("ctx-1", 1.0, 0.9))
    memory.store(_record("ctx-1", 0.0, 0.5))
    report = memory.audit("ctx-1")
    assert report["applicability"] == pytest.approx(0.7)
    assert report["mean_outcome"] == pytest.approx(0.5)
    assert report["count"] == 2


def test_audit_empty_context():
    memory = AuditableMemory()
    report = memory.audit("missing")
    assert report["applicability"] == 0.0
    assert "notes" in report


def test_refresh_if_needed_triggered_by_high_prediction_error():
    memory = AuditableMemory()
    assert memory.refresh_if_needed("ctx-1", prediction_error=2.0, threshold=1.0) is True


def test_refresh_if_needed_not_triggered_by_low_prediction_error():
    memory = AuditableMemory()
    assert memory.refresh_if_needed("ctx-1", prediction_error=0.5, threshold=1.0) is False
