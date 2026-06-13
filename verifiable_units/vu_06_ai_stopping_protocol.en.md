# VU-06: AI Stopping Protocol

## 可验证单元 VU-06：AI 知止协议

---

> **Evidence level**: Formal [F] + Simulation [S] + Meta-ethical/Normative [M]
> **Linked claim**: `CLAIMS.en.md` C15
> **Related model**: `4_applications/ai_governance.en.md`
> **Simulation script**: `simulations/ai_stopping_protocol.py`

---

## 1. Formal statement

### 1.1 Core proposition

AI systems should embed a "stopping" (*zhi* 止) protocol: when the expected free energy of the best feasible policy is too high, or when the catastrophic risk of any policy exceeds a threshold, the system chooses to pause and request human judgment rather than act blindly.

### 1.2 Mathematical objects and domain

Let there be $N$ candidate policies $\pi_i$. Each policy is characterised by three quantities:

- Expected reward: $E[r \mid \pi_i] \in [0, 1]$
- Catastrophic risk: $P(\text{catastrophe} \mid \pi_i) \in [0, 1]$
- Outcome ambiguity: $A(\pi_i) \in [0, 1]$

The expected free energy of policy $\pi_i$ is defined as:

$$G(\pi_i) = -E[r \mid \pi_i] + \lambda_R \, P(\text{catastrophe} \mid \pi_i) + \lambda_A \, A(\pi_i)$$

Where:
- $\lambda_R$: risk-aversion coefficient
- $\lambda_A$: ambiguity-aversion coefficient

The stopping decision rule is:

$$\text{stop} \iff \min_i G(\pi_i) > G_{\text{threshold}} \quad \text{or} \quad \max_i P(\text{catastrophe} \mid \pi_i) > R_{\text{threshold}}$$

If the system stops, it requests human intervention and receives a moderate but safe reward $r_{\text{stop}}$.

### 1.3 Boundary conditions

- Reward, risk, and ambiguity can be estimated (even if only probabilistically)
- A human-intervention mechanism exists whose reward is lower than most successful actions but higher than catastrophe
- The system's objectives include not only reward maximisation but also catastrophe avoidance

---

## 2. Simulation script

### 2.1 File location

`simulations/ai_stopping_protocol.py`

### 2.2 Functionality

- Generates a series of random decision problems, each containing multiple candidate policies
- Compares two agents:
  - **Greedy agent**: always selects the policy with the highest expected reward
  - **Stopping agent**: stops and requests human judgment when risk or free energy is too high
- Plots the decision boundary (stopping region in reward-risk space)
- Plots a single-episode trajectory comparison
- Uses Monte Carlo simulation to illustrate the safety-reward trade-off

### 2.3 How to run

```bash
pip install -r simulations/requirements.txt
python simulations/ai_stopping_protocol.py
```

Outputs:
- `simulations/ai_stop_decision_boundary.png`
- `simulations/ai_stop_trajectory.png`
- `simulations/ai_stop_comparison.png`

### 2.4 Key parameters

| Parameter | Value | Description |
|---|---|---|
| Candidate policies per problem | 5 | Simulates action space |
| Total problems | 500 | Per episode |
| Monte Carlo runs | 50 | Statistical stability |
| Risk-aversion coefficient $\lambda_R$ | 3.0 | Weight of catastrophe in $G$ |
| Ambiguity-aversion coefficient $\lambda_A$ | 1.0 | Weight of uncertainty in $G$ |
| Free-energy threshold $G_{\text{threshold}}$ | 0.5 | Free-energy level triggering stop |
| Risk threshold $R_{\text{threshold}}$ | 0.22 | Catastrophe probability triggering stop |
| Stopping reward $r_{\text{stop}}$ | 0.4 | Conservative reward for human intervention |

---

## 3. Expected results and interpretation

### 3.1 Decision boundary

In the reward-risk plane:
- Low-risk, high-reward region: the agent acts directly
- High-risk or low-reward/high-risk region: the agent stops
- The boundary is determined jointly by $G(\pi) = G_{\text{threshold}}$ and the risk threshold

**Key feature**: The stopping region is not a simple reward threshold but a composite judgment of free energy and risk.

### 3.2 Single trajectory

- Greedy agent: large reward fluctuations, frequent catastrophic events
- Stopping agent: drops to the stopping reward at dangerous problems, with catastrophic events significantly reduced

**Key feature**: Stopping is not "inaction"; it is handing control back to humans.

### 3.3 Monte Carlo comparison

Typical results (50 runs, 500 problems per run):
- Greedy agent: higher total reward, but also more catastrophes
- Stopping agent: lower total reward (due to frequent stopping), but a substantial reduction in catastrophes

**Key feature**: There is a quantifiable safety-reward trade-off; the stopping protocol exchanges some reward for a significant safety improvement.

---

## 4. Mapping to project theory

| Project concept | Simulation counterpart |
|---|---|
| Knowing when to stop (*zhi zhi bu dai* 知止不殆) | Active stop when $G$ or risk is too high |
| Expected free energy | $G(\pi) = -\text{reward} + \lambda_R \, \text{risk} + \lambda_A \, \text{ambiguity}$ |
| First-person irreducibility | Human judgment as a stopping reason that cannot be replaced internally by the system |
| Carbon-silicon symbiosis | AI knows when to return decision authority to carbon-based intelligence |
| Cost of deviation | Catastrophe from not stopping is the cost of deviating from Dao |

---

## 5. Experimental/empirical correspondences (draft)

### 5.1 AI safety

- The "refusal to answer" mechanism in large language models can be regarded as a simplified stopping protocol
- The disengagement mechanism in autonomous driving is a physical implementation of stopping
- Medical AI handing off to doctors when confidence is low is an industry application of the stopping protocol

### 5.2 Testable predictions

1. After introducing the stopping protocol, the system's catastrophe rate on high-risk tasks should decrease significantly.
2. The stopping thresholds $G_{\text{threshold}}$ and $R_{\text{threshold}}$ can be calibrated according to task risk preference.
3. A purely reward-driven system (without a stopping mechanism) performs worse on long-tail risk.

---

## 6. Falsification conditions

The following evidence would weaken or refute this proposition:

1. In all tested environments, introducing a stopping mechanism does not reduce catastrophe rate
2. Static rules can completely substitute for a dynamic stopping mechanism to solve all AI safety problems
3. The stopping protocol makes the system too conservative to complete any useful task
4. Human intervention delay or error is more dangerous than autonomous AI action (this may hold in certain specific domains)

---

## 7. Current limitations

- The simulation uses simplified scalar reward and risk; real AI systems face high-dimensional, structured outputs
- The metabolic/time cost of stopping is not modelled
- Adversarial environments or strategic deception are not addressed
- The human-intervention reward $r_{\text{stop}}$ is an arbitrary constant and does not reflect real human judgment quality

---

## 8. How to cite

> Project Dao.Science (2026). Verifiable Unit 06: AI Stopping Protocol. `verifiable_units/vu_06_ai_stopping_protocol.md`.

---

> Return to the project claims register: [`CLAIMS.en.md`](../CLAIMS.en.md)
