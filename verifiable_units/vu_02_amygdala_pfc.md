# 可验证单元 VU-02：杏仁核-前额叶竞争与“念起即觉”窗口

## Verifiable Unit 02: Amygdala-PFC Competition and the Golden Window

---

> **证据等级**：形式化 [F] + 仿真 [S] + 神经证据 [N] + 行为预测 [B]  
> **对应模型**：`2_models/100ms_model.md` §4.4、§7  
> **仿真脚本**：`simulations/amygdala_pfc_hijack.py`

---

## 1. 形式化声明

### 1.1 核心命题

情绪刺激在约 74 ms 触发杏仁核（amygdala）活动，而完整意识情绪体验约 300–500 ms 才形成。在这两者之间存在一个“黄金窗口”（~100–300 ms），在此期间前额叶（PFC）能否及时对杏仁核进行自上而下调控，决定情绪反应是被“劫持”还是被“重新评估”。冥想训练通过增强 PFC→杏仁核抑制权重 $\alpha_T$、提高杏仁核→PFC 传递效率 $\beta$、缩短传导延迟 $\delta$，系统性提升窗口内的干预成功率。

### 1.2 数学对象与定义域

状态变量：
- $A(t) \in [0, 1]$：杏仁核归一化激活
- $P(t) \in [0, 1]$：前额叶调控激活

竞争动力学（`100ms_model.md`）：

$$\frac{dA}{dt} = \alpha_B \cdot S(t) - \alpha_T \cdot P(t) \cdot A(t) - \gamma_A \cdot A(t)$$

$$\frac{dP}{dt} = \beta \cdot A(t - \delta) - \gamma_P \cdot P(t)$$

其中：
- $S(t)$：威胁刺激强度（已归一化）
- $\alpha_B$：自下而上驱动系数，$[\alpha_B] = [t]^{-1}$
- $\alpha_T$：自上而下调控系数，$[\alpha_T] = [t]^{-1}$
- $\gamma_A, \gamma_P$：衰减率，$[t]^{-1}$
- $\beta$：PFC 对杏仁核警报的响应增益，$[t]^{-1}$
- $\delta$：杏仁核→PFC 传导延迟，$\delta \approx 100$–$200$ ms

### 1.3 边界条件

- $A(0), P(0) \in [0, 1]$
- $\alpha_B, \alpha_T, \gamma_A, \gamma_P, \beta \geq 0$
- $\delta \geq 0$

---

## 2. 仿真脚本

### 2.1 文件位置

`simulations/amygdala_pfc_hijack.py`

### 2.2 功能

- 对延迟微分方程做 Euler 数值积分
- 对比两种参数 regime：弱 $\alpha_T$/长 $\delta$ → 杏仁核劫持；强 $\alpha_T$/短 $\delta$ → 成功重评
- 扫描 $(\alpha_T, \delta)$ 参数空间，绘制“劫持 / 混合 / 调控”相图

### 2.3 运行方式

```bash
pip install -r simulations/requirements.txt
python simulations/amygdala_pfc_hijack.py
```

输出：
- `simulations/amygdala_pfc_trajectories.png`
- `simulations/amygdala_pfc_parameter_space.png`

### 2.4 关键参数

| 参数 | 劫持案例 | 调控案例 | 生物学解释 |
|------|---------|---------|-----------|
| $\alpha_B$ | 0.6 | 0.6 | 威胁驱动强度 |
| $\alpha_T$ | 0.08 | 0.45 | PFC→杏仁核抑制 |
| $\beta$ | 0.22 | 0.35 | 杏仁核→PFC 响应增益 |
| $\gamma_A$ | 0.08 | 0.08 | 杏仁核衰减 |
| $\gamma_P$ | 0.06 | 0.06 | PFC 衰减 |
| $\delta$ | 120 ms | 80 ms | 传导延迟 |

---

## 3. 实验方案草案

### 3.1 研究问题

冥想训练是否通过降低杏仁核-PFC 调控延迟 $\delta$ 和提高 PFC→杏仁核抑制强度 $\alpha_T$，使被试在情绪面孔后向掩蔽任务中表现出更短的情绪觉察延迟和更低的杏仁核反应峰值？

### 3.2 被试

- 实验组：长期冥想者（>1,000 小时），N = 25
- 对照组：年龄、性别、教育匹配的非冥想者，N = 25

### 3.3 任务与指标

**任务**：后向掩蔽恐惧面孔任务（stimulus onset asynchrony, SOA = 17–33 ms）+ 认知重评任务。

**主要指标**：
1. 杏仁核对无意识恐惧面孔的峰值反应时间（EEG/MEG 源定位）
2. PFC→杏仁核有效连接强度（动态因果模型，DCM）
3. 主观情绪强度评分（重评 vs 观看）
4. 反应时：情绪 Stroop 或点探测任务

**统计假设**：
- $H_0$：两组在杏仁核峰值、PFC→杏仁核连接和重评效果上无差异
- $H_1$：冥想组杏仁核峰值更低、PFC→杏仁核抑制连接更强、重评效果更大
- 预期效应量：Cohen's $d \approx 0.6$–$0.8$

### 3.4 与仿真的对应

| 实验指标 | 仿真对应 | 预期方向 |
|---------|---------|---------|
| 杏仁核峰值降低 | $\alpha_T$ 增大或 $\delta$ 减小使 $A_{\max}$ 下降 | 冥想组 < 对照组 |
| 重评效果增强 | $\alpha_T$ 增大 | 冥想组 > 对照组 |
| 情绪觉察延迟缩短 | $\delta$ 减小 | 冥想组 < 对照组 |
| 无意识威胁反应减弱 | $\alpha_B$ 减小或早期 $\alpha_T$ 增强 | 冥想组 < 对照组 |

---

## 4. 反事实条件

以下证据会削弱或推翻本命题：

1. 长期冥想者与非冥想者在后向掩蔽恐惧面孔任务中杏仁核反应无差异
2. 在控制重评策略后，冥想者的 PFC→杏仁核有效连接未增强
3. 经颅磁刺激（TMS）暂时抑制 dlPFC 后，冥想者的情绪调控优势消失
4. 模型仿真显示，无论 $\alpha_T$ 如何增加，系统都无法避免劫持

---

## 5. 当前局限

- 仿真使用确定性/随机 Euler 积分，未与真实 EEG/fMRI 时间序列拟合
- 延迟项用离散历史数组近似，真实神经传导具有更复杂的分布
- 参数值基于文献数量级估计，需通过试点数据校准
- 实验方案尚未经过伦理审查或预注册

---

## 6. 如何引用

> Project Dao.Science (2026). Verifiable Unit 02: Amygdala-PFC Competition and the Golden Window. `verifiable_units/vu_02_amygdala_pfc.md`.
