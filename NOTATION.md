# 项目符号与约定说明

## Project Dao.Science — Notation and Dimensional Conventions

---

## 1. 符号总表

下表列出 Project Dao.Science 各模块中反复出现的核心符号。每个符号给出：中文含义、数学对象/定义域、量纲、首次出现文件。

| 符号 | 中文含义 | 数学对象 / 定义域 | 量纲 | 首次出现 |
|------|---------|-----------------|------|---------|
| $F$ | 变分自由能 | 标量；$F \geq -\ln P(o)$ | 奈特（nats） | `01_dao_as_process.md` |
| $G(\pi)$ / $G(\pi_\theta)$ | 预期自由能 | 标量；策略 $\pi$ 或参数化策略 $\pi_\theta$ 的函数 | 奈特（nats） | `01_dao_as_process.md` |
| $\pi$ | 离散行动策略 | 离散索引或策略向量 | 无量纲 | `01_dao_as_process.md` |
| $\theta \in \mathbb{R}^d$ | 策略连续参数 | 实向量 | 依参数而定 | `01_dao_as_process.md` |
| $\Pi$ | 精度矩阵 | 半正定矩阵 | $[\text{方差}]^{-1}$ | `01_dao_as_process.md` |
| $\sigma(x)$ | Sigmoid / Softmax | $\sigma(x)=1/(1+e^{-x})$ 或 softmax | 无量纲 | `01_dao_as_process.md` |
| $AB(t)$ | 觉知带宽 | 标量；$AB(t) \in [0, 1]$ | 无量纲 | `02_one_as_bandwidth.md` |
| $R_{\text{DMN}}(t)$ | DMN 标准化活动 | 标量；BOLD 相对基线变化 | 无量纲（% 变化或 z 分数） | `02_one_as_bandwidth.md` |
| $R_0$ | DMN 基线水平 | 标量 | 同 $R_{\text{DMN}}$ | `02_one_as_bandwidth.md` |
| $R_{\text{max}}$ | DMN 最大观测变化 | 标量 | 同 $R_{\text{DMN}}$ | `02_one_as_bandwidth.md` |
| $\alpha$ | 焦点-全局注意参数 | 标量；$\alpha \in [0, 1]$ | 无量纲 | `attention_model.md` |
| $a(t), A(t)$ | 杏仁核激活 | 标量；归一化到 $[0, 1]$ | 无量纲 | `100ms_model.md` |
| $p(t), P(t)$ | 前额叶调控激活 | 标量；归一化到 $[0, 1]$ | 无量纲 | `100ms_model.md` |
| $\tau_a, \tau_p$ | 时间常数 | 标量；$>0$ | 秒（s） | `100ms_model.md` |
| $\gamma_A, \gamma_P$ | 衰减率 | 标量；$>0$ | $\text{s}^{-1}$ | `100ms_model.md` |
| $D(t)$ | DMN 活动水平 | 标量；归一化到 $[0, 1]$ | 无量纲 | `dmn_self_model.md` |
| $I(t)$ | 岛叶/内感受活动 | 标量；归一化到 $[0, 1]$ | 无量纲 | `dmn_self_model.md` |
| $w_{ij}$ | 连接权重 | 标量 | 依上下文 | `100ms_model.md`, `dmn_self_model.md` |
| $SAB(t)$ | 社会觉知带宽 | 标量；$SAB(t) \in [0, 1]$ | 无量纲 | `social_cognition.md` |
| $\delta_{\text{RPE}}$ | 奖励预测误差 | 标量 | 奖励单位 | `02_flow_with_causes.md` |
| $\Pi_{\text{De}}$ | 德的精度矩阵 | 半正定矩阵 | $[\text{方差}]^{-1}$ | `01_dao_as_process.md` |

---

## 2. 量纲约定

### 2.1 激活水平的无量纲化

本项目中的神经活动变量（$A, P, D, I, MNS_{\text{act}}, MEN_{\text{act}}$ 等）均视为**归一化激活水平**，取值区间通常为 $[0, 1]$。其物理对应可以是：

- fMRI BOLD 信号相对于基线的标准化变化（% signal change 或 z-score）
- 神经元群体发放率的归一化值
- EEG/MEG 频段功率的归一化值

**理由**：不同脑区的原始活动量纲不同（BOLD、放电率、场电位），直接相加会导致量纲不一致。归一化后，竞争/耦合方程中的权重统一为速率量纲 $[t]^{-1}$，便于分析和仿真。

### 2.2 自由能与信息论量

变分自由能 $F$ 和预期自由能 $G$ 均以**奈特（nats）**为单位（自然对数底）。若使用以 2 为底的对数，则单位为比特（bits）；转换关系为 $1\ \text{bit} = \ln 2\ \text{nats}$。

### 2.3 精度矩阵

精度矩阵 $\Pi$ 是协方差矩阵的逆，量纲为 $[\text{变量单位}]^{-2}$。当变量为无量纲的归一化信号时，精度矩阵也是无量纲的。

### 2.4 时间常数 vs 衰减率

- 时间常数（$\tau$）：出现在 $\tau \frac{dx}{dt} = \dots$ 形式中，量纲为 $[t]$。
- 衰减率（$\gamma$）：出现在 $\frac{dx}{dt} = \dots - \gamma x$ 形式中，量纲为 $[t]^{-1}$。

本项目统一使用：
- $\tau$ 表示时间常数
- $\gamma$ 表示衰减率

避免用 $\tau$ 同时表示时间常数和衰减率，以减少混淆。

---

## 3. 证据等级徽章

为区分"形式化"与"已验证"，本项目引入五级证据状态徽章。每个核心命题应在首次出现时标注其当前证据等级。

| 徽章 | 等级 | 含义 | 例子 |
|------|------|------|------|
| **F** | Formal | 纯形式化/数学类比；尚未经过仿真或实验验证 | $\text{Dao} \equiv -\nabla_\theta G(\pi_\theta)$ |
| **S** | Simulation | 有可运行的仿真脚本，但尚未与行为/神经数据对比 | DMN-岛叶双稳态 ODE 的数值积分 |
| **B** | Behavioral | 能导出可检验的行为预测，但尚未完成实验 | 100ms 模型预测的干预成功率曲线 |
| **N** | Neural | 有神经科学文献或数据支持其神经对应 | DMN 在冥想中下调（Brewer et al., 2011） |
| **M** | Meta-ethical / Normative | 包含规范性主张，无法被纯经验证伪 | "知止"作为 AI 停止标准 |

**使用格式**：在文件开头或关键方程后标注，例如：

> $$\text{Dao} \equiv -\nabla_\theta G(\pi_\theta) \quad \text{[F]}$$

> 长期冥想者 DMN-TPN 反相关增强 \quad \text{[N]}

---

## 4. "隐喻—模型"声明模板

每个核心映射应明确其可操作代理、定义域和可证伪条件：

```markdown
**映射声明**：X ≈ Y
- **可操作代理**：如何测量 X 和 Y
- **定义域**：该映射在哪些条件下成立
- **可证伪条件**：什么证据会削弱该映射
- **证据等级**：[F/S/B/N/M]
```

---

## 5. 常见误区提示

1. **不要把 $-\nabla_\pi G(\pi)$ 当作对离散策略索引求导**。标准主动推理中 $\pi$ 常是离散索引；对离散索引写梯度没有标准数学意义。应使用连续参数化形式 $-\nabla_\theta G(\pi_\theta)$，或离散选择形式 $\arg\min_\pi G(\pi)$。

2. **不要把 $AB(t)$ 当作容量减去资源**。$R_{\text{DMN}}$ 不是可与 $C_{\text{max}}$ 直接相减的资源量。应使用标准化形式 $AB(t) = 1 - [R_{\text{DMN}}(t) - R_0]/[R_{\text{max}} - R_0]$，使 $AB(t)$ 成为无量纲的相对可用比例。

3. **竞争方程中的交叉项需要统一量纲**。当不同脑区变量相加或相乘时，应先将它们归一化到无量纲区间，并明确所有系数量纲。

4. **softmax 中的参数必须保持向量一致性**。$P(\pi) = \sigma(-\gamma \cdot G(\pi))$ 中的 $G(\pi)$ 必须是按策略索引的向量；不应将全局标量 $\min_\pi G(\pi)$ 直接喂入 softmax，否则所有策略概率相同。

---

*本文件随项目发展持续更新。最后更新：2026年6月13日。*
