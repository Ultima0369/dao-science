# 可验证单元 VU-10：AI 扩张的行星热力学边界

## Verifiable Unit 10: Planetary Thermodynamic Boundary for AI Expansion

---

> **证据等级**：形式化 [F] + 仿真 [S] + 物理/第一性原理 [P]  
> **对应主张**：`CLAIMS.md` C24  
> **对应文件**：`4_applications/ai_governance.md` 第 7 节  
> **仿真脚本**：`simulations/planetary_ai_thermodynamics.py`

---

## 1. 形式化声明

### 1.1 核心命题

即使 AI 的能源输入趋近于免费（廉价光伏、可控核聚变等），AI 系统的物理扩张仍受地球红外辐射散热能力的硬约束。当全球 AI 废热功率持续超过地球向太空的辐射功率余量时，地表温度必然上升。

### 1.2 数学对象与定义域

设：
- $S_0 \approx 1361\ \text{W m}^{-2}$：太阳常数
- $R_\oplus \approx 6.371 \times 10^6\ \text{m}$：地球半径
- $\alpha \approx 0.30$：地球反照率
- $\varepsilon \approx 0.61$：有效红外发射率（已考虑温室效应）
- $\sigma$：斯特藩-玻尔兹曼常数

地球吸收的太阳功率：

$$P_\text{solar} = S_0 \cdot \pi R_\oplus^2 \cdot (1 - \alpha) \approx 1.21 \times 10^{17}\ \text{W}$$

地球向外辐射功率（ Stefan-Boltzmann ）：

$$P_\text{out}(T) = \sigma \cdot \varepsilon \cdot 4\pi R_\oplus^2 \cdot T^4$$

无 AI 时能量平衡给出当前参考温度：

$$T_\text{eq} = \left( \frac{P_\text{solar}}{\sigma \cdot \varepsilon \cdot 4\pi R_\oplus^2} \right)^{1/4} \approx 288\ \text{K}\ (15^\circ\text{C})$$

加入 AI 废热 $P_\text{AI}$ 后的新平衡温度：

$$T_\text{eq}(P_\text{AI}) = \left( \frac{P_\text{solar} + P_\text{AI}}{\sigma \cdot \varepsilon \cdot 4\pi R_\oplus^2} \right)^{1/4}$$

### 1.3 热力学停止协议

把 VU-06 的「知止」扩展到行星尺度：

$$\text{stop} \iff P_\text{AI waste heat} > \eta \cdot P_\text{Earth radiative cooling}$$

其中 $\eta \in (0, 1)$ 是行星热预算余量系数（例如 $0.10$ 或 $0.50$）。

### 1.4 行星之德指标：热预算占用率

为把「行星之德」可操作化，定义**行星热预算占用率**（Planetary Heat-Budget Occupancy, PHBO）：

$$\rho_H(t) = \frac{P_\text{AI waste heat}(t)}{\eta \cdot P_\text{Earth radiative cooling}}$$

governance dashboard 用交通灯区域解释：

| 区间 | 颜色 | 含义 |
|---|---|---|
| $\rho_H < 0.5$ | 绿 | 安全余量充足 |
| $0.5 \leq \rho_H < 0.9$ | 黄 | caution，需审计与减速 |
| $\rho_H \geq 0.9$ | 红 | 临界，触发自动降级或停止 |
| $\rho_H \geq 1.0$ | — | 越过行星热力学停止阈值 |

PHBO 把抽象的「德」转化为可监测、可审计、可自动触发的物理量。

### 1.5 边界条件

- AI 废热最终全部进入地球热库（兰道尔原理：不可逆擦除至少产生 $k_B T \ln 2$ 热量）。
- 地球向外散热的主要机制是红外辐射。
- 忽略人类主动把废热排向太空的工程方案（当前不在技术经济可行范围内）。

---

## 2. 仿真脚本

### 2.1 文件位置

`simulations/planetary_ai_thermodynamics.py`

### 2.2 功能

- 计算地球无 AI 时的热平衡温度。
- 绘制 AI 废热功率与平衡温升的曲线，标出当前全球功耗、当前 AI 功耗、吸收太阳功率的位置。
- 模拟不同年增长率（10%、30%、50%）下 AI 废热与全球温度的时序轨迹。
- 对比四种治理策略：无约束增长、10% 太阳预算上限、10% 太阳预算停止协议、50% 太阳预算停止协议。
- 绘制行星之德治理 dashboard，展示 PHBO 随时间的交通灯演化。

### 2.3 运行方式

```bash
pip install -r simulations/requirements.txt
python simulations/planetary_ai_thermodynamics.py
```

输出：
- `simulations/ai_heat_equilibrium.png`
- `simulations/ai_heat_trajectory.png`
- `simulations/ai_heat_policy_comparison.png`
- `simulations/ai_heat_governance_dashboard.png`

### 2.4 关键参数

| 参数 | 值 | 说明 |
|---|---|---|
| 太阳常数 $S_0$ | 1361 W/m² | 地球轨道处太阳辐射 |
| 反照率 $\alpha$ | 0.30 | 地球反射率 |
| 有效发射率 $\varepsilon$ | 0.61 | 温室效应修正 |
| 当前全球功耗 | 18 TW | 参考人类总功率 |
| 当前 AI 功耗 | 0.05 TW | 2025 年量级估算 |
| 年增长情景 | 10%、30%、50% | 不同扩张速率 |
| 热预算阈值 $\eta$ | 0.10、0.50 | 触发停止/上限的行星余量比例 |
| 温度上限 | 10000 K | 仅用于避免数值溢出，不代表可居住 |
| 安全余量系数 $\eta$ | 0.10 | PHBO 分母中的行星散热余量比例 |
| 交通灯阈值 | 0.5 / 0.9 / 1.0 | 绿/黄/红/停止 |

---

## 3. 预期结果与解读

### 3.1 平衡边界曲线

- 当 $P_\text{AI}$ 远小于 $P_\text{solar}$ 时，温升可忽略。
- 当 $P_\text{AI}$ 接近 $P_\text{solar}$ 时，温升急剧上升（$T \propto (P_\text{solar} + P_\text{AI})^{1/4}$）。
- 吸收太阳功率 $\sim 121{,}000$ TW 是行星热力学边界的数量级参考。

### 3.2 增长轨迹

- 30% 年增长率下，AI 废热约 40 年后即可达到 10% 太阳预算。
- 温度响应存在热惯性（地球热容大），但一旦越过阈值，温升不可逆地累积。
- 50% 年增长会在更短时间内触发极端温升。

### 3.3 行星之德 Dashboard

- 30% 年增长率、$\eta=10\%$ 情景下，PHBO 约 40 年突破 1.0（越过停止阈值）。
- 交通灯区域把抽象的热力学约束转化为可操作的治理信号。
- PHBO 可作为国际 AI 热预算协议的共同指标。

### 3.4 治理策略对比

| 策略 | 温度结果 |
|---|---|
| 无约束 | 温度在数十年内突破可居住范围 |
| 10% 上限 / 停止 | 温度基本维持在当前基准附近 |
| 50% 停止 | 温升有限但显著，仍可能扰动气候系统 |

**关键特征**：停止协议不是限制 AI「能力」，而是把物理约束内嵌为不可绕过的治理规则。

---

## 4. 与项目理论的对应

| 项目概念 | 仿真对应 |
|---|---|
| 知止不殆 | 热预算阈值触发停止 |
| 德 | 行星之德：人类与 AI 对地球能量预算的注意力化调配 |
| 偏离代价 | 越过热边界后地表温度上升、生态退化 |
| 碳硅共生 | AI 扩张速度受碳基星球的物理约束调节 |
| 最小作用量 | 在热预算约束内寻找最大信息量/有用功 |

---

## 5. 实验/经验对应（草案）

### 5.1 数据中心热排放

- 大型数据中心的热排放已造成局部城市热岛效应。
- 液冷、余热回收只能改变热量分布，不能减少总废热。

### 5.2 能源与气候研究

- 全球能源消耗与地表温度长期趋势的相关性已被广泛研究。
- 可再生能源替代化石能源减少的是碳排放，不是废热；废热是能量守恒的必然产物。

### 5.3 可检验预测

1. 若 AI 算力功率保持高增长率，未来数十年内其废热将占全球废热的显著比例。
2. 任何声称「能源无限即可无限计算」的方案必须说明废热如何排向太空。
3. 行星尺度的 AI 治理协议应包含热预算审计与自动降级机制。

---

## 6. 反事实条件

以下证据会削弱或推翻本命题：

1. 实验证明地球可在任意废热功率下通过非辐射机制维持稳态温度。
2. 证明信息擦除可以不产生热力学熵增（违反兰道尔原理）。
3. 工程上实现将 AI 废热大规模直接排向太空而不影响地表。
4. 观测显示 AI 废热功率增长被自然反馈机制自动抑制。

---

## 7. 当前局限

- 模型高度简化：未考虑大气环流、海洋热惯性细节、反照率反馈、温室气体变化。
- 当前 AI 功耗估算存在数量级不确定性。
- 未建模区域热不均匀性（数据中心局部过热 vs 全球平均）。
- 未纳入碳硅共生中的「具身/符号」分工对功耗结构的影响。

---

## 8. 如何引用

> Project Dao.Science (2026). Verifiable Unit 10: Planetary Thermodynamic Boundary for AI Expansion. `verifiable_units/vu_10_planetary_ai_thermodynamics.md`.

---

> 返回项目主张登记册：[`CLAIMS.md`](../CLAIMS.md)
