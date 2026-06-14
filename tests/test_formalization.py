"""Unit tests for dao_science formalization stubs."""

import numpy as np
import pytest

from dao_science import (
    awareness_bandwidth,
    cost_of_deviation,
    critical_handover_signal,
    dao_gradient_step,
    de_ming_allocation,
    expected_free_energy,
    planetary_heat_budget_occupancy,
    policy_selection,
    precision_weighted_update,
)


def test_expected_free_energy() -> None:
    assert expected_free_energy(0.5, -0.2) == pytest.approx(0.7)
    assert expected_free_energy(0.0, 0.0) == pytest.approx(0.0)


def test_policy_selection_is_probability_distribution() -> None:
    probs = policy_selection(np.array([1.0, 2.0, 3.0]), gamma=1.0)
    assert probs.shape == (3,)
    assert np.isclose(probs.sum(), 1.0)
    assert np.all(probs >= 0)


def test_policy_selection_prefers_lower_free_energy() -> None:
    probs = policy_selection(np.array([3.0, 1.0, 2.0]), gamma=10.0)
    assert probs[1] > probs[2] > probs[0]


def test_dao_gradient_step() -> None:
    theta = np.array([1.0, 2.0])
    grad = np.array([0.5, -0.5])
    updated = dao_gradient_step(theta, grad, eta=0.1)
    np.testing.assert_allclose(updated, [0.95, 2.05])


def test_awareness_bandwidth() -> None:
    assert awareness_bandwidth(0.0, 0.0, 1.0) == pytest.approx(1.0)
    assert awareness_bandwidth(1.0, 0.0, 1.0) == pytest.approx(0.0)
    assert awareness_bandwidth(0.5, 0.0, 1.0) == pytest.approx(0.5)


def test_awareness_bandwidth_invalid_range() -> None:
    with pytest.raises(ValueError):
        awareness_bandwidth(0.5, 1.0, 1.0)


def test_precision_weighted_update() -> None:
    assert precision_weighted_update(0.0, 1.0, 0.5) == pytest.approx(0.5)


def test_cost_of_deviation() -> None:
    assert cost_of_deviation(1.2, 1.0) == pytest.approx(0.2)
    assert cost_of_deviation(0.9, 1.0) == pytest.approx(0.0)


def test_de_ming_allocation_sums_to_total() -> None:
    allocation = de_ming_allocation(
        mu=np.array([1.0, 0.5, 0.2]),
        sigma=np.array([0.1, 0.1, 0.1]),
        total_energy=1.0,
    )
    assert np.isclose(allocation.sum(), 1.0)
    assert allocation[0] > allocation[1] > allocation[2]


def test_critical_handover_signal() -> None:
    high_tension_declining = critical_handover_signal(1.0, -1.0, theta=0.5, k=8.0)
    low_tension = critical_handover_signal(0.1, -1.0, theta=0.5, k=8.0)
    assert high_tension_declining > low_tension


def test_planetary_heat_budget_occupancy() -> None:
    assert planetary_heat_budget_occupancy(10.0, 0.1, 1000.0) == pytest.approx(0.1)


def test_planetary_heat_budget_occupancy_invalid() -> None:
    with pytest.raises(ValueError):
        planetary_heat_budget_occupancy(10.0, 0.0, 1000.0)
