"""Smoke tests for simulation scripts."""

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SIM_DIR = ROOT / "simulations"

SIMULATIONS = sorted(p for p in SIM_DIR.glob("*.py") if p.name != "__init__.py")

EXPECTED_OUTPUTS = {
    "dmn_insula_bistable.py": [
        "dmn_insula_timeseries.png",
        "dmn_insula_bifurcation.png",
        "dmn_insula_phase_portrait.png",
    ],
    "amygdala_pfc_hijack.py": [
        "amygdala_pfc_trajectories.png",
        "amygdala_pfc_parameter_space.png",
    ],
    "dmn_ecn_creativity.py": [
        "dmn_ecn_creativity_timeseries.png",
        "dmn_ecn_coupling_scan.png",
    ],
    "emergence_vs_phase_transition.py": [
        "ising_phase_transition.png",
        "boids_emergence.png",
        "emergence_vs_phase_comparison.png",
    ],
    "attention_precision_optimization.py": [
        "attention_static_weights.png",
        "attention_alpha_sweep.png",
        "attention_dynamic_switching.png",
        "attention_pathology.png",
    ],
    "ai_stopping_protocol.py": [
        "ai_stop_decision_boundary.png",
        "ai_stop_trajectory.png",
        "ai_stop_comparison.png",
    ],
    "carbon_silicon_symbiosis.py": [
        "carbon_silicon_cost_surface.png",
        "carbon_silicon_task_allocation.png",
        "carbon_silicon_strategy_comparison.png",
        "carbon_silicon_l3_interpretation.png",
        "carbon_silicon_heat_tradeoff.png",
    ],
    "de_ming_energy_allocation.py": [
        "de_ming_allocation_trajectory.png",
        "de_ming_cumulative_regret.png",
        "de_ming_change_detection.png",
    ],
    "planetary_ai_thermodynamics.py": [
        "ai_heat_equilibrium.png",
        "ai_heat_trajectory.png",
        "ai_heat_policy_comparison.png",
        "ai_heat_governance_dashboard.png",
        "ai_heat_observer_events.png",
        "ai_heat_observer_events.csv",
    ],
    "relational_attunement_oscillator.py": [
        "relational_attunement_timeseries.png",
        "relational_attunement_phase_portrait.png",
        "relational_attunement_metrics.png",
    ],
    "scale_moral_silence.py": [
        "scale_moral_silence.png",
    ],
}


@pytest.mark.parametrize("script_path", SIMULATIONS, ids=lambda p: p.name)
def test_simulation_runs(script_path: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        env={**dict(__import__("os").environ), "PYTHONDONTWRITEBYTECODE": "1"},
    )
    assert result.returncode == 0, (
        f"{script_path.name} failed with exit code {result.returncode}:\n"
        f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )

    expected = EXPECTED_OUTPUTS.get(script_path.name)
    if expected:
        for filename in expected:
            out = SIM_DIR / filename
            assert out.exists(), f"{script_path.name} did not produce {filename}"
