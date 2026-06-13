#!/usr/bin/env python3
"""DMN-ECN flexible coupling simulation for creativity/insight.

This script implements the simplified DMN-ECN model from
`4_applications/creativity_innovation.md` and
`verifiable_units/vu_03_dmn_ecn.md`:

    tau_D dD/dt = -D + w_DD * sigma(D) - w_ED * sigma(E) + S_D(t) + eta_D
    tau_E dE/dt = -E + w_EE * sigma(E) + w_DE(t) * sigma(D) + S_E(t) + eta_E

The dynamic coupling weight w_DE(t) is low during incubation and surges
when DMN activation D exceeds a threshold while ECN is still low,
modelling the "Aha!" capture of a remote association by executive control.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = Path(__file__).resolve().parent

T_MAX = 30.0  # seconds
DT = 0.01  # seconds

SIGMOID = lambda x, beta=10.0, theta=0.5: 1.0 / (1.0 + np.exp(-beta * (x - theta)))


def dynamic_coupling(
    D: float,
    E: float,
    t: float,
    incubation_end: float = 10.0,
    w_DE_low: float = 0.15,
    w_DE_high: float = 1.2,
    D_threshold: float = 0.55,
    E_threshold: float = 0.35,
) -> float:
    """Return time-varying DMN->ECN coupling weight.

    During incubation the coupling is low.  If DMN is highly active while ECN
    is low, an insight event is triggered and coupling surges.
    """
    if t < incubation_end:
        return w_DE_low
    if D_threshold < D and E_threshold > E:
        # Insight capture: DMN content recruited by ECN.
        return w_DE_high
    return w_DE_low + 0.3 * (w_DE_high - w_DE_low)


def simulate(
    tau_D: float = 1.0,
    tau_E: float = 0.8,
    w_DD: float = 1.5,
    w_EE: float = 1.3,
    w_ED: float = 0.8,
    S_D: float = 0.12,
    S_E: float = 0.08,
    sigma_noise: float = 0.02,
    seed: int = 42,
    w_DE_low: float = 0.15,
    w_DE_high: float = 1.2,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Euler integration of the DMN-ECN creativity model.

    Returns
    -------
    t, D, E, w_DE, insight_flag : arrays
    """
    rng = np.random.default_rng(seed)
    n_steps = int(T_MAX / DT) + 1
    t = np.linspace(0, T_MAX, n_steps)
    D = np.zeros(n_steps)
    E = np.zeros(n_steps)
    w_DE = np.zeros(n_steps)
    insight = np.zeros(n_steps, dtype=bool)

    D[0] = 0.1
    E[0] = 0.1

    for i in range(1, n_steps):
        d = D[i - 1]
        e = E[i - 1]
        time = t[i - 1]

        w = dynamic_coupling(d, e, time, w_DE_low=w_DE_low, w_DE_high=w_DE_high)
        w_DE[i - 1] = w

        eta_D = rng.normal(0, sigma_noise)
        eta_E = rng.normal(0, sigma_noise)

        dDdt = (-d + w_DD * SIGMOID(d) - w_ED * SIGMOID(e) + S_D + eta_D) / tau_D
        dEdt = (-e + w_EE * SIGMOID(e) + w * SIGMOID(d) + S_E + eta_E) / tau_E

        D[i] = float(np.clip(d + dDdt * DT, 0.0, 1.0))
        E[i] = float(np.clip(e + dEdt * DT, 0.0, 1.0))

        insight[i] = w > 0.8 and d > 0.5 and e > 0.4

    w_DE[-1] = w_DE[-2]
    return t, D, E, w_DE, insight


def plot_timeseries(save_dir: Path = OUTPUT_DIR) -> None:
    """Plot a single DMN-ECN creativity trajectory."""
    t, D, E, w_DE, insight = simulate()

    fig, axes = plt.subplots(3, 1, figsize=(11, 9), sharex=True)

    axes[0].plot(t, D, label="DMN D(t)", color="#6a1b9a", linewidth=2)
    axes[0].plot(t, E, label="ECN E(t)", color="#00695c", linewidth=2)
    axes[0].axvspan(10, 30, color="gold", alpha=0.1, label="Evaluation window")
    axes[0].set_ylabel("Activation")
    axes[0].set_ylim(-0.05, 1.05)
    axes[0].set_title("DMN-ECN Creativity Dynamics")
    axes[0].legend(loc="upper right")
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(t, w_DE, label=r"DMN$\rightarrow$ECN coupling $w_{DE}(t)$", color="#e65100", linewidth=2)
    axes[1].set_ylabel("Coupling weight")
    axes[1].set_ylim(-0.05, 1.4)
    axes[1].legend(loc="upper right")
    axes[1].grid(True, alpha=0.3)

    axes[2].fill_between(t, 0, insight.astype(float), color="#2e7d32", alpha=0.4, label="Insight event")
    axes[2].set_ylabel("Insight flag")
    axes[2].set_xlabel("Time (s)")
    axes[2].set_ylim(-0.05, 1.05)
    axes[2].legend(loc="upper right")

    plt.tight_layout()
    out = save_dir / "dmn_ecn_creativity_timeseries.png"
    fig.savefig(out, dpi=150)
    print(f"Saved: {out}")
    plt.close(fig)


def plot_coupling_scan(save_dir: Path = OUTPUT_DIR) -> None:
    """Scan w_DE_high and DMN self-excitation w_DD; count insight events."""
    w_DD_vals = np.linspace(1.0, 2.0, 25)
    w_DE_high_vals = np.linspace(0.4, 1.6, 25)
    insight_count = np.zeros((len(w_DD_vals), len(w_DE_high_vals)))

    for i, w_DD in enumerate(w_DD_vals):
        for j, w_DE_high in enumerate(w_DE_high_vals):
            t, D, E, w_DE, insight = simulate(w_DD=w_DD, w_DE_high=w_DE_high, seed=42)
            # Count discrete insight bursts.
            insight_count[i, j] = np.sum(np.diff(insight.astype(int)) == 1)

    fig, ax = plt.subplots(figsize=(9, 6))
    im = ax.imshow(
        insight_count,
        aspect="auto",
        origin="lower",
        extent=[w_DE_high_vals[0], w_DE_high_vals[-1], w_DD_vals[0], w_DD_vals[-1]],
        cmap="YlGnBu",
        interpolation="nearest",
    )
    ax.set_xlabel(r"Insight coupling strength $w_{DE}^{high}$")
    ax.set_ylabel(r"DMN self-excitation $w_{DD}$")
    ax.set_title("Number of insight events across parameter space")
    fig.colorbar(im, ax=ax, label="insight bursts")
    plt.tight_layout()
    out = save_dir / "dmn_ecn_coupling_scan.png"
    fig.savefig(out, dpi=150)
    print(f"Saved: {out}")
    plt.close(fig)


def main() -> None:
    print("Running DMN-ECN creativity simulation...")
    plot_timeseries()
    plot_coupling_scan()
    print("Done.")


if __name__ == "__main__":
    main()
