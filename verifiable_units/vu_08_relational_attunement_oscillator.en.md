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

## 4. Experimental Protocol (Draft)

### 4.1 Research Question

In a controlled dyadic interaction task, when one partner precisely takes over leadership at the other's tension peak-and-decay inflection point ($t^*$), does this simultaneously produce: (a) higher physiological/behavioral synchrony, (b) lower subjective load, and (c) more coordinated interaction than constant high support or complete isolation?

### 4.2 Participants

- 60 pairs of adult participants (120 total), randomly paired.
- Exclusion criteria: severe psychiatric or neurological disorders, cardiovascular medication affecting autonomic measures.
- Informed consent obtained; participants are not informed about the "attunement" hypothesis beforehand.

### 4.3 Task and Conditions

**Task**: A cooperative rhythmic task. Each pair sits in a sound-attenuated booth and holds a force-sensing grip ring or follows a metronome while walking in place; periodic perturbations are delivered (e.g., abrupt noise in headphones, resistance pulses on a pedal).

**Three conditions** (counterbalanced within or between pairs):
1. **Isolated**: Participants sit back-to-back with no information exchange.
2. **Rigid support**: Participants face each other or are connected via a haptic belt that maintains constant high coupling.
3. **Attuned handover**: The system continuously estimates each participant's tension $T(t)$ and its derivative $\dot{T}(t)$. When one participant reaches a peak of $h(T, \dot{T})$ and the partner is not overloaded, the system prompts the partner to "take over."

### 4.4 Primary Measures

1. **Physiological synchrony**: Heart-rate variability (HRV) coherence, skin conductance (EDA) cross-correlation.
2. **Behavioral coordination**: Movement onset/offset asynchrony, phase-locking value (PLV).
3. **Subjective scales**: Interaction load (short NASA-TLX), connectedness (IRI or 5-item custom scale), felt safety.
4. **Model mapping**: $\kappa$ maps to support gain; $\theta$ maps to $t^*$ detection threshold; $T_{\max}$ maps to subjective overload point.

### 4.5 Statistical Hypotheses

- $H_0$: No significant differences among the three conditions in synchrony, load, or connectedness.
- $H_1$: Attuned handover outperforms isolated and rigid support on synchrony and connectedness, and shows lower load than rigid support.
- Expected effect size: Cohen's $d \approx 0.5$–$0.7$ (medium to large).

## 5. Key Findings

- Isolated agents oscillate independently and lack support in valleys.
- Rigid constant coupling locks phases but amplifies total energy.
- Attuned coupling provides timed support at the partner's $t^*$, keeping combined tension smooth without overload.
- Typical metrics: attuned mode matches isolated mode in mean/peak tension while preserving relational coordination.

## 6. Falsification Conditions

Evidence that would weaken or refute this claim:
1. Constant high coupling is always better than or equal to attuned coupling.
2. Ignoring the partner's $t^*$ reduces interpersonal tension more than precise handover.
3. Relational attunement is fully explained by linguistic content, independent of attentional timing.
4. No detectable critical handover point exists in dyadic systems.

---

> Back to claims register: [`CLAIMS.en.md`](../CLAIMS.en.md)
