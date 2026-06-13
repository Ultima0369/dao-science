# 可验证单元 VU-01：DMN-岛叶双稳态切换

## Verifiable Unit 01: DMN-Insula Bistable Switching

---

> **证据等级**：形式化 [F] + 仿真 [S] + 神经证据 [N]  
> **对应模型**：`2_models/dmn_self_model.md` §3.4  
> **仿真脚本**：`simulations/dmn_insula_bistable.py`

---

## 1. 形式化声明

### 1.1 核心命题

默认模式网络（DMN）与岛叶/内感受网络之间的竞争可以被建模为一个双稳态动力系统。冥想训练通过增强岛叶驱动和降低 DMN 自维持权重，使系统从"叙事自我"吸引子切换到"最小自我"吸引子。

### 1.2 数学对象与定义域

状态变量：
- $D(t) \in [0, 1]$：DMN 归一化激活水平
- $I(t) \in [0, 1]$：岛叶/内感受网络归一化激活水平

ODE 系统（`dmn_self_model.md`）：

$$\tau_D \frac{dD}{dt} = -D + w_{DD} \cdot \sigma(D) - w_{ID} \cdot \sigma(I) + S_D(t)$$

$$\tau_I \frac{dI}{dt} = -I + w_{II} \cdot \sigma(I) - w_{DI} \cdot \sigma(D) + S_I(t) + \alpha \cdot B(t)$$

其中：
- $\sigma(x) = 1 / (1 + e^{-\beta(x - \theta)})$
- 所有系数量纲为 $[t]^{-1}$
- $D, I$ 为无量纲归一化激活

### 1.3 边界条件

- $D(0), I(0) \in [0, 1]$
- $w_{DD}, w_{II} > 0$（自维持）
- $w_{ID}, w_{DI} > 0$（相互抑制）

---

## 2. 仿真脚本

### 2.1 文件位置

`simulations/dmn_insula_bistable.py`

### 2.2 功能

- 对两组初始条件（DMN 占优 vs 岛叶占优）进行时间序列积分
- 扫描注意力放大系数 $\alpha$，绘制分岔图
- 绘制相图与零倾线，展示双稳态吸引子

### 2.3 运行方式

```bash
pip install -r simulations/requirements.txt
python simulations/dmn_insula_bistable.py
```

输出：
- `simulations/dmn_insula_timeseries.png`
- `simulations/dmn_insula_bifurcation.png`
- `simulations/dmn_insula_phase_portrait.png`

### 2.4 关键参数（产生双稳态）

| 参数 | 值 | 生物学解释 |
|------|-----|-----------|
| $\tau_D$ | 1.0 s | DMN 时间常数 |
| $\tau_I$ | 0.8 s | 岛叶时间常数 |
| $w_{DD}$ | 1.6 | DMN 自维持权重 |
| $w_{II}$ | 1.4 | 岛叶自维持权重 |
| $w_{ID}$ | 0.9 | 岛叶→DMN 抑制 |
| $w_{DI}$ | 1.0 | DMN→岛叶抑制 |
| $S_D$ | 0.1 | DMN 外部驱动 |
| $S_I$ | 0.05 | 岛叶外部驱动 |
| $\alpha$ | 1.0 | 呼吸锚定放大系数 |
| $B$ | 0.4 | 呼吸锚定强度 |

---

## 3. 实验方案草案

### 3.1 研究问题

长期冥想练习是否通过降低 DMN 自维持权重 $w_{DD}$ 和增强岛叶→DMN 抑制权重 $w_{ID}$，使 DMN-岛叶双稳态系统的切换阈值降低？

### 3.2 被试

- 实验组：有经验的冥想者（>1,000 小时练习），N = 25
- 对照组：年龄、性别、教育程度匹配的非冥想者，N = 25

### 3.3 任务与指标

**任务**：静息态 fMRI 扫描 + 呼吸锚定任务（5 分钟有节奏呼吸专注）。

**主要指标**：
1. DMN-岛叶功能连接：PCC 与前岛叶时间序列的负相关强度
2. 切换阈值：在呼吸锚定任务中，DMN 活动首次显著下降所需的时间
3. 反刍量表（RRS）得分

**统计假设**：
- $H_0$：两组在切换阈值和 DMN-岛叶负相关强度上无显著差异
- $H_1$：冥想组切换阈值更低，DMN-岛叶负相关更强
- 预期效应量：Cohen's $d \approx 0.8$（中等到大效应）

### 3.4 与仿真的对应

| 实验指标 | 仿真对应 | 预期方向 |
|---------|---------|---------|
| 切换阈值降低 | $\alpha$ 增大或 $w_{DD}$ 减小时 $D^*$ 下降 | 冥想组 < 对照组 |
| DMN-岛叶负相关增强 | $w_{ID}, w_{DI}$ 增大 | 冥想组 > 对照组 |
| 反刍降低 | DMN 吸引子深度变浅 | 冥想组 < 对照组 |

---

## 4. 反事实条件

以下证据会削弱或推翻本命题：

1. 在严格控制下，长期冥想者与非冥想者在 DMN-岛叶切换阈值上无差异
2. 提高岛叶驱动（如通过呼吸反馈训练）不能降低 DMN 活动
3. 在病变或 TMS 抑制岛叶后，冥想者的 DMN 下调效应消失
4. 模型仿真显示，无论参数如何调整，系统都不存在双稳态

---

## 5. 当前局限

- 仿真是现象学模型，未与真实 fMRI 时间序列数据拟合
- 参数值目前为理论设定，需要从文献或试点数据中校准
- 实验方案尚未通过伦理审查或试点验证

---

## 6. 如何引用

> Project Dao.Science (2026). Verifiable Unit 01: DMN-Insula Bistable Switching. `verifiable_units/vu_01_dmn_insula.md`.
