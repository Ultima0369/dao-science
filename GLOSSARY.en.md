# Project Glossary and Concept Index

## 项目概念索引与术语表

---

> This document is the English concept index for Project Dao.Science. Each entry contains: English → Chinese → short definition → primary location. Grouped by layer.
>
> For the complete glossary, see [`GLOSSARY.md`](GLOSSARY.md).

---

## I. Core Axioms

| Term | Chinese | Definition | Primary file |
|------|---------|------------|--------------|
| Dao | 道 (Dao) | Dynamic process of mind-enabled action ≡ $-\nabla_\theta G(\pi_\theta)$ (continuous parameterization) or $\pi_{\text{accord}} = \arg\min_\pi G(\pi)$ (discrete selection)—gradient flow on expected free energy | `1_first_principles/01_dao_as_process.md` |
| One | 一 (Yi) | Unobstructed awareness bandwidth $AB(t) = 1 - [R_{\text{DMN}}(t) - R_0] / [R_{\text{max}} - R_0]$ | `1_first_principles/02_one_as_bandwidth.md` |
| Map Not Territory | 相非物 | Mental content is 100% appearance of things, not the totality of things | `1_first_principles/03_map_not_territory.md` |
| L0–L7 Spectrum | L0-L7 频谱 | Eight-layer cognitive terrain from noumenon (L0) to relational collapse (L7) | `0_motivation/L0_L7_spectrum.md` |

---

## II. The L0–L7 Spectrum

| Level | Name | Content | Relational state |
|-------|------|---------|------------------|
| **L0** | Absolute fact / Noumenon | Awareness itself, awakened insight, what cannot be captured by language | The relation of awareness to itself—"seeing" |
| **L1** | Physical law / Natural law | Reproducibly verifiable knowledge, mathematical theorems, physical laws | The contractual relation between humans and nature |
| **L2** | Individual reality / Subjective fact | Personal feelings, pain, joy, bodily sensations | The inner relation of self to itself |
| **L3** | Group consensus / Cultural inheritance | Narrative, ritual, tradition, kinship, collective memory | The cultural relation between person and group |
| **L4** | Rational cooperation / Contractual spirit | Logical reasoning, law, project management, scientific method | The contractual relation between persons |
| **L5** | Non-interference / Relational rupture | Indifference, avoidance, rigidified boundaries | Relational entropy—no further investment |
| **L6** | Pure delusion / Nihilism | Conceptual spinning, closed belief loops detached from reality | Mental content self-reproduces—no longer calibrated |
| **L7** | War / Self-destruction | Systematic, organized destructive behavior | The negative endpoint of the relational spectrum |

---

## III. Predictive Coding & Active Inference

| Term | Chinese | Symbol | Definition |
|------|---------|--------|------------|
| Free Energy Principle | 自由能原理 | $F$ | Self-organizing systems minimize variational free energy to maintain non-equilibrium steady state |
| Variational Free Energy | 变分自由能 | $F = D_{KL}[Q(s) \| P(s\|o)] - \ln P(o)$ | KL divergence between approximate and true posteriors minus log model evidence |
| Expected Free Energy | 预期自由能 | $G(\pi)$ | Expected future free energy under strategy $\pi$—drives action selection |
| Precision Matrix | 精度矩阵 | $\Pi$ | Inverse variance of prediction errors—determines weight of belief update |
| Precision Weighting | 精度加权 | | High-precision prediction errors influence belief updates more than low-precision ones |
| Generative Model | 生成模型 | | Brain's hierarchical probabilistic model of how the world generates sensory data |
| Prediction Error | 预测误差 | $\xi$ | Difference between sensory input and generative-model prediction |
| Perceptual Inference | 感知推理 | $\dot{\mu}$ | Updating hidden-state estimates by gradient descent to minimize prediction error |
| Active Inference | 主动推理 | | Selecting action policy $\pi$ to minimize expected free energy |
| Policy Selection | 策略选择 | $P(\pi) = \sigma(-\gamma G(\pi))$ | Soft-maximizing expected free energy to choose action policy |
| Prior Preferences | 先验偏好 | $P(o\|C)$ | Types of sensory states the system expects/desires |
| Epistemic Value | 认知价值 | | Information-gain component of EFE—act to reduce uncertainty |
| Pragmatic Value | 实用价值 | | Preference-satisfaction component of EFE—act to obtain desired outcomes |

---

## IV. Daoist Concept Mappings

| Daoist concept | English | Formalization | Equation |
|----------------|---------|---------------|----------|
| Dao | Dao / The Way | Gradient flow of expected free energy | $\text{Dao} \equiv -\nabla_\theta G(\pi_\theta)$ |
| De | De / Virtue | Precision matrix of the generative model | $\Pi_{\text{gen}}$ |
| Wu Wei | Wu Wei / Non-action | Action aligned with minimum expected free energy | $\pi_{\text{accord}} = \arg\min_\pi G(\pi)$ |
| Zhi Zhi | Knowing when to stop | Halting criterion when uncertainty or deviation cost exceeds threshold | $\text{Cost}(\pi_{\text{dev}}) > \theta_{\text{stop}}$ |
| Guan | Guan / Contemplation | Uniform precision allocation—open awareness | $\Pi_{\text{attention}} \approx \bar{\Pi}$ |

---

## V. Neuroscience & Cognitive Models

| Term | Chinese | Definition | Primary file |
|------|---------|------------|--------------|
| DMN | 默认模式网络 | Default Mode Network; active during self-referential processing and mind-wandering | `2_models/dmn_self_model.md` |
| TPN | 任务正网络 | Task-Positive Network; active during externally directed attention | `2_models/attention_model.md` |
| Insula | 岛叶 | Brain region integrating interoceptive and exteroceptive signals | `2_models/dmn_self_model.md` |
| Amygdala Hijack | 杏仁核劫持 | Amygdala-driven response before prefrontal regulation engages | `2_models/100ms_model.md` |
| Hebbian Learning | Hebbian 学习 | Cells that fire together wire together | `2_models/neuroplasticity_loop.md` |
| LTP | 长时程增强 | Long-term potentiation—synaptic strengthening | `2_models/neuroplasticity_loop.md` |
| LTD | 长时程抑制 | Long-term depression—synaptic weakening | `2_models/neuroplasticity_loop.md` |
| STDP | 脉冲时序依赖可塑性 | Spike-timing-dependent plasticity | `2_models/neuroplasticity_loop.md` |
| Meta-plasticity | 元可塑性 | Plasticity of synaptic plasticity itself | `2_models/neuroplasticity_loop.md` |
| Awareness Bandwidth | 觉知带宽 | Relative available cognitive resources when DMN is down-regulated | `1_first_principles/02_one_as_bandwidth.md` |
| Attentional Precision | 注意力精度 | Precision weight assigned to a sensory channel or hypothesis | `2_models/attention_model.md` |

---

## VI. Practice Methodology

| Term | Chinese | Definition | Primary file |
|------|---------|------------|--------------|
| Li Ru | 理入 | Entry through understanding—establishing the view | `3_methodology/li_ru.md` |
| Xing Ru | 行入 | Entry through practice—the four practices | `3_methodology/xing_ru/` |
| Embracing Suffering | 报冤行 | First practice: accepting suffering as karmic debt | `3_methodology/xing_ru/01_embrace_suffering.md` |
| Flowing with Causes | 随缘行 | Second practice: flowing with causes and conditions | `3_methodology/xing_ru/02_flow_with_causes.md` |
| Seeking Nothing | 无所求行 | Third practice: releasing attachment and seeking | `3_methodology/xing_ru/03_seek_nothing.md` |
| Acting in Accordance | 称法行 | Fourth practice: acting in accordance with reality | `3_methodology/xing_ru/04_act_in_accordance.md` |
| N-of-1 Protocol | N-of-1 协议 | Turning first-person experience into testable data | `3_methodology/n_of_1_protocol.md` |

---

## VII. Applications

| Term | Chinese | Definition | Primary file |
|------|---------|------------|--------------|
| AI Governance | AI 治理 | Compiling "knowing when to stop" into AI safety constraints | `4_applications/ai_governance.md` |
| Education by Field | 境教 | Environmental design as pedagogy | `4_applications/education_by_field.md` |
| Clinical Mental Health | 临床心理健康 | Applying the four practices in anxiety, depression, PTSD | `4_applications/clinical_mental_health.md` |
| Creativity & Innovation | 创造力与创新 | Wu-wei creativity and insight emergence | `4_applications/creativity_innovation.md` |
| Carbon-Silicon Symbiosis | 碳硅共生 | Relational leap from "it" to "thou" between humans and AI | `4_applications/carbon_silicon_symbiosis.md` |
| Management | 管理 | Manager as first-person node in organizational complex system | `4_applications/management.md` |

---

## VIII. Evidence Badges

| Badge | Level | Meaning |
|-------|-------|---------|
| **F** | Formal | Formalized definition or mathematical analogy |
| **S** | Simulation | Supported by runnable simulation |
| **B** | Behavioral | Supported by behavioral/phenomenological evidence |
| **N** | Neural | Supported by neuroscience evidence |
| **M** | Meta-ethical / Normative | Normative claim not purely empirically falsifiable |

For full details see [`NOTATION.en.md`](NOTATION.en.md).

---

> 返回中文版：[`GLOSSARY.md`](GLOSSARY.md)
