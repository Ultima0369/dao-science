# VU-02: Amygdala-PFC Competition and the Golden Window

## Verifiable Unit 02: Amygdala-PFC Competition and the Golden Window

---

> **Evidence level**: Formal [F] + Simulation [S] + Neural evidence [N] + Behavioural prediction [B]  
> **Linked claim**: `CLAIMS.en.md` C06  
> **Related model**: `2_models/100ms_model.md` §4.4, §7  
> **Simulation script**: `simulations/amygdala_pfc_hijack.py`

---

## 1. Formal statement

### 1.1 Core proposition

Emotional stimuli trigger amygdala activity at around 74 ms, whereas a full conscious emotional experience forms only around 300–500 ms. Between these two events lies a "golden window" (~100–300 ms) in which prefrontal cortex (PFC) top-down regulation of the amygdala determines whether the emotional response is "hijacked" or "reappraised". Meditation training systematically improves intervention success within this window by strengthening PFC→amygdala inhibition weight $\alpha_T$, increasing amygdala→PFC transmission efficiency $\beta$, and shortening conduction delay $\delta$.

### 1.2 Mathematical objects and domain

State variables:
- $A(t) \in [0, 1]$: normalized amygdala activation
- $P(t) \in [0, 1]$: normalized prefrontal regulatory activation

Competition dynamics (`100ms_model.md`):

$$\frac{dA}{dt} = \alpha_B \cdot S(t) - \alpha_T \cdot P(t) \cdot A(t) - \gamma_A \cdot A(t)$$

$$\frac{dP}{dt} = \beta \cdot A(t - \delta) - \gamma_P \cdot P(t)$$

Where:
- $S(t)$: threat stimulus intensity (normalized)
- $\alpha_B$: bottom-up drive coefficient, $[\alpha_B] = [t]^{-1}$
- $\alpha_T$: top-down regulation coefficient, $[\alpha_T] = [t]^{-1}$
- $\gamma_A, \gamma_P$: decay rates, $[t]^{-1}$
- $\beta$: PFC response gain to amygdala alarm, $[t]^{-1}$
- $\delta$: amygdala→PFC conduction delay, $\delta \approx 100$–$200$ ms

### 1.3 Boundary conditions

- $A(0), P(0) \in [0, 1]$
- $\alpha_B, \alpha_T, \gamma_A, \gamma_P, \beta \geq 0$
- $\delta \geq 0$

---

## 2. Simulation script

### 2.1 File location

`simulations/amygdala_pfc_hijack.py`

### 2.2 Functionality

- Numerical Euler integration of the delay differential equation
- Contrasts two parameter regimes: weak $\alpha_T$ / long $\delta$ → amygdala hijacking; strong $\alpha_T$ / short $\delta$ → successful reappraisal
- Scans the $(\alpha_T, \delta)$ parameter space and plots a "hijack / mixed / regulation" phase diagram

### 2.3 How to run

```bash
pip install -r simulations/requirements.txt
python simulations/amygdala_pfc_hijack.py
```

Outputs:
- `simulations/amygdala_pfc_trajectories.png`
- `simulations/amygdala_pfc_parameter_space.png`

### 2.4 Key parameters

| Parameter | Hijack case | Regulation case | Biological interpretation |
|-----------|-------------|-----------------|---------------------------|
| $\alpha_B$ | 0.6 | 0.6 | Threat drive intensity |
| $\alpha_T$ | 0.08 | 0.45 | PFC→amygdala inhibition |
| $\beta$ | 0.22 | 0.35 | Amygdala→PFC response gain |
| $\gamma_A$ | 0.08 | 0.08 | Amygdala decay |
| $\gamma_P$ | 0.06 | 0.06 | PFC decay |
| $\delta$ | 120 ms | 80 ms | Conduction delay |

---

## 3. Experimental protocol draft

### 3.1 Research question

Does meditation training shorten emotion-awareness delay and reduce amygdala response peak in a backward-masked emotional-face task by decreasing amygdala-PFC regulation delay $\delta$ and increasing PFC→amygdala inhibition strength $\alpha_T$?

### 3.2 Participants

- Experimental group: long-term meditators (>1,000 hours), N = 25
- Control group: age-, sex-, and education-matched non-meditators, N = 25

### 3.3 Task and measures

**Task**: backward-masked fearful-face task (stimulus onset asynchrony, SOA = 17–33 ms) + cognitive reappraisal task.

**Primary measures**:
1. Peak amygdala response time to unconscious fearful faces (EEG/MEG source localisation)
2. PFC→amygdala effective connectivity strength (Dynamic Causal Modelling, DCM)
3. Subjective emotional intensity rating (reappraise vs watch)
4. Reaction time in emotional Stroop or dot-probe task

**Statistical hypotheses**:
- $H_0$: No group difference in amygdala peak, PFC→amygdala connectivity, or reappraisal effect
- $H_1$: Meditators show lower amygdala peak, stronger PFC→amygdala inhibitory connectivity, and larger reappraisal effect
- Expected effect size: Cohen's $d \approx 0.6$–$0.8$

### 3.4 Mapping to simulation

| Experimental measure | Simulation counterpart | Expected direction |
|----------------------|------------------------|--------------------|
| Lower amygdala peak | $\alpha_T$ increase or $\delta$ decrease reduces $A_{\max}$ | Meditators < controls |
| Stronger reappraisal effect | $\alpha_T$ increase | Meditators > controls |
| Shorter emotion-awareness delay | $\delta$ decrease | Meditators < controls |
| Weaker unconscious threat response | $\alpha_B$ decrease or early $\alpha_T$ increase | Meditators < controls |

---

## 4. Falsification conditions

The following evidence would weaken or refute this proposition:

1. Long-term meditators and non-meditators show no difference in amygdala response to backward-masked fearful faces
2. After controlling for reappraisal strategy, meditators do not show enhanced PFC→amygdala effective connectivity
3. Transcranial magnetic stimulation (TMS) temporarily suppressing dlPFC eliminates meditators' emotion-regulation advantage
4. Model simulations show that hijacking cannot be avoided regardless of how much $\alpha_T$ is increased

---

## 5. Current limitations

- The simulation uses deterministic/stochastic Euler integration and has not been fitted to real EEG/fMRI time series
- The delay term is approximated with a discrete history array; real neural conduction has a more complex distribution
- Parameter values are order-of-magnitude estimates from the literature and need calibration with pilot data
- The experimental protocol has not passed ethical review or pre-registration

---

## 6. How to cite

> Project Dao.Science (2026). Verifiable Unit 02: Amygdala-PFC Competition and the Golden Window. `verifiable_units/vu_02_amygdala_pfc.md`.
