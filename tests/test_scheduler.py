"""Unit tests for dao_science.scheduler wave-frequency scheduler."""
from __future__ import annotations

import numpy as np
import pytest

from dao_science.scheduler import WaveScheduler


def test_step_preserves_total_power_budget():
    scheduler = WaveScheduler(shape=(3, 3), total_power_budget=9.0)
    grid = scheduler.step(t=0.0)
    assert pytest.approx(grid.sum()) == 9.0


def test_step_all_nodes_nonnegative():
    scheduler = WaveScheduler(shape=(4, 4), total_power_budget=16.0)
    grid = scheduler.step(t=1.5)
    assert np.all(grid >= 0)


def test_phi_returns_float():
    scheduler = WaveScheduler(shape=(2, 2), total_power_budget=4.0)
    value = scheduler.phi(0, 0, t=0.0)
    assert isinstance(value, float)


def test_metrics_has_expected_keys():
    scheduler = WaveScheduler(shape=(3, 3), total_power_budget=9.0)
    trace = np.stack([scheduler.step(float(t)) for t in range(5)])
    metrics = scheduler.metrics(trace)
    assert set(metrics.keys()) == {"power_smoothness", "thermal_entropy", "throughput_variance"}
