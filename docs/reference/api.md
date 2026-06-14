# 工程接口（Engineering API）

`src/dao_science/` 把 `NOTATION.md` 与 `verifiable_units/` 中的形式化对象映射为可导入的 Python 函数与类。它们都是无状态、轻量、可组合的算法存根，用于在仿真、审计与实验协议之间建立「符号 → 代码 → 数据」的可追溯链。

---

## 安装与导入

```bash
pip install -e .
```

```python
from dao_science.core import awareness_bandwidth, cost_of_deviation
from dao_science.experience import AuditableMemory, ExperienceRecord
from dao_science.scheduler import WaveScheduler
from dao_science.hardware import BreakerFSM, SensorReading
```

完整可运行示例见 [`examples/`](https://github.com/Ultima0369/dao-science/tree/main/examples)。

---

## `dao_science.core`

核心数学对象的 Python 存根。

| 函数 | 对应形式化对象 | 说明 |
|---|---|---|
| `sigmoid(x)` | $\sigma(x)$ | Logistic sigmoid |
| `softmax(x)` | $\sigma(\mathbf{x})$ | 数值稳定 softmax |
| `expected_free_energy(kl, preference)` | $G(\pi)$ | 预期自由能（EFE） |
| `policy_selection(free_energies, gamma)` | $P(\pi)=\sigma(-\gamma G(\pi))$ | 软最大策略选择 |
| `dao_gradient_step(theta, grad_g, eta)` | $\theta_{t+1}=\theta_t-\eta\nabla_\theta G$ | 沿负梯度更新参数 |
| `gradient_flow(theta, grad_func, lr)` | 同上，接受梯度函数 | 高阶封装 |
| `awareness_bandwidth(r_dmn, r0, rmax)` | $AB(t)$ | 觉知带宽归一化 |
| `precision_weighted_update(mu, pe, pi)` | $\mu+\pi\cdot\varepsilon$ | 精度加权信念更新 |
| `cost_of_deviation(g_actual, g_optimal)` | $\text{Cost}(\pi_{\text{dev}})$ | 偏离最优策略的代价 |
| `wu_wei_threshold(grad_norm, tau)` | $\|\nabla_\theta G\| < \tau$ | 无为阈值判定 |
| `de_precision_matrix(dim)` | $\Pi_{\text{德}}$ | 德的精度矩阵（单位阵存根） |
| `reward_prediction_error(actual, expected)` | $\delta_{\text{RPE}}$ | 奖励预测误差 |
| `impermanence_corrected_rpe(actual, expected, kappa)` | $\text{RPE}_{\text{随缘}}$ | 无常修正 RPE |
| `social_awareness_bandwidth(ab, mns, men, ai_shared, dmn_self, weights)` | $SAB(t)$ | 社会觉知带宽 |
| `de_ming_allocation(mu, sigma, ...)` | 德-明能量分配 | 按收益与不确定性分配能量 |
| `critical_handover_signal(...)` | $h(T, \dot T)$ | 关系调谐临界交接信号 |
| `planetary_heat_budget_occupancy(...)` | $\rho_H$ | 行星热预算占用率 |

---

## `dao_science.experience`

可审计经验存储器，把「行入-理入」实践记录为可检索、可审计的数据结构。

- `ExperienceRecord`：单条经验（时间戳、上下文哈希、决策、结果、置信度、审计日志）。
- `AuditableMemory`：按上下文哈希索引记录，提供 `store()`、`retrieve()`、`audit()`、`refresh_if_needed()`。

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

波浪频率集群调度模拟器。给定二维节点网格与总功率预算，模拟「全局同步时钟」与「行波相位」两种模式下的功率平滑度、热分布熵与吞吐量方差。

- `WaveScheduler(shape, total_power_budget, ...)`
- `phi(i, j, t)`：节点相位传播函数。
- `step(t)`：返回当前时刻的归一化功率网格。
- `metrics(trace)`：从时间轨迹中提取聚合指标。

---

## `dao_science.hardware`

硬件抽象层 + 三态熔断器。定义 `ThermalSensor`、`PowerController`、`HardwareBreaker` 抽象接口；`BreakerFSM` 在本地传感器阈值越界时独立触发 `NORMAL → THROTTLE → HALT` 状态迁移。

```python
breaker = BreakerFSM(p_max=100.0, t_max=80.0, dtdt_max=10.0)
reading = SensorReading(p_watts=150.0, t_junction=70.0, dt_dt=5.0)
assert breaker.transition(reading).name == "THROTTLE"
```

---

## 设计原则

1. **无状态**：模块级没有可变全局变量，便于并行与测试。
2. **类型注解**：使用 `numpy.typing.NDArray` 与 Python 类型提示，通过 `mypy src tests`。
3. **可测试**：每个公开函数/方法都有对应的 `tests/test_core.py` 用例。
4. **可追溯**：函数名、方程编号与 `NOTATION.md` / `verifiable_units/` 中的定义保持对齐。

---

> 返回导航入口：[`0_motivation/project_map.md`](../0_motivation/project_map.md)
