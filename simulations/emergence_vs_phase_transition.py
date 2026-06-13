#!/usr/bin/env python3
"""Distinguish emergence from phase transition in simulated systems.

This script compares two idealized systems:

1. 2D Ising model — a canonical phase transition. Magnetization flips when an
   external control parameter (temperature) crosses a threshold. The parts
   (spins) do not change their local rule; only the global state changes.

2. Boids flocking — a canonical emergence model. Flock-level order (polarization)
   arises from local interaction rules. There is no single external knob that
   triggers a discontinuous flip; instead, order grows smoothly as interaction
   strength or density increases, and the property "flock" is not defined for
   an isolated bird.

Run with:
    python simulations/emergence_vs_phase_transition.py

Outputs:
    simulations/ising_phase_transition.png
    simulations/boids_emergence.png
    simulations/emergence_vs_phase_comparison.png
"""

from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = Path(__file__).parent
RNG = np.random.default_rng(42)


# ---------------------------------------------------------------------------
# 1. Ising model: phase transition
# ---------------------------------------------------------------------------

def ising_metropolis(grid: np.ndarray, beta: float, steps: int) -> np.ndarray:
    """Run Metropolis updates on a 2D Ising grid."""
    n = grid.shape[0]
    for _ in range(steps):
        i = RNG.integers(0, n)
        j = RNG.integers(0, n)
        s = grid[i, j]
        # Periodic neighbors
        neighbors = (
            grid[(i - 1) % n, j]
            + grid[(i + 1) % n, j]
            + grid[i, (j - 1) % n]
            + grid[i, (j + 1) % n]
        )
        dE = 2 * s * neighbors
        if dE < 0 or RNG.random() < np.exp(-beta * dE):
            grid[i, j] = -s
    return grid


def ising_magnetization(grid: np.ndarray) -> float:
    return float(np.abs(grid.mean()))


def run_ising_phase_transition(
    n: int = 40,
    equilibration: int = 200_000,
    samples: int = 50,
    temperatures: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Return (temperatures, magnetizations) for the 2D Ising model."""
    if temperatures is None:
        temperatures = np.linspace(1.5, 3.5, 25)
    magnetizations = []
    for T in temperatures:
        beta = 1.0 / T
        grid = RNG.choice([-1, 1], size=(n, n))
        grid = ising_metropolis(grid, beta, equilibration)
        mags = []
        for _ in range(samples):
            grid = ising_metropolis(grid, beta, equilibration // samples)
            mags.append(ising_magnetization(grid))
        magnetizations.append(np.mean(mags))
    return temperatures, np.array(magnetizations)


# ---------------------------------------------------------------------------
# 2. Boids model: emergence
# ---------------------------------------------------------------------------

class Boids:
    """Minimal 2D boids simulation."""

    def __init__(
        self,
        n: int = 200,
        width: float = 60.0,
        height: float = 60.0,
        max_speed: float = 2.0,
        perception: float = 15.0,
        separation: float = 1.5,
        alignment_weight: float = 0.05,
        cohesion_weight: float = 0.005,
        separation_weight: float = 0.1,
    ):
        self.n = n
        self.width = width
        self.height = height
        self.max_speed = max_speed
        self.perception = perception
        self.separation = separation
        self.alignment_weight = alignment_weight
        self.cohesion_weight = cohesion_weight
        self.separation_weight = separation_weight

        self.positions = RNG.uniform(0, width, size=(n, 2))
        angles = RNG.uniform(0, 2 * np.pi, size=n)
        self.velocities = np.stack([np.cos(angles), np.sin(angles)], axis=1) * max_speed

    def step(self) -> None:
        """Vectorized boids update using pairwise distances."""
        # Pairwise displacement matrix (n, n, 2)
        diff = self.positions[:, np.newaxis, :] - self.positions[np.newaxis, :, :]
        # Minimum image convention for periodic boundaries
        diff[:, :, 0] -= self.width * np.round(diff[:, :, 0] / self.width)
        diff[:, :, 1] -= self.height * np.round(diff[:, :, 1] / self.height)

        dists = np.linalg.norm(diff, axis=2)
        # Perception mask (exclude self)
        neigh = (dists < self.perception) & (dists > 0)
        # Count neighbors per boid
        counts = neigh.sum(axis=1, keepdims=True)

        # Alignment: average velocity of neighbors
        align = np.einsum('ij,jk->ik', neigh.astype(float), self.velocities)
        align_norm = np.linalg.norm(align, axis=1, keepdims=True)
        with np.errstate(divide="ignore", invalid="ignore"):
            align = np.where(align_norm > 0, align / align_norm * self.max_speed, 0)

        # Cohesion: vector to center of mass of neighbors
        cohesion = np.einsum('ij,jk->ik', neigh.astype(float), self.positions)
        with np.errstate(divide="ignore", invalid="ignore"):
            cohesion = np.where(counts > 0, cohesion / counts - self.positions, 0)
        cohesion_norm = np.linalg.norm(cohesion, axis=1, keepdims=True)
        with np.errstate(divide="ignore", invalid="ignore"):
            cohesion = np.where(cohesion_norm > 0, cohesion / cohesion_norm * self.max_speed, 0)

        # Separation: avoid neighbors within separation radius
        close = dists < self.separation
        # Zero out self
        close[np.arange(self.n), np.arange(self.n)] = False
        sep = np.einsum('ij,ijk->ik', -close.astype(float), diff)
        sep_norm = np.linalg.norm(sep, axis=1, keepdims=True)
        with np.errstate(divide="ignore", invalid="ignore"):
            sep = np.where(sep_norm > 0, sep / sep_norm * self.max_speed, 0)

        accelerations = (
            self.alignment_weight * (align - self.velocities)
            + self.cohesion_weight * (cohesion - self.velocities)
            + self.separation_weight * (sep - self.velocities)
        )

        self.velocities += accelerations
        # Limit speed
        speeds = np.linalg.norm(self.velocities, axis=1, keepdims=True)
        self.velocities = np.where(
            speeds > self.max_speed,
            self.velocities / speeds * self.max_speed,
            self.velocities,
        )
        self.positions += self.velocities
        # Periodic boundaries
        self.positions[:, 0] %= self.width
        self.positions[:, 1] %= self.height

    def order_parameter(self) -> float:
        """Polarization: magnitude of mean normalized velocity vector."""
        mean_v = self.velocities.mean(axis=0)
        return float(np.linalg.norm(mean_v) / self.max_speed)


def run_boids_emergence(
    alignment_weights: np.ndarray | None = None,
    n: int = 200,
    steps: int = 500,
    burn_in: int = 300,
) -> tuple[np.ndarray, np.ndarray]:
    """Return (alignment_weights, order_parameters) for the boids model."""
    if alignment_weights is None:
        alignment_weights = np.linspace(0.0, 0.8, 25)
    order_params = []
    for aw in alignment_weights:
        boids = Boids(n=n, alignment_weight=aw)
        for _ in range(burn_in):
            boids.step()
        op = []
        for _ in range(steps - burn_in):
            boids.step()
            op.append(boids.order_parameter())
        order_params.append(np.mean(op))
    return alignment_weights, np.array(order_params)


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

def plot_ising(temps: np.ndarray, mags: np.ndarray) -> None:
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(temps, mags, "o-", color="#1565c0", label="Magnetization $|m|$")
    ax.axvline(
        2 / np.log(1 + np.sqrt(2)),
        color="#c62828",
        linestyle="--",
        label="Exact $T_c$ for infinite 2D Ising",
    )
    ax.set_xlabel("Temperature $T$")
    ax.set_ylabel("Magnetization $|m|$")
    ax.set_title("Phase transition: 2D Ising model")
    ax.legend()
    ax.set_ylim(-0.05, 1.05)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "ising_phase_transition.png", dpi=150)
    plt.close(fig)


def plot_boids(align_weights: np.ndarray, order_params: np.ndarray) -> None:
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(align_weights, order_params, "o-", color="#2e7d32", label="Polarization")
    ax.set_xlabel("Alignment weight $w_{\mathrm{align}}$")
    ax.set_ylabel("Order parameter (polarization)")
    ax.set_title("Emergence: Boids flocking")
    ax.legend()
    ax.set_ylim(-0.05, 1.05)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "boids_emergence.png", dpi=150)
    plt.close(fig)


def plot_comparison(temps: np.ndarray, mags: np.ndarray, align_weights: np.ndarray, order_params: np.ndarray) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].plot(temps, mags, "o-", color="#1565c0")
    axes[0].axvline(
        2 / np.log(1 + np.sqrt(2)),
        color="#c62828",
        linestyle="--",
    )
    axes[0].set_xlabel("External control parameter: temperature $T$")
    axes[0].set_ylabel("Order parameter: $|m|$")
    axes[0].set_title("Phase transition\nstate flip at a threshold")
    axes[0].set_ylim(-0.05, 1.05)

    axes[1].plot(align_weights, order_params, "o-", color="#2e7d32")
    axes[1].set_xlabel("Internal interaction parameter: alignment weight")
    axes[1].set_ylabel("Order parameter: polarization")
    axes[1].set_title("Emergence\norder grows from local rules")
    axes[1].set_ylim(-0.05, 1.05)

    fig.suptitle("Emergence ≠ Phase transition: two different kinds of macro-order", fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "emergence_vs_phase_comparison.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Running Ising phase-transition simulation...")
    temps, mags = run_ising_phase_transition(n=40, equilibration=100_000, samples=30)
    plot_ising(temps, mags)

    print("Running Boids emergence simulation...")
    align_weights, order_params = run_boids_emergence(n=200, steps=600, burn_in=350)
    plot_boids(align_weights, order_params)

    plot_comparison(temps, mags, align_weights, order_params)

    print(f"Figures saved to {OUT_DIR}")
    print(f"Ising Tc (exact, infinite lattice): {2 / np.log(1 + np.sqrt(2)):.3f}")
    print(f"Boids max order parameter: {order_params.max():.3f}")


if __name__ == "__main__":
    main()
