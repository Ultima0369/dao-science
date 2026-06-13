#!/usr/bin/env python3
"""De-Ming energy allocation model.

"De" is formalized as the attentional-energy allocation that minimizes expected
free energy across multiple goals. "Ming" is the penetrating awareness that
updates the agent's model of which goals are rewarding (yang/variables) and
which are stable (yin/constants), and re-allocates energy accordingly.

This simulation compares four agent types:

1. De-Ming agent:    allocates energy by expected reward / uncertainty and
                     updates beliefs via prediction-error feedback.
2. Dogmatic agent:   fixes an allocation based on initial beliefs and never
                     updates (false Ming).
3. Random agent:     allocates energy uniformly at random.
4. Greedy agent:     allocates all energy to the currently estimated best goal.

Run with:
    python simulations/de_ming_energy_allocation.py

Outputs:
    simulations/de_ming_allocation_trajectory.png
    simulations/de_ming_cumulative_regret.png
    simulations/de_ming_change_detection.png
"""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = Path(__file__).parent
RNG = np.random.default_rng(42)


# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

class Environment:
    """Task rewards and uncertainties that may change over time."""

    def __init__(self, n_tasks: int = 4, total_steps: int = 200):
        self.n_tasks = n_tasks
        self.total_steps = total_steps
        self.rewards = np.zeros((total_steps, n_tasks))
        self.uncertainties = np.zeros((total_steps, n_tasks))

        # Phase 1: tasks 0 and 1 are good, tasks 2 and 3 are poor
        self.rewards[:100, :] = [0.8, 0.7, 0.2, 0.1]
        self.uncertainties[:100, :] = [0.15, 0.20, 0.10, 0.10]

        # Phase 2: abrupt reversal — tasks 2 and 3 become good
        self.rewards[100:, :] = [0.2, 0.1, 0.8, 0.7]
        self.uncertainties[100:, :] = [0.10, 0.10, 0.15, 0.20]

    def sample(self, t: int, allocation: np.ndarray) -> np.ndarray:
        """Sample outcomes given energy allocation to each task."""
        # More energy → lower effective observation noise
        effective_sigma = self.uncertainties[t] / np.sqrt(allocation + 0.01)
        return RNG.normal(self.rewards[t], effective_sigma)


# ---------------------------------------------------------------------------
# Agents
# ---------------------------------------------------------------------------

class Agent:
    """Base class with belief update and allocation."""

    def __init__(self, n_tasks: int, total_energy: float = 1.0):
        self.n_tasks = n_tasks
        self.total_energy = total_energy
        self.mu = np.ones(n_tasks) * 0.5  # estimated reward
        self.sigma = np.ones(n_tasks) * 0.5  # estimated uncertainty
        self.allocations = []
        self.rewards_seen = []
        self.regrets = []
        self.free_energies = []

    def allocate(self, t: int) -> np.ndarray:
        raise NotImplementedError

    def update(self, t: int, outcome: np.ndarray, env: "Environment") -> None:
        raise NotImplementedError

    def record(self, t: int, allocation: np.ndarray, outcome: np.ndarray, env: "Environment") -> None:
        optimal_reward = env.rewards[t].max() * self.total_energy
        actual_reward = np.sum(allocation * env.rewards[t])

        # Switching cost: changing allocation is metabolically/attentionally expensive
        if len(self.allocations) > 0:
            switch_cost = 0.3 * np.sum(np.abs(allocation - self.allocations[-1]))
            actual_reward -= switch_cost

        self.regrets.append(optimal_reward - actual_reward)

        # Free-energy proxy: negative log-likelihood under current beliefs
        fe = 0.5 * np.sum(
            np.log(2 * np.pi * self.sigma**2)
            + ((outcome - self.mu) ** 2) / (self.sigma**2 + 1e-6)
        )
        self.free_energies.append(fe)
        self.allocations.append(allocation.copy())
        self.rewards_seen.append(outcome.copy())


class DeMingAgent(Agent):
    """De = energy allocation by expected reward / uncertainty.
    Ming = Bayesian-like update with surprise-driven change detection."""

    def __init__(self, n_tasks: int, total_energy: float = 1.0, beta: float = 2.0):
        super().__init__(n_tasks, total_energy)
        self.beta = beta
        self.learning_rate = 0.2
        self.surprise_threshold = 2.0
        self.change_detected = []

    def allocate(self, t: int) -> np.ndarray:
        # De: allocate by signal-to-uncertainty ratio
        score = self.mu / (self.sigma + 0.05)
        weights = np.exp(self.beta * score)
        weights /= weights.sum()
        return self.total_energy * weights

    def update(self, t: int, outcome: np.ndarray, env: "Environment") -> None:
        prediction_error = np.abs(outcome - self.mu)
        surprise = prediction_error > self.surprise_threshold * self.sigma
        self.change_detected.append(int(surprise.sum()))

        # Ming: adapt learning rate and uncertainty on surprise
        lr = np.where(surprise, 0.6, self.learning_rate)
        self.mu = self.mu + lr * (outcome - self.mu)

        # Uncertainty update: inflate on surprise, otherwise smooth
        new_sigma_sq = (1 - lr) * self.sigma**2 + lr * prediction_error**2
        new_sigma_sq = np.where(surprise, new_sigma_sq * 2.0, new_sigma_sq)
        self.sigma = np.sqrt(np.clip(new_sigma_sq, 0.01, 2.0))


class DogmaticAgent(Agent):
    """Fixes allocation based on initial-phase beliefs; never updates (false Ming)."""

    def __init__(self, n_tasks: int, total_energy: float = 1.0):
        super().__init__(n_tasks, total_energy)
        # Dogmatic De: encode the (initially correct) belief that tasks 0,1 are best.
        self.fixed_allocation = self.total_energy * np.array([0.45, 0.40, 0.10, 0.05])

    def allocate(self, t: int) -> np.ndarray:
        return self.fixed_allocation.copy()

    def update(self, t: int, outcome: np.ndarray, env: "Environment") -> None:
        self.change_detected = []  # no change detection
        pass


class RandomAgent(Agent):
    """Random allocation."""

    def allocate(self, t: int) -> np.ndarray:
        w = RNG.random(self.n_tasks)
        return self.total_energy * w / w.sum()

    def update(self, t: int, outcome: np.ndarray, env: "Environment") -> None:
        pass


class StubbornAgent(Agent):
    """Always allocate all energy to task 0 and never update.

    Represents egoic fixation: a false Ming that cannot recognize change.
    """

    def allocate(self, t: int) -> np.ndarray:
        a = np.zeros(self.n_tasks)
        a[0] = self.total_energy
        return a

    def update(self, t: int, outcome: np.ndarray, env: "Environment") -> None:
        pass


# ---------------------------------------------------------------------------
# Simulation runner
# ---------------------------------------------------------------------------

def run_agent(agent: Agent, env: Environment) -> None:
    for t in range(env.total_steps):
        allocation = agent.allocate(t)
        outcome = env.sample(t, allocation)
        agent.update(t, outcome, env)
        agent.record(t, allocation, outcome, env)


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------

def plot_allocations(agents: dict, env: Environment) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True, sharey=True)
    axes = axes.flatten()
    colors = ["#c62828", "#1565c0", "#2e7d32", "#f9a825"]

    for idx, (name, agent) in enumerate(agents.items()):
        ax = axes[idx]
        allocations = np.array(agent.allocations)
        for i in range(env.n_tasks):
            ax.plot(allocations[:, i], label=f"Task {i}", color=colors[i])
        ax.axvline(100, color="gray", linestyle="--", alpha=0.5, label="Environment change")
        ax.set_ylabel("Energy allocation")
        ax.set_title(name)
        ax.set_ylim(0, 1.0)
        ax.grid(True, alpha=0.3)
        ax.legend(loc="upper right", fontsize=8)

    axes[-1].set_xlabel("Time step")
    axes[-2].set_xlabel("Time step")
    fig.suptitle("Energy allocation trajectories", fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "de_ming_allocation_trajectory.png", dpi=150)
    plt.close(fig)


def plot_regret(agents: dict, env: Environment) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    for name, agent in agents.items():
        cum_regret = np.cumsum(agent.regrets)
        axes[0].plot(cum_regret, label=name, linewidth=2)
    axes[0].axvline(100, color="gray", linestyle="--", alpha=0.5)
    axes[0].set_xlabel("Time step")
    axes[0].set_ylabel("Cumulative regret")
    axes[0].set_title("Cumulative regret (lower is better)")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    for name, agent in agents.items():
        cum_fe = np.cumsum(agent.free_energies)
        axes[1].plot(cum_fe, label=name, linewidth=2)
    axes[1].axvline(100, color="gray", linestyle="--", alpha=0.5)
    axes[1].set_xlabel("Time step")
    axes[1].set_ylabel("Cumulative free-energy proxy")
    axes[1].set_title("Belief-model fit (lower is better)")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "de_ming_cumulative_regret.png", dpi=150)
    plt.close(fig)


def plot_change_detection(agents: dict, env: Environment) -> None:
    fig, ax = plt.subplots(figsize=(10, 4))

    deming = agents["De-Ming"]
    detected = np.array(deming.change_detected)
    ax.plot(detected, color="#c62828", drawstyle="steps-post", linewidth=2)
    ax.axvline(100, color="gray", linestyle="--", alpha=0.5, label="Environment change")
    ax.set_xlabel("Time step")
    ax.set_ylabel("Number of tasks flagged as surprising")
    ax.set_title("Ming: surprise-driven change detection in De-Ming agent")
    ax.set_ylim(-0.1, env.n_tasks + 0.1)
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "de_ming_change_detection.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    env = Environment(n_tasks=4, total_steps=200)

    agents = {
        "De-Ming": DeMingAgent(n_tasks=4),
        "Dogmatic": DogmaticAgent(n_tasks=4),
        "Random": RandomAgent(n_tasks=4),
        "Stubborn": StubbornAgent(n_tasks=4),
    }

    for name, agent in agents.items():
        print(f"Running {name} agent...")
        run_agent(agent, env)

    print("\nFinal cumulative regret:")
    for name, agent in agents.items():
        print(f"  {name:10s}: {np.sum(agent.regrets):.2f}")

    print("\nFinal cumulative free-energy proxy:")
    for name, agent in agents.items():
        print(f"  {name:10s}: {np.sum(agent.free_energies):.2f}")

    print("Plotting allocation trajectories...")
    plot_allocations(agents, env)

    print("Plotting regret...")
    plot_regret(agents, env)

    print("Plotting change detection...")
    plot_change_detection(agents, env)

    print(f"Figures saved to {OUT_DIR}")


if __name__ == "__main__":
    main()
