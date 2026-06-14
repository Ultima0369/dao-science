# Verifiable Unit 10: Planetary Thermodynamic Boundary for AI Expansion

> **Evidence class**: Formal [F] + Simulation [S] + Physical/First-principles [P]  
> **Linked claim**: `CLAIMS.en.md` C24  
> **Linked file**: `4_applications/ai_governance.md` Section 7  
> **Simulation script**: `simulations/planetary_ai_thermodynamics.py`

---

## 1. Formal Statement

Even if energy inputs for AI become effectively free (cheap photovoltaics, controlled fusion, etc.), the physical expansion of AI systems is constrained by Earth's ability to radiate waste heat into space. When global AI waste-heat power persistently exceeds Earth's outgoing infrared radiative capacity, surface temperature must rise.

## 2. Core Equations

Absorbed solar power:

$$P_\text{solar} = S_0 \cdot \pi R_\oplus^2 \cdot (1 - \alpha) \approx 1.21 \times 10^{17}\ \text{W}$$

Outgoing radiation:

$$P_\text{out}(T) = \sigma \cdot \varepsilon \cdot 4\pi R_\oplus^2 \cdot T^4$$

Equilibrium temperature with AI waste heat $P_\text{AI}$:

$$T_\text{eq}(P_\text{AI}) = \left( \frac{P_\text{solar} + P_\text{AI}}{\sigma \cdot \varepsilon \cdot 4\pi R_\oplus^2} \right)^{1/4}$$

Thermodynamic stopping protocol:

$$\text{stop} \iff P_\text{AI waste heat} > \eta \cdot P_\text{Earth radiative cooling}$$

Planetary Heat-Budget Occupancy (PHBO):

$$\rho_H(t) = \frac{P_\text{AI waste heat}(t)}{\eta \cdot P_\text{Earth radiative cooling}}$$

Traffic-light interpretation: safe $\rho_H < 0.5$, caution $0.5$–$0.9$, critical $0.9$–$1.0$, stop $\geq 1.0$.

## 3. Simulation

Run:

```bash
python simulations/planetary_ai_thermodynamics.py
```

Outputs:
- `simulations/ai_heat_equilibrium.png`
- `simulations/ai_heat_trajectory.png`
- `simulations/ai_heat_policy_comparison.png`
- `simulations/ai_heat_governance_dashboard.png`
- `simulations/ai_heat_observer_events.png`
- `simulations/ai_heat_observer_events.csv`

### 3.1 Hard-Boundary Observer

To move VU-10 from post-hoc simulation to online observability, the script includes `PowerThermalObserver`:

- Monitors three hard boundaries: $P_{\max}$ (max AI power), $T_{\max}$ (junction/ambient temperature ceiling), and $\max |dT/dt|$ (temperature rate limit).
- Crossing any boundary triggers `THROTTLE` (frequency scaling / migration) or `HALT` (shutdown), with events logged to `ai_heat_observer_events.csv`.
- Shares the same state semantics as the three-state breaker `BreakerFSM` in `src/dao_science/hardware.py`: `NORMAL → THROTTLE → HALT`. State transitions depend only on local sensor thresholds, so the breaker can act even if software locks up.

## 4. Experimental / Data Protocol (Draft)

### 4.1 Research Question

Based on published global energy, datacenter power, and climate data, if AI compute power maintains a high annual growth rate (≥30%), will its waste heat reach a significant fraction of Earth's infrared radiative cooling capacity within the next several decades, causing the Planetary Heat-Budget Occupancy (PHBO) to exceed governance thresholds?

### 4.2 Data Sources

- **Global AI power**: IEA electricity reports, major cloud-provider sustainability reports, academic estimates (e.g., Masanet et al., 2020; Wu, 2022).
- **Global total power**: World Bank energy statistics, BP Statistical Review of World Energy.
- **Climate and radiation data**: IPCC AR6 global mean surface temperature series, NASA GISS temperature anomalies, CERES satellite radiative fluxes.

### 4.3 Analysis Plan

1. **Historical calibration**: Calibrate initial values and growth rates in the simulation using 2010–2025 AI power data.
2. **Scenario projection**: Under 10%, 30%, and 50% annual growth rates, compute $P_\text{AI waste heat}$ and PHBO from 2025 to 2100.
3. **Temperature impact estimate**: Feed $P_\text{AI}$ as an additional heat source into a simplified energy-balance model (EBM) to estimate surface temperature rise, and compare sensitivity with complex GCM outputs.
4. **Policy sensitivity**: Test how different heat-budget thresholds $\eta$ (1%, 10%, 50%) affect the year at which the "red light" is triggered.

### 4.4 Primary Output Metrics

- AI waste heat as a percentage of global waste heat.
- PHBO = $P_\text{AI waste heat} / (\eta \cdot P_\text{Earth radiative cooling})$.
- Equilibrium temperature increase $\Delta T$ attributable to $P_\text{AI}$.
- "Red light" trigger year under each governance strategy.

### 4.5 Statistical / Model Hypotheses

- $H_0$: Under high-growth scenarios, PHBO remains below 0.5 (safe zone) throughout the 21st century.
- $H_1$: Under a 30% annual growth scenario, PHBO crosses 1.0 (stop threshold) around 2060–2070.
- Uncertainty propagation: Monte Carlo sampling over AI power trajectories and climate feedback parameters.

## 5. Key Findings

- Absorbed solar power sets the order-of-magnitude planetary boundary (~121,000 TW).
- At 30% annual growth, AI waste heat reaches 10% of the solar budget in roughly 40 years.
- Unconstrained exponential growth drives surface temperature out of the habitable range within decades to centuries.
- A thermodynamic stop/cap protocol keeps temperature near the pre-AI baseline.
- The PHBO dashboard turns abstract thermodynamic constraints into an actionable governance signal.

## 6. Falsification Conditions

Evidence that would weaken or refute this claim:
1. Demonstration that Earth can maintain steady-state temperature at arbitrary waste-heat power without radiating the excess to space.
2. Violation of Landauer's principle (erasing information with zero thermodynamic entropy cost).
3. Large-scale engineering capability to dump AI waste heat directly into space without affecting the surface.
4. Observed automatic negative feedback that suppresses AI power growth before thermal limits matter.

---

> Back to claims register: [`CLAIMS.en.md`](../CLAIMS.en.md)
