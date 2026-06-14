# Verifiable Unit 11: Scale and Moral Silence

> **Evidence class**: Formal [F] + Behavioral [B]
> **Linked claim**: `CLAIMS.en.md` C26
> **Linked file**: `1_first_principles/11_scale_and_moral_silence.en.md`
> **Simulation script**: `simulations/scale_moral_silence.py`

---

## 1. Formal Statement

For a given event $E$, moral response $M_s(E)$ varies with the observational scale $s$. When $s$ falls outside the range $[s_{\min}, s_{\max}]$ calibrated by everyday normative vocabulary, subjects exhibit **moral silence**: they still perceive the territory, but struggle to express a moral judgment with available language.

Formalized hypotheses:

$$
S(s) = \alpha \, \bigl(\ln s - \ln s_{\text{opt}}\bigr)^2 + S_0
\tag{11.1}
$$

$$
A(s) = A_{\max} \exp\!\left(-\frac{|\ln s - \ln s_{\text{opt}}|}{\tau}\right)
\tag{11.2}
$$

- $S(s)$: moral-silence index (higher = harder to articulate moral judgment).
- $A(s)$: action propensity (higher = more willing to act).
- $s_{\text{opt}}$: scale at which everyday normative language is best calibrated (e.g., community/city scale, $10^2$–$10^4$ people).

Predictions:
1. At $s \ll s_{\text{opt}}$ (personal trauma) and $s \gg s_{\text{opt}}$ (planetary or cosmological scales), $S(s)$ is higher and $A(s)$ is lower.
2. Near $s_{\text{opt}}$, $A(s)$ peaks and $S(s)$ reaches a minimum.

---

## 2. Operational Variables

| Variable | Operational definition | Measurement |
|---|---|---|
| Scale $s$ | Number of affected people / temporal horizon / spatial scope in the event description | Experimental manipulation: same event in 4 scale versions |
| Moral silence $S$ | "I find it hard to describe the moral nature of this event" 1–7 | 3-item scale, mean score |
| Response latency $T$ | Time to choose "good / bad / hard to judge" | Key-press reaction time (ms) |
| Action propensity $A$ | "I am willing to take a concrete action about this" 1–7 | Action-commitment scale + behavioral proxy |

---

## 3. Simulation Script

### 3.1 File

`simulations/scale_moral_silence.py`

### 3.2 Function

- Plots $S(s)$ and $A(s)$ as functions of scale $s$.
- Marks $s_{\text{opt}}$, $s_{\min}$, and $s_{\max}$ regions.
- Outputs `simulations/scale_moral_silence.png`.

### 3.3 Run

```bash
python simulations/scale_moral_silence.py
```

---

## 4. Experimental / Data Protocol (Draft)

### 4.1 Research Question

When the same moral event is described at different scales (personal, community, national, planetary, cosmic), do moral silence, judgment reaction time, and action propensity follow the hypothesized U-shaped / inverted-U-shaped patterns?

### 4.2 Design

- **Participants**: Adults 18–60, $N \geq 120$ ($\geq 30$ per between-subjects cell if needed).
- **Design**: Within-subject 5 (scale) × 3 (event type: fraud, environmental harm, resource allocation) mixed design.
- **Materials**: Each event written in 5 versions, differing only in affected population and spatiotemporal scope:
  - Personal: 1 person, today
  - Community: $10^2$ people, this week
  - National: $10^7$ people, one decade
  - Planetary: $10^9$ people, one century
  - Cosmic: all of human civilization, $10^8$ years
- **Procedure**:
  1. Read event description.
  2. Key-press judgment: good / bad / hard to judge; record RT.
  3. Complete moral-silence and action-propensity scales.
  4. Behavioral proxy: virtual donation, petition signature, or sharing intent.

### 4.3 Controls

- Latin-square order of the 5 scale versions.
- Match event severity, victim identifiability, and emotional arousal across scales via pilot ratings.
- Covary extreme political or religious orientation.

### 4.4 Primary Output Metrics

- Mean moral silence and SD per scale.
- Median RT per scale (after outlier removal).
- Action-propensity rating and behavioral conversion rate.
- Fitted curve parameters: $s_{\text{opt}}$, $\alpha$, $\tau$.

### 4.5 Statistical / Model Hypotheses

- $H_0$: Scale has no significant main effect on moral silence or action propensity.
- $H_1$: Moral silence follows a U-shaped quadratic relationship with scale; action propensity follows an inverted-U; the turning point lies at the community/national scale.
- Analysis: repeated-measures ANOVA + mixed-effects model + nonlinear least-squares fit.

### 4.6 Falsification Conditions

- If the cosmic-scale version produces the highest action propensity, the core hypothesis is falsified.
- If personal-trauma and cosmic scales do not differ in moral silence and both are lower than intermediate scales, the predicted direction is wrong.
- If RT does not correlate positively with moral-silence ratings, the "language-bandwidth limitation" mechanism is questionable.

---

## 5. Known Limitations

- Scale manipulation in the lab relies on text; ecological validity is limited.
- Cultural differences may shift $s_{\text{opt}}$ (collectivist vs. individualist framing).
- Behavioral proxies may not predict real-world action.

---

## 6. Relations to Other VUs

- `vu_01_dmn_insula.en.md`: moral silence may co-occur with insula-anterior cingulate responses.
- `vu_03_dmn_ecn.en.md`: scale switching may rely on flexible DMN-ECN coupling.
- `vu_10_planetary_ai_thermodynamics.en.md`: cosmological thermodynamic narratives are a typical trigger for moral silence.

---

*Last updated: 2026-06-14*
