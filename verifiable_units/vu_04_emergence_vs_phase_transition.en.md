# VU-04: Emergence Is Not Phase Transition

## 可验证单元 VU-04：涌现 ≠ 相变

## Verifiable Unit 04: Emergence Is Not Phase Transition

---

> **Evidence level**: Formal [F] + Simulation [S] + Meta-ethical/Normative [M]  
> **Linked claim**: `CLAIMS.en.md` C10  
> **Related model**: `1_first_principles/06_emergence.en.md`  
> **Simulation script**: `simulations/emergence_vs_phase_transition.py`

---

## 1. Formal statement

### 1.1 Core proposition

Emergence and phase transition are two distinct kinds of macroscopic order-generation mechanisms:

- **Phase transition**: The system state jumps because an external control parameter crosses a threshold; the local rules of microscopic units remain unchanged, and only global statistical quantities change.
- **Emergence**: The macroscopic properties of the system arise from internal organisational relations; these properties do not exist in isolated units, nor are they jumps triggered by a single external threshold.

### 1.2 Mathematical objects and domain

**Phase-transition prototype**: 2D Ising model

$$H = -J \sum_{\langle i,j \rangle} s_i s_j, \quad s_i \in \{-1, +1\}$$

Control parameter: temperature $T$ (or $\beta = 1/T$).  
Order parameter: magnetisation $|m| = |\frac{1}{N}\sum_i s_i|$.  
Critical temperature (exact solution for the infinite lattice):

$$T_c = \frac{2}{\ln(1+\sqrt{2})} \approx 2.269$$

**Emergence prototype**: Boids flocking model

Each individual's velocity update is synthesised from three local rules:

1. **Alignment**: $\vec{v}_i^{\text{align}} = \frac{1}{|N_i|}\sum_{j \in N_i} \vec{v}_j$
2. **Cohesion**: $\vec{v}_i^{\text{coh}} = \frac{1}{|N_i|}\sum_{j \in N_i} \vec{p}_j - \vec{p}_i$
3. **Separation**: $\vec{v}_i^{\text{sep}} = -\sum_{j: d_{ij}<d_0} (\vec{p}_j - \vec{p}_i)$

Where $N_i$ is the perceptual neighbourhood of individual $i$. Control parameter: alignment weight $w_{\text{align}}$.  
Order parameter: polarisation $\phi = \|\frac{1}{N}\sum_i \hat{v}_i\| \in [0,1]$.

### 1.3 Discrimination criteria

| Feature | Phase transition | Emergence |
|---|---|---|
| Driver | External control parameter crosses threshold | Internal local rules act continuously |
| Order-parameter curve | Jump/singularity at the critical point | Smooth growth with interaction strength |
| Isolated unit | Has the same local rules as the whole | Does not possess the whole-level property |
| Reducibility | In principle reducible to the microscopic partition function | Macroscopic property depends on relational structure, not reducible to a single individual |
| Examples | Ferromagnetic–paramagnetic transition, water freezing | Bird flocks, ant colonies, consciousness? |

---

## 2. Simulation script

### 2.1 File location

`simulations/emergence_vs_phase_transition.py`

### 2.2 Functionality

- Performs Metropolis sampling of the 2D Ising model and plots magnetisation versus temperature
- Numerically simulates the Boids model and plots polarisation versus alignment weight
- Compares the morphological differences between the two order-generation mechanisms side by side

### 2.3 How to run

```bash
pip install -r simulations/requirements.txt
python simulations/emergence_vs_phase_transition.py
```

Outputs:
- `simulations/ising_phase_transition.png`
- `simulations/boids_emergence.png`
- `simulations/emergence_vs_phase_comparison.png`

### 2.4 Key parameters

**Ising model**

| Parameter | Value | Interpretation |
|---|---|---|
| Lattice size | $40 \times 40$ | Finite-size effects are evident, but sufficient to demonstrate the phase transition |
| Equilibration steps | $10^5$ | Metropolis thermalisation |
| Samples | 30 | Averaged at each temperature |
| Temperature range | $T \in [1.5, 3.5]$ | Spans the theoretical critical temperature |
| Critical temperature (infinite lattice) | $T_c \approx 2.269$ | Reference line |

**Boids model**

| Parameter | Value | Interpretation |
|---|---|---|
| Number of individuals | 200 | Sufficient to exhibit collective behaviour |
| Domain | $60 \times 60$ | Periodic boundary |
| Perception radius | 15 | Local interaction range |
| Separation radius | 1.5 | Collision avoidance |
| Maximum speed | 2.0 | Normalised units |
| Separation weight | 0.1 | Weak separation, allowing aggregation |
| Cohesion weight | 0.005 | Weak cohesion |
| Alignment-weight scan | $[0, 0.8]$ | Internal interaction strength |
| Equilibration steps | 300 | Discard transients |
| Sampling steps | 300 | Average polarisation |

---

## 3. Expected results and interpretation

### 3.1 Ising model

- Low-temperature region ($T < T_c$): the system spontaneously chooses up or down magnetisation, $|m| > 0$
- Critical region ($T \approx T_c$): magnetisation drops rapidly under finite-size conditions
- High-temperature region ($T > T_c$): thermal fluctuations destroy long-range order, $|m| \approx 0$

**Key feature**: A steep transition occurs near $T_c$; the transition is driven by the external temperature parameter.

### 3.2 Boids model

- $w_{\text{align}} = 0$: individuals move randomly, polarisation close to 0
- $w_{\text{align}}$ increases: local alignment produces flocks, polarisation rises smoothly
- Large $w_{\text{align}}$: a stable global flock forms, polarisation saturates

**Key feature**: Polarisation grows continuously with the internal interaction parameter; flock as a whole-level property does not exist in an isolated individual.

### 3.3 Mapping to project claims

| Project claim | Simulation counterpart |
|---|---|
| Emergence ≠ phase transition | The two curves have different shapes: one jumps at an external threshold, the other grows smoothly with internal interaction strength |
| Emergence is a novel property of relational structure | The Boids flock cannot be read off from the rules of a single individual |
| Phase transition is a parameter-driven state flip | Ising magnetisation flips at $T_c$ |

---

## 4. Experimental / empirical correspondence (draft)

### 4.1 Neuroscience

- **Phase-transition-like phenomena**: seizure thresholds, wakefulness–anaesthesia transitions (possibly)
- **Emergence-like phenomena**: gamma synchrony, dynamic coupling patterns between the default mode network and the executive control network

### 4.2 Organisational / social systems

- **Phase-transition-like phenomena**: market crashes at critical points, panic outbreaks
- **Emergence-like phenomena**: team culture, innovation climate, trust networks

### 4.3 Testable predictions

1. A genuinely emergent property should satisfy: **after removing or altering local interaction rules, the macroscopic property disappears or changes, rather than merely shifting the parameter threshold**.
2. A phase-transition property should satisfy: **near the critical point the system is highly sensitive to small perturbations, and far from the critical point it is almost entirely determined by the control parameter**.

---

## 5. Counterfactual conditions

The following evidence would weaken or overturn this proposition:

1. All phenomena classified as "emergence" are shown to be reducible to a phase transition in some external control parameter
2. The flocking behaviour of Boids-type models is shown to be merely a disguised phase transition (e.g., an unidentified order-parameter threshold exists)
3. Macroscopic properties such as consciousness and culture are shown to be completely determined by thresholds of underlying physical parameters
4. Complex-systems science proves that strong emergence does not exist and that weak emergence is mathematically equivalent to phase transition

---

## 6. Current limitations

- The simulations are minimal models; real systems are usually mixtures of phase transition and emergence
- The Ising model on a $40 \times 40$ lattice has obvious finite-size noise
- The Boids model has not been fitted to real animal flocking data
- "Emergence" remains philosophically contested between strong and weak versions; this simulation only demonstrates the quantitative features of weak emergence

---

## 7. How to cite

> Project Dao.Science (2026). Verifiable Unit 04: Emergence Is Not Phase Transition. `verifiable_units/vu_04_emergence_vs_phase_transition.md`.

---

> Return to project claim registry: [`CLAIMS.en.md`](../CLAIMS.en.md)
