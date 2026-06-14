#!/usr/bin/env python3
"""Scale and moral silence simulation.

Illustrates the hypothesized relationship between observational scale,
moral-silence (difficulty articulating a moral judgment), and action
propensity. The model assumes that everyday normative vocabulary is
calibrated around a community-scale optimum; both smaller (personal trauma)
and larger (planetary/cosmic) scales degrade articulability and action.

Run with:
    python simulations/scale_moral_silence.py

Outputs:
    simulations/scale_moral_silence.png
"""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = Path(__file__).parent

# Model parameters
S_OPT = 1e3          # Optimal scale (community/city)
ALPHA = 1.5          # Curvature of moral silence
S0 = 1.0             # Baseline moral silence
A_MAX = 1.0          # Maximum action propensity
TAU = 1.5            # Width of action propensity peak

# Discrete scale labels for annotation
SCALE_LABELS = {
    1: "Personal\n($10^0$)",
    1e2: "Community\n($10^2$)",
    1e4: "City/Nation\n($10^4$–$10^7$)",
    1e9: "Planetary\n($10^9$)",
    1e12: "Cosmic\n($10^{12}$+)",
}


def moral_silence(s: np.ndarray) -> np.ndarray:
    """Equation (11.1): U-shaped moral silence."""
    return ALPHA * (np.log(s / S_OPT)) ** 2 + S0


def action_propensity(s: np.ndarray) -> np.ndarray:
    """Equation (11.2): inverted-U action propensity."""
    return A_MAX * np.exp(-np.abs(np.log(s / S_OPT)) / TAU)


def plot_scale_moral_silence() -> None:
    s = np.logspace(-1, 13, 500)
    silence = moral_silence(s)
    action = action_propensity(s)

    fig, ax1 = plt.subplots(figsize=(10, 6))
    color_silence = "#c44e52"
    color_action = "#4c72b0"

    ax1.semilogx(s, silence, color=color_silence, lw=2.5, label="Moral silence $S(s)$")
    ax1.set_xlabel("Observational scale $s$ (affected population)", fontsize=12)
    ax1.set_ylabel("Moral silence $S(s)$", color=color_silence, fontsize=12)
    ax1.tick_params(axis="y", labelcolor=color_silence)
    ax1.set_ylim(0, max(silence) * 1.1)

    ax2 = ax1.twinx()
    ax2.semilogx(s, action, color=color_action, lw=2.5, linestyle="--", label="Action propensity $A(s)$")
    ax2.set_ylabel("Action propensity $A(s)$", color=color_action, fontsize=12)
    ax2.tick_params(axis="y", labelcolor=color_action)
    ax2.set_ylim(0, 1.1)

    # Mark optimal scale
    ax1.axvline(S_OPT, color="gray", linestyle=":", alpha=0.7)
    ax1.text(S_OPT, max(silence) * 0.95, "$s_{\\text{opt}}$", ha="center", fontsize=11)

    # Annotate example scale regions
    for value, label in SCALE_LABELS.items():
        ax1.axvline(value, color="lightgray", linestyle="-", alpha=0.4)
        ax1.text(value, max(silence) * 0.05, label, rotation=90, va="bottom", ha="right", fontsize=8)

    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2)

    ax1.set_title("Scale and Moral Silence: Hypothesized $S(s)$ and $A(s)$", fontsize=14, pad=20)
    fig.tight_layout()
    out_path = OUT_DIR / "scale_moral_silence.png"
    fig.savefig(out_path, dpi=150)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    plot_scale_moral_silence()
