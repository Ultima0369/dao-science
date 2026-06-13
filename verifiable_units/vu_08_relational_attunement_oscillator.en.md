# Verifiable Unit 08: Relational Attunement as Coupled Oscillators

> **Evidence class**: Formal [F] + Simulation [S] + Behavioral prediction [B] + Meta-ethical [M]  
> **Linked claim**: `CLAIMS.en.md` C21  
> **Linked model**: `2_models/relational_attunement.md`  
> **Simulation script**: `simulations/relational_attunement_oscillator.py`

---

## 1. Formal Statement

Relational attunement is not control; it is the adaptive allocation of attentional precision so that the partner's vital tension can be released and transformed. This can be demonstrated with two coupled oscillators: isolated agents dissipate separately, rigid coupling amplifies and captures, while critical-handover attunement produces a dance of "soft overcoming hard" and "firmness within softness."

## 2. Core Equations

Tension dynamics for each agent:

$$\tau \frac{dT_i}{dt} = -T_i + I_i(t) + \kappa \cdot A_j(t) \cdot T_j(t)$$

Critical handover signal:

$$h(T, \dot{T}) = \sigma\big(T \cdot (-\dot{T}) - \theta\big)$$

Adaptive attention:

$$A_j(t) = h(T_i, \dot{T}_i) \cdot \big(1 - \sigma(T_j - T_{\text{max}})\big)$$

## 3. Simulation

Run:

```bash
python simulations/relational_attunement_oscillator.py
```

Outputs:
- `simulations/relational_attunement_timeseries.png`
- `simulations/relational_attunement_phase_portrait.png`
- `simulations/relational_attunement_metrics.png`

## 4. Key Findings

- Isolated agents oscillate independently and lack support in valleys.
- Rigid constant coupling locks phases but amplifies total energy.
- Attuned coupling provides timed support at the partner's $t^*$, keeping combined tension smooth without overload.
- Typical metrics: attuned mode matches isolated mode in mean/peak tension while preserving relational coordination.

## 5. Falsification Conditions

Evidence that would weaken or refute this claim:
1. Constant high coupling is always better than or equal to attuned coupling.
2. Ignoring the partner's $t^*$ reduces interpersonal tension more than precise handover.
3. Relational attunement is fully explained by linguistic content, independent of attentional timing.
4. No detectable critical handover point exists in dyadic systems.

---

> Back to claims register: [`CLAIMS.en.md`](../CLAIMS.en.md)
