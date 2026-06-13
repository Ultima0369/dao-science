# VU-01: DMN-Insula Bistable Switching

## Verifiable Unit 01: DMN-Insula Bistable Switching

---

> **Evidence level**: Formal [F] + Simulation [S] + Neural evidence [N]  
> **Linked claim**: `CLAIMS.en.md` C07  
> **Related model**: `2_models/dmn_self_model.md` §3.4  
> **Simulation script**: `simulations/dmn_insula_bistable.py`

---

## 1. Formal statement

### 1.1 Core proposition

The competition between the Default Mode Network (DMN) and the insula/interoceptive network can be modelled as a bistable dynamical system. Meditation training shifts the system from the "narrative self" attractor to the "minimal self" attractor by strengthening insula drive and reducing DMN self-sustaining weights.

### 1.2 Mathematical objects and domain

State variables:
- $D(t) \in [0, 1]$: normalized DMN activation level
- $I(t) \in [0, 1]$: normalized insula/interoceptive network activation level

ODE system (`dmn_self_model.md`):

$$\tau_D \frac{dD}{dt} = -D + w_{DD} \cdot \sigma(D) - w_{ID} \cdot \sigma(I) + S_D(t)$$

$$\tau_I \frac{dI}{dt} = -I + w_{II} \cdot \sigma(I) - w_{DI} \cdot \sigma(D) + S_I(t) + \alpha \cdot B(t)$$

Where:
- $\sigma(x) = 1 / (1 + e^{-\beta(x - \theta)})$
- All coefficients have dimension $[t]^{-1}$
- $D$ and $I$ are dimensionless normalized activations

### 1.3 Boundary conditions

- $D(0), I(0) \in [0, 1]$
- $w_{DD}, w_{II} > 0$ (self-sustaining)
- $w_{ID}, w_{DI} > 0$ (mutual inhibition)

---

## 2. Simulation script

### 2.1 File location

`simulations/dmn_insula_bistable.py`

### 2.2 Functionality

- Integrates time series for two initial conditions (DMN-dominated vs insula-dominated)
- Scans the attention amplification coefficient $\alpha$ and plots a bifurcation diagram
- Plots phase portraits and nullclines to illustrate the bistable attractors

### 2.3 How to run

```bash
pip install -r simulations/requirements.txt
python simulations/dmn_insula_bistable.py
```

Outputs:
- `simulations/dmn_insula_timeseries.png`
- `simulations/dmn_insula_bifurcation.png`
- `simulations/dmn_insula_phase_portrait.png`

### 2.4 Key parameters (yielding bistability)

| Parameter | Value | Biological interpretation |
|-----------|-------|---------------------------|
| $\tau_D$ | 1.0 s | DMN time constant |
| $\tau_I$ | 0.8 s | Insula time constant |
| $w_{DD}$ | 1.6 | DMN self-sustaining weight |
| $w_{II}$ | 1.4 | Insula self-sustaining weight |
| $w_{ID}$ | 0.9 | Insula→DMN inhibition |
| $w_{DI}$ | 1.0 | DMN→insula inhibition |
| $S_D$ | 0.1 | DMN external drive |
| $S_I$ | 0.05 | Insula external drive |
| $\alpha$ | 1.0 | Breath-anchor amplification coefficient |
| $B$ | 0.4 | Breath-anchor intensity |

---

## 3. Experimental protocol draft

### 3.1 Research question

Does long-term meditation practice lower the switching threshold of the DMN-insula bistable system by reducing the DMN self-sustaining weight $w_{DD}$ and strengthening insula→DMN inhibition $w_{ID}$?

### 3.2 Participants

- Experimental group: experienced meditators (>1,000 hours practice), N = 25
- Control group: age-, sex-, and education-matched non-meditators, N = 25

### 3.3 Task and measures

**Task**: resting-state fMRI scan + breath-anchor task (5 minutes of rhythmic breath-focused attention).

**Primary measures**:
1. DMN-insula functional connectivity: negative correlation strength between PCC and anterior insula time series
2. Switching threshold: time from breath-anchor onset to first significant DMN activity decrease
3. Rumination Response Scale (RRS) score

**Statistical hypotheses**:
- $H_0$: No significant group difference in switching threshold or DMN-insula anti-correlation
- $H_1$: Meditators show a lower switching threshold and stronger DMN-insula anti-correlation
- Expected effect size: Cohen's $d \approx 0.8$ (medium to large effect)

### 3.4 Mapping to simulation

| Experimental measure | Simulation counterpart | Expected direction |
|----------------------|------------------------|--------------------|
| Lower switching threshold | $D^*$ decreases as $\alpha$ increases or $w_{DD}$ decreases | Meditators < controls |
| Stronger DMN-insula anti-correlation | $w_{ID}, w_{DI}$ increase | Meditators > controls |
| Reduced rumination | DMN attractor becomes shallower | Meditators < controls |

---

## 4. Falsification conditions

The following evidence would weaken or refute this proposition:

1. Long-term meditators and non-meditators show no difference in DMN-insula switching threshold under controlled conditions
2. Increasing insula drive (e.g., via respiratory feedback training) does not reduce DMN activity
3. The DMN-downregulation effect in meditators disappears after insula lesion or TMS suppression
4. Model simulations show that the system is not bistable for any parameter setting

---

## 5. Current limitations

- The simulation is a phenomenological model and has not been fitted to real fMRI time series
- Parameter values are currently theoretical and need calibration against literature or pilot data
- The experimental protocol has not passed ethical review or pilot validation

---

## 6. How to cite

> Project Dao.Science (2026). Verifiable Unit 01: DMN-Insula Bistable Switching. `verifiable_units/vu_01_dmn_insula.md`.
