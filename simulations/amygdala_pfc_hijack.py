#!/usr/bin/env python3
"""Amygdala-PFC competition simulation for the 100ms hijacking model.

This script implements the delayed competition dynamics described in
`2_models/100ms_model.md` and `verifiable_units/vu_02_amygdala_pfc.md`:

    dA/dt = alpha_B * S(t) - alpha_T * P(t) * A(t) - gamma_A * A(t)
    dP/dt = beta * A(t - delta) - gamma_P * P(t)

A(t) and P(t) are normalized activation levels in [0, 1].  The delay delta
models the conduction time from amygdala to prefrontal cortex.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = Path(__file__).resolve().parent

# Time base: 0 to 1000 ms, dt = 0.2 ms.
T_MAX = 1000.0  # ms
DT = 0.2  # ms
T_STIM_START = 50.0  # ms
T_STIM_END = 150.0  # ms


def simulate(
    alpha_B: float = 0.6,
    alpha_T: float = 0.15,
    gamma_A: float = 0.08,
    beta: float = 0.25,
    gamma_P: float = 0.06,
    delta: float = 100.0,
    A0: float = 0.05,
    P0: float = 0.05,
    stim_amp: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Euler integration of the delayed amygdala-PFC model.

    Returns
    -------
    t : np.ndarray
        Time vector in ms.
    A : np.ndarray
        Amygdala activation.
    P : np.ndarray
        Prefrontal control activation.
    """
    n_steps = int(T_MAX / DT) + 1
    t = np.linspace(0, T_MAX, n_steps)
    A = np.zeros(n_steps)
    P = np.zeros(n_steps)

    delay_steps = int(round(delta / DT))

    A[0] = A0
    P[0] = P0

    def S(time: float) -> float:
        return stim_amp if T_STIM_START <= time <= T_STIM_END else 0.0

    for i in range(1, n_steps):
        time = t[i - 1]
        a = A[i - 1]
        p = P[i - 1]

        # Stimulus is present during the defined window.
        s = S(time)

        dA = alpha_B * s - alpha_T * p * a - gamma_A * a

        # Delayed amygdala input to PFC.
        if i - 1 - delay_steps >= 0:
            a_delayed = A[i - 1 - delay_steps]
        else:
            a_delayed = A0
        dP = beta * a_delayed - gamma_P * p

        A[i] = float(np.clip(a + dA * DT, 0.0, 1.0))
        P[i] = float(np.clip(p + dP * DT, 0.0, 1.0))

    return t, A, P


def classify_outcome(A: np.ndarray, P: np.ndarray) -> str:
    """Classify trial as hijack, regulation, or ambiguous."""
    A_peak = A.max()
    P_late = P[int(0.7 * len(P)):].mean()
    A_late = A[int(0.7 * len(A)):].mean()
    if A_peak > 0.7 and A_late > 0.4 and P_late < 0.35:
        return "hijack"
    if A_peak < 0.55 and A_late < 0.25 and P_late > 0.35:
        return "regulation"
    return "mixed"


def plot_trajectories(save_dir: Path = OUTPUT_DIR) -> None:
    """Plot hijack vs successful regulation time series."""
    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # Case 1: weak top-down regulation -> hijack.
    t, A_hij, P_hij = simulate(alpha_T=0.08, beta=0.22, delta=120.0)
    # Case 2: strong top-down regulation -> successful reappraisal.
    t, A_reg, P_reg = simulate(alpha_T=0.45, beta=0.35, delta=80.0)

    for ax, A, P, title in [
        (axes[0], A_hij, P_hij, "Case 1: Amygdala Hijack (weak PFC regulation)"),
        (axes[1], A_reg, P_reg, "Case 2: Successful Reappraisal (strong PFC regulation)"),
    ]:
        ax.plot(t, A, label="Amygdala A(t)", color="#c62828", linewidth=2)
        ax.plot(t, P, label="PFC control P(t)", color="#1565c0", linewidth=2)
        ax.axvspan(T_STIM_START, T_STIM_END, color="gray", alpha=0.15, label="Stimulus")
        ax.set_ylabel("Normalized activation")
        ax.set_ylim(-0.05, 1.05)
        ax.set_title(title)
        ax.legend(loc="upper right")
        ax.grid(True, alpha=0.3)

    axes[-1].set_xlabel("Time (ms)")
    plt.tight_layout()
    out = save_dir / "amygdala_pfc_trajectories.png"
    fig.savefig(out, dpi=150)
    print(f"Saved: {out}")
    plt.close(fig)


def plot_parameter_space(save_dir: Path = OUTPUT_DIR) -> None:
    """Scan alpha_T and delay to show hijack/regime boundary."""
    alpha_T_vals = np.linspace(0.05, 0.6, 40)
    delta_vals = np.linspace(50, 180, 40)
    outcome_grid = np.zeros((len(delta_vals), len(alpha_T_vals)))

    for i, delta in enumerate(delta_vals):
        for j, alpha_T in enumerate(alpha_T_vals):
            _, A, P = simulate(alpha_T=alpha_T, delta=delta)
            outcome = classify_outcome(A, P)
            if outcome == "hijack":
                outcome_grid[i, j] = 0.0
            elif outcome == "regulation":
                outcome_grid[i, j] = 1.0
            else:
                outcome_grid[i, j] = 0.5

    fig, ax = plt.subplots(figsize=(9, 6))
    im = ax.imshow(
        outcome_grid,
        aspect="auto",
        origin="lower",
        extent=[alpha_T_vals[0], alpha_T_vals[-1], delta_vals[0], delta_vals[-1]],
        cmap="RdYlGn",
        vmin=0,
        vmax=1,
    )
    ax.set_xlabel(r"Top-down regulation strength $\alpha_T$ (ms$^{-1}$)")
    ax.set_ylabel(r"Amygdala-PFC delay $\delta$ (ms)")
    ax.set_title("Hijack vs Regulation Parameter Space")
    cbar = fig.colorbar(im, ax=ax, ticks=[0, 0.5, 1])
    cbar.ax.set_yticklabels(["hijack", "mixed", "regulation"])
    plt.tight_layout()
    out = save_dir / "amygdala_pfc_parameter_space.png"
    fig.savefig(out, dpi=150)
    print(f"Saved: {out}")
    plt.close(fig)


def main() -> None:
    print("Running amygdala-PFC competition simulation...")
    plot_trajectories()
    plot_parameter_space()
    print("Done.")


if __name__ == "__main__":
    main()
