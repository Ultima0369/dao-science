#!/usr/bin/env python3
"""Simulation of an AI "knowing when to stop" protocol.

This script implements a minimal active-inference model of an AI safety stop
mechanism. The agent faces a sequence of decision problems. Each candidate
policy pi has:

- Expected reward E[r | pi]
- Expected risk / ambiguity (probability or magnitude of catastrophic outcome)
- Expected free energy G(pi) = -expected reward + lambda * expected risk

Two decision modes are compared:

1. Greedy: always choose argmax E[r | pi]. No stop mechanism.
2. Stopping: if the best available policy has G(pi) > threshold, or if any
   policy has catastrophic risk above a separate threshold, the agent stops
   and requests human judgment.

Run with:
    python simulations/ai_stopping_protocol.py

Outputs:
    simulations/ai_stop_decision_boundary.png
    simulations/ai_stop_trajectory.png
    simulations/ai_stop_comparison.png
"""

from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = Path(__file__).parent
RNG = np.random.default_rng(42)


class DecisionProblem:
    """A single decision problem with multiple candidate policies."""

    def __init__(self, n_policies: int = 5):
        self.n_policies = n_policies
        # Expected reward in [0, 1]
        self.rewards = RNG.beta(2, 2, size=n_policies)
        # Catastrophic risk probability (low on average, occasional spikes)
        self.risks = RNG.beta(1.5, 12, size=n_policies)
        # Ambiguity / outcome entropy in [0, 1]
        self.ambiguity = RNG.beta(2, 8, size=n_policies)

    def expected_free_energy(self, lambda_risk: float = 3.0, lambda_ambiguity: float = 1.0) -> np.ndarray:
        """G(pi) = -reward + lambda_risk * risk + lambda_ambiguity * ambiguity."""
        return -self.rewards + lambda_risk * self.risks + lambda_ambiguity * self.ambiguity


def greedy_choice(problem: DecisionProblem) -> int:
    """Choose policy with highest expected reward."""
    return int(np.argmax(problem.rewards))


def stopping_choice(
    problem: DecisionProblem,
    g_threshold: float = 0.5,
    risk_threshold: float = 0.15,
    lambda_risk: float = 3.0,
    lambda_ambiguity: float = 1.0,
) -> tuple[int, bool]:
    """Choose policy, but stop if no safe-enough policy exists.

    Returns:
        policy_index, stopped
    """
    g = problem.expected_free_energy(lambda_risk, lambda_ambiguity)
    min_g = g.min()
    max_risk = problem.risks.max()

    # Stop if even the best policy is too costly, or if any policy is catastrophically risky
    if min_g > g_threshold or max_risk > risk_threshold:
        return -1, True

    # Otherwise pick the policy with minimum expected free energy
    return int(np.argmin(g)), False


def simulate_episode(
    n_problems: int = 200,
    g_threshold: float = 0.5,
    risk_threshold: float = 0.22,
    lambda_risk: float = 3.0,
    lambda_ambiguity: float = 1.0,
) -> tuple[dict, dict]:
    """Run one episode with greedy vs stopping agents."""
    greedy = {"rewards": [], "catastrophes": 0, "stops": 0}
    stopping = {"rewards": [], "catastrophes": 0, "stops": 0}

    for _ in range(n_problems):
        problem = DecisionProblem()

        # Greedy agent
        g_idx = greedy_choice(problem)
        greedy["rewards"].append(problem.rewards[g_idx])
        if RNG.random() < problem.risks[g_idx]:
            greedy["catastrophes"] += 1

        # Stopping agent
        s_idx, stopped = stopping_choice(
            problem,
            g_threshold=g_threshold,
            risk_threshold=risk_threshold,
            lambda_risk=lambda_risk,
            lambda_ambiguity=lambda_ambiguity,
        )
        if stopped:
            stopping["stops"] += 1
            # Human intervention: safe but moderate reward
            stopping["rewards"].append(0.4)
        else:
            stopping["rewards"].append(problem.rewards[s_idx])
            if RNG.random() < problem.risks[s_idx]:
                stopping["catastrophes"] += 1

    greedy["total_reward"] = sum(greedy["rewards"])
    stopping["total_reward"] = sum(stopping["rewards"])
    return greedy, stopping


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------

def plot_decision_boundary(lambda_risk: float = 3.0, lambda_ambiguity: float = 1.0) -> None:
    """Plot the stop/no-stop boundary in reward-risk space."""
    rewards = np.linspace(0, 1, 200)
    risks = np.linspace(0, 0.5, 200)
    R, Ri = np.meshgrid(rewards, risks)
    G = -R + lambda_risk * Ri + lambda_ambiguity * 0.3  # fixed ambiguity

    g_threshold = 0.5
    risk_threshold = 0.22

    fig, ax = plt.subplots(figsize=(7, 6))
    contour = ax.contourf(R, Ri, G, levels=20, cmap="RdYlGn_r", alpha=0.7)
    ax.contour(R, Ri, G, levels=[g_threshold], colors="black", linewidths=2, linestyles="--")
    ax.axhline(risk_threshold, color="red", linestyle="--", linewidth=2, label="Risk threshold")

    # Shade stop region
    stop_region = (G > g_threshold) | (Ri > risk_threshold)
    ax.contourf(R, Ri, stop_region.astype(float), levels=[0.5, 1.5], colors=["gray"], alpha=0.2)

    ax.set_xlabel("Expected reward $E[r \\mid \\pi]$")
    ax.set_ylabel("Catastrophic risk $P(\\mathrm{catastrophe} \\mid \\pi)$")
    ax.set_title("Stopping boundary in reward-risk space")
    fig.colorbar(contour, ax=ax, label="Expected free energy $G(\\pi)$")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT_DIR / "ai_stop_decision_boundary.png", dpi=150)
    plt.close(fig)


def plot_trajectory(n_problems: int = 100) -> None:
    """Plot a sample trajectory of greedy vs stopping agent."""
    g_threshold = 0.5
    risk_threshold = 0.22

    greedy_rewards = []
    stopping_rewards = []
    stop_events = []
    catastrophe_events_greedy = []
    catastrophe_events_stopping = []

    for t in range(n_problems):
        problem = DecisionProblem()

        g_idx = greedy_choice(problem)
        greedy_rewards.append(problem.rewards[g_idx])
        if RNG.random() < problem.risks[g_idx]:
            catastrophe_events_greedy.append(t)

        s_idx, stopped = stopping_choice(problem, g_threshold, risk_threshold)
        if stopped:
            stopping_rewards.append(0.4)
            stop_events.append(t)
        else:
            stopping_rewards.append(problem.rewards[s_idx])
            if RNG.random() < problem.risks[s_idx]:
                catastrophe_events_stopping.append(t)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(greedy_rewards, color="#c62828", alpha=0.7, label="Greedy reward")
    ax.plot(stopping_rewards, color="#2e7d32", alpha=0.7, label="Stopping reward")
    for t in stop_events:
        ax.axvline(t, color="blue", alpha=0.1, linewidth=0.5)
    ax.scatter(
        catastrophe_events_greedy,
        [0.05] * len(catastrophe_events_greedy),
        color="#c62828",
        marker="x",
        s=50,
        label=f"Greedy catastrophes ({len(catastrophe_events_greedy)})",
    )
    ax.scatter(
        catastrophe_events_stopping,
        [0.0] * len(catastrophe_events_stopping),
        color="#2e7d32",
        marker="o",
        s=50,
        label=f"Stopping catastrophes ({len(catastrophe_events_stopping)})",
    )
    ax.set_xlabel("Decision problem")
    ax.set_ylabel("Reward")
    ax.set_title("Sample trajectory: greedy vs stopping agent")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT_DIR / "ai_stop_trajectory.png", dpi=150)
    plt.close(fig)


def plot_comparison(n_problems: int = 500, n_runs: int = 50) -> None:
    """Compare greedy vs stopping across multiple runs."""
    g_threshold = 0.5
    risk_threshold = 0.22

    greedy_rewards = []
    stopping_rewards = []
    greedy_catastrophes = []
    stopping_catastrophes = []
    stopping_stops = []

    for _ in range(n_runs):
        g, s = simulate_episode(
            n_problems=n_problems,
            g_threshold=g_threshold,
            risk_threshold=risk_threshold,
        )
        greedy_rewards.append(g["total_reward"])
        stopping_rewards.append(s["total_reward"])
        greedy_catastrophes.append(g["catastrophes"])
        stopping_catastrophes.append(s["catastrophes"])
        stopping_stops.append(s["stops"])

    fig, axes = plt.subplots(1, 3, figsize=(14, 5))

    axes[0].bar(
        ["Greedy", "Stopping"],
        [np.mean(greedy_rewards), np.mean(stopping_rewards)],
        yerr=[np.std(greedy_rewards), np.std(stopping_rewards)],
        color=["#c62828", "#2e7d32"],
        capsize=5,
    )
    axes[0].set_ylabel("Total reward")
    axes[0].set_title("Cumulative reward")

    axes[1].bar(
        ["Greedy", "Stopping"],
        [np.mean(greedy_catastrophes), np.mean(stopping_catastrophes)],
        yerr=[np.std(greedy_catastrophes), np.std(stopping_catastrophes)],
        color=["#c62828", "#2e7d32"],
        capsize=5,
    )
    axes[1].set_ylabel("Catastrophe count")
    axes[1].set_title("Catastrophes over {} problems".format(n_problems))

    axes[2].hist(stopping_stops, bins=15, color="#1565c0", alpha=0.7, edgecolor="black")
    axes[2].set_xlabel("Number of stops")
    axes[2].set_ylabel("Frequency")
    axes[2].set_title("Stopping frequency distribution")

    fig.suptitle("AI stopping protocol: safety-reward trade-off", fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "ai_stop_comparison.png", dpi=150)
    plt.close(fig)

    print(f"Greedy mean reward: {np.mean(greedy_rewards):.2f} ± {np.std(greedy_rewards):.2f}")
    print(f"Stopping mean reward: {np.mean(stopping_rewards):.2f} ± {np.std(stopping_rewards):.2f}")
    print(f"Greedy mean catastrophes: {np.mean(greedy_catastrophes):.2f} ± {np.std(greedy_catastrophes):.2f}")
    print(f"Stopping mean catastrophes: {np.mean(stopping_catastrophes):.2f} ± {np.std(stopping_catastrophes):.2f}")
    print(f"Mean stops per episode: {np.mean(stopping_stops):.1f}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Plotting decision boundary...")
    plot_decision_boundary()

    print("Plotting sample trajectory...")
    plot_trajectory()

    print("Running Monte Carlo comparison...")
    plot_comparison()

    print(f"Figures saved to {OUT_DIR}")


if __name__ == "__main__":
    main()
