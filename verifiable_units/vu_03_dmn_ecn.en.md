# VU-03: DMN-ECN Flexible Coupling and Insight

## Verifiable Unit 03: DMN-ECN Flexible Coupling and Insight

---

> **Evidence level**: Formal [F] + Simulation [S] + Neural evidence [N] + Behavioural prediction [B]  
> **Linked claim**: `CLAIMS.en.md` C25  
> **Related model**: `4_applications/creativity_innovation.md` §2.4  
> **Simulation script**: `simulations/dmn_ecn_creativity.py`

---

## 1. Formal statement

### 1.1 Core proposition

Creativity is not the product of the Default Mode Network (DMN) or the Executive Control Network (ECN) operating alone, but of their dynamic coupling. During incubation, the DMN freely associates at low coupling strength; when the DMN generates a candidate that highly matches the problem representation, the DMN→ECN coupling weight $w_{DE}(t)$ suddenly increases, the ECN "captures" that candidate and processes it precisely, and the subjective experience is an "Aha!" moment. Highly creative individuals are characterised not by stronger DMN or ECN activity, but by $w_{DE}(t)$'s ability to switch flexibly between low values (incubation) and high values (capture).

### 1.2 Mathematical objects and domain

State variables:
- $D(t) \in [0, 1]$: normalized DMN activation
- $E(t) \in [0, 1]$: normalized ECN activation

Coupled dynamical system (`creativity_innovation.md`):

$$\tau_D \frac{dD}{dt} = -D + w_{DD} \cdot \sigma(D) - w_{ED} \cdot \sigma(E) + S_D(t) + \eta_D$$

$$\tau_E \frac{dE}{dt} = -E + w_{EE} \cdot \sigma(E) + w_{DE}(t) \cdot \sigma(D) + S_E(t) + \eta_E$$

Where:
- $\sigma(x) = 1 / (1 + e^{-\beta(x - \theta)})$
- $w_{DE}(t)$: time-varying DMN→ECN coupling weight
- $\eta_D, \eta_E$: Gaussian noise terms
- All temporal coefficients have dimension $[t]^{-1}$; state variables are dimensionless

### 1.3 Boundary conditions

- $D(0), E(0) \in [0, 1]$
- $w_{DD}, w_{EE} > 0$ (self-sustaining)
- $w_{ED} > 0$ (ECN→DMN inhibition)
- $w_{DE}(t) \geq 0$, low during incubation and high during capture

---

## 2. Simulation script

### 2.1 File location

`simulations/dmn_ecn_creativity.py`

### 2.2 Functionality

- Simulates DMN-ECN coupled-system trajectories across an "incubation → capture → verification" cycle
- Dynamically switches $w_{DE}(t)$: low coupling (incubation) → high coupling (insight capture)
- Scans DMN self-excitation $w_{DD}$ and insight coupling $w_{DE}^{\text{high}}$, and counts insight events

### 2.3 How to run

```bash
pip install -r simulations/requirements.txt
python simulations/dmn_ecn_creativity.py
```

Outputs:
- `simulations/dmn_ecn_creativity_timeseries.png`
- `simulations/dmn_ecn_coupling_scan.png`

### 2.4 Key parameters

| Parameter | Value | Biological interpretation |
|-----------|-------|---------------------------|
| $\tau_D$ | 1.0 s | DMN time constant |
| $\tau_E$ | 0.8 s | ECN time constant |
| $w_{DD}$ | 1.5 | DMN self-sustaining |
| $w_{EE}$ | 1.3 | ECN self-sustaining |
| $w_{ED}$ | 0.8 | ECN→DMN inhibition |
| $w_{DE}^{\text{low}}$ | 0.15 | Low coupling during incubation |
| $w_{DE}^{\text{high}}$ | 1.2 | High coupling during insight capture |
| $S_D$ | 0.12 | Sustained problem-representation drive to DMN |
| $S_E$ | 0.08 | ECN baseline input |

---

## 3. Experimental protocol draft

### 3.1 Research question

In creative problem-solving tasks, do highly creative participants show a sudden increase in DMN-ECN functional connectivity immediately before insight, and does the magnitude of this increase predict subjective insight intensity and subsequent solution accuracy?

### 3.2 Participants

- High-creativity group: upper 25% scorers on creativity tests (e.g., Remote Associates Test / Alternate Uses Test), N = 30
- Control group: participants matched for educational background but with average creativity scores, N = 30

### 3.3 Task and measures

**Task**: compound remote associate task (CRA) or insight problems, recorded with fMRI or EEG.

**Primary measures**:
1. Sudden increase in DMN (PCC/mPFC)–ECN (dlPFC/IPS) functional connectivity 2–4 s before insight
2. Right anterior superior temporal gyrus (aSTG) gamma burst (~40 Hz) at insight onset
3. ACC gamma activity 300 ms before insight
4. Subjective insight-intensity rating and objective solution accuracy

**Statistical hypotheses**:
- $H_0$: No difference between high-creativity and control groups in pre-insight DMN-ECN coupling increase
- $H_1$: High-creativity group shows stronger pre-insight DMN-ECN coupling increase, positively correlated with accuracy
- Expected effect size: Cohen's $d \approx 0.7$–$0.9$

### 3.4 Mapping to simulation

| Experimental measure | Simulation counterpart | Expected direction |
|----------------------|------------------------|--------------------|
| Pre-insight surge in DMN-ECN connectivity | $w_{DE}(t)$ transitions from low to high | High-creativity > controls |
| DMN free association during incubation | High DMN activation under low $w_{DE}$ | High-creativity group shows larger DMN fluctuations |
| Post-insight ECN enhancement during verification | Sustained high $E(t)$ under high $w_{DE}$ | Positively correlated with accuracy |
| Creativity training effect | Increased dynamic range of $w_{DE}$ | More insight events after training |

---

## 4. Falsification conditions

The following evidence would weaken or refute this proposition:

1. After controlling for task difficulty, high-creativity and control participants show no difference in pre-insight DMN-ECN coupling increase
2. TMS suppression of dlPFC does not impair subjective insight reports, suggesting ECN capture is not necessary for insight
3. Model simulations show that no transient produced by varying $w_{DE}(t)$ corresponds to a reportable "Aha!" experience
4. The temporal coupling between insight experience and DMN-ECN connectivity is shown to be an artefact of respiration or head motion

---

## 5. Current limitations

- The simulation uses a simplified two-node model and does not include the parietal attention network, salience network, or other multi-network interactions
- The switching rule for $w_{DE}(t)$ is heuristic; it should be estimated from real data using state-space models
- The model does not distinguish "small insights" (local restructuring) from "large insights" (paradigm shifts)
- The experimental protocol needs pre-registration and multi-centre validation

---

## 6. How to cite

> Project Dao.Science (2026). Verifiable Unit 03: DMN-ECN Flexible Coupling and Insight. `verifiable_units/vu_03_dmn_ecn.md`.
