# 可验证单元 VU-09：德-明能量调配模型

## Verifiable Unit 09: De-Ming Energy Allocation Model

---

> **证据等级**：形式化 [F] + 仿真 [S] + 行为预测 [B] + 元伦理/规范 [M]  
> **对应主张**：`CLAIMS.md` C23  
> **对应模型**：`1_first_principles/10_de_and_ming.md`  
> **仿真脚本**：`simulations/de_ming_energy_allocation.py`

---

## 1. 形式化声明

### 1.1 核心命题

「德」是生命系统对精力/注意力的注意力化调配；「明」是带宽约束下统合阴阳、识别常量与变量并输出确定行动的穿透性觉知。德-明闭环可形式化为：在多个目标之间分配有限能量（德），根据观测反馈更新对奖励与不确定性的信念（明），再重新分配能量。

### 1.2 数学对象与定义域

设 Agent 面对 $N$ 个目标，总能量为 $E_{\text{total}}$。每个目标 $i$ 在时刻 $t$ 有：
- 真实奖励 $r_i(t)$（可能随时间变化）
- 真实不确定性 $\sigma_i(t)$
- Agent 的信念：估计奖励 $\mu_i(t)$，估计不确定性 $s_i(t)$

**德** —— 能量分配：

$$a_i(t) = E_{\text{total}} \cdot \text{softmax}\left( \beta \cdot \frac{\mu_i(t)}{s_i(t) + \epsilon} \right)$$

即把更多精力投向奖励高且不确定性低的目标（信噪比最大化）。

**明** —— 信念更新与变化检测：

观测结果 $o_i(t) \sim \mathcal{N}(r_i(t), \sigma_i(t)^2 / a_i(t))$。预测误差：

$$\text{PE}_i(t) = |o_i(t) - \mu_i(t)|$$

若 $\text{PE}_i(t) > \theta \cdot s_i(t)$，则目标 $i$ 被标记为「惊奇」，明触发快速学习并扩大不确定性：

$$\mu_i \leftarrow \mu_i + \eta_{\text{surprise}} \cdot (o_i - \mu_i)$$
$$s_i^2 \leftarrow 2 \cdot \big[(1 - \eta_{\text{surprise}}) s_i^2 + \eta_{\text{surprise}} \text{PE}_i^2\big]$$

否则进行常规平滑更新。

### 1.3 德-明闭环

$$\text{明}(t) \rightarrow \text{德}(t) \rightarrow \text{行动} \rightarrow \text{反馈} \rightarrow \text{明}(t+1) \rightarrow \text{德}(t+1)$$

### 1.4 边界条件

- 总能量有限：$\sum_i a_i(t) = E_{\text{total}}$
- 目标奖励与不确定性可被概率估计
- 环境可能发生非平稳变化
- 能量调配有切换成本

---

## 2. 仿真脚本

### 2.1 文件位置

`simulations/de_ming_energy_allocation.py`

### 2.2 功能

- 生成两阶段非平稳环境：前 100 步任务 0/1 最优，后 100 步任务 2/3 最优
- 比较四种 Agent：
  - **De-Ming**：自适应能量调配 + 惊奇驱动的信念更新
  - **Dogmatic**：按初始阶段最优分配固定能量，不更新信念
  - **Random**：随机分配能量
  - **Stubborn**：把所有能量固定投入任务 0，永不更新
- 绘制能量分配轨迹、累积后悔值、信念模型拟合度、明的变化检测信号

### 2.3 运行方式

```bash
pip install -r simulations/requirements.txt
python simulations/de_ming_energy_allocation.py
```

输出：
- `simulations/de_ming_allocation_trajectory.png`
- `simulations/de_ming_cumulative_regret.png`
- `simulations/de_ming_change_detection.png`

### 2.4 关键参数

| 参数 | 值 | 说明 |
|---|---|---|
| 目标数 $N$ | 4 | 竞争能量的任务维度 |
| 总步数 | 200 | 环境在 t=100 处切换 |
| 总能量 $E_{\text{total}}$ | 1.0 | 每步可分配的能量单位 |
| 调配温度 $\beta$ | 2.0 |  exploitation-exploration 锐度 |
| 常规学习率 $\eta$ | 0.2 | 无惊奇时的信念更新速度 |
| 惊奇学习率 | 0.6 | 检测到变化时的快速更新 |
| 惊奇阈值 $\theta$ | 2.0 | 预测误差超过几倍不确定性即触发惊奇 |
| 切换成本 | 0.3 / 单位变化 | 能量分配大幅变动的代价 |

---

## 3. 预期结果与解读

### 3.1 能量分配轨迹

- **De-Ming**：前 100 步集中在任务 0/1；t=100 后迅速检测到环境变化，重新分配至任务 2/3。
- **Dogmatic**：固定停留在初始最优分配，环境变化后持续亏损。
- **Random**：无结构地波动，长期后悔最高。
- **Stubborn**：全部能量锁定任务 0，第二阶段后悔线性累积。

### 3.2 累积后悔值

典型结果：

| Agent | 最终累积后悔 |
|---|---|
| De-Ming | ~11 |
| Dogmatic | ~69 |
| Random | ~108 |
| Stubborn | ~60 |

**关键特征**：De-Ming 的德-明闭环在非平稳环境中显著优于固定策略与随机策略。

### 3.3 明的变化检测

- 环境切换前后，De-Ming 的惊奇计数出现峰值。
- 明不是一次性「顿悟」，而是持续监测预测误差、识别常量与变量的动态过程。

### 3.4 信念模型拟合

- Stubborn 因永不更新，信念与现实的偏差随时间指数放大。
- De-Ming、Dogmatic、Random 的信念拟合度相近，但 De-Ming 因主动探索所有目标而保持模型可用性。

---

## 4. 与项目理论的对应

| 项目概念 | 仿真对应 |
|---|---|
| 德 | 能量分配向量 $a_i(t)$ |
| 明 | 预测误差监测、惊奇检测、信念更新 |
| 阴阳统合 | 平衡 exploitation（高 μ）与 exploration（低 s） |
| 识别常量与变量 | 区分稳定目标与发生变化的任务 |
| 输出确定行动 | softmax 将信念转化为唯一能量分配 |
| 反教条护栏 | 惊奇机制防止信念固化成遮蔽 |
| 最小作用量 | 以最低后悔值实现目标维持 |

---

## 5. 实验/经验对应（草案）

### 5.1 现实映射

- 个人时间管理：把精力投向高回报且可控的事务，同时保留注意力余量监测环境变化。
- 组织资源分配：在核心业务（常量）与新兴机会（变量）之间动态调配预算。
- AI 系统：在已知高奖励策略与新策略探索之间保持平衡，并检测分布偏移。

### 5.2 可检验预测

1. 当环境稳定时，德会收敛到奖励-不确定性比最高的目标。
2. 当环境突变时，明的惊奇信号先于行为显著调整出现。
3. 固定最优策略在环境变化后表现劣于自适应策略。
4. 完全固执于单一目标在长期非平稳环境中后悔值最高。

---

## 6. 反事实条件

以下证据会削弱或推翻本命题：

1. 固定分配策略在所有测试环境中都优于德-明闭环
2. 惊奇检测机制不能加速对环境变化的适应
3. 能量调配中的切换成本可以忽略不计，使随机策略与德-明策略无差异
4. 信念更新本身成为遮蔽：更新后的信念比旧信念更偏离现实

---

## 7. 当前局限

- 奖励与不确定性为标量，真实决策目标多为高维结构化
- 环境仅有一次突变，未测试渐变、周期变化或多时间尺度变化
- 未建模多个 Agent 之间的德-明互动（如组织、关系）
- softmax 温度 β 与学习率需针对具体领域校准

---

## 8. 如何引用

> Project Dao.Science (2026). Verifiable Unit 09: De-Ming Energy Allocation Model. `verifiable_units/vu_09_de_ming_energy_allocation.md`.

---

> 返回项目主张登记册：[`CLAIMS.md`](../CLAIMS.md)
