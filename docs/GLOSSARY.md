# 项目概念索引与术语表

## Project Glossary and Concept Index

---

> 本文档是 Project Dao.Science 的完整概念索引。每个术语包含：中文 → English → 简短定义 → 主要出现位置。按层级分组。

---

## 一、核心公理 (Core Axioms)

| 术语 | 英文 | 定义 | 主要文件 |
|------|------|------|---------|
| 道 (Dao) | Dao / The Way | 意识启用的动态过程 ≡ $-\nabla_\theta G(\pi_\theta)$（连续参数化）或 $\pi_{\text{顺道}} = \arg\min_\pi G(\pi)$（离散选择）——预期自由能上的梯度流 | `1_first_principles/01_dao_as_process.md` |
| 一 (Yi) | One / Unity | 无阻塞的觉知带宽 $AB(t) = 1 - [R_{\text{DMN}}(t) - R_0] / [R_{\text{max}} - R_0]$ | `1_first_principles/02_one_as_bandwidth.md` |
| 相非物 | Map Not Territory | 心智内容百分百是万物之相，非万物全部 | `1_first_principles/03_map_not_territory.md` |
| L0-L7 频谱 | L0-L7 Spectrum | 从物自体（L0）到关系坍缩（L7）的八层认知地形图 | `0_motivation/L0_L7_spectrum.md` |

---

## 二、L0-L7 频谱

| 层级 | 名称 | 内容 | 关系状态 |
|------|------|------|---------|
| **L0** | 绝对事实 / 物自体 | 觉知本身、觉悟性洞见、不可被语言捕获 | 觉知与自身的关系——"明白" |
| **L1** | 物理规律 / 自然法则 | 可重复验证的知识、数学定理、物理定律 | 人与自然的契约关系 |
| **L2** | 个体实情 / 主观事实 | 个人感受、痛苦、喜悦、身体感知 | 自我与自身的内在关系 |
| **L3** | 群体共识 / 文化传承 | 叙事、仪式、传统、亲情、集体记忆 | 人与群体的文化关系 |
| **L4** | 理性合作 / 契约精神 | 逻辑推理、法律、项目管理、科学方法 | 人与人的契约关系 |
| **L5** | 互不干涉 / 关系断裂 | 冷漠、回避、边界固化 | 关系熵增——不再投入 |
| **L6** | 纯粹妄想 / 虚无主义 | 概念空转、脱离现实的信念闭环 | 心智内容自我繁殖——不再校准 |
| **L7** | 陷入战争 / 自取灭亡 | 系统的、有组织的毁灭行为 | 关系频谱的负向终点 |

---

## 三、预测编码与主动推理 (Predictive Coding & Active Inference)

| 术语 | 英文 | 符号 | 定义 |
|------|------|------|------|
| 自由能原理 | Free Energy Principle (FEP) | $F$ | 自组织系统最小化变分自由能以维持非平衡稳态 |
| 变分自由能 | Variational Free Energy | $F = D_{KL}[Q(s) \| P(s\|o)] - \ln P(o)$ | 近似后验与真实后验的 KL 散度 − 对数模型证据 |
| 预期自由能 | Expected Free Energy (EFE) | $G(\pi)$ | 策略 $\pi$ 下的预期未来自由能——驱动行动选择 |
| 精度矩阵 | Precision Matrix | $\Pi$ | 预测误差的逆方差——决定信念更新的权重 |
| 精度加权 | Precision Weighting | | 高精度预测误差 > 低精度预测误差对信念更新的影响 |
| 生成模型 | Generative Model | | 大脑关于世界如何生成感官数据的层级化概率模型 |
| 预测误差 | Prediction Error | $\xi$ | 感官输入与生成模型预测之间的差异 |
| 感知推理 | Perceptual Inference | $\dot{\mu}$ | 通过梯度下降更新隐藏状态估计以最小化预测误差 |
| 主动推理 | Active Inference | | 通过选择行动策略 $\pi$ 以最小化预期自由能 |
| 策略选择 | Policy Selection | $P(\pi) = \sigma(-\gamma G(\pi))$ | 软最大化预期自由能以选择行动策略（式 13ℴ） |
| 先验偏好 | Prior Preferences | $P(o\|C)$ | 系统期望接收的感官状态类型 |
| 认知价值 | Epistemic Value | | EFE 的信息增益组分——行动以减少不确定性 |
| 实用价值 | Pragmatic Value | | EFE 的偏好满足组分——行动以获得期望结果 |

---

## 四、道家概念映射 (Daoist Concept Mappings)

| 道家概念 | 英文 | 形式化定义 | 方程编号 |
|---------|------|-----------|---------|
| 道 (Dao) | The Way | $\text{Dao} \equiv -\nabla_\theta G(\pi_\theta)$（连续参数化）; $\pi_{\text{顺道}} = \arg\min_\pi G(\pi)$（离散选择） | (11) / (13) |
| 无为 (Wu-wei) | Effortless Action | 行动于 $\|\nabla_\theta G(\pi_\theta)\| < \tau$ 时 | (14) |
| 德 (De) | Virtue / Potency | $\Pi_{\text{德}} \equiv$ 生成模型的精度矩阵 | (15) |
| 自然 (Ziran) | Spontaneity | $\dot{\mu} = -\nabla_\mu F$（自组织动力学） | — |
| 观 (Guan) | Open Monitoring | $\Pi^{\text{attn}}_{\text{观}} \approx \frac{1}{N} I_N$ | (20) |
| 明 (Ming) | Clarity | $H[Q(s\|o)] \to 0$（低熵后验） | (21) |
| 玄 (Xuan) | Deep Reality | 高层级隐藏状态 $v^{(i)}, i \gg 1$ | — |
| 朴 (Pu) | Uncarved Block | 先验分布 $P(s)$ | — |
| 虚 (Xu) | Emptiness | 熵最大化后验 | — |
| 静 (Jing) | Stillness | $\dot{\mu} \approx 0$（收敛的信念更新） | — |
| 反 (Fan) | Return | 闭合的感知-行动循环 | — |
| 知足 (Zhi-zu) | Contentment | 局部自由能最小化（满意化） | — |
| 无 (Wu) | Non-Being | 极限层级 $v^{(\infty)}$（不可观察的生成模型层级） | — |

---

## 五、"二入四行"体系 (Two Entrances & Four Practices)

### 理入 (Li-ru / Entry by Principle)

| 术语 | 操作 | 神经对应 |
|------|------|---------|
| 理入 | 通过 L1/L4 的认知框架建立正确的最高层级先验 | 下调叙事自我的先验精度 |

### 行入四行 (Xing-ru / Entry by Practice — Four Practices)

| 行入 | 中文 | 核心操作 | 神经机制 | 临床对应 |
|------|------|---------|---------|---------|
| 报冤行 | Embrace Suffering | 甘心忍受逆境——重新框定为"过去习惯的成熟" | PFC↑ 调控杏仁核↓ | 认知重评 + ACT 接纳 |
| 随缘行 | Flow with Causes | 不执取顺境——看到"这也是条件的暂时聚合" | RPE 无常修正：$\delta_{\text{impermanence}}$ | 认知去融合 + 归因修正 |
| 无所求行 | Seek Nothing | 停止对特定结果的执着——"有求皆苦，无求乃乐" | 下调 NAc "想要"（wanting），保留"喜欢"（liking） | MBCT 去中心化 + 渴求冲浪 |
| 称法行 | Act in Accordance | 行动与"法"协调——"修行六度而无所行" | 降低行动-自我归属感（SoA）去耦合 | 行为激活 + 流状态 |

### 六度 (Six Paramitas)

| 六度 | 英文 | 生成模型优化维度 |
|------|------|----------------|
| 布施 (Dana) | Generosity | 降低"我-资源"刚性绑定 |
| 持戒 (Sila) | Ethical Conduct | 策略空间中的伦理约束先验 |
| 忍辱 (Ksanti) | Patience | 降低杏仁核对威胁的自动化反应 |
| 精进 (Virya) | Diligence | 维持后训练的持续性和强度 |
| 禅定 (Dhyana) | Concentration | 增强元参数 $\alpha$ 的调控精度 |
| 智慧 (Prajna) | Wisdom | 下调自我模型精度，上调"空性"精度 |

---

## 六、神经科学核心概念 (Core Neuroscience Concepts)

### 脑网络

| 术语 | 英文 | 核心节点 | 功能 |
|------|------|---------|------|
| 默认模式网络 | Default Mode Network (DMN) | mPFC, PCC, 角回 | 叙事自我、自传体记忆、走神 |
| 任务正性网络 | Task-Positive Network (TPN) | 背侧注意网络 | 外部任务执行、知觉加工 |
| 突显网络 | Salience Network | 前岛叶, dACC | DMN ↔ TPN 切换 |
| 镜像神经元系统 | Mirror Neuron System | 前运动皮层, 顶下小叶 | 观察学习、共情、模仿 |

### 脑区

| 术语 | 英文缩写 | 功能 |
|------|---------|------|
| 内侧前额叶皮层 | mPFC | 自我指涉加工、社会认知 |
| 后扣带回皮层 | PCC | 自传体记忆、DMN 集线器 |
| 前扣带回皮层 | ACC | 冲突监测、错误检测、认知控制 |
| 前岛叶 | Anterior Insula | 内感受的有意识感知、"全局情绪时刻" |
| 后岛叶 | Posterior Insula | 初级内感受皮层（身体状态的原始表征） |
| 杏仁核 | Amygdala | 威胁检测、恐惧条件化、情绪突显 |
| 伏隔核 | NAc | 奖励加工、"想要"（incentive salience） |
| 腹侧被盖区 | VTA | 多巴胺能神经元胞体、"想要"信号源 |
| 海马体 | Hippocampus | 情节记忆、空间导航、模式分离 |
| 颞顶联合区 | TPJ | 自我-他人区分、视角转换、SoA 高级判断 |

### 神经机制

| 术语 | 英文 | 定义 |
|------|------|------|
| 长时程增强 | LTP | 同步激活 → 突触增强 (NMDA 受体 → Ca²⁺ → CaMKII) |
| 长时程抑制 | LTD | 异步/低频激活 → 突触减弱 |
| 脉冲时序依赖可塑性 | STDP | Δt = t_post − t_pre 决定 LTP (>0) 或 LTD (<0) |
| 元可塑性 | Metaplasticity | 可塑性的可塑性——Bienenstock-Cooper-Munro (BCM) 滑动阈值 |
| Hebb 定律 | Hebb's Rule | "Fire together, wire together" |
| 认知重评 | Cognitive Reappraisal | PFC 调控杏仁核——重新解释刺激意义 |
| 去中心化 | Decentering | 将思维视为心智事件而非现实的反映 |
| 内感受 | Interoception | 对身体内部状态的感知（心跳、呼吸、内脏） |
| 自我归属感 | Sense of Agency (SoA) | "我在做这个"的感觉——"比较器模型" |
| 流状态 | Flow State | 完全沉浸——自我意识丧失 + 时间扭曲 + 暂时性前额叶活动降低 |

### 神经化学

| 术语 | 英文 | 功能 |
|------|------|------|
| 多巴胺 | Dopamine | "想要"（incentive salience）、RPE 编码 |
| 阿片类物质 | Opioids | "喜欢"（hedonic impact）——愉悦本身 |
| 内源性大麻素 | Endocannabinoids | "喜欢"——与阿片类物质协同 |
| NMDA 受体 | NMDA Receptor | 突触可塑性的"分子开关"——Ca²⁺ 内流 |
| 去甲肾上腺素 | Norepinephrine | 警觉、应激、"战斗或逃跑" |

---

## 七、核心方程索引 (Core Equation Index)

| 编号 | 方程 | 含义 | 主要文件 |
|------|------|------|---------|
| (1) | $v^{(i)} = g^{(i)}(v^{(i+1)}, \theta^{(i)}) + z^{(i)}$ | 层级化生成模型 | `01_dao_as_process.md` |
| (2) | $\xi^{(i)} = v^{(i)} - g^{(i)}(v^{(i+1)}, \theta^{(i)})$ | 预测误差 | `01_dao_as_process.md` |
| (4) | $F = D_{KL}[Q(s) \| P(s\|o)] - \ln P(o)$ | 变分自由能 | `01_dao_as_process.md` |
| (7) | $G(\pi) = E_{Q(o, s\|\pi)}[\ln Q(s\|\pi) - \ln P(o, s\|\pi)]$ | 预期自由能 | `01_dao_as_process.md` |
| (11) | $\text{道} \equiv -\nabla_\theta G(\pi_\theta)$ | 道作为梯度流（连续参数化） | `01_dao_as_process.md` |
| (12) | $\frac{d\theta}{dt} = -\eta \cdot \nabla_\theta G(\pi_\theta)$ | 策略参数的梯度流动力学 | `01_dao_as_process.md` |
| (13) | $\pi_{\text{顺道}} = \arg\min_\pi G(\pi)$ | 顺道的最优策略选择（离散形式） | `01_dao_as_process.md` |
| (13ℴ) | $P(\pi) = \sigma(-\gamma \cdot G(\pi))$ | 顺道的软最大化策略分布 | `01_dao_as_process.md` |
| (14) | $\text{无为} \equiv$ 行动于 $\|\nabla_\theta G(\pi_\theta)\| < \tau$ | 无为的阈值定义 | `01_dao_as_process.md` |
| (15) | $\Pi_{\text{德}} \equiv$ 生成模型的精度矩阵 | 德作为精度 | `01_dao_as_process.md` |
| (16) | $\Pi^{\text{eff}} = \Pi^{\text{base}} \otimes \Pi^{\text{attn}}$ | 注意力调制的有效精度 | `01_dao_as_process.md` |
| (20) | $\Pi^{\text{attn}}_{\text{观}} \approx \frac{1}{N} I_N$ | 观作为均匀精度 | `01_dao_as_process.md` |
| (21) | $\text{明} \equiv H[Q(s\|o)] \to 0$ | 明 = 低熵后验（清晰的觉知） | `01_dao_as_process.md` |
| AB(t) | $AB(t) = 1 - [R_{\text{DMN}}(t) - R_0] / [R_{\text{max}} - R_0]$ | 觉知带宽（标准化） | `02_one_as_bandwidth.md` |
| α | $\alpha \in [0, 1]$ | 注意力焦点-全局连续谱参数 | `attention_model.md` |
| RPE | $\delta_{\text{RPE}} = R_{\text{actual}} - R_{\text{predicted}}$ | 奖励预测误差 | `02_flow_with_causes.md` |
| 无常修正 | $\delta_{\text{corrected}} = \delta_{\text{RPE}} - \delta_{\text{impermanence}}$ | 随缘行的 RPE 修正 | `02_flow_with_causes.md` |
| 念起即觉 | $T_{\text{awareness}} = T_{\text{amygdala}} + \Delta T_{\text{detection}}$ | 觉知延迟 | `100ms_model.md` |
| 杏仁核-PFC 竞争 | $\tau_a \frac{da}{dt} = -a + w_{sa}S + w_{aa}f(a) - w_{pa}p$ | 竞争动力学 | `100ms_model.md` |
| DMN-岛叶竞争 | $\tau_D \frac{dD}{dt} = -D + w_{DD}\sigma(D) - w_{ID}\sigma(I) + S_D$ | 双稳态系统 | `dmn_self_model.md` |

---

## 八、关键引用作者索引 (Key Author Index)

| 作者 | 核心贡献 | 关键引用 |
|------|---------|---------|
| Friston, K. | 自由能原理、主动推理 | Friston (2010), Friston et al. (2017) |
| Clark, A. | 预测处理、"冲浪不确定性" | Clark (2016) |
| Seth, A. | 预测处理中的自我与意识 | Seth (2021) |
| LeDoux, J. | 情绪双通路理论 | LeDoux (1996, 2000) |
| Raichle, M. | DMN 的发现与命名 | Raichle et al. (2001) |
| Craig, A.D. (Bud) | 内感受与岛叶 | Craig (2002, 2009) |
| Metzinger, T. | 自我模型理论 | Metzinger (2003) |
| Damasio, A. | 多层自我、躯体标记假说 | Damasio (2010) |
| Gallagher, S. | 最小自我 vs 叙事自我 | Gallagher (2000) |
| Berridge, K. & Robinson, T. | "想要" vs "喜欢" | Berridge & Robinson (1998, 2003) |
| Korzybski, A. | "地图非疆域" | Korzybski (1933) |
| Csikszentmihalyi, M. | 流状态 | Csikszentmihalyi (1990) |
| Broughton, J. | 达摩《二入四行论》敦煌本英译 | Broughton (1999) |
| Kabat-Zinn, J. | MBSR 正念减压 | Kabat-Zinn (1990) |
| Hayes, S. | ACT 接纳承诺疗法 | Hayes et al. (2006) |
| Teasdale, J. | MBCT、去中心化 | Teasdale et al. (2002) |
| Ochsner, K. | 认知重评的 fMRI 研究 | Ochsner et al. (2002) |
| Hebb, D.O. | Hebb 定律 | Hebb (1949) |
| Varela, F. | 神经现象学 | Varela (1996) |

---

## 九、文件导航矩阵 (File Navigation Matrix)

| 文件 | 层级 | 核心命题 | 前一篇 | 后一篇 |
|------|------|---------|--------|--------|
| `project_map.md` | 导航 | 概念地图+六条阅读路径 | — | `why_this_matters.md` |
| `objections_and_replies.md` | 动机（元） | 六项核心挑战与回应 | (任一路径后) | (返回路径) |
| `why_this_matters.md` | 动机 | 三大危机+四方汇聚 | `project_map.md` | `cognition_in_progress.md` |
| `cognition_in_progress.md` | 动机 | 认知过程正在进行时+误会地图 | `why_this_matters.md` | `abstraction_dialogue.md` |
| `abstraction_dialogue.md` | 动机 | 两棵树+抽象的解释说 | `cognition_in_progress.md` | `L0_L7_spectrum.md` |
| `L0_L7_spectrum.md` | 动机 | L0-L7八层事实频谱 | `abstraction_dialogue.md` | `01_dao_as_process.md` |
| `01_dao_as_process.md` | 第一性原理 | 道 ≡ −∇G(π) | `L0_L7_spectrum.md` | `02_one_as_bandwidth.md` |
| `02_one_as_bandwidth.md` | 第一性原理 | AB(t) = Cmax − RDMN(t) | `01_dao_as_process.md` | `03_map_not_territory.md` |
| `03_map_not_territory.md` | 第一性原理 | 心智内容=万物之相 | `02_one_as_bandwidth.md` | `04_philosophy_of_science.md` |
| `04_philosophy_of_science.md` | 第一性原理 | 科学知识=多层嵌套L0-L7产物 | `03_map_not_territory.md` | `05_first_person_epistemology.md` |
| `05_first_person_epistemology.md` | 第一性原理 | 第一人称认识论+个体独特性+L0/L2 数据源 | `04_philosophy_of_science.md` | `06_emergence.md` |
| `06_emergence.md` | 第一性原理 | 涌现性+弱/强涌现+层级跃迁+约束条件 | `05_first_person_epistemology.md` | `07_cost_of_deviation.md` |
| `07_cost_of_deviation.md` | 第一性原理 | 偏离代价+Cost(π_dev)=G(π_actual)−G(π_opt)+预警信号+价值对齐失败 | `06_emergence.md` | `attention_model.md` |
| `attention_model.md` | 心智模型 | α 参数收放自如 | `07_cost_of_deviation.md` | `100ms_model.md` |
| `100ms_model.md` | 心智模型 | 念起即觉 + 竞争动力学 | `attention_model.md` | `neuroplasticity_loop.md` |
| `neuroplasticity_loop.md` | 心智模型 | 后训练 + Hebbian 重塑 | `100ms_model.md` | `dmn_self_model.md` |
| `dmn_self_model.md` | 心智模型 | DMN-岛叶-内感受三角 | `neuroplasticity_loop.md` | `social_cognition.md` |
| `social_cognition.md` | 心智模型 | 镜像共鸣+心智化+同体大悲 | `dmn_self_model.md` | `hypoxia_fifty_demons.md` |
| `hypoxia_fifty_demons.md` | 心智模型（补充） | 缺氧→前额叶失能→五十阴魔 | `social_cognition.md` | `li_ru.md` |
| `li_ru.md` | 实践方法 | 理入=下调叙事自我先验精度 | `hypoxia_fifty_demons.md` | `n_of_1_protocol.md` |
| `n_of_1_protocol.md` | 实践方法 | N-of-1 实验+个人科学+结构化日志 | `li_ru.md` | `01_embrace_suffering.md` |
| `01_embrace_suffering.md` | 实践方法 | 报冤行↔认知重评+ACT | `n_of_1_protocol.md` | `02_flow_with_causes.md` |
| `02_flow_with_causes.md` | 实践方法 | 随缘行↔RPE无常修正 | `01_embrace_suffering.md` | `03_seek_nothing.md` |
| `03_seek_nothing.md` | 实践方法 | 无所求行↔下调wanting | `02_flow_with_causes.md` | `04_act_in_accordance.md` |
| `04_act_in_accordance.md` | 实践方法 | 称法行↔降低SoA | `03_seek_nothing.md` | `ai_governance.md` |
| `ai_governance.md` | 应用 | 知止不殆+碳硅共生 | `04_act_in_accordance.md` | `education_by_field.md` |
| `education_by_field.md` | 应用 | 境教=环境设计作为教学法 | `ai_governance.md` | `clinical_mental_health.md` |
| `clinical_mental_health.md` | 应用 | 四行在临床中的应用 | `education_by_field.md` | `creativity_innovation.md` |
| `creativity_innovation.md` | 应用 | 无为的创造+酝酿-顿悟 | `clinical_mental_health.md` | `carbon_silicon_symbiosis.md` |
| `carbon_silicon_symbiosis.md` | 应用 | 碳硅共生+被需要+知止 | `creativity_innovation.md` | — |

---

## 十、项目术语 (Project Terms)

| 术语 | 英文 | 定义 | 主要文件 |
|------|------|------|---------|
| 第一人称认识论 | First-Person Epistemology | 在科学内部为第一人称经验与个体独特性建立不可还原地位的认识论框架 | `1_first_principles/05_first_person_epistemology.md` |
| 第一人称数据 | First-Person Data | 以觉知本身（L0）和个体实情（L2）为来源、原则上只有经验主体能直接获取的数据 | `1_first_principles/05_first_person_epistemology.md` |
| 结构化现象学报告 | Structured Phenomenological Report | 包含时间戳、情境、维度、强度、可信度、可证伪预测六要素的第一人称报告格式 | `1_first_principles/05_first_person_epistemology.md` |
| 个体参数化 | Individual Parameterization | 在群体共享的生成模型结构中，校准个体特有的先验精度、学习率等参数 | `1_first_principles/05_first_person_epistemology.md` |
| 认识论谦逊 | Epistemic Humility | 明确规律的适用边界，把个体例外视为模型校准信号而非噪声的认识论姿态 | `1_first_principles/05_first_person_epistemology.md` |
| N-of-1 实验 | N-of-1 Trial | 以单一被试（通常是自己）为对象、通过多次条件切换判断干预效果的单被试实验设计 | `3_methodology/n_of_1_protocol.md` |
| 个人科学 | Personal Science | 个体使用系统化方法在自己身上进行研究、以优化自身福祉的实践 | `3_methodology/n_of_1_protocol.md` |
| 生态瞬间评估 | Ecological Momentary Assessment (EMA) | 在自然日常生活情境中重复收集体验、行为和生理数据的方法 | `3_methodology/n_of_1_protocol.md` |
| 认知过程正在进行时 | Cognition in Progress | 认知总是用已定格的信息理解流动现实，因此误会不可避免 | `0_motivation/cognition_in_progress.md` |
| 误会地图 | Misunderstanding Map | 将感知、记忆、语言等认知失真机制映射到 L0-L7 频谱的分析工具 | `0_motivation/cognition_in_progress.md` |
| 认知转换链 | Cognitive Transformation Chain | 现实 → 感知采样 → 记忆重构 → 语言表达 → 他人理解的连续转换过程 | `0_motivation/cognition_in_progress.md` |
| 抽象即压缩 | Abstraction as Compression | 心智把异质个体信息折叠进范畴标签，以丢失细节换取行动效率 | `0_motivation/abstraction_dialogue.md` |
| 有效范围 | Effective Range | 日常行动在“足够好”的范围内运作，而非追求纳米级精度 | `0_motivation/abstraction_dialogue.md` |
| 涌现性 | Emergence | 系统整体表现出其组成部分所不具备的新性质 | `1_first_principles/06_emergence.md` |
| 弱涌现 | Weak Emergence | 新性质原则上可由微观规律推导，但实际计算不可行 | `1_first_principles/06_emergence.md` |
| 强涌现 | Strong Emergence | 新性质无法由微观规律完全推导，具有认识论上的不可还原性 | `1_first_principles/06_emergence.md` |
| 层级跃迁 | Level Jump | 从较低认知/物理尺度向较高尺度过渡时出现的性质突变 | `1_first_principles/06_emergence.md` |
| 计算不可约性 | Computational Irreducibility | 系统的宏观行为无法被更短的算法预测，必须逐步模拟 | `1_first_principles/06_emergence.md` |
| 偏离代价 | Cost of Deviation | 实际策略与最优策略之间的预期自由能差值：Cost(π_dev) = G(π_actual) − G(π_optimal) | `1_first_principles/07_cost_of_deviation.md` |
| 代价函数 | Cost Function | 将"偏离道"形式化为可观测、可测量的自由能增加量的数学函数 | `1_first_principles/07_cost_of_deviation.md` |
| 精度错配 | Precision Misallocation | 生成模型对某些先验赋予过高精度或对感官证据赋予过低精度，导致系统选择次优策略 | `1_first_principles/07_cost_of_deviation.md` |
| 价值对齐失败 | Value Alignment Failure | DMN 叙事自我为维持自我一致性而系统性高估 symbolic rewards、低估 physiological costs | `1_first_principles/07_cost_of_deviation.md` |
| 预警信号 | Early Warning Signal | 可被第一人称觉察的偏离道早期指标，按 L0-L7 层级组织 | `1_first_principles/07_cost_of_deviation.md` |
| 累积代价 | Cumulative Cost | 偏离代价在时间上的积分——短期偏离通常可逆，长期累积可能导致不可逆的结构损伤 | `1_first_principles/07_cost_of_deviation.md` |
| 叙事自我 | Narrative Self | 由 DMN 维持的跨时间连贯的自我叙事——"我是谁，我来自哪里，我要去哪里" | `1_first_principles/07_cost_of_deviation.md` |

---

## 十一、学术预印本索引

| # | 标题 | 来源模块 | 核心方程 | 参考文献 |
|---|------|---------|---------|---------|
| 1 | [道作为过程](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_1/main.tex) | `01_dao_as_process.md` | 道 ≡ -∇_θ G(π_θ)（21 方程） | 15 |
| 2 | [L0-L7 事实频谱](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_2/main.tex) | `L0_L7_spectrum.md` | L0-L7 认知频谱框架 | 11 |
| 3 | [DMN-自我-内感受三角](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_3/main.tex) | `dmn_self_model.md` | DMN-岛叶双稳态 ODE（6 方程） | 18 |
| 4 | [科学知识的认知层级](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_4/main.tex) | `04_philosophy_of_science.md` | 贝叶斯后验归纳（1 方程） | 12 |
| 5 | [社会认知与镜像共鸣](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_5/main.tex) | `social_cognition.md` | SAB(t) 操作化（2 方程） | 22 |
| 6 | [创造力与创新](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_6/main.tex) | `creativity_innovation.md` | DMN-ECN 耦合 ODE（3 方程） | 15 |
| 7 | [碳硅共生](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_7/main.tex) | `carbon_silicon_symbiosis.md` | 知止 EFE 形式化（2 方程） | 12 |
| 8 | [境教](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_8/main.tex) | `education_by_field.md` | 四大道场设计原则 | 12 |

所有预印本使用标准 LaTeX 编译（`pdflatex main.tex` × 2）。详见 `paper/README.md`。

---

*本索引随项目内容更新而持续维护。最后更新：2026年6月13日。*
