#!/usr/bin/env python3
"""Simulation of the DMN-insula bistable competition model.

This script implements the dimensionally consistent ODEs from
`2_models/dmn_self_model.md` and provides:
- Time-series integration for DMN-dominant and insula-dominant initial states
- Bifurcation diagram over the attention-amplification parameter alpha
- Phase portrait (D vs I) for a fixed parameter set

Run with:
    python simulations/dmn_insula_bistable.py

Outputs:
    simulations/dmn_insula_timeseries.png
    simulations/dmn_insula_bifurcation.png
    simulations/dmn_insula_phase_portrait.png
"""

from pathlib import Path

import _compat  # noqa: F401  # ensures dao_science is importable
import matplotlib
import numpy as np
from scipy.integrate import solve_ivp

from dao_science.core import generalized_sigmoid

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = Path(__file__).parent


def dmn_insula_ode(t, y, params):
    """RHS of the DMN-insula competition model.

    Variables D and I are normalized activation levels in [0, 1].
    All coefficients have dimensions of [time]^-1.
    """
    D, I = y
    tau_D = params["tau_D"]
    tau_I = params["tau_I"]
    w_DD = params["w_DD"]
    w_II = params["w_II"]
    w_ID = params["w_ID"]
    w_DI = params["w_DI"]
    S_D = params["S_D"]
    S_I = params["S_I"]
    alpha = params["alpha"]
    B = params["B"]

    dDdt = (-D + w_DD * generalized_sigmoid(D) - w_ID * generalized_sigmoid(I) + S_D) / tau_D
    dIdt = (-I + w_II * generalized_sigmoid(I) - w_DI * generalized_sigmoid(D) + S_I + alpha * B) / tau_I
    return [dDdt, dIdt]


def integrate(params, y0, t_span, t_eval):
    sol = solve_ivp(
        lambda t, y: dmn_insula_ode(t, y, params),
        t_span,
        y0,
        t_eval=t_eval,
        method="RK45",
    )
    return sol.t, sol.y[0], sol.y[1]


def plot_timeseries(params):
    t_span = (0, 20)
    t_eval = np.linspace(*t_span, 2000)

    fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    # DMN-dominant initial condition
    _, D1, I1 = integrate(params, y0=[0.8, 0.1], t_span=t_span, t_eval=t_eval)
    axes[0].plot(t_eval, D1, label="DMN $D(t)$", color="#1565c0")
    axes[0].plot(t_eval, I1, label="Insula $I(t)$", color="#2e7d32")
    axes[0].set_title("Initial state: DMN-dominant ($D_0=0.8, I_0=0.1$)")
    axes[0].set_ylabel("Normalized activation")
    axes[0].set_ylim(-0.05, 1.05)
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Insula-dominant initial condition
    _, D2, I2 = integrate(params, y0=[0.1, 0.8], t_span=t_span, t_eval=t_eval)
    axes[1].plot(t_eval, D2, label="DMN $D(t)$", color="#1565c0")
    axes[1].plot(t_eval, I2, label="Insula $I(t)$", color="#2e7d32")
    axes[1].set_title("Initial state: insula-dominant ($D_0=0.1, I_0=0.8$)")
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Normalized activation")
    axes[1].set_ylim(-0.05, 1.05)
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    fig.suptitle("DMN-insula bistable dynamics", fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "dmn_insula_timeseries.png", dpi=150)
    plt.close(fig)
    print("Saved dmn_insula_timeseries.png")


def plot_bifurcation(params):
    """Steady-state DMN activation as a function of alpha (anchor effort)."""
    alphas = np.linspace(0.0, 2.0, 200)
    D_finals = []
    t_span = (0, 50)
    t_eval = np.linspace(*t_span, 1000)

    for a in alphas:
        p = {**params, "alpha": a}
        # Start from DMN-dominant basin
        _, D, I = integrate(p, y0=[0.8, 0.1], t_span=t_span, t_eval=t_eval)
        D_finals.append(D[-1])

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(alphas, D_finals, color="#1565c0", lw=2)
    ax.axhline(0.5, color="gray", linestyle="--", alpha=0.5)
    ax.set_xlabel(r"Attention amplification $\alpha$")
    ax.set_ylabel("Steady-state DMN activation $D^*$")
    ax.set_title("Bifurcation: anchor effort drives DMN→insula switch")
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "dmn_insula_bifurcation.png", dpi=150)
    plt.close(fig)
    print("Saved dmn_insula_bifurcation.png")


def plot_phase_portrait(params):
    """Phase portrait with nullclines and a few trajectories."""
    D_grid = np.linspace(0, 1, 100)
    I_grid = np.linspace(0, 1, 100)
    D_mesh, I_mesh = np.meshgrid(D_grid, I_grid)

    # Compute vector field
    dD = np.zeros_like(D_mesh)
    dI = np.zeros_like(I_mesh)
    for i in range(D_mesh.shape[0]):
        for j in range(D_mesh.shape[1]):
            deriv = dmn_insula_ode(0, [D_mesh[i, j], I_mesh[i, j]], params)
            dD[i, j] = deriv[0]
            dI[i, j] = deriv[1]

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.streamplot(D_mesh, I_mesh, dD, dI, color="lightgray", linewidth=0.5, density=1.5)

    # Nullclines: dD/dt = 0 and dI/dt = 0
    D_null = []
    I_null_D = []
    for D in D_grid:
        for I in I_grid:
            if abs(-D + params["w_DD"] * generalized_sigmoid(D) - params["w_ID"] * generalized_sigmoid(I) + params["S_D"]) < 0.03:
                D_null.append(D)
                I_null_D.append(I)

    D_null_I = []
    I_null = []
    for D in D_grid:
        for I in I_grid:
            if abs(-I + params["w_II"] * generalized_sigmoid(I) - params["w_DI"] * generalized_sigmoid(D) + params["S_I"] + params["alpha"] * params["B"]) < 0.03:
                D_null_I.append(D)
                I_null.append(I)

    ax.scatter(D_null, I_null_D, s=1, color="#1565c0", label="$dD/dt=0$ nullcline")
    ax.scatter(D_null_I, I_null, s=1, color="#2e7d32", label="$dI/dt=0$ nullcline")

    # Sample trajectories
    t_span = (0, 30)
    t_eval = np.linspace(*t_span, 500)
    for y0 in [(0.9, 0.1), (0.1, 0.9), (0.5, 0.5)]:
        _, D_traj, I_traj = integrate(params, y0=y0, t_span=t_span, t_eval=t_eval)
        ax.plot(D_traj, I_traj, lw=1.5, alpha=0.7)
        ax.plot(D_traj[0], I_traj[0], "o", markersize=5)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("DMN activation $D$")
    ax.set_ylabel("Insula activation $I$")
    ax.set_title("Phase portrait: two stable attractors")
    ax.legend(markerscale=4)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "dmn_insula_phase_portrait.png", dpi=150)
    plt.close(fig)
    print("Saved dmn_insula_phase_portrait.png")


def main():
    # Base parameters producing a bistable regime.
    params = {
        "tau_D": 1.0,
        "tau_I": 0.8,
        "w_DD": 1.6,
        "w_II": 1.4,
        "w_ID": 0.9,
        "w_DI": 1.0,
        "S_D": 0.1,
        "S_I": 0.05,
        "alpha": 1.0,
        "B": 0.4,
    }

    plot_timeseries(params)
    plot_bifurcation(params)
    plot_phase_portrait(params)
    print(f"\nAll outputs written to {OUT_DIR}/")


if __name__ == "__main__":
    main()
