#!/usr/bin/env python3
r"""Attention as precision optimization across multiple sensory channels.

This script implements a minimal predictive-coding model of attention:

- The environment emits a scalar state s(t) at each time step.
- N sensory channels provide noisy observations o_i(t) = s(t) + eta_i,
  where eta_i ~ N(0, sigma_i^2).
- The agent allocates attentional precision weights w_i to each channel.
- Under predictive coding, optimal weights are proportional to the inverse
  variance (precision) of each channel: w_i^* \propto 1 / sigma_i^2.
- A meta-parameter alpha in [0, 1] interpolates between:
    * alpha -> 1 (focused): softmax over channel quality -> winner-take-all
    * alpha -> 0 (global): uniform weights -> all channels monitored equally

Run with:
    python simulations/attention_precision_optimization.py

Outputs:
    simulations/attention_static_weights.png
    simulations/attention_alpha_sweep.png
    simulations/attention_dynamic_switching.png
    simulations/attention_pathology.png
"""

from pathlib import Path

import _compat  # noqa: F401  # ensures dao_science is importable
import matplotlib
import numpy as np

from dao_science.core import softmax

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = Path(__file__).parent
RNG = np.random.default_rng(42)


def allocate_weights(precisions: np.ndarray, alpha: float, beta: float = 4.0) -> np.ndarray:
    """Allocate attention weights as a function of alpha.

    alpha -> 1: focused, softmax over channel precisions.
    alpha -> 0: global, uniform weights.
    """
    n = len(precisions)
    quality = precisions  # higher precision = higher quality
    focus_weights = softmax(quality, beta=beta)
    open_weights = np.ones(n) / n
    weights = alpha * focus_weights + (1 - alpha) * open_weights
    return weights / weights.sum()


def bayesian_estimate(observations: np.ndarray, weights: np.ndarray) -> float:
    """Weighted average estimate of the latent state."""
    return float(np.average(observations, weights=weights))


def rmse(estimates: np.ndarray, true_values: np.ndarray) -> float:
    return float(np.sqrt(np.mean((estimates - true_values) ** 2)))


# ---------------------------------------------------------------------------
# 1. Static demonstration: weights for a fixed set of channels
# ---------------------------------------------------------------------------

def run_static_demo() -> None:
    sigmas = np.array([0.5, 1.0, 2.0, 3.0, 5.0])
    precisions = 1.0 / sigmas**2
    optimal_weights = precisions / precisions.sum()

    alphas = [0.0, 0.25, 0.5, 0.75, 1.0]
    weight_curves = [allocate_weights(precisions, a) for a in alphas]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    x = np.arange(len(sigmas)) + 1
    width = 0.12
    for i, (alpha, w) in enumerate(zip(alphas, weight_curves)):
        axes[0].bar(x + i * width - 2 * width, w, width, label=f"α={alpha:.2f}")
    axes[0].set_xticks(x)
    axes[0].set_xticklabels([f"ch{i}\nσ={s:.1f}" for i, s in enumerate(sigmas, start=1)])
    axes[0].set_ylabel("Attention weight $w_i$")
    axes[0].set_title("Precision allocation vs meta-parameter α")
    axes[0].legend()
    axes[0].set_ylim(0, 1.0)

    axes[1].bar(x, optimal_weights, color="#1565c0", alpha=0.7, label=r"Bayes-optimal $w_i \propto 1/\sigma_i^2$")
    axes[1].set_xticks(x)
    axes[1].set_xticklabels([f"ch{i}\nσ={s:.1f}" for i, s in enumerate(sigmas, start=1)])
    axes[1].set_ylabel("Optimal weight")
    axes[1].set_title("Predictive-coding optimum")
    axes[1].legend()
    axes[1].set_ylim(0, 1.0)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "attention_static_weights.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 2. Alpha sweep: estimation error as a function of alpha
# ---------------------------------------------------------------------------

def run_alpha_sweep(n_trials: int = 500) -> None:
    sigmas = np.array([0.5, 1.0, 2.0, 3.0, 5.0])
    precisions = 1.0 / sigmas**2
    alphas = np.linspace(0, 1, 51)

    rmses = []
    for alpha in alphas:
        weights = allocate_weights(precisions, alpha)
        true_states = RNG.normal(0, 1, size=n_trials)
        noise = RNG.normal(0, sigmas, size=(n_trials, len(sigmas)))
        observations = true_states[:, None] + noise
        estimates = np.average(observations, axis=1, weights=weights)
        rmses.append(rmse(estimates, true_states))

    rmses = np.array(rmses)
    optimal_weights = precisions / precisions.sum()
    optimal_noise = RNG.normal(0, sigmas, size=(n_trials, len(sigmas)))
    optimal_estimates = np.average(
        RNG.normal(0, 1, size=n_trials)[:, None] + optimal_noise,
        axis=1,
        weights=optimal_weights,
    )
    optimal_rmse = rmse(optimal_estimates, RNG.normal(0, 1, size=n_trials))

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(alphas, rmses, color="#2e7d32", linewidth=2, label="Actual RMSE")
    ax.axhline(
        optimal_rmse,
        color="#1565c0",
        linestyle="--",
        label="Bayes-optimal RMSE (proportional weights)",
    )
    ax.set_xlabel("Meta-parameter α (1=focused, 0=global)")
    ax.set_ylabel("Root-mean-square error (RMSE)")
    ax.set_title("Estimation accuracy vs attention mode")
    ax.legend()
    ax.set_xlim(0, 1)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "attention_alpha_sweep.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 3. Dynamic switching: environment reliability changes over time
# ---------------------------------------------------------------------------

def run_dynamic_switching(n_steps: int = 400) -> None:
    sigmas = np.array([0.5, 1.0, 2.0, 3.0, 5.0])
    precisions = 1.0 / sigmas**2

    # True state random walk
    true_states = np.cumsum(RNG.normal(0, 0.1, size=n_steps))

    # Observation noise
    noise = RNG.normal(0, sigmas, size=(n_steps, len(sigmas)))
    observations = true_states[:, None] + noise

    # Reliability schedule: channels swap quality at step 200
    reliability_phase = np.ones((n_steps, len(sigmas)))
    reliability_phase[:200, :] = 1.0
    reliability_phase[200:, :] = np.array([5.0, 3.0, 2.0, 1.0, 0.5])  # reversed quality

    # Static alpha agents
    alpha_focused = 1.0
    alpha_global = 0.0
    alpha_adaptive = 0.5

    est_focused = np.zeros(n_steps)
    est_global = np.zeros(n_steps)
    est_adaptive = np.zeros(n_steps)

    for t in range(n_steps):
        eff_precisions = precisions * reliability_phase[t]
        w_focused = allocate_weights(eff_precisions, alpha_focused)
        w_global = allocate_weights(eff_precisions, alpha_global)
        w_adaptive = allocate_weights(eff_precisions, alpha_adaptive)

        est_focused[t] = bayesian_estimate(observations[t], w_focused)
        est_global[t] = bayesian_estimate(observations[t], w_global)
        est_adaptive[t] = bayesian_estimate(observations[t], w_adaptive)

    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    axes[0].plot(true_states, color="black", linewidth=2, label="True state")
    axes[0].plot(est_focused, color="#c62828", alpha=0.7, label=f"Focused α={alpha_focused}")
    axes[0].plot(est_global, color="#1565c0", alpha=0.7, label=f"Global α={alpha_global}")
    axes[0].plot(est_adaptive, color="#2e7d32", alpha=0.7, label=f"Adaptive α={alpha_adaptive}")
    axes[0].axvline(200, color="gray", linestyle="--", alpha=0.5)
    axes[0].set_ylabel("State estimate")
    axes[0].set_title("Tracking a state with changing channel reliability")
    axes[0].legend(loc="upper left")

    rmse_focused = rmse(est_focused, true_states)
    rmse_global = rmse(est_global, true_states)
    rmse_adaptive = rmse(est_adaptive, true_states)

    axes[1].bar(
        ["Focused (α=1)", "Global (α=0)", "Adaptive (α=0.5)"],
        [rmse_focused, rmse_global, rmse_adaptive],
        color=["#c62828", "#1565c0", "#2e7d32"],
    )
    axes[1].set_ylabel("RMSE")
    axes[1].set_title("Overall estimation error")
    axes[1].tick_params(axis="x", rotation=15)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "attention_dynamic_switching.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 4. Pathology: rigid alpha unable to recover from attention hijack
# ---------------------------------------------------------------------------

def run_pathology_demo(n_steps: int = 300) -> None:
    sigmas = np.array([0.5, 1.0, 2.0, 3.0, 5.0])
    precisions = 1.0 / sigmas**2
    true_states = np.cumsum(RNG.normal(0, 0.1, size=n_steps))
    noise = RNG.normal(0, sigmas, size=(n_steps, len(sigmas)))
    observations = true_states[:, None] + noise

    # Channel 1 (low noise) gets a large transient outlier at t=100..120
    observations[100:120, 0] += 6.0

    # Rigid high-alpha: locks onto channel 1 even after outlier
    # Rigid low-alpha: spreads attention uniformly
    # Flexible: can down-weight channel 1 after detecting anomaly
    est_rigid_focus = np.zeros(n_steps)
    est_rigid_open = np.zeros(n_steps)
    est_flexible = np.zeros(n_steps)

    # Running estimate of each channel precision (inverse variance of recent PE)
    window = 20
    pe_memory = np.zeros((window, len(sigmas)))

    for t in range(n_steps):
        w_rigid_focus = allocate_weights(precisions, alpha=1.0)
        w_rigid_open = allocate_weights(precisions, alpha=0.0)

        # Flexible: estimate recent precision from prediction errors
        if t == 0:
            adaptive_precisions = precisions.copy()
        else:
            # Recent prediction error for each channel vs previous flexible estimate
            recent_pe = observations[max(0, t - window):t] - est_flexible[max(0, t - window):t, None]
            if len(recent_pe) > 1:
                var = np.var(recent_pe, axis=0) + 1e-6
                adaptive_precisions = 1.0 / var
            else:
                adaptive_precisions = precisions.copy()
        w_flexible = allocate_weights(adaptive_precisions, alpha=0.7)

        est_rigid_focus[t] = bayesian_estimate(observations[t], w_rigid_focus)
        est_rigid_open[t] = bayesian_estimate(observations[t], w_rigid_open)
        est_flexible[t] = bayesian_estimate(observations[t], w_flexible)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(true_states, color="black", linewidth=2, label="True state")
    ax.plot(est_rigid_focus, color="#c62828", alpha=0.7, label="Rigid focus (α=1, hijacked)")
    ax.plot(est_rigid_open, color="#1565c0", alpha=0.7, label="Rigid open (α=0, noisy)")
    ax.plot(est_flexible, color="#2e7d32", linewidth=2, label="Flexible precision (recovers)")
    ax.axvspan(100, 120, color="gray", alpha=0.2, label="Channel 1 outlier")
    ax.set_xlabel("Time step")
    ax.set_ylabel("State estimate")
    ax.set_title("Attention hijack and recovery")
    ax.legend(loc="upper left")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "attention_pathology.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Running static attention allocation demo...")
    run_static_demo()

    print("Running alpha sweep...")
    run_alpha_sweep(n_trials=1000)

    print("Running dynamic switching demo...")
    run_dynamic_switching(n_steps=400)

    print("Running pathology demo...")
    run_pathology_demo(n_steps=300)

    print(f"Figures saved to {OUT_DIR}")


if __name__ == "__main__":
    main()
