# Engineering API

`src/dao_science/` maps formal objects from `NOTATION.md` and `verifiable_units/` into importable Python functions and classes. These are stateless, lightweight, composable algorithmic stubs that create a traceable chain from symbol → code → data across simulations, audits, and experimental protocols.

---

## Installation and Import

```bash
pip install -e .
```

```python
from dao_science.core import awareness_bandwidth, cost_of_deviation
from dao_science.experience import AuditableMemory, ExperienceRecord
from dao_science.scheduler import WaveScheduler
from dao_science.hardware import BreakerFSM, SensorReading
```

See [`examples/`](https://github.com/Ultima0369/dao-science/tree/main/examples) for runnable integration examples.

---

## `dao_science.core`

Python stubs for core formal objects.

| Function | Formal object | Description |
|---|---|---|
| `sigmoid(x)` | $\sigma(x)$ | Logistic sigmoid |
| `softmax(x)` | $\sigma(\mathbf{x})$ | Numerically stable softmax |
| `expected_free_energy(kl, preference)` | $G(\pi)$ | Expected free energy (EFE) |
| `policy_selection(free_energies, gamma)` | $P(\pi)=\sigma(-\gamma G(\pi))$ | Soft-max policy selection |
| `dao_gradient_step(theta, grad_g, eta)` | $\theta_{t+1}=\theta_t-\eta\nabla_\theta G$ | Parameter update along negative gradient |
| `gradient_flow(theta, grad_func, lr)` | Same as above | Higher-order wrapper accepting a gradient callable |
| `awareness_bandwidth(r_dmn, r0, rmax)` | $AB(t)$ | Normalized awareness bandwidth |
| `precision_weighted_update(mu, pe, pi)` | $\mu+\pi\cdot\varepsilon$ | Precision-weighted belief update |
| `cost_of_deviation(g_actual, g_optimal)` | $\text{Cost}(\pi_{\text{dev}})$ | Cost of deviating from the optimal policy |
| `wu_wei_threshold(grad_norm, tau)` | $\|\nabla_\theta G\| < \tau$ | Wu-wei threshold predicate |
| `de_precision_matrix(dim)` | $\Pi_{\text{De}}$ | De precision matrix (identity stub) |
| `reward_prediction_error(actual, expected)` | $\delta_{\text{RPE}}$ | Reward prediction error |
| `impermanence_corrected_rpe(actual, expected, kappa)` | $\text{RPE}_{\text{suiyuan}}$ | Impermanence-corrected RPE |
| `social_awareness_bandwidth(ab, mns, men, ai_shared, dmn_self, weights)` | $SAB(t)$ | Social awareness bandwidth |
| `de_ming_allocation(mu, sigma, ...)` | De-Ming energy allocation | Allocate energy by expected reward and uncertainty |
| `critical_handover_signal(...)` | $h(T, \dot T)$ | Critical handover signal for relational attunement |
| `planetary_heat_budget_occupancy(...)` | $\rho_H$ | Planetary heat-budget occupancy |

---

## `dao_science.experience`

Auditable experience memory. Maps the "practice-as-proof" methodology into a retrievable, auditable data structure.

- `ExperienceRecord`: a single experience sample (timestamp, context hash, decision, outcome, confidence, audit log).
- `AuditableMemory`: context-hash-indexed store with `store()`, `retrieve()`, `audit()`, and `refresh_if_needed()`.

```python
memory = AuditableMemory()
memory.store(ExperienceRecord(
    timestamp="2026-06-14T00:00:00Z",
    context_hash="market-scam",
    decision="warn-elder",
    outcome=0.8,
    confidence=0.7,
))
print(memory.audit("market-scam"))
```

---

## `dao_science.scheduler`

Wave-frequency cluster scheduler simulator. Given a 2-D grid of nodes and a fixed total power budget, it simulates global synchronous clocking versus travelling-wave phasing through aggregate metrics: power smoothness, thermal entropy, and throughput variance.

- `WaveScheduler(shape, total_power_budget, ...)`
- `phi(i, j, t)`: phase-propagation function for a node.
- `step(t)`: normalized power-allocation grid at time `t`.
- `metrics(trace)`: aggregate metrics from a time trace.

---

## `dao_science.hardware`

Hardware abstraction layer + three-state breaker. Defines abstract `ThermalSensor`, `PowerController`, and `HardwareBreaker` interfaces; `BreakerFSM` transitions independently through `NORMAL → THROTTLE → HALT` based only on local sensor thresholds.

```python
breaker = BreakerFSM(p_max=100.0, t_max=80.0, dtdt_max=10.0)
reading = SensorReading(p_watts=150.0, t_junction=70.0, dt_dt=5.0)
assert breaker.transition(reading).name == "THROTTLE"
```

---

## Design Principles

1. **Stateless**: no module-level mutable globals, enabling parallel execution and easy testing.
2. **Typed**: uses `numpy.typing.NDArray` and Python type hints; checked with `mypy src tests`.
3. **Testable**: every public function/method has a corresponding case in `tests/test_core.py`.
4. **Traceable**: function names and equation references align with definitions in `NOTATION.md` and `verifiable_units/`.

---

> Return to navigation: [`0_motivation/project_map.md`](../0_motivation/project_map.md)
