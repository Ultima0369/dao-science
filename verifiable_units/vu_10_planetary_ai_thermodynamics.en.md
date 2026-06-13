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

## 3. Simulation

Run:

```bash
python simulations/planetary_ai_thermodynamics.py
```

Outputs:
- `simulations/ai_heat_equilibrium.png`
- `simulations/ai_heat_trajectory.png`
- `simulations/ai_heat_policy_comparison.png`

## 4. Key Findings

- Absorbed solar power sets the order-of-magnitude planetary boundary (~121,000 TW).
- At 30% annual growth, AI waste heat reaches 10% of the solar budget in roughly 40 years.
- Unconstrained exponential growth drives surface temperature out of the habitable range within decades to centuries.
- A thermodynamic stop/cap protocol keeps temperature near the pre-AI baseline.

## 5. Falsification Conditions

Evidence that would weaken or refute this claim:
1. Demonstration that Earth can maintain steady-state temperature at arbitrary waste-heat power without radiating the excess to space.
2. Violation of Landauer's principle (erasing information with zero thermodynamic entropy cost).
3. Large-scale engineering capability to dump AI waste heat directly into space without affecting the surface.
4. Observed automatic negative feedback that suppresses AI power growth before thermal limits matter.

---

> Back to claims register: [`CLAIMS.en.md`](../CLAIMS.en.md)
