#!/usr/bin/env python3
"""Planetary thermodynamic boundary for AI expansion.

This script models the energy balance of Earth with AI waste heat as an
additional term. Even with unlimited energy input (e.g., fusion or solar),
AI expansion is constrained by Earth's ability to radiate waste heat into
space.

Key physics:
- Earth absorbs solar radiation over its cross-sectional area pi*R^2.
- Earth radiates infrared over its full surface area 4*pi*R^2.
- At equilibrium without AI: P_solar = sigma * epsilon * 4*pi*R^2 * T_eq^4.
- With AI waste heat P_AI: T rises until P_solar + P_AI = P_out(T).
- If P_AI grows without bound, temperature rises without bound (modulo
  radiative area changes).

Run with:
    python simulations/planetary_ai_thermodynamics.py

Outputs:
    simulations/ai_heat_equilibrium.png
    simulations/ai_heat_trajectory.png
    simulations/ai_heat_policy_comparison.png
    simulations/ai_heat_governance_dashboard.png
"""

from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = Path(__file__).parent

# ---------------------------------------------------------------------------
# Physical constants and Earth parameters
# ---------------------------------------------------------------------------

SIGMA = 5.670374419e-8  # Stefan-Boltzmann constant [W m^-2 K^-4]
R_EARTH = 6.371e6       # Earth radius [m]
S0 = 1361.0             # Solar constant [W m^-2]
ALBEDO = 0.30           # Bond albedo
EPSILON = 0.61          # Effective emissivity (greenhouse-adjusted)

# Areas
A_ABSORB = np.pi * R_EARTH**2      # Cross-sectional area absorbing sunlight
A_RADIATE = 4 * np.pi * R_EARTH**2 # Full surface area radiating to space

# Absorbed solar power
P_SOLAR = S0 * A_ABSORB * (1 - ALBEDO)

# Equilibrium temperature without AI
T_EQ = (P_SOLAR / (SIGMA * EPSILON * A_RADIATE)) ** 0.25

# Effective heat capacity of Earth system (mostly oceans, top 100m)
# C = mass * specific heat; approximate globally averaged water-equivalent
C_EARTH = 5.0e24  # [J K^-1], rough estimate

print(f"Absorbed solar power: {P_SOLAR:.3e} W = {P_SOLAR/1e12:.1f} TW")
print(f"Equilibrium temperature without AI: {T_EQ - 273.15:.2f} C")


# ---------------------------------------------------------------------------
# Core physics functions
# ---------------------------------------------------------------------------

def radiated_power(temperature: float) -> float:
    """Outgoing infrared radiation [W].

    A temperature ceiling avoids floating-point overflow for physically
    absurd scenarios used only to illustrate unbounded growth.
    """
    T = min(float(temperature), 1e6)  # clamp far above physical relevance
    return SIGMA * EPSILON * A_RADIATE * T**4


def equilibrium_temperature(p_ai: float) -> float:
    """Equilibrium surface temperature for a given AI waste heat [W]."""
    total = P_SOLAR + p_ai
    return (total / (SIGMA * EPSILON * A_RADIATE)) ** 0.25


def simulate_temperature(
    p_ai_func,
    years: np.ndarray,
    t0: float = T_EQ,
    max_temp: float = 10000.0,
    dt_days: float = 1.0,
) -> np.ndarray:
    """Integrate temperature dynamics with time-varying AI heat.

    Uses fixed daily explicit-Euler steps and caps temperature at
    ``max_temp`` K so that unbounded-growth scenarios do not overflow.
    """
    dt = dt_days * 24 * 3600  # seconds
    t = t0
    temps = []
    year_prev = years[0]
    for year in years:
        span = (year - year_prev) * 365.25 * 24 * 3600  # seconds
        n_steps = max(1, int(np.ceil(span / dt)))
        dt_local = span / n_steps
        for _ in range(n_steps):
            if t >= max_temp:
                break
            p_ai = p_ai_func(year_prev + (year - year_prev) * 0.5)
            dTdt = (P_SOLAR + p_ai - radiated_power(t)) / C_EARTH
            t = min(t + dTdt * dt_local, max_temp)
        temps.append(t)
        year_prev = year
    return np.array(temps)


# ---------------------------------------------------------------------------
# Scenarios
# ---------------------------------------------------------------------------

def exponential_growth(p0: float, rate: float, years: np.ndarray) -> np.ndarray:
    """P_AI(t) = P0 * exp(rate * t)."""
    return p0 * np.exp(rate * years)


def capped_growth(p0: float, rate: float, cap: float, years: np.ndarray) -> np.ndarray:
    """Exponential growth until cap, then flat."""
    return np.minimum(p0 * np.exp(rate * years), cap)


def stop_protocol(
    p0: float, rate: float, threshold: float, years: np.ndarray
) -> np.ndarray:
    """Exponential growth until threshold, then stop."""
    p = p0 * np.exp(rate * years)
    p[p > threshold] = threshold
    return p


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------

def plot_equilibrium_curve() -> None:
    """Plot equilibrium temperature vs AI waste heat power."""
    p_ai = np.logspace(8, 17, 500)  # 1e8 W to 1e17 W
    temps = equilibrium_temperature(p_ai)
    deltas = temps - T_EQ

    # Reference: current global power ~ 18 TW, current AI ~ 0.05 TW
    current_global = 18e12
    current_ai = 0.05e12

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.semilogx(p_ai / 1e12, deltas, color="#c62828", linewidth=2)
    ax.axvline(current_global / 1e12, color="gray", linestyle="--", alpha=0.7, label="Current global power (~18 TW)")
    ax.axvline(current_ai / 1e12, color="blue", linestyle="--", alpha=0.7, label="Current AI power (~0.05 TW)")
    ax.axvline(P_SOLAR / 1e12, color="green", linestyle="--", alpha=0.7, label="Absorbed solar power (~121,000 TW)")
    ax.set_xlabel("AI waste heat power [TW]")
    ax.set_ylabel("Equilibrium temperature rise [K]")
    ax.set_title("Planetary thermodynamic boundary for AI")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "ai_heat_equilibrium.png", dpi=150)
    plt.close(fig)


def plot_trajectory() -> None:
    """Plot temperature trajectory under exponential AI growth."""
    years = np.linspace(0, 200, 1000)
    p0 = 0.05e12  # 0.05 TW

    rates = {
        "10%/year": 0.10,
        "30%/year": 0.30,
        "50%/year": 0.50,
    }

    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    for name, rate in rates.items():
        p_ai = exponential_growth(p0, rate, years)
        temps = simulate_temperature(lambda y: p0 * np.exp(rate * y), years)
        axes[0].semilogy(years, p_ai / 1e12, label=name)
        axes[1].plot(years, temps - 273.15, label=name)

    axes[0].axhline(P_SOLAR / 1e12, color="green", linestyle="--", alpha=0.7, label="Solar absorbed")
    axes[0].set_ylabel("AI waste heat [TW]")
    axes[0].set_title("AI power growth scenarios")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].axhline(T_EQ - 273.15, color="gray", linestyle="--", alpha=0.5, label="Pre-AI baseline")
    axes[1].set_xlabel("Years from now")
    axes[1].set_ylabel("Global mean temperature [C]")
    axes[1].set_title("Temperature response to AI waste heat")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "ai_heat_trajectory.png", dpi=150)
    plt.close(fig)


def plot_policy_comparison() -> None:
    """Compare governance policies: unconstrained, cap, stop protocol."""
    years = np.linspace(0, 150, 750)
    p0 = 0.05e12
    rate = 0.30

    # Policies
    policies = {
        "Unconstrained": lambda y: exponential_growth(p0, rate, y),
        "Cap at 10% solar": lambda y: capped_growth(p0, rate, 0.10 * P_SOLAR, y),
        "Stop at 10% solar": lambda y: stop_protocol(p0, rate, 0.10 * P_SOLAR, y),
        "Stop at 50% solar": lambda y: stop_protocol(p0, rate, 0.50 * P_SOLAR, y),
    }

    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    colors = ["#c62828", "#1565c0", "#2e7d32", "#f9a825"]

    for (name, policy), color in zip(policies.items(), colors):
        p_ai = policy(years)
        temps = simulate_temperature(
            lambda y: policy(np.array([y]))[0], years
        )
        axes[0].semilogy(years, p_ai / 1e12, label=name, color=color)
        axes[1].plot(years, temps - 273.15, label=name, color=color)

    axes[0].axhline(P_SOLAR / 1e12, color="green", linestyle="--", alpha=0.5, label="Solar absorbed")
    axes[0].set_ylabel("AI waste heat [TW]")
    axes[0].set_title("Governance policy comparison (30% annual growth)")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].axhline(T_EQ - 273.15, color="gray", linestyle="--", alpha=0.5, label="Pre-AI baseline")
    axes[1].set_xlabel("Years from now")
    axes[1].set_ylabel("Global mean temperature [C]")
    axes[1].set_title("Temperature response by policy")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "ai_heat_policy_comparison.png", dpi=150)
    plt.close(fig)


def plot_governance_dashboard() -> None:
    """Planetary heat-budget occupancy dashboard with traffic-light zones."""
    years = np.linspace(0, 120, 600)
    p0 = 0.05e12
    rate = 0.30
    eta = 0.10  # 10% solar budget as threshold

    p_ai = exponential_growth(p0, rate, years)
    occupancy = p_ai / (eta * P_SOLAR)

    fig, ax = plt.subplots(figsize=(10, 5))

    # Traffic-light background zones
    ax.axhspan(0, 0.5, color="green", alpha=0.1, label="Safe (<50%)")
    ax.axhspan(0.5, 0.9, color="yellow", alpha=0.1, label="Caution (50-90%)")
    ax.axhspan(0.9, 10, color="red", alpha=0.1, label="Critical (>90%)")

    ax.plot(years, occupancy, color="#1565c0", linewidth=2.5, label=r"$\rho_H(t)$")
    ax.axhline(1.0, color="red", linestyle="--", linewidth=2, label="Stop threshold")

    ax.set_xlabel("Years from now")
    ax.set_ylabel(r"Planetary heat-budget occupancy $\rho_H$")
    ax.set_title("Planetary De dashboard: AI heat-budget occupancy (30% growth, η=10%)")
    ax.set_ylim(0, 5)
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "ai_heat_governance_dashboard.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Plotting equilibrium thermodynamic boundary...")
    plot_equilibrium_curve()

    print("Plotting temperature trajectories...")
    plot_trajectory()

    print("Plotting policy comparison...")
    plot_policy_comparison()

    print("Plotting governance dashboard...")
    plot_governance_dashboard()

    print(f"Figures saved to {OUT_DIR}")
    print(f"Solar absorbed: {P_SOLAR/1e12:.1f} TW")
    print(f"Current AI heat ~0.05 TW is {(0.05e12/P_SOLAR)*100:.4f}% of solar budget")
    print(f"At 30% annual growth, AI reaches 10% of solar budget in ~{np.log(0.10*P_SOLAR/0.05e12)/0.30:.1f} years")


if __name__ == "__main__":
    main()
