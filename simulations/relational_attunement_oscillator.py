#!/usr/bin/env python3
"""Relational attunement as coupled vital-tension oscillators.

This script models two agents in a relationship as coupled dynamical systems.
Each agent has a vitality/tension state T_i(t) that rises and falls with its
own impulses. The agents can "attune" to each other by allocating attention
(precision) to the partner, especially at the partner's critical handover
point t* — the moment when the partner's impulse peaks and begins to decline.

Three scenarios are compared:

1. Isolated:      no coupling; each agent oscillates independently.
2. Rigid support: constant high coupling; synchronization but risk of capture.
3. Attuned:       adaptive attention that increases at t* and withdraws
                  otherwise; complementary (anti-phase) dance with preserved
                  individuality.

Run with:
    python simulations/relational_attunement_oscillator.py

Outputs:
    simulations/relational_attunement_timeseries.png
    simulations/relational_attunement_phase_portrait.png
    simulations/relational_attunement_metrics.png
"""

from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = Path(__file__).parent

# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------

TAU = 4.0          # tension decay time constant (slower without support)
DT = 0.01          # integration step
T_END = 80.0       # total simulation time
N_STEPS = int(T_END / DT)
TIME = np.linspace(0, T_END, N_STEPS)

# Impulses: two offset pulse trains so that agents have different natural rhythms
IMPULSE_PERIOD = 14.0
IMPULSE_WIDTH = 1.8
IMPULSE_AMP = 3.0
PHASE_1 = 0.0
PHASE_2 = 5.0


def impulse_train(t: float, phase: float) -> float:
    """Periodic Gaussian impulses."""
    t_mod = (t - phase) % IMPULSE_PERIOD
    # Handle wrap-around by checking distance to both nearest pulses
    if t_mod > IMPULSE_PERIOD / 2:
        t_mod -= IMPULSE_PERIOD
    return IMPULSE_AMP * np.exp(-0.5 * (t_mod / IMPULSE_WIDTH) ** 2)


def sigmoid(x: float, k: float = 5.0, x0: float = 0.0) -> float:
    return 1.0 / (1.0 + np.exp(-k * (x - x0)))


# ---------------------------------------------------------------------------
# Attention / handover functions
# ---------------------------------------------------------------------------

def handover_signal(T: float, dT: float) -> float:
    """High when tension is high but declining (critical handover point t*)."""
    return sigmoid(T * (-dT) - 0.5, k=8.0)


def attention_attuned(T_other: float, dT_other: float, T_self: float) -> float:
    """Adaptive attention: peak when partner is at t* (high but declining).

    The agent withdraws attention if it is itself overwhelmed.
    """
    at_handover = handover_signal(T_other, dT_other)
    not_overwhelmed = 1.0 - sigmoid(T_self - 4.0, k=2.0)
    return at_handover * not_overwhelmed


def attention_rigid(T_other: float, dT_other: float, T_self: float) -> float:
    """Constant moderate attention (rigid support / control)."""
    return 0.35


def attention_isolated(T_other: float, dT_other: float, T_self: float) -> float:
    """No attention allocated to partner."""
    return 0.0


# ---------------------------------------------------------------------------
# Dynamics
# ---------------------------------------------------------------------------

def simulate(attention_func, kappa: float = 1.5):
    """Integrate the coupled tension dynamics."""
    T1 = np.zeros(N_STEPS)
    T2 = np.zeros(N_STEPS)
    A12 = np.zeros(N_STEPS)  # agent 1's attention to agent 2
    A21 = np.zeros(N_STEPS)  # agent 2's attention to agent 1

    T1[0] = 0.1
    T2[0] = 0.1

    for i in range(N_STEPS - 1):
        t = TIME[i]
        I1 = impulse_train(t, PHASE_1)
        I2 = impulse_train(t, PHASE_2)

        # Derivatives for handover detection (simple finite difference)
        dT1 = (T1[i] - T1[max(0, i - 1)]) / DT if i > 0 else 0.0
        dT2 = (T2[i] - T2[max(0, i - 1)]) / DT if i > 0 else 0.0

        A12[i] = attention_func(T2[i], dT2, T1[i])
        A21[i] = attention_func(T1[i], dT1, T2[i])

        # Support direction: agent j's attention to agent i provides a
        # well-timed boost when i is at the critical handover point (t*).
        # The boost is proportional to j's available vitality, modeling
        # "critical handover" — one dancer catches the other as they descend.
        support_1 = kappa * A21[i] * T2[i]  # agent 2 catches agent 1
        support_2 = kappa * A12[i] * T1[i]  # agent 1 catches agent 2

        # Tension dynamics: own impulse - natural decay + timed support
        dT1dt = (-T1[i] + I1 + support_1) / TAU
        dT2dt = (-T2[i] + I2 + support_2) / TAU

        T1[i + 1] = T1[i] + dT1dt * DT
        T2[i + 1] = T2[i] + dT2dt * DT

    # Compute final attention values
    dT1 = np.gradient(T1, DT)
    dT2 = np.gradient(T2, DT)
    A12 = np.array([attention_func(T2[i], dT2[i], T1[i]) for i in range(N_STEPS)])
    A21 = np.array([attention_func(T1[i], dT1[i], T2[i]) for i in range(N_STEPS)])

    return T1, T2, A12, A21


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def mean_tension(T1: np.ndarray, T2: np.ndarray) -> float:
    return float(np.mean(T1 + T2))


def peak_tension(T1: np.ndarray, T2: np.ndarray) -> float:
    return float(np.max(np.maximum(T1, T2)))


def attunement_index(T1: np.ndarray, T2: np.ndarray) -> float:
    """High when tensions are anti-correlated (complementary dance)."""
    # Use a lag-1 cross-correlation over a window; anti-phase is the target.
    ccf = np.correlate(T1 - T1.mean(), T2 - T2.mean(), mode="full")
    ccf /= np.sqrt(np.sum((T1 - T1.mean()) ** 2) * np.sum((T2 - T2.mean()) ** 2))
    lags = np.arange(-len(T1) + 1, len(T1))
    # Find peak magnitude correlation and its lag
    idx = np.argmax(np.abs(ccf))
    return float(ccf[idx]), int(lags[idx])


def free_energy_proxy(T1: np.ndarray, T2: np.ndarray) -> float:
    """Lower when the pair collectively regulates tension."""
    return float(np.mean(T1 ** 2 + T2 ** 2))


def combined_variance(T1: np.ndarray, T2: np.ndarray) -> float:
    """Lower variance of combined tension = smoother co-regulation."""
    return float(np.var(T1 + T2))


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------

def plot_timeseries(scenarios: dict) -> None:
    fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
    colors = {"isolated": "#7b1fa2", "rigid": "#1565c0", "attuned": "#2e7d32"}

    for name, (T1, T2, A12, A21) in scenarios.items():
        color = colors[name]
        axes[0].plot(TIME, T1, color=color, alpha=0.7, label=f"{name} agent 1")
        axes[0].plot(TIME, T2, color=color, alpha=0.7, linestyle="--", label=f"{name} agent 2")
    axes[0].set_ylabel("Vitality tension $T(t)$")
    axes[0].set_title("Relational attunement: tension dynamics")
    axes[0].legend(ncol=2, fontsize=8)
    axes[0].grid(True, alpha=0.3)

    # Plot only attuned attention for clarity
    T1, T2, A12, A21 = scenarios["attuned"]
    axes[1].plot(TIME, A12, color="#c62828", label="Agent 1 → Agent 2")
    axes[1].plot(TIME, A21, color="#f9a825", label="Agent 2 → Agent 1")
    axes[1].set_ylabel("Attention $A(t)$")
    axes[1].set_title("Adaptive attention in attuned scenario (peaks at $t^*$)")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    # Combined system tension (sum) for all scenarios
    for name, (T1, T2, A12, A21) in scenarios.items():
        axes[2].plot(TIME, T1 + T2, color=colors[name], label=name)
    axes[2].set_xlabel("Time")
    axes[2].set_ylabel("Combined tension $T_1 + T_2$")
    axes[2].set_title("Lower combined tension = better co-regulation")
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "relational_attunement_timeseries.png", dpi=150)
    plt.close(fig)


def plot_phase_portrait(scenarios: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    titles = ["Isolated", "Rigid support", "Attuned"]
    names = ["isolated", "rigid", "attuned"]
    colors = {"isolated": "#7b1fa2", "rigid": "#1565c0", "attuned": "#2e7d32"}

    for ax, title, name in zip(axes, titles, names):
        T1, T2, _, _ = scenarios[name]
        ax.plot(T1, T2, color=colors[name], alpha=0.7)
        ax.plot(T1[0], T2[0], "o", color="black", label="start")
        ax.plot(T1[-1], T2[-1], "s", color="red", label="end")
        ax.set_xlabel("Agent 1 tension $T_1$")
        ax.set_ylabel("Agent 2 tension $T_2$")
        ax.set_title(title)
        ax.grid(True, alpha=0.3)
        ax.legend()

    fig.suptitle("Phase portraits: isolated vs rigid vs attuned coupling", fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "relational_attunement_phase_portrait.png", dpi=150)
    plt.close(fig)


def plot_metrics(scenarios: dict) -> None:
    names = list(scenarios.keys())
    mean_T = []
    peak_T = []
    free_E = []
    var_comb = []
    corr = []
    lags = []

    for name, (T1, T2, _, _) in scenarios.items():
        mean_T.append(mean_tension(T1, T2))
        peak_T.append(peak_tension(T1, T2))
        free_E.append(free_energy_proxy(T1, T2))
        var_comb.append(combined_variance(T1, T2))
        c, lag = attunement_index(T1, T2)
        corr.append(c)
        lags.append(lag)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    colors = ["#7b1fa2", "#1565c0", "#2e7d32"]

    axes[0, 0].bar(names, mean_T, color=colors)
    axes[0, 0].set_ylabel("Mean combined tension")
    axes[0, 0].set_title("Average vitality load")

    axes[0, 1].bar(names, peak_T, color=colors)
    axes[0, 1].set_ylabel("Peak tension")
    axes[0, 1].set_title("Maximum overload")

    axes[1, 0].bar(names, free_E, color=colors)
    axes[1, 0].set_ylabel("Free-energy proxy")
    axes[1, 0].set_title("Lower = better co-regulation")

    axes[1, 1].bar(names, var_comb, color=colors)
    axes[1, 1].set_ylabel("Variance of $T_1 + T_2$")
    axes[1, 1].set_title("Lower variance = smoother co-regulation")

    for ax in axes.flat:
        ax.tick_params(axis="x", rotation=15)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "relational_attunement_metrics.png", dpi=150)
    plt.close(fig)

    print("\nMetrics:")
    for name, m, p, f, v, c, lag in zip(names, mean_T, peak_T, free_E, var_comb, corr, lags):
        print(f"  {name:10s}: mean={m:.2f}, peak={p:.2f}, free_E={f:.2f}, var={v:.2f}, corr={c:.3f} @ lag={lag}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Simulating isolated agents...")
    isolated = simulate(attention_isolated, kappa=0.0)

    print("Simulating rigid support...")
    rigid = simulate(attention_rigid, kappa=1.5)

    print("Simulating attuned relationship...")
    attuned = simulate(attention_attuned, kappa=1.5)

    scenarios = {"isolated": isolated, "rigid": rigid, "attuned": attuned}

    print("Plotting time series...")
    plot_timeseries(scenarios)

    print("Plotting phase portraits...")
    plot_phase_portrait(scenarios)

    print("Plotting metrics...")
    plot_metrics(scenarios)

    print(f"Figures saved to {OUT_DIR}")


if __name__ == "__main__":
    main()
