# Verifiable Unit 09: De-Ming Energy Allocation Model

> **Evidence class**: Formal [F] + Simulation [S] + Behavioral prediction [B] + Meta-ethical [M]  
> **Linked claim**: `CLAIMS.en.md` C23  
> **Linked model**: `1_first_principles/10_de_and_ming.md`  
> **Simulation script**: `simulations/de_ming_energy_allocation.py`

---

## 1. Formal Statement

"De" is the attentional allocation of vital energy; "Ming" is the penetrating awareness that integrates yin-yang, distinguishes constants from variables, and outputs determined action. The De-Ming loop can be formalized as: allocate limited energy across competing goals (De), update beliefs about rewards and uncertainties from feedback (Ming), and re-allocate energy.

## 2. Core Equations

De (energy allocation):

$$a_i(t) = E_{\text{total}} \cdot \text{softmax}\left( \beta \cdot \frac{\mu_i(t)}{s_i(t) + \epsilon} \right)$$

Ming (change detection):

$$\text{PE}_i(t) = |o_i(t) - \mu_i(t)|$$

If $\text{PE}_i(t) > \theta \cdot s_i(t)$, flag surprise and update beliefs rapidly:

$$\mu_i \leftarrow \mu_i + \eta_{\text{surprise}} \cdot (o_i - \mu_i)$$
$$s_i^2 \leftarrow 2 \cdot \big[(1 - \eta_{\text{surprise}}) s_i^2 + \eta_{\text{surprise}} \text{PE}_i^2\big]$$

## 3. Simulation

Run:

```bash
python simulations/de_ming_energy_allocation.py
```

Outputs:
- `simulations/de_ming_allocation_trajectory.png`
- `simulations/de_ming_cumulative_regret.png`
- `simulations/de_ming_change_detection.png`

## 4. Key Findings

- De-Ming agent reallocates energy when the environment changes at t=100.
- Dogmatic (fixed phase-1-optimal) and Stubborn (single-task fixation) accumulate high regret after the change.
- Random allocation performs worst overall.
- Surprise-driven change detection is the Ming signature that enables adaptation.

## 5. Falsification Conditions

Evidence that would weaken or refute this claim:
1. A fixed allocation outperforms the De-Ming loop across environments.
2. Surprise detection does not accelerate adaptation to change.
3. Belief updates consistently increase deviation from reality (updates become veils).
4. Switching costs are negligible, making random and De-Ming strategies equivalent.

---

> Back to claims register: [`CLAIMS.en.md`](../CLAIMS.en.md)
