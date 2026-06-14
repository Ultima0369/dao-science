"""Executable stubs for core formalizations in Project Dao.Science.

Every function corresponds to an equation or definition in `NOTATION.md`
and/or a `verifiable_units/` protocol. They are designed to be:

- Stateless (no module-level globals)
- Typed (PEP 484)
- Cheap to unit-test
- Composable into larger simulations
"""

from __future__ import annotations

import numpy as np
import numpy.typing as npt

FloatArray = npt.NDArray[np.float64]

__all__ = [
    "FloatArray",
    "sigmoid",
    "softmax",
    "expected_free_energy",
    "policy_selection",
    "dao_gradient_step",
    "gradient_flow",
    "awareness_bandwidth",
    "precision_weighted_update",
    "cost_of_deviation",
    "wu_wei_threshold",
    "de_precision_matrix",
    "de_ming_allocation",
    "reward_prediction_error",
    "impermanence_corrected_rpe",
    "social_awareness_bandwidth",
    "critical_handover_signal",
    "planetary_heat_budget_occupancy",
]


def sigmoid(x: float | FloatArray) -> float | FloatArray:
    r"""Logistic sigmoid $\sigma(x) = 1 / (1 + e^{-x})$.

    See `NOTATION.md` and `1_first_principles/01_dao_as_process.md`.
    """
    x_arr = np.asarray(x, dtype=np.float64)
    return 1.0 / (1.0 + np.exp(-x_arr))


def generalized_sigmoid(
    x: float | FloatArray,
    beta: float = 10.0,
    theta: float = 0.5,
) -> float | FloatArray:
    r"""Generalized logistic sigmoid with steepness and threshold.

    ``sigma(x; beta, theta) = 1 / (1 + exp(-beta * (x - theta)))``.

    Args:
        x: Input value(s).
        beta: Steepness parameter (larger = sharper transition).
        theta: Threshold parameter (center of transition).

    Returns:
        Sigmoid activation in (0, 1).
    """
    x_arr = np.asarray(x, dtype=np.float64)
    return 1.0 / (1.0 + np.exp(-beta * (x_arr - theta)))


def softmax(
    x: FloatArray,
    axis: int | None = None,
    beta: float = 1.0,
) -> FloatArray:
    """Numerically stable softmax over an array.

    Equation (13a): `P(pi) = sigma(-gamma * G(pi))`.

    Args:
        x: Input logits or energies.
        axis: Axis along which to compute softmax. Defaults to all elements.
        beta: Inverse temperature; larger values make the distribution sharper.

    Returns:
        Probability distribution summing to 1.
    """
    x_arr = np.asarray(x, dtype=np.float64)
    scaled = beta * x_arr
    shifted = scaled - np.max(scaled, axis=axis, keepdims=True)
    exp_shifted = np.exp(shifted)
    return exp_shifted / np.sum(exp_shifted, axis=axis, keepdims=True)


def expected_free_energy(
    kl_divergence: float,
    expected_log_preference: float,
) -> float:
    """Expected free energy of a policy (EFE).

    See `NOTATION.md` and `1_first_principles/01_dao_as_process.md`.
    A minimal operational form: epistemic cost (KL) minus pragmatic value
    (expected log preference).

    Args:
        kl_divergence: Expected KL divergence under the policy.
        expected_log_preference: Expected log preference over outcomes.

    Returns:
        Scalar expected free energy.
    """
    return float(kl_divergence - expected_log_preference)


def policy_selection(
    free_energies: FloatArray,
    gamma: float = 1.0,
) -> FloatArray:
    """Soft-max policy selection from expected free energies.

    Equation (13a): `P(pi) = sigma(-gamma * G(pi))`.

    Args:
        free_energies: Array of G(pi) for each policy.
        gamma: Inverse-temperature parameter.

    Returns:
        Probability distribution over policies.
    """
    logits = -gamma * np.asarray(free_energies, dtype=np.float64)
    return softmax(logits)


def dao_gradient_step(
    theta: FloatArray,
    grad_g: FloatArray,
    eta: float = 0.01,
) -> FloatArray:
    """One gradient-descent step along the negative gradient of expected free energy.

    Equation (12): `d theta / dt = -eta * nabla_theta G(pi_theta)`.

    Args:
        theta: Current parameter vector.
        grad_g: Gradient of expected free energy w.r.t. theta.
        eta: Learning rate.

    Returns:
        Updated parameter vector.
    """
    return np.asarray(theta, dtype=np.float64) - eta * np.asarray(grad_g, dtype=np.float64)


def gradient_flow(
    theta: FloatArray,
    grad_func,
    learning_rate: float = 0.01,
) -> FloatArray:
    """Higher-level stub: gradient flow on expected free energy.

    Same semantics as `dao_gradient_step`, but accepts a gradient callable
    instead of a pre-computed gradient vector. Useful for chaining in
    simulations and unit tests.

    Args:
        theta: Current parameter vector.
        grad_func: Callable mapping theta -> gradient vector of G.
        learning_rate: Learning rate (eta).

    Returns:
        Updated parameter vector.
    """
    theta_arr = np.asarray(theta, dtype=np.float64)
    return dao_gradient_step(theta_arr, grad_func(theta_arr), eta=learning_rate)


def awareness_bandwidth(
    r_dmn: float,
    r0: float = 0.0,
    rmax: float = 1.0,
) -> float:
    """Normalized awareness bandwidth AB(t).

    Equation in `1_first_principles/02_one_as_bandwidth.md`:
    `AB(t) = 1 - (R_DMN(t) - R_0) / (R_max - R_0)`.

    Args:
        r_dmn: Current DMN activity level.
        r0: Baseline DMN activity.
        rmax: Maximum observed DMN activity.

    Returns:
        Bandwidth in [0, 1].
    """
    denom = rmax - r0
    if denom <= 0:
        raise ValueError("rmax must be greater than r0")
    return float(np.clip(1.0 - (r_dmn - r0) / denom, 0.0, 1.0))


def precision_weighted_update(
    mu: float,
    prediction_error: float,
    precision: float,
) -> float:
    """Single precision-weighted belief update.

    ``mu_new = mu + precision * prediction_error``.
    Higher precision -> larger update for the same PE.

    Args:
        mu: Current belief estimate.
        prediction_error: Sensory prediction error.
        precision: Precision (inverse variance) weight.

    Returns:
        Updated belief estimate.
    """
    return float(mu + precision * prediction_error)


def cost_of_deviation(
    g_actual: float,
    g_optimal: float,
) -> float:
    """Cost of deviating from the optimal policy.

    `1_first_principles/07_cost_of_deviation.md`:
    ``Cost(pi_dev) = G(pi_actual) - G(pi_optimal)``.

    Args:
        g_actual: Expected free energy of the actual policy.
        g_optimal: Expected free energy of the optimal policy.

    Returns:
        Non-negative cost.
    """
    return float(max(0.0, g_actual - g_optimal))


def de_ming_allocation(
    mu: FloatArray,
    sigma: FloatArray,
    total_energy: float = 1.0,
    beta: float = 2.0,
    epsilon: float = 1e-8,
) -> FloatArray:
    """Energy allocation vector from the De-Ming model.

    Equation in `verifiable_units/vu_09_de_ming_energy_allocation.md`:
    ``a_i = E_total * softmax(beta * mu_i / (s_i + epsilon))``.

    Args:
        mu: Estimated reward for each goal.
        sigma: Estimated uncertainty for each goal.
        total_energy: Total energy budget to distribute.
        beta: Exploitation-exploration sharpness.
        epsilon: Small constant to avoid division by zero.

    Returns:
        Energy allocation vector summing to `total_energy`.
    """
    mu_arr = np.asarray(mu, dtype=np.float64)
    sigma_arr = np.asarray(sigma, dtype=np.float64)
    logits = beta * mu_arr / (sigma_arr + epsilon)
    exp_logits = np.exp(logits - np.max(logits))
    weights = exp_logits / np.sum(exp_logits)
    return total_energy * weights


def critical_handover_signal(
    tension: float,
    d_tension: float,
    theta: float = 0.5,
    k: float = 8.0,
) -> float:
    """Critical handover signal h(T, dT/dt) for relational attunement.

    Equation in `verifiable_units/vu_08_relational_attunement_oscillator.md`:
    high when tension is high and declining.

    Args:
        tension: Partner's current tension T.
        d_tension: Time derivative of tension dT/dt.
        theta: Threshold parameter.
        k: Sigmoid steepness.

    Returns:
        Handover probability in (0, 1).
    """
    return float(1.0 / (1.0 + np.exp(-k * (tension * (-d_tension) - theta))))


def planetary_heat_budget_occupancy(
    p_ai_waste: float,
    eta: float,
    p_cooling: float,
) -> float:
    """Planetary Heat-Budget Occupancy (PHBO).

    Equation in `verifiable_units/vu_10_planetary_ai_thermodynamics.md`:
    ``rho_H = P_AI_waste / (eta * P_Earth_cooling)``.

    Args:
        p_ai_waste: Global AI waste-heat power.
        eta: Planetary heat-budget margin coefficient.
        p_cooling: Earth's radiative cooling power.

    Returns:
        Occupancy ratio.
    """
    denom = eta * p_cooling
    if denom <= 0:
        raise ValueError("eta and p_cooling must be positive")
    return float(p_ai_waste / denom)


def wu_wei_threshold(grad_norm: float, tau: float = 1e-3) -> bool:
    """Wu-wei predicate: action when gradient norm is below threshold.

    Equation (14): ``无为 ≡ 行动于 ||∇_θ G(π_θ)|| < τ``.

    Args:
        grad_norm: Norm of the expected-free-energy gradient.
        tau: Small threshold.

    Returns:
        True if the system is in the Wu-wei regime.
    """
    return float(grad_norm) < float(tau)


def de_precision_matrix(dim: int) -> FloatArray:
    """Stub for 德 (De) as the precision matrix of the generative model.

    Equation (15): ``Π_德 ≡ 生成模型的精度矩阵``.

    Returns:
        An identity precision matrix of shape (dim, dim).
    """
    return np.eye(dim, dtype=np.float64)


def reward_prediction_error(actual: float, expected: float) -> float:
    """Reward prediction error (RPE).

    ``δ_RPE = R_actual - R_expected``.
    """
    return float(actual - expected)


def impermanence_corrected_rpe(
    actual: float,
    expected: float,
    kappa: float = 0.0,
) -> float:
    """RPE corrected by impermanence awareness (随缘行).

    ``RPE_suiyuan = R_actual - R_expected - κ * R_actual``.

    Args:
        actual: Actual reward.
        expected: Expected reward.
        kappa: Impermanence awareness coefficient in [0, 1].

    Returns:
        Corrected RPE.
    """
    if not 0.0 <= kappa <= 1.0:
        raise ValueError("kappa must be in [0, 1]")
    return float((1.0 - kappa) * actual - expected)


def social_awareness_bandwidth(
    ab: float,
    mns: float,
    men: float,
    ai_shared: float,
    dmn_self: float,
    weights: tuple[float, float, float] = (1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0),
) -> float:
    """Social Awareness Bandwidth (SAB).

    Equation in `2_models/social_cognition.md`:
    ``SAB(t) = AB(t) * [w_M σ(MNS) + w_E σ(MEN) + w_A σ(AI_shared)] * [1 - σ(DMN_self)]``.

    Args:
        ab: Awareness bandwidth AB(t) in [0, 1].
        mns: Normalized mirror-neuron system activity.
        men: Normalized mentalizing network activity.
        ai_shared: Normalized anterior-insula shared activity.
        dmn_self: Normalized DMN self-referential activity.
        weights: Weights (w_M, w_E, w_A) summing to 1.

    Returns:
        Social awareness bandwidth in [0, 1].
    """
    w_m, w_e, w_a = weights
    if not np.isclose(w_m + w_e + w_a, 1.0):
        raise ValueError("weights must sum to 1")
    social_component = (
        w_m * float(sigmoid(mns))
        + w_e * float(sigmoid(men))
        + w_a * float(sigmoid(ai_shared))
    )
    self_boundary = 1.0 - float(sigmoid(dmn_self))
    return float(np.clip(ab * social_component * self_boundary, 0.0, 1.0))
