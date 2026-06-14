"""Unit tests for dao_science.core formalization stubs."""
from __future__ import annotations

import numpy as np
import pytest

from dao_science.core import (
    awareness_bandwidth,
    cost_of_deviation,
    critical_handover_signal,
    dao_gradient_step,
    de_ming_allocation,
    de_precision_matrix,
    expected_free_energy,
    generalized_sigmoid,
    gradient_flow,
    impermanence_corrected_rpe,
    planetary_heat_budget_occupancy,
    policy_selection,
    precision_weighted_update,
    reward_prediction_error,
    sigmoid,
    social_awareness_bandwidth,
    softmax,
    wu_wei_threshold,
)


def test_expected_free_energy_is_kl_minus_preference():
    assert expected_free_energy(0.5, 0.2) == pytest.approx(0.3)


def test_policy_selection_is_normalized():
    probs = policy_selection(np.array([1.0, 2.0, 3.0]))
    assert pytest.approx(probs.sum()) == 1.0
    assert np.all(probs > 0)


def test_policy_selection_prefers_lower_free_energy():
    probs = policy_selection(np.array([3.0, 1.0]))
    assert probs[1] > probs[0]


def test_dao_gradient_step_descends():
    theta = np.array([1.0, 2.0])
    grad = np.array([0.5, -0.5])
    updated = dao_gradient_step(theta, grad, eta=0.1)
    np.testing.assert_allclose(updated, theta - 0.1 * grad)


def test_gradient_flow_calls_grad_func():
    theta = np.array([1.0, 2.0])
    grad = np.array([0.1, 0.2])
    updated = gradient_flow(theta, lambda x: grad, learning_rate=0.5)
    np.testing.assert_allclose(updated, theta - 0.5 * grad)


def test_awareness_bandwidth_bounds():
    assert awareness_bandwidth(0.5, 0.5, 1.5) == pytest.approx(1.0)
    assert awareness_bandwidth(1.5, 0.5, 1.5) == pytest.approx(0.0)
    assert 0.0 <= awareness_bandwidth(1.0, 0.5, 1.5) <= 1.0


def test_awareness_bandwidth_invalid_range_raises():
    with pytest.raises(ValueError):
        awareness_bandwidth(1.0, 1.0, 1.0)


def test_precision_weighted_update():
    assert precision_weighted_update(0.0, 0.5, 2.0) == pytest.approx(1.0)


def test_cost_of_deviation_is_nonnegative():
    assert cost_of_deviation(1.0, 0.5) == pytest.approx(0.5)
    assert cost_of_deviation(0.5, 1.0) == pytest.approx(0.0)
    assert cost_of_deviation(1.0, 1.0) == pytest.approx(0.0)


def test_de_ming_allocation_sums_to_budget():
    mu = np.array([1.0, 2.0, 0.5])
    sigma = np.array([0.1, 0.2, 0.5])
    allocation = de_ming_allocation(mu, sigma, total_energy=10.0)
    assert pytest.approx(allocation.sum()) == 10.0
    assert np.all(allocation >= 0)
    # Higher mu/sigma ratio → higher allocation
    assert allocation[1] > allocation[0] > allocation[2]


def test_critical_handover_signal_peaks_when_tension_high_and_declining():
    high_declining = critical_handover_signal(tension=0.9, d_tension=-0.5)
    low_rising = critical_handover_signal(tension=0.1, d_tension=0.5)
    assert high_declining > low_rising


def test_planetary_heat_budget_occupancy():
    rho = planetary_heat_budget_occupancy(p_ai_waste=1e13, eta=0.1, p_cooling=1e17)
    assert pytest.approx(rho) == 1e-3


def test_planetary_heat_budget_occupancy_invalid():
    with pytest.raises(ValueError):
        planetary_heat_budget_occupancy(1e13, 0.0, 1e17)


def test_sigmoid_zero():
    assert sigmoid(0.0) == pytest.approx(0.5)


def test_sigmoid_extremes():
    assert sigmoid(-10.0) < 0.01
    assert sigmoid(10.0) > 0.99


def test_generalized_sigmoid_standard():
    """At x=theta, output should be 0.5."""
    assert generalized_sigmoid(0.5, beta=10.0, theta=0.5) == pytest.approx(0.5)


def test_generalized_sigmoid_extremes():
    """Far from theta, output should saturate."""
    assert generalized_sigmoid(-10.0, beta=1.0, theta=0.0) < 0.01
    assert generalized_sigmoid(10.0, beta=1.0, theta=0.0) > 0.99


def test_generalized_sigmoid_array():
    result = generalized_sigmoid(np.array([-10.0, 0.0, 10.0]), beta=1.0, theta=0.0)
    assert result.shape == (3,)
    assert result[1] == pytest.approx(0.5)


def test_softmax_normalized():
    probs = softmax(np.array([1.0, 2.0, 3.0]))
    assert pytest.approx(probs.sum()) == 1.0
    assert np.all(probs > 0)


def test_wu_wei_threshold():
    assert wu_wei_threshold(0.0005, tau=1e-3) is True
    assert wu_wei_threshold(0.002, tau=1e-3) is False


def test_de_precision_matrix():
    pi = de_precision_matrix(3)
    assert pi.shape == (3, 3)
    np.testing.assert_allclose(pi, np.eye(3))


def test_reward_prediction_error():
    assert reward_prediction_error(1.0, 0.5) == pytest.approx(0.5)


def test_impermanence_corrected_rpe():
    assert impermanence_corrected_rpe(1.0, 0.5, kappa=0.0) == pytest.approx(0.5)
    assert impermanence_corrected_rpe(1.0, 0.5, kappa=1.0) == pytest.approx(-0.5)


def test_impermanence_corrected_rpe_invalid_kappa():
    with pytest.raises(ValueError):
        impermanence_corrected_rpe(1.0, 0.5, kappa=1.5)


def test_social_awareness_bandwidth_peak_conditions():
    sab = social_awareness_bandwidth(
        ab=1.0,
        mns=10.0,
        men=10.0,
        ai_shared=10.0,
        dmn_self=-10.0,
    )
    assert sab > 0.9


def test_social_awareness_bandwidth_low_when_self_high():
    sab = social_awareness_bandwidth(
        ab=1.0,
        mns=10.0,
        men=10.0,
        ai_shared=10.0,
        dmn_self=10.0,
    )
    assert sab < 0.1


def test_social_awareness_bandwidth_invalid_weights():
    with pytest.raises(ValueError):
        social_awareness_bandwidth(
            ab=1.0,
            mns=0.0,
            men=0.0,
            ai_shared=0.0,
            dmn_self=0.0,
            weights=(0.5, 0.5, 0.5),
        )
