# Project Dao.Science — Notation and Dimensional Conventions

## 项目符号与约定说明

---

## 1. Notation Overview

The table below lists core symbols that recur across Project Dao.Science modules. For each symbol we give: meaning, mathematical object/domain, dimension, and first appearance.

| Symbol | Meaning | Mathematical object / domain | Dimension | First appears in |
|--------|---------|------------------------------|-----------|------------------|
| $F$ | Variational free energy | Scalar; $F \geq -\ln P(o)$ | nats | `01_dao_as_process.md` |
| $G(\pi)$ / $G(\pi_\theta)$ | Expected free energy | Scalar; function of strategy $\pi$ or parameterized strategy $\pi_\theta$ | nats | `01_dao_as_process.md` |
| $\pi$ | Discrete action strategy | Discrete index or strategy vector | dimensionless | `01_dao_as_process.md` |
| $\theta \in \mathbb{R}^d$ | Continuous strategy parameters | Real vector | parameter-dependent | `01_dao_as_process.md` |
| $\Pi$ | Precision matrix | Positive semi-definite matrix | $[\text{variance}]^{-1}$ | `01_dao_as_process.md` |
| $\sigma(x)$ | Sigmoid / Softmax | $\sigma(x)=1/(1+e^{-x})$ or softmax | dimensionless | `01_dao_as_process.md` |
| $AB(t)$ | Awareness bandwidth | Scalar; $AB(t) \in [0, 1]$ | dimensionless | `02_one_as_bandwidth.md` |
| $R_{\text{DMN}}(t)$ | DMN standardized activity | Scalar; BOLD change relative to baseline | dimensionless (% change or z-score) | `02_one_as_bandwidth.md` |
| $R_0$ | DMN baseline level | Scalar | same as $R_{\text{DMN}}$ | `02_one_as_bandwidth.md` |
| $R_{\text{max}}$ | Maximum observed DMN change | Scalar | same as $R_{\text{DMN}}$ | `02_one_as_bandwidth.md` |
| $\alpha$ | Focus-global attention parameter | Scalar; $\alpha \in [0, 1]$ | dimensionless | `attention_model.md` |
| $a(t), A(t)$ | Amygdala activation | Scalar; normalized to $[0, 1]$ | dimensionless | `100ms_model.md` |
| $p(t), P(t)$ | Prefrontal regulation activation | Scalar; normalized to $[0, 1]$ | dimensionless | `100ms_model.md` |
| $\tau_a, \tau_p$ | Time constants | Scalar; $>0$ | seconds (s) | `100ms_model.md` |
| $\gamma_A, \gamma_P$ | Decay rates | Scalar; $>0$ | $\text{s}^{-1}$ | `100ms_model.md` |
| $D(t)$ | DMN activity level | Scalar; normalized to $[0, 1]$ | dimensionless | `dmn_self_model.md` |
| $I(t)$ | Insula / interoceptive activity | Scalar; normalized to $[0, 1]$ | dimensionless | `dmn_self_model.md` |
| $w_{ij}$ | Connection weight | Scalar | context-dependent | `100ms_model.md`, `dmn_self_model.md` |
| $SAB(t)$ | Social awareness bandwidth | Scalar; $SAB(t) \in [0, 1]$ | dimensionless | `social_cognition.md` |
| $\delta_{\text{RPE}}$ | Reward prediction error | Scalar | reward units | `02_flow_with_causes.md` |
| $\Pi_{\text{De}}$ | Precision matrix of De (virtue) | Positive semi-definite matrix | $[\text{variance}]^{-1}$ | `01_dao_as_process.md` |

---

## 2. Dimensional Conventions

### 2.1 Dimensionless activation levels

Neural activity variables in this project ($A, P, D, I, MNS_{\text{act}}, MEN_{\text{act}}$, etc.) are treated as **normalized activation levels**, usually in $[0, 1]$. Their physical counterparts may be:

- fMRI BOLD signal change relative to baseline (% signal change or z-score)
- Normalized neuronal population firing rate
- Normalized EEG/MEG band power

**Rationale**: Raw activity has different dimensions across brain regions (BOLD, firing rate, field potential). Direct addition would create dimensional inconsistency. After normalization, weights in competition/coupling equations have rate dimension $[t]^{-1}$, facilitating analysis and simulation.

### 2.2 Free energy and information-theoretic quantities

Variational free energy $F$ and expected free energy $G$ are measured in **nats** (natural-log units). If base-2 logarithms are used, the unit is bits; the conversion is $1\ \text{bit} = \ln 2\ \text{nats}$.

### 2.3 Precision matrix

The precision matrix $\Pi$ is the inverse of the covariance matrix, with dimension $[\text{variable unit}]^{-2}$. When variables are dimensionless normalized signals, the precision matrix is also dimensionless.

### 2.4 Time constants vs. decay rates

- Time constant ($\tau$): appears in the form $\tau \frac{dx}{dt} = \dots$, dimension $[t]$.
- Decay rate ($\gamma$): appears in the form $\frac{dx}{dt} = \dots - \gamma x$, dimension $[t]^{-1}$.

This project consistently uses:
- $\tau$ for time constants
- $\gamma$ for decay rates

This avoids confusion from using $\tau$ for both.

---

## 3. Evidence-Level Badges

To distinguish "formalization" from "verification," this project introduces five evidence-status badges. Each core proposition should be labeled with its current evidence level at first appearance.

| Badge | Level | Meaning | Example |
|-------|-------|---------|---------|
| **F** | Formal | Pure formalization/mathematical analogy; not yet validated by simulation or experiment | $\text{Dao} \equiv -\nabla_\theta G(\pi_\theta)$ |
| **S** | Simulation | Runnable simulation exists but has not been compared to behavioral/neural data | Numerical integration of DMN-insula bistable ODE |
| **B** | Behavioral | Derives testable behavioral predictions but experiment not yet completed | 100ms model's predicted intervention-success curve |
| **N** | Neural | Neuroscience literature or data supports its neural correlate | DMN down-regulation during meditation (Brewer et al., 2011) |
| **M** | Meta-ethical / Normative | Contains normative claims not purely empirically falsifiable | "Knowing when to stop" as an AI halting standard |

**Usage format**: Label at the start of a file or after key equations, e.g.:

> $$\text{Dao} \equiv -\nabla_\theta G(\pi_\theta) \quad \text{[F]}$$

> Long-term meditators show enhanced DMN-TPN anti-correlation \quad \text{[N]}

---

## 4. "Metaphor—Model" Declaration Template

Every core mapping should explicitly state its operational proxy, domain of validity, and falsification condition:

```markdown
**Mapping claim**: X ≈ Y
- **Operational proxy**: How to measure X and Y
- **Domain of validity**: Under what conditions the mapping holds
- **Falsification condition**: What evidence would weaken the mapping
- **Evidence level**: [F/S/B/N/M]
```

---

## 5. Common Pitfalls

1. **Do not interpret $-\nabla_\pi G(\pi)$ as differentiating with respect to a discrete strategy index.** In standard active inference $\pi$ is often a discrete index; taking a gradient with respect to a discrete index has no standard mathematical meaning. Use the continuous parameterization $-\nabla_\theta G(\pi_\theta)$, or the discrete selection form $\arg\min_\pi G(\pi)$.

2. **Do not treat $AB(t)$ as capacity minus resources.** $R_{\text{DMN}}$ is not a resource amount that can be directly subtracted from $C_{\text{max}}$. Use the normalized form $AB(t) = 1 - [R_{\text{DMN}}(t) - R_0]/[R_{\text{max}} - R_0]$, so that $AB(t)$ is a dimensionless relative available proportion.

3. **Cross-terms in competition equations must have consistent dimensions.** When variables from different brain regions are added or multiplied, normalize them to a dimensionless interval first and make the dimensions of all coefficients explicit.

4. **Parameters in softmax must remain vector-consistent.** In $P(\pi) = \sigma(-\gamma \cdot G(\pi))$, $G(\pi)$ must be a vector indexed by strategy; do not feed a global scalar $\min_\pi G(\pi)$ into softmax, or all strategy probabilities will be identical.

---

*This file is updated as the project evolves. Last updated: 2026-06-13.*

> 返回中文版：[`NOTATION.md`](NOTATION.md)
