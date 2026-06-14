"""Project Dao.Science - executable formalization stubs.

This package provides runnable Python stubs for the mathematical objects
defined in `NOTATION.md`. Each function is intentionally minimal: it
implements the core computation so that `verifiable_units/` can import and
compose them, while full simulations remain in `simulations/`.
"""

from dao_science.core import (
    awareness_bandwidth,
    cost_of_deviation,
    critical_handover_signal,
    dao_gradient_step,
    de_ming_allocation,
    de_precision_matrix,
    expected_free_energy,
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

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "awareness_bandwidth",
    "cost_of_deviation",
    "critical_handover_signal",
    "dao_gradient_step",
    "de_ming_allocation",
    "de_precision_matrix",
    "expected_free_energy",
    "gradient_flow",
    "impermanence_corrected_rpe",
    "planetary_heat_budget_occupancy",
    "policy_selection",
    "precision_weighted_update",
    "reward_prediction_error",
    "sigmoid",
    "social_awareness_bandwidth",
    "softmax",
    "wu_wei_threshold",
]
