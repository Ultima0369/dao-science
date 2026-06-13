# VU-05: Attention as Precision Optimization

## 可验证单元 VU-05：注意力作为精度优化

---

> **Evidence level**: Formal [F] + Simulation [S] + Neural evidence [N] + Behavioural prediction [B]  
> **Linked claim**: `CLAIMS.en.md` C05  
> **Related model**: `2_models/attention_model.md`  
> **Simulation script**: `simulations/attention_precision_optimization.py`

---

## 1. Formal statement

### 1.1 Core proposition

Within the predictive coding framework, attention is equivalent to an optimization of the **precision** of prediction errors. The metaparameter α controls the distribution of attention between focal focusing (high α) and global awareness (low α):

- **High α → focal attention**: precision weights concentrate on the small number of most reliable channels, producing a winner-take-all pattern.
- **Low α → global awareness**: precision weights are close to uniformly distributed, allowing the system to monitor multiple information sources simultaneously.
- **Flexible α**: the system can dynamically switch between the two modes according to task demands and environmental reliability.

### 1.2 Mathematical objects and domain

Consider $N$ sensory channels, each providing a noisy observation of the hidden state $s(t)$:

$$o_i(t) = s(t) + \eta_i(t), \quad \eta_i \sim \mathcal{N}(0, \sigma_i^2)$$

The channel precision is $\gamma_i = 1/\sigma_i^2$. In predictive coding, the optimal precision weights satisfy:

$$w_i^* \propto \gamma_i = \frac{1}{\sigma_i^2}$$

This project proposes an α-controlled interpolation:

$$\mathbf{w}(\alpha) = \alpha \cdot \mathrm{softmax}(\beta \, \boldsymbol{\gamma}) + (1 - \alpha) \cdot \frac{1}{N}\mathbf{1}$$

Where:
- $\alpha \in [0, 1]$: focal-global metaparameter
- $\beta$: softmax inverse temperature, controlling selection sharpness in focal mode
- $\boldsymbol{\gamma}$: channel precision vector
- $\mathbf{1}$: all-ones vector

The hidden-state estimate is the weighted average:

$$\hat{s}(t) = \sum_i w_i \, o_i(t)$$

### 1.3 Boundary conditions

- Channel noise is known or can be estimated online.
- The hidden state is relatively stable on the observation timescale.
- Attention weights satisfy $\sum_i w_i = 1$.

---

## 2. Simulation script

### 2.1 File location

`simulations/attention_precision_optimization.py`

### 2.2 Functionality

- For a fixed multi-channel system, displays the precision-weight distribution under different values of α.
- Compares the result with the Bayesian-optimal weights $w_i^* \propto 1/\sigma_i^2$.
- Scans α and shows that estimation error decreases monotonically as focality increases.
- Simulates time-varying channel reliability and compares tracking performance between rigid and adaptive α.
- Simulates a single channel producing an unusually large outlier (attention hijack) and shows how a flexible precision system recovers.

### 2.3 How to run

```bash
pip install -r simulations/requirements.txt
python simulations/attention_precision_optimization.py
```

Outputs:
- `simulations/attention_static_weights.png`
- `simulations/attention_alpha_sweep.png`
- `simulations/attention_dynamic_switching.png`
- `simulations/attention_pathology.png`

### 2.4 Key parameters

| Parameter | Value | Biological interpretation |
|-----------|-------|---------------------------|
| Number of channels | 5 | Simulating multiple sensory channels |
| Channel noise σ | [0.5, 1.0, 2.0, 3.0, 5.0] | Decreasing channel reliability |
| α scan range | [0, 1] | From global to focal |
| Softmax β | 4.0 | Selection sharpness in focal mode |
| Simulation steps | 300–1000 | Depends on subplot |

---

## 3. Expected results and interpretation

### 3.1 Static weight allocation

- α = 0: all channel weights ≈ 0.2, global monitoring.
- As α increases: weights gradually shift toward low-noise channels (ch1, ch2).
- α = 1: weights approach the softmax distribution, producing a strong bias toward ch1.

**Key feature**: α continuously tunes the focality of the precision distribution.

### 3.2 Estimation error as a function of α

- Lower α produces noisier estimates (higher RMSE).
- Higher α brings estimates closer to Bayesian-optimal (lower RMSE).
- However, full focusing also renders the system sensitive to single-channel outliers; see the pathology demonstration.

**Key feature**: an optimal α exists that depends on the task noise structure.

### 3.3 Dynamic switching

When environmental reliability reverses midway:
- A fixed high α may still perform well if it happens to match the new reliability ordering.
- A fixed low α remains noisy throughout.
- An adaptive α (which estimates precision online from recent prediction errors) can stay near optimal continuously.

**Key feature**: flexible precision estimation is more robust to change than a rigid α.

### 3.4 Attention hijacking and recovery

When ch1 exhibits a large +6 outlier during t = 100..120:
- Rigid focusing (α = 1) is hijacked: the estimate is strongly pulled away.
- Rigid openness (α = 0) remains noisy but is not hijacked.
- The flexible system downregulates ch1 precision on the basis of recent prediction errors and recovers more quickly.

**Key feature**: “freely contract and expand” does not mean permanently high α; rather, it means dynamically adjusting to channel reliability.

---

## 4. Mapping to project theory

| Project concept | Simulation counterpart |
|-----------------|------------------------|
| Attention = precision optimization | Weights $w_i$ are driven by channel precision $\gamma_i$ |
| α parameter | Interpolation between uniform distribution and softmax focal distribution |
| 收 (focus) | α → 1, winner-take-all |
| 放 (global awareness) | α → 0, uniform monitoring |
| 自如 (flexibility) | Online precision update based on recent prediction errors |
| Fear/desire hijacking | A single channel’s precision is abnormally upweighted, locking the system |
| 痴 (fixation/rigidity) | α loses its dynamic range and cannot adjust to the environment |

---

## 5. Experimental/empirical correspondences (draft)

### 5.1 Neuroscience predictions

1. **Precision regulation axis**: activity patterns along the anterior cingulate cortex (ACC) → locus coeruleus (LC) → thalamic reticular nucleus (TRN) axis should vary with task focal demands.
2. **Meditation training**: long-term meditators should show faster α switching and larger DMN–task-positive network anti-correlation changes in focal-open switching tasks.
3. **ADHD**: can be modelled as excessive noise or excessively high switching cost in α regulation.
4. **Anxiety/depression**: can be modelled as α becoming rigidly fixed at high focality (anxious rumination) or low focality (depressive apathy).

### 5.2 Testable behavioural predictions

- In multi-sensory cue tasks, participants should rely more on low-noise channels, with weights approximating inverse variance.
- When a channel suddenly becomes unreliable, healthy participants should rapidly downweight it; anxious participants may show slower downweighting.

---

## 6. Falsification conditions

The following evidence would weaken or refute this proposition:

1. In multi-channel perceptual tasks, human attention allocation is independent of channel precision.
2. Increasing the precision of a channel does not increase the probability that it is attended.
3. Meditation training does not alter focal-global switching ability.
4. The nervous system lacks a neural gain-control mechanism corresponding to precision weighting.

---

## 7. Current limitations

- The simulation uses Gaussian noise and a scalar hidden state; real perception is hierarchical and nonlinear.
- The neural implementation of α has not been directly modelled in the simulation.
- Top-down task goals (the Query in Q/K/V attention) are not included.
- The metabolic cost of attention switching is not modelled.

---

## 8. How to cite

> Project Dao.Science (2026). Verifiable Unit 05: Attention as Precision Optimization. `verifiable_units/vu_05_attention_precision_optimization.md`.

---

> Return to the project claim register: [`CLAIMS.en.md`](../CLAIMS.en.md)
