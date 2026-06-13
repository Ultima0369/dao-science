# 可验证单元 VU-03：DMN-ECN 动态耦合与顿悟

## Verifiable Unit 03: DMN-ECN Flexible Coupling and Insight

---

> **证据等级**：形式化 [F] + 仿真 [S] + 神经证据 [N] + 行为预测 [B]  
> **对应模型**：`4_applications/creativity_innovation.md` §2.4  
> **仿真脚本**：`simulations/dmn_ecn_creativity.py`

---

## 1. 形式化声明

### 1.1 核心命题

创造力不是默认模式网络（DMN）或执行控制网络（ECN）单独运作的产物，而是两者之间的动态耦合。在酝酿阶段，DMN 以低耦合强度自由联想；当 DMN 产生与问题表征高度匹配的候选时，DMN→ECN 耦合权重 $w_{DE}(t)$ 突然升高，执行控制网络“捕获”该候选并进行精密加工，主观体验为“顿悟”（Aha!）。高创造力个体的特征不是 DMN 或 ECN 更强，而是 $w_{DE}(t)$ 能在低值（酝酿）和高值（捕获）之间灵活切换。

### 1.2 数学对象与定义域

状态变量：
- $D(t) \in [0, 1]$：DMN 归一化激活
- $E(t) \in [0, 1]$：ECN 归一化激活

耦合动力系统（`creativity_innovation.md`）：

$$\tau_D \frac{dD}{dt} = -D + w_{DD} \cdot \sigma(D) - w_{ED} \cdot \sigma(E) + S_D(t) + \eta_D$$

$$\tau_E \frac{dE}{dt} = -E + w_{EE} \cdot \sigma(E) + w_{DE}(t) \cdot \sigma(D) + S_E(t) + \eta_E$$

其中：
- $\sigma(x) = 1 / (1 + e^{-\beta(x - \theta)})$
- $w_{DE}(t)$：时变 DMN→ECN 耦合权重
- $\eta_D, \eta_E$：高斯噪声项
- 所有时间系数 $[t]^{-1}$，状态变量无量纲

### 1.3 边界条件

- $D(0), E(0) \in [0, 1]$
- $w_{DD}, w_{EE} > 0$（自维持）
- $w_{ED} > 0$（ECN→DMN 抑制）
- $w_{DE}(t) \geq 0$，在酝酿期低、捕获期高

---

## 2. 仿真脚本

### 2.1 文件位置

`simulations/dmn_ecn_creativity.py`

### 2.2 功能

- 模拟 DMN-ECN 耦合系统在“酝酿→捕获→验证”周期中的轨迹
- 动态切换 $w_{DE}(t)$：低耦合（酝酿）→ 高耦合（顿悟捕获）
- 扫描 DMN 自兴奋 $w_{DD}$ 与洞察耦合 $w_{DE}^{high}$，统计顿悟事件数

### 2.3 运行方式

```bash
pip install -r simulations/requirements.txt
python simulations/dmn_ecn_creativity.py
```

输出：
- `simulations/dmn_ecn_creativity_timeseries.png`
- `simulations/dmn_ecn_coupling_scan.png`

### 2.4 关键参数

| 参数 | 值 | 生物学解释 |
|------|-----|-----------|
| $\tau_D$ | 1.0 s | DMN 时间常数 |
| $\tau_E$ | 0.8 s | ECN 时间常数 |
| $w_{DD}$ | 1.5 | DMN 自维持 |
| $w_{EE}$ | 1.3 | ECN 自维持 |
| $w_{ED}$ | 0.8 | ECN→DMN 抑制 |
| $w_{DE}^{low}$ | 0.15 | 酝酿期低耦合 |
| $w_{DE}^{high}$ | 1.2 | 顿悟期高耦合 |
| $S_D$ | 0.12 | 问题表征对 DMN 的持续驱动 |
| $S_E$ | 0.08 | ECN 基线输入 |

---

## 3. 实验方案草案

### 3.1 研究问题

在创造性问题解决任务中，高创造力被试是否在顿悟前表现出 DMN-ECN 功能连接的突然增强，且该增强幅度预测顿悟的主观报告强度和后续解决方案的正确率？

### 3.2 被试

- 高创造力组：经创造力测验（如远程联想测验 RAT / 替代用途测验 AUT）筛选的上 25%，N = 30
- 对照组：匹配教育背景但创造力得分中等的被试，N = 30

### 3.3 任务与指标

**任务**：复合远距离联想任务（compound remote associate task, CRA）或沙漏问题（insight problems），在 fMRI 或 EEG 中记录。

**主要指标**：
1. 顿悟前 2–4 s 内 DMN（PCC/mPFC）与 ECN（dlPFC/IPS）功能连接的突然增强
2. 顿悟时刻右侧前颞上回（aSTG）γ 波爆发（~40 Hz）
3. ACC 在顿悟前 300 ms 的 γ 波活动
4. 主观顿悟强度评分与客观解题正确率

**统计假设**：
- $H_0$：高创造力组与对照组在顿悟前 DMN-ECN 耦合增强幅度上无差异
- $H_1$：高创造力组顿悟前 DMN-ECN 耦合增强更显著，且与正确率正相关
- 预期效应量：Cohen's $d \approx 0.7$–$0.9$

### 3.4 与仿真的对应

| 实验指标 | 仿真对应 | 预期方向 |
|---------|---------|---------|
| 顿悟前 DMN-ECN 连接激增 | $w_{DE}(t)$ 从低值跃迁到高值 | 高创造力组 > 对照组 |
| 酝酿期 DMN 自由联想 | 低 $w_{DE}$ 下 DMN 高激活 | 高创造力组 DMN 波动更大 |
| 顿悟后验证阶段 ECN 增强 | 高 $w_{DE}$ 下 E(t) 持续高 | 与正确率正相关 |
| 创造力训练效果 | 提高 $w_{DE}$ 的动态范围 | 训练后顿悟数增加 |

---

## 4. 反事实条件

以下证据会削弱或推翻本命题：

1. 在控制任务难度后，高创造力者与对照组的 DMN-ECN 顿悟前耦合增强无差异
2. TMS 抑制 dlPFC 后仍出现正常的主观顿悟报告，说明 ECN 捕获不是顿悟的必要条件
3. 模型仿真显示，无论 $w_{DE}(t)$ 如何变化，系统都不产生可被报告为“顿悟”的瞬态
4. 顿悟体验与 DMN-ECN 耦合的时间锁定关系被证明是呼吸或头动伪影

---

## 5. 当前局限

- 仿真用简化的双节点模型，未纳入顶叶注意网络、突显网络等多网络交互
- $w_{DE}(t)$ 的切换规则是启发式设定，需用真实数据驱动（如状态空间模型）估计
- 未区分“小顿悟”（局部重构）与“大顿悟”（范式转移）
- 实验方案需预注册，并使用多中心样本验证

---

## 6. 如何引用

> Project Dao.Science (2026). Verifiable Unit 03: DMN-ECN Flexible Coupling and Insight. `verifiable_units/vu_03_dmn_ecn.md`.
