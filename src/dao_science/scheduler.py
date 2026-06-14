"""Wave-frequency cluster scheduler simulator.

Models a grid of compute nodes where each node follows its own sinusoidal
frequency/phase schedule. The global power budget is fixed; the simulator
compares emergent properties of synchronous clocking versus wave-like phasing
(e.g., lower power-variance and better thermal entropy).
"""

from __future__ import annotations

import numpy as np
import numpy.typing as npt

FloatArray = npt.NDArray[np.float64]

__all__ = ["FloatArray", "WaveScheduler"]


class WaveScheduler:
    """Discrete-event-ish scheduler for wave-frequency cluster operation.

    Args:
        shape: 2-D grid dimensions (rows, cols).
        total_power_budget: Total power to distribute across nodes.
        base_freq: Baseline operating frequency (arbitrary units).
        wave_speed: Angular speed of the travelling phase wave.
        wave_amp: Amplitude of the frequency perturbation.
    """

    def __init__(
        self,
        shape: tuple[int, int],
        total_power_budget: float,
        base_freq: float = 1.0,
        wave_speed: float = 0.5,
        wave_amp: float = 0.3,
    ) -> None:
        self.shape = shape
        self.total_power_budget = total_power_budget
        self.base_freq = base_freq
        self.wave_speed = wave_speed
        self.wave_amp = wave_amp
        self.n_nodes = shape[0] * shape[1]

    def phi(self, i: int, j: int, t: float) -> float:
        """Phase propagation function for node (i, j) at time t."""
        return float(
            self.base_freq
            + self.wave_amp
            * np.sin(self.wave_speed * t - 0.5 * (i + j))
        )

    def step(self, t: float) -> FloatArray:
        """Return the normalized power allocation grid at time t."""
        grid = np.zeros(self.shape, dtype=np.float64)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                grid[i, j] = self.phi(i, j, t)
        # Normalize to total power budget (guard against zero sum).
        total = grid.sum()
        if total <= 0:
            grid[:] = self.total_power_budget / self.n_nodes
        else:
            grid = grid / total * self.total_power_budget
        return grid

    def metrics(self, trace: FloatArray) -> dict[str, float]:
        """Aggregate metrics over a time trace of grids.

        Args:
            trace: Array of shape (time_steps, rows, cols).

        Returns:
            ``power_smoothness``: std-dev of total power over time.
            ``thermal_entropy``: Shannon entropy of the final spatial distribution.
            ``throughput_variance``: variance of the whole trace.
        """
        trace_arr = np.asarray(trace, dtype=np.float64)
        final = trace_arr[-1]
        final_sum = final.sum()
        if final_sum <= 0:
            thermal_entropy = 0.0
        else:
            p = final / final_sum
            p = p[p > 0]
            thermal_entropy = float(-np.sum(p * np.log(p)))
        return {
            "power_smoothness": float(np.std(trace_arr.sum(axis=(1, 2)))),
            "thermal_entropy": thermal_entropy,
            "throughput_variance": float(np.var(trace_arr)),
        }
