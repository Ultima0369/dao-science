#!/usr/bin/env python3
"""Simulation of carbon-silicon task allocation and niche complementarity.

This script models tasks as points in a 2D skill space:

- x-axis: first-person / embodied / social intelligence requirement (carbon strength)
- y-axis: symbolic / logical / scalable processing requirement (silicon strength)

Two agents are compared:

- Carbon agent: efficient at high-x tasks, inefficient at high-y tasks
- Silicon agent: efficient at high-y tasks, inefficient at high-x tasks

Four allocation strategies are compared:

1. Carbon-only: all tasks done by carbon
2. Silicon-only: all tasks done by silicon
3. Random split: tasks assigned randomly
4. Niche-complementary split: each task assigned to the agent with lower cost

The simulation demonstrates that carbon-silicon symbiosis outperforms either
agent working alone, especially when the task distribution spans both skill
dimensions.

Run with:
    python simulations/carbon_silicon_symbiosis.py

Outputs:
    simulations/carbon_silicon_cost_surface.png
    simulations/carbon_silicon_task_allocation.png
    simulations/carbon_silicon_strategy_comparison.png
    simulations/carbon_silicon_l3_interpretation.png
    simulations/carbon_silicon_heat_tradeoff.png
"""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = Path(__file__).parent
RNG = np.random.default_rng(42)


# ---------------------------------------------------------------------------
# Agent cost functions
# ---------------------------------------------------------------------------

def carbon_cost(x: float, y: float) -> float:
    """Carbon cost: low for embodied/social tasks, high for symbolic/scale tasks."""
    return 0.3 * x + 1.8 * y + 0.2


def silicon_cost(x: float, y: float) -> float:
    """Silicon cost: low for symbolic/scale tasks, high for embodied/social tasks."""
    return 1.7 * x + 0.3 * y + 0.2


def carbon_heat(x: float, y: float) -> float:
    """Carbon heat cost: low for embodied, moderate for symbolic."""
    return 0.2 * x + 0.6 * y


def silicon_heat(x: float, y: float) -> float:
    """Silicon heat cost: high for embodied, low for symbolic."""
    return 0.8 * x + 0.3 * y


def total_cost_with_heat(
    x: np.ndarray,
    y: np.ndarray,
    assignment: np.ndarray,
    lambda_heat: float = 0.0,
) -> float:
    """Total cost including cognitive and thermodynamic (heat) costs."""
    c_total = carbon_cost(x, y) + lambda_heat * carbon_heat(x, y)
    s_total = silicon_cost(x, y) + lambda_heat * silicon_heat(x, y)
    cost = np.where(assignment == 0, c_total, s_total)
    return float(cost.sum())


def allocate_niche_complementary_with_heat(
    x: np.ndarray, y: np.ndarray, lambda_heat: float = 0.0
) -> np.ndarray:
    """Assign each task to the agent with lower total (cognitive + heat) cost."""
    c_total = carbon_cost(x, y) + lambda_heat * carbon_heat(x, y)
    s_total = silicon_cost(x, y) + lambda_heat * silicon_heat(x, y)
    return (s_total < c_total).astype(int)


# ---------------------------------------------------------------------------
# Task generation
# ---------------------------------------------------------------------------

def generate_tasks(n: int = 200) -> tuple[np.ndarray, np.ndarray]:
    """Generate task requirements in [0, 1]^2 with some correlation."""
    mean = [0.5, 0.5]
    cov = [[0.08, -0.03], [-0.03, 0.08]]
    tasks = RNG.multivariate_normal(mean, cov, size=n)
    tasks = np.clip(tasks, 0, 1)
    return tasks[:, 0], tasks[:, 1]


# ---------------------------------------------------------------------------
# Allocation strategies
# ---------------------------------------------------------------------------

def total_cost(x: np.ndarray, y: np.ndarray, assignment: np.ndarray) -> float:
    """assignment[i] = 0 for carbon, 1 for silicon."""
    c_cost = carbon_cost(x, y)
    s_cost = silicon_cost(x, y)
    cost = np.where(assignment == 0, c_cost, s_cost)
    return float(cost.sum())


def allocate_carbon_only(n: int) -> np.ndarray:
    return np.zeros(n, dtype=int)


def allocate_silicon_only(n: int) -> np.ndarray:
    return np.ones(n, dtype=int)


def allocate_random(n: int) -> np.ndarray:
    return RNG.integers(0, 2, size=n)


def allocate_niche_complementary(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Assign each task to the agent with lower cost."""
    c_cost = carbon_cost(x, y)
    s_cost = silicon_cost(x, y)
    return (s_cost < c_cost).astype(int)


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------

def plot_cost_surface() -> None:
    """Show carbon vs silicon cost over the skill space."""
    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)

    C = carbon_cost(X, Y)
    S = silicon_cost(X, Y)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    im0 = axes[0].contourf(X, Y, C, levels=20, cmap="YlOrRd")
    axes[0].set_title("Carbon cost")
    axes[0].set_xlabel("First-person / embodied need")
    axes[0].set_ylabel("Symbolic / scalable need")
    fig.colorbar(im0, ax=axes[0])

    im1 = axes[1].contourf(X, Y, S, levels=20, cmap="YlGnBu")
    axes[1].set_title("Silicon cost")
    axes[1].set_xlabel("First-person / embodied need")
    axes[1].set_ylabel("Symbolic / scalable need")
    fig.colorbar(im1, ax=axes[1])

    advantage = C - S  # positive: silicon cheaper; negative: carbon cheaper
    im2 = axes[2].contourf(X, Y, advantage, levels=20, cmap="RdYlGn", alpha=0.8)
    axes[2].contour(X, Y, advantage, levels=[0], colors="black", linewidths=2)
    axes[2].set_title("Comparative advantage\n(positive = silicon cheaper)")
    axes[2].set_xlabel("First-person / embodied need")
    axes[2].set_ylabel("Symbolic / scalable need")
    fig.colorbar(im2, ax=axes[2])

    fig.tight_layout()
    fig.savefig(OUT_DIR / "carbon_silicon_cost_surface.png", dpi=150)
    plt.close(fig)


def plot_task_allocation(x: np.ndarray, y: np.ndarray) -> None:
    """Show tasks colored by optimal allocation."""
    assignment = allocate_niche_complementary(x, y)

    fig, ax = plt.subplots(figsize=(7, 7))
    scatter = ax.scatter(
        x,
        y,
        c=assignment,
        cmap="RdYlGn",
        alpha=0.7,
        edgecolors="black",
        linewidths=0.5,
    )
    # Decision boundary: carbon_cost(x,y) = silicon_cost(x,y)
    # 0.3x + 1.8y + 0.2 = 1.7x + 0.3y + 0.2
    # 1.5y = 1.4x
    # y = (1.4 / 1.5) x
    bx = np.linspace(0, 1, 100)
    by = (1.4 / 1.5) * bx
    ax.plot(bx, by, "k--", linewidth=2, label="Decision boundary")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("First-person / embodied need")
    ax.set_ylabel("Symbolic / scalable need")
    ax.set_title("Niche-complementary task allocation")
    # Custom legend for agent assignment
    from matplotlib.lines import Line2D
    legend_handles = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#c62828", markersize=10, label="Carbon"),
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#2e7d32", markersize=10, label="Silicon"),
        Line2D([0], [0], color="black", linewidth=2, linestyle="--", label="Decision boundary"),
    ]
    ax.legend(handles=legend_handles, loc="upper left")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "carbon_silicon_task_allocation.png", dpi=150)
    plt.close(fig)


def plot_strategy_comparison(n_tasks: int = 500, n_runs: int = 50) -> None:
    """Compare allocation strategies across multiple task distributions."""
    strategies = {
        "Carbon only": allocate_carbon_only,
        "Silicon only": allocate_silicon_only,
        "Random split": allocate_random,
        "Niche complementarity": allocate_niche_complementary,
    }

    costs = {name: [] for name in strategies}
    carbon_shares = {name: [] for name in strategies}

    for _ in range(n_runs):
        x, y = generate_tasks(n_tasks)
        for name, allocator in strategies.items():
            if name == "Niche complementarity":
                assignment = allocator(x, y)
            else:
                assignment = allocator(n_tasks)
            costs[name].append(total_cost(x, y, assignment))
            carbon_shares[name].append(1 - assignment.mean())

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    names = list(strategies.keys())
    mean_costs = [np.mean(costs[name]) for name in names]
    std_costs = [np.std(costs[name]) for name in names]
    colors = ["#c62828", "#1565c0", "#7b1fa2", "#2e7d32"]

    axes[0].bar(names, mean_costs, yerr=std_costs, color=colors, capsize=5)
    axes[0].set_ylabel("Total cost")
    axes[0].set_title("Strategy cost comparison")
    axes[0].tick_params(axis="x", rotation=15)

    mean_carbon = [np.mean(carbon_shares[name]) for name in names]
    axes[1].bar(names, mean_carbon, color=colors, alpha=0.7)
    axes[1].set_ylabel("Carbon task share")
    axes[1].set_ylim(0, 1)
    axes[1].set_title("Carbon involvement by strategy")
    axes[1].tick_params(axis="x", rotation=15)

    fig.suptitle("Carbon-silicon symbiosis: niche complementarity", fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "carbon_silicon_strategy_comparison.png", dpi=150)
    plt.close(fig)

    for name in names:
        print(f"{name}: cost = {np.mean(costs[name]):.1f} ± {np.std(costs[name]):.1f}")


def plot_heat_tradeoff(n_tasks: int = 500, n_runs: int = 50) -> None:
    """Show how thermodynamic cost changes optimal carbon-silicon allocation."""
    lambda_values = np.linspace(0, 3, 30)
    carbon_shares = []
    cost_carbon_only = []
    cost_silicon_only = []
    cost_complementary = []

    for lam in lambda_values:
        shares = []
        c_only = []
        s_only = []
        comp = []
        for _ in range(n_runs):
            x, y = generate_tasks(n_tasks)
            assignment = allocate_niche_complementary_with_heat(x, y, lam)
            shares.append(1 - assignment.mean())
            c_only.append(total_cost_with_heat(x, y, allocate_carbon_only(n_tasks), lam))
            s_only.append(total_cost_with_heat(x, y, allocate_silicon_only(n_tasks), lam))
            comp.append(total_cost_with_heat(x, y, assignment, lam))
        carbon_shares.append(np.mean(shares))
        cost_carbon_only.append(np.mean(c_only))
        cost_silicon_only.append(np.mean(s_only))
        cost_complementary.append(np.mean(comp))

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].plot(lambda_values, carbon_shares, color="#2e7d32", linewidth=2)
    axes[0].set_xlabel(r"Heat cost weight $\lambda_H$")
    axes[0].set_ylabel("Optimal carbon task share")
    axes[0].set_title("Thermodynamic pressure shifts tasks toward carbon")
    axes[0].set_ylim(0, 1)
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(lambda_values, cost_carbon_only, color="#c62828", label="Carbon only")
    axes[1].plot(lambda_values, cost_silicon_only, color="#1565c0", label="Silicon only")
    axes[1].plot(lambda_values, cost_complementary, color="#2e7d32", label="Niche complementarity")
    axes[1].set_xlabel(r"Heat cost weight $\lambda_H$")
    axes[1].set_ylabel("Total cost")
    axes[1].set_title("Complementary allocation stays optimal under heat constraints")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "carbon_silicon_heat_tradeoff.png", dpi=150)
    plt.close(fig)

    print(f"At lambda_H=0, carbon share = {carbon_shares[0]:.2f}")
    print(f"At lambda_H=3, carbon share = {carbon_shares[-1]:.2f}")


def plot_l3_interpretation() -> None:
    """Demonstrate L3 creative interpretation as collaborative task."""
    # L3 tasks require both dimensions simultaneously
    n = 50
    x_l3 = RNG.uniform(0.6, 0.9, size=n)  # high embodied/social need
    y_l3 = RNG.uniform(0.6, 0.9, size=n)  # high symbolic/logical need

    # Carbon-only and silicon-only costs
    c_only = carbon_cost(x_l3, y_l3).sum()
    s_only = silicon_cost(x_l3, y_l3).sum()

    # Collaborative: carbon provides first-person/embodied input, silicon provides
    # symbolic/logical structure, combined cost is less than either alone.
    # Model collaboration as reducing the dominant term for each agent.
    collaborative = (
        0.3 * x_l3 + 0.3 * y_l3 + 0.2  # each agent focuses on its strength
    ).sum()

    fig, ax = plt.subplots(figsize=(7, 5))
    names = ["Carbon only", "Silicon only", "Collaborative L3"]
    values = [c_only, s_only, collaborative]
    colors = ["#c62828", "#1565c0", "#2e7d32"]
    ax.bar(names, values, color=colors)
    ax.set_ylabel("Total cost")
    ax.set_title("L3 creative interpretation: collaboration beats either alone")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "carbon_silicon_l3_interpretation.png", dpi=150)
    plt.close(fig)

    print(f"L3 Carbon only: {c_only:.1f}")
    print(f"L3 Silicon only: {s_only:.1f}")
    print(f"L3 Collaborative: {collaborative:.1f}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Plotting cost surfaces...")
    plot_cost_surface()

    print("Plotting task allocation...")
    x, y = generate_tasks(200)
    plot_task_allocation(x, y)

    print("Running strategy comparison...")
    plot_strategy_comparison(n_tasks=500, n_runs=50)

    print("Plotting L3 interpretation...")
    plot_l3_interpretation()

    print("Plotting heat tradeoff...")
    plot_heat_tradeoff(n_tasks=500, n_runs=50)

    print(f"Figures saved to {OUT_DIR}")


if __name__ == "__main__":
    main()
