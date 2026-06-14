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

## V. Core Neuroscience Concepts

### Brain Networks

| Term | Chinese | Core nodes | Function |
|------|---------|------------|----------|
| Default Mode Network (DMN) | 默认模式网络 | mPFC, PCC, angular gyrus | Narrative self, autobiographical memory, mind-wandering |
| Task-Positive Network (TPN) | 任务正性网络 | Dorsal attention network | External task execution, perceptual processing |
| Salience Network | 突显网络 | Anterior insula, dACC | Switching between DMN and TPN |
| Mirror Neuron System | 镜像神经元系统 | Premotor cortex, inferior parietal lobule | Observational learning, empathy, imitation |

### Brain Regions

| Term | Abbreviation | Function |
|------|--------------|----------|
| Medial Prefrontal Cortex | mPFC | Self-referential processing, social cognition |
| Posterior Cingulate Cortex | PCC | Autobiographical memory, DMN hub |
| Anterior Cingulate Cortex | ACC | Conflict monitoring, error detection, cognitive control |
| Anterior Insula | AI | Conscious perception of interoception, "global emotional moment" |
| Posterior Insula | PI | Primary interoceptive cortex (raw representation of bodily states) |
| Amygdala | — | Threat detection, fear conditioning, emotional salience |
| Nucleus Accumbens | NAc | Reward processing, "wanting" (incentive salience) |
| Ventral Tegmental Area | VTA | Dopaminergic neuron soma, source of "wanting" signals |
| Hippocampus | — | Episodic memory, spatial navigation, pattern separation |
| Temporoparietal Junction | TPJ | Self-other distinction, perspective taking, high-level SoA judgment |

### Neural Mechanisms

| Term | Chinese | Definition |
|------|---------|------------|
| Long-Term Potentiation (LTP) | 长时程增强 | Synchronous activation → synaptic strengthening (NMDA receptor → Ca²⁺ → CaMKII) |
| Long-Term Depression (LTD) | 长时程抑制 | Asynchronous/low-frequency activation → synaptic weakening |
| Spike-Timing-Dependent Plasticity (STDP) | 脉冲时序依赖可塑性 | $\Delta t = t_{\text{post}} - t_{\text{pre}}$ determines LTP (>0) or LTD (<0) |
| Metaplasticity | 元可塑性 | Plasticity of plasticity—Bienenstock-Cooper-Munro (BCM) sliding threshold |
| Hebb's Rule | Hebb 定律 | "Cells that fire together wire together" |
| Cognitive Reappraisal | 认知重评 | PFC regulation of amygdala—reinterpreting stimulus meaning |
| Decentering | 去中心化 | Viewing thoughts as mental events rather than reflections of reality |
| Interoception | 内感受 | Perception of the body's internal state (heartbeat, respiration, viscera) |
| Sense of Agency (SoA) | 自我归属感 | "I am doing this" feeling—comparator model |
| Flow State | 流状态 | Full immersion—loss of self-consciousness, time distortion, transient prefrontal hypofrontality |

### Neurochemistry

| Term | Chinese | Function |
|------|---------|----------|
| Dopamine | 多巴胺 | "Wanting" (incentive salience), RPE encoding |
| Opioids | 阿片类物质 | "Liking" (hedonic impact)—pleasure itself |
| Endocannabinoids | 内源性大麻素 | "Liking"—synergizes with opioids |
| NMDA Receptor | NMDA 受体 | "Molecular switch" of synaptic plasticity—Ca²⁺ influx |
| Norepinephrine | 去甲肾上腺素 | Arousal, stress, "fight or flight" |

---

## VI. Two Entrances & Four Practices

### Li-ru (Entry by Principle)

| Term | Operation | Neural correlate |
|------|-----------|------------------|
| Li-ru | Establish correct top-level priors through L1/L4 cognitive frameworks | Down-regulate narrative-self prior precision |

### Xing-ru / Entry by Practice — Four Practices

| Xing-ru | Chinese | Core operation | Neural mechanism | Clinical correlate |
|---------|---------|----------------|------------------|--------------------|
| Embrace Suffering | 报冤行 | Willingly endure adversity—reframe it as "the ripening of past habits" | PFC↑ regulates amygdala↓ | Cognitive reappraisal + ACT acceptance |
| Flow with Causes | 随缘行 | Non-attachment to favorable conditions—see "this too is a temporary aggregation of conditions" | RPE impermanence correction: $\delta_{\text{impermanence}}$ | Cognitive defusion + attribution correction |
| Seek Nothing | 无所求行 | Stop clinging to specific outcomes—"with seeking comes suffering, without seeking comes joy" | Down-regulate NAc "wanting" while preserving "liking" | MBCT decentering + urge surfing |
| Act in Accordance | 称法行 | Act in harmony with "Dharma"—"cultivate the six perfections while acting without acting" | Decouple action-self attribution (SoA) | Behavioral activation + flow state |

### Six Paramitas

| Paramita | Chinese | Generative-model optimization dimension |
|----------|---------|----------------------------------------|
| Dana (Generosity) | 布施 | Reduce "self-resource" rigidity |
| Sila (Ethical Conduct) | 持戒 | Ethical-constraint prior in policy space |
| Ksanti (Patience) | 忍辱 | Reduce amygdala automatic threat response |
| Virya (Diligence) | 精进 | Maintain post-training continuity and intensity |
| Dhyana (Concentration) | 禅定 | Enhance meta-parameter $\alpha$ regulatory precision |
| Prajna (Wisdom) | 智慧 | Down-regulate self-model precision, up-regulate "emptiness" precision |

---

## VII. Core Equation Index

| # | Equation | Meaning | Primary file |
|---|----------|---------|--------------|
| (1) | $v^{(i)} = g^{(i)}(v^{(i+1)}, \theta^{(i)}) + z^{(i)}$ | Hierarchical generative model | `1_first_principles/01_dao_as_process.md` |
| (2) | $\xi^{(i)} = v^{(i)} - g^{(i)}(v^{(i+1)}, \theta^{(i)})$ | Prediction error | `1_first_principles/01_dao_as_process.md` |
| (3) | $\dot{\mu}^{(i)} = -\frac{\partial \tilde{\epsilon}^{(i)T}}{\partial \mu^{(i)}} \Pi^{(i)} \tilde{\epsilon}^{(i)} + \frac{\partial g^{(i)T}}{\partial \mu^{(i)}} \Pi_{v}^{(i-1)} \tilde{\epsilon}_{v}^{(i-1)} - \Pi_{v}^{(i)} \tilde{\epsilon}_{v}^{(i)}$ | Perceptual inference dynamics | `1_first_principles/01_dao_as_process.md` |
| (4) | $F = D_{KL}[Q(s) \| P(s\|o)] - \ln P(o)$ | Variational free energy | `1_first_principles/01_dao_as_process.md` |
| (5) | $F \geq -\ln P(o)$ | Free-energy inequality | `1_first_principles/01_dao_as_process.md` |
| (6) | $F = -E_{Q(s)}[\ln P(o \| s)] + D_{KL}[Q(s) \| P(s)]$ | Free-energy accuracy-complexity decomposition | `1_first_principles/01_dao_as_process.md` |
| (7) | $G(\pi) = E_{Q(o, s\|\pi)}[\ln Q(s\|\pi) - \ln P(o, s\|\pi)]$ | Expected free energy | `1_first_principles/01_dao_as_process.md` |
| (8) | $G(\pi) = -E_{Q(o\|\pi)}[D_{KL}[Q(s\|o, \pi) \| Q(s\|\pi)]] - E_{Q(o\|\pi)}[\ln P(o\|C)]$ | EFE epistemic-pragmatic decomposition | `1_first_principles/01_dao_as_process.md` |
| (9) | $G(\pi) = D_{KL}[Q(o\|\pi) \| P(o\|C)] + E_{Q(s\|\pi)}[H[P(o\|s)]]$ | EFE risk-ambiguity decomposition | `1_first_principles/01_dao_as_process.md` |
| (10) | $P(\pi) = \sigma(-\gamma \cdot G(\pi))$ | Policy selection (discrete soft-max) | `1_first_principles/01_dao_as_process.md` |
| (11) | $\text{Dao} \equiv -\nabla_\theta G(\pi_\theta)$ | Dao as gradient flow (continuous parameterization) | `1_first_principles/01_dao_as_process.md` |
| (12) | $\frac{d\theta}{dt} = -\eta \cdot \nabla_\theta G(\pi_\theta)$ | Gradient-flow dynamics of policy parameters | `1_first_principles/01_dao_as_process.md` |
| (13) | $\pi_{\text{accord}} = \arg\min_\pi G(\pi)$ | Optimal policy selection in accord with Dao (discrete form) | `1_first_principles/01_dao_as_process.md` |
| (13a) | $P(\pi) = \sigma(-\gamma \cdot G(\pi))$ | Soft-max policy distribution in accord with Dao | `1_first_principles/01_dao_as_process.md` |
| (14) | $\text{Wu-wei} \equiv$ action when $\|\nabla_\theta G(\pi_\theta)\| < \tau$ | Threshold definition of Wu-wei | `1_first_principles/01_dao_as_process.md` |
| (15) | $\Pi_{\text{De}} \equiv$ precision matrix of the generative model | De as precision | `1_first_principles/01_dao_as_process.md` |
| (16) | $\Pi^{\text{eff}} = \Pi^{\text{base}} \otimes \Pi^{\text{attn}}$ | Attention-modulated effective precision | `1_first_principles/01_dao_as_process.md` |
| (17) | $\|\Pi^{\text{attn}}\|_{\text{max}} \gg \|\Pi^{\text{attn}}\|_{\text{min}}$ | Gathering—convergent precision configuration | `1_first_principles/01_dao_as_process.md` |
| (18) | $\|\Pi^{\text{attn}}\|_{\text{max}} \approx \|\Pi^{\text{attn}}\|_{\text{min}}$ | Releasing—diffuse precision configuration | `1_first_principles/01_dao_as_process.md` |
| (19) | $\text{Dynamic Range} = \frac{\max_t \|\Pi^{\text{attn}}(t)\|_{\max}}{\min_t \|\Pi^{\text{attn}}(t)\|_{\max}} \gg 1$ | Ease—precision dynamic range | `1_first_principles/01_dao_as_process.md` |
| (20) | $\tilde{\Pi}^{\text{attn}}_{\text{Guan}} \approx \frac{1}{N} I_N$ | Guan as normalized uniform precision | `1_first_principles/01_dao_as_process.md` |
| (21) | $\text{Ming} \equiv H[Q(s\|o)] \to 0$ | Ming = low-entropy posterior (clear awareness) | `1_first_principles/01_dao_as_process.md` |
| AB(t) | $AB(t) = 1 - [R_{\text{DMN}}(t) - R_0] / [R_{\text{max}} - R_0]$ | Awareness bandwidth (normalized) | `1_first_principles/02_one_as_bandwidth.md` |
| α | $\alpha \in [0, 1]$ | Focus-global attention continuum parameter | `2_models/attention_model.md` |
| RPE | $\delta_{\text{RPE}} = R_{\text{actual}} - R_{\text{predicted}}$ | Reward prediction error | `3_methodology/xing_ru/02_flow_with_causes.md` |
| Impermanence correction | $\delta_{\text{corrected}} = \delta_{\text{RPE}} - \delta_{\text{impermanence}}$ | RPE correction for Flowing with Causes | `3_methodology/xing_ru/02_flow_with_causes.md` |
| Awareness at thought's arising | $T_{\text{awareness}} = T_{\text{amygdala}} + \Delta T_{\text{detection}}$ | Awareness latency | `2_models/100ms_model.md` |
| Amygdala-PFC competition | $\tau_a \frac{da}{dt} = -a + w_{sa}S + w_{aa}f(a) - w_{pa}p$ | Competitive dynamics | `2_models/100ms_model.md` |
| DMN-Insula competition | $\tau_D \frac{dD}{dt} = -D + w_{DD}\sigma(D) - w_{ID}\sigma(I) + S_D$ | Bistable system | `2_models/dmn_self_model.md` |
| (11.1) | $S(s) = \alpha (\ln s - \ln s_{\text{opt}})^2 + S_0$ | Scale dependence of moral silence | `verifiable_units/vu_11_scale_and_moral_silence.en.md` |
| (11.2) | $A(s) = A_{\max} \exp(-|\ln s - \ln s_{\text{opt}}| / \tau)$ | Scale dependence of action propensity | `verifiable_units/vu_11_scale_and_moral_silence.en.md` |

---

## VIII. Key Author Index

| Author | Core contribution | Key references |
|--------|-------------------|----------------|
| Friston, K. | Free Energy Principle, Active Inference | Friston (2010), Friston et al. (2017) |
| Clark, A. | Predictive processing, "surfing uncertainty" | Clark (2016) |
| Seth, A. | Self and consciousness in predictive processing | Seth (2021) |
| LeDoux, J. | Dual-pathway theory of emotion | LeDoux (1996, 2000) |
| Raichle, M. | Discovery and naming of the DMN | Raichle et al. (2001) |
| Craig, A.D. (Bud) | Interoception and insula | Craig (2002, 2009) |
| Metzinger, T. | Self-model theory | Metzinger (2003) |
| Damasio, A. | Multi-layered self, somatic marker hypothesis | Damasio (2010) |
| Gallagher, S. | Minimal self vs. narrative self | Gallagher (2000) |
| Berridge, K. & Robinson, T. | "Wanting" vs. "liking" | Berridge & Robinson (1998, 2003) |
| Korzybski, A. | "The map is not the territory" | Korzybski (1933) |
| Csikszentmihalyi, M. | Flow state | Csikszentmihalyi (1990) |
| Broughton, J. | English translation of Bodhidharma's *Two Entrances and Four Practices* (Dunhuang manuscript) | Broughton (1999) |
| Kabat-Zinn, J. | Mindfulness-Based Stress Reduction (MBSR) | Kabat-Zinn (1990) |
| Hayes, S. | Acceptance and Commitment Therapy (ACT) | Hayes et al. (2006) |
| Teasdale, J. | MBCT, decentering | Teasdale et al. (2002) |
| Ochsner, K. | fMRI studies of cognitive reappraisal | Ochsner et al. (2002) |
| Hebb, D.O. | Hebb's rule | Hebb (1949) |
| Varela, F. | Neurophenomenology | Varela (1996) |

---

## IX. File Navigation Matrix

| File | Layer | Core proposition | Previous | Next |
|------|-------|------------------|----------|------|
| `project_map.md` | Navigation | Concept map + six reading paths | — | `why_this_matters.md` |
| `objections_and_replies.md` | Motivation (meta) | Six core challenges and replies | (after any path) | (return to path) |
| `why_this_matters.md` | Motivation | Three crises + four convergences | `project_map.md` | `cognition_in_progress.md` |
| `cognition_in_progress.md` | Motivation | Cognition in progress + misunderstanding map | `why_this_matters.md` | `abstraction_dialogue.md` |
| `abstraction_dialogue.md` | Motivation | Two trees + abstraction as explanation | `cognition_in_progress.md` | `L0_L7_spectrum.md` |
| `L0_L7_spectrum.md` | Motivation | L0–L7 eight-layer fact spectrum | `abstraction_dialogue.md` | `01_dao_as_process.md` |
| `01_dao_as_process.md` | First principles | Dao ≡ −∇G(π) | `L0_L7_spectrum.md` | `02_one_as_bandwidth.md` |
| `02_one_as_bandwidth.md` | First principles | AB(t) = 1 − [R_DMN(t) − R_0]/[R_max − R_0] | `01_dao_as_process.md` | `03_map_not_territory.md` |
| `03_map_not_territory.md` | First principles | Mental content = appearance of things | `02_one_as_bandwidth.md` | `04_philosophy_of_science.md` |
| `04_philosophy_of_science.md` | First principles | Scientific knowledge = nested L0–L7 product | `03_map_not_territory.md` | `05_first_person_epistemology.md` |
| `05_first_person_epistemology.md` | First principles | First-person epistemology + individual uniqueness + L0/L2 data sources | `04_philosophy_of_science.md` | `06_emergence.md` |
| `06_emergence.md` | First principles | Emergence + weak/strong emergence + level jumps + constraints | `05_first_person_epistemology.md` | `07_cost_of_deviation.md` |
| `07_cost_of_deviation.md` | First principles | Cost of deviation + Cost(π_dev)=G(π_actual)−G(π_opt) + early warning signals + value-alignment failure | `06_emergence.md` | `attention_model.md` |
| `attention_model.md` | Mental model | α parameter: gather and release at will | `07_cost_of_deviation.md` | `100ms_model.md` |
| `100ms_model.md` | Mental model | Awareness at thought's arising + competitive dynamics | `attention_model.md` | `neuroplasticity_loop.md` |
| `neuroplasticity_loop.md` | Mental model | Post-training + Hebbian reshaping | `100ms_model.md` | `dmn_self_model.md` |
| `dmn_self_model.md` | Mental model | DMN–insula–interoception triangle | `neuroplasticity_loop.md` | `social_cognition.md` |
| `social_cognition.md` | Mental model | Mirror resonance + mentalizing + compassion of same-body | `dmn_self_model.md` | `hypoxia_fifty_demons.md` |
| `hypoxia_fifty_demons.md` | Mental model (supplement) | Hypoxia → prefrontal failure → fifty demons | `social_cognition.md` | `li_ru.md` |
| `li_ru.md` | Practice method | Li-ru = down-regulate narrative-self prior precision | `hypoxia_fifty_demons.md` | `n_of_1_protocol.md` |
| `n_of_1_protocol.md` | Practice method | N-of-1 experiment + personal science + structured log | `li_ru.md` | `01_embrace_suffering.md` |
| `01_embrace_suffering.md` | Practice method | Embrace Suffering ↔ cognitive reappraisal + ACT | `n_of_1_protocol.md` | `02_flow_with_causes.md` |
| `02_flow_with_causes.md` | Practice method | Flow with Causes ↔ RPE impermanence correction | `01_embrace_suffering.md` | `03_seek_nothing.md` |
| `03_seek_nothing.md` | Practice method | Seek Nothing ↔ down-regulate wanting | `02_flow_with_causes.md` | `04_act_in_accordance.md` |
| `04_act_in_accordance.md` | Practice method | Act in Accordance ↔ reduce SoA | `03_seek_nothing.md` | `ai_governance.md` |
| `ai_governance.md` | Application | Knowing when to stop + carbon-silicon symbiosis | `04_act_in_accordance.md` | `education_by_field.md` |
| `education_by_field.md` | Application | Education by field = environmental design as pedagogy | `ai_governance.md` | `clinical_mental_health.md` |
| `clinical_mental_health.md` | Application | Four practices in clinical settings | `education_by_field.md` | `creativity_innovation.md` |
| `creativity_innovation.md` | Application | Wu-wei creativity + incubation–insight | `clinical_mental_health.md` | `carbon_silicon_symbiosis.md` |
| `carbon_silicon_symbiosis.md` | Application | Carbon-silicon symbiosis + being needed + knowing when to stop | `creativity_innovation.md` | — |

---

## X. Project Terms

| Term | Chinese | Definition | Primary file |
|------|---------|------------|--------------|
| First-Person Epistemology | 第一人称认识论 | An epistemological framework that establishes an irreducible place for first-person experience and individual uniqueness within science | `1_first_principles/05_first_person_epistemology.md` |
| First-Person Data | 第一人称数据 | Data sourced from awareness itself (L0) and individual reality (L2), accessible in principle only to the experiencing subject | `1_first_principles/05_first_person_epistemology.md` |
| Structured Phenomenological Report | 结构化现象学报告 | First-person report format including timestamp, context, dimensions, intensity, confidence, and falsifiable predictions | `1_first_principles/05_first_person_epistemology.md` |
| Individual Parameterization | 个体参数化 | Calibrating individual-specific parameters such as prior precision and learning rates within a population-shared generative-model structure | `1_first_principles/05_first_person_epistemology.md` |
| Epistemic Humility | 认识论谦逊 | The epistemological stance of explicitly marking the boundaries of a regularity's applicability and treating individual exceptions as model-calibration signals rather than noise | `1_first_principles/05_first_person_epistemology.md` |
| N-of-1 Trial | N-of-1 实验 | Single-subject experimental design (usually self-experimentation) that uses repeated condition switches to judge intervention effects | `3_methodology/n_of_1_protocol.md` |
| Personal Science | 个人科学 | The practice of individuals using systematic methods to conduct research on themselves to optimize their own well-being | `3_methodology/n_of_1_protocol.md` |
| Ecological Momentary Assessment (EMA) | 生态瞬间评估 | Method for repeatedly collecting experience, behavior, and physiological data in natural daily-life contexts | `3_methodology/n_of_1_protocol.md` |
| Cognition in Progress | 认知过程正在进行时 | Cognition always understands flowing reality through already-fixed information, so misunderstanding is inevitable | `0_motivation/cognition_in_progress.md` |
| Misunderstanding Map | 误会地图 | Analytical tool that maps perceptual, memory, and linguistic distortion mechanisms onto the L0–L7 spectrum | `0_motivation/cognition_in_progress.md` |
| Cognitive Transformation Chain | 认知转换链 | Continuous transformation process: reality → perceptual sampling → memory reconstruction → linguistic expression → others' understanding | `0_motivation/cognition_in_progress.md` |
| Abstraction as Compression | 抽象即压缩 | The mind folds heterogeneous individual information into category labels, trading lost detail for action efficiency | `0_motivation/abstraction_dialogue.md` |
| Effective Range | 有效范围 | Daily action operates within a "good enough" range rather than pursuing nanometer-level precision | `0_motivation/abstraction_dialogue.md` |
| Emergence | 涌现性 | A system as a whole exhibits new properties not possessed by its components | `1_first_principles/06_emergence.md` |
| Weak Emergence | 弱涌现 | New properties are in principle derivable from micro-laws but practically incomputable | `1_first_principles/06_emergence.md` |
| Strong Emergence | 强涌现 | New properties cannot be fully derived from micro-laws and are epistemically irreducible | `1_first_principles/06_emergence.md` |
| Level Jump | 层级跃迁 | Qualitative property change occurring in the transition from lower to higher cognitive/physical scales | `1_first_principles/06_emergence.md` |
| Computational Irreducibility | 计算不可约性 | A system's macroscopic behavior cannot be predicted by a shorter algorithm and must be simulated step by step | `1_first_principles/06_emergence.md` |
| Cost of Deviation | 偏离代价 | Expected free-energy difference between actual and optimal policy: Cost(π_dev) = G(π_actual) − G(π_optimal) | `1_first_principles/07_cost_of_deviation.md` |
| Cost Function | 代价函数 | Mathematical function that formalizes "deviation from Dao" as an observable, measurable increase in free energy | `1_first_principles/07_cost_of_deviation.md` |
| Precision Misallocation | 精度错配 | A generative model assigns excessive precision to certain priors or insufficient precision to sensory evidence, leading the system to choose suboptimal policies | `1_first_principles/07_cost_of_deviation.md` |
| Value Alignment Failure | 价值对齐失败 | The DMN narrative self systematically overvalues symbolic rewards and undervalues physiological costs to maintain self-consistency | `1_first_principles/07_cost_of_deviation.md` |
| Early Warning Signal | 预警信号 | First-person detectable early indicator of deviation from Dao, organized by L0–L7 layer | `1_first_principles/07_cost_of_deviation.md` |
| Cumulative Cost | 累积代价 | Time-integral of cost of deviation—short-term deviations are usually reversible, but long-term accumulation may cause irreversible structural damage | `1_first_principles/07_cost_of_deviation.md` |
| Narrative Self | 叙事自我 | Cross-temporally coherent self-narrative maintained by the DMN—"who I am, where I come from, where I am going" | `1_first_principles/07_cost_of_deviation.md` |

---

## XI. Preprint Index

| # | Title | Source module | Core equation | References |
|---|-------|---------------|---------------|------------|
| 1 | [Dao as Process](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_1/main.tex) | `01_dao_as_process.md` | Dao ≡ -∇_θ G(π_θ) (21 equations) | 15 |
| 2 | [L0–L7 Fact Spectrum](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_2/main.tex) | `L0_L7_spectrum.md` | L0–L7 cognitive-spectrum framework | 11 |
| 3 | [DMN–Self–Interoception Triangle](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_3/main.tex) | `dmn_self_model.md` | DMN–insula bistable ODE (6 equations) | 18 |
| 4 | [Cognitive Hierarchy of Scientific Knowledge](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_4/main.tex) | `04_philosophy_of_science.md` | Bayesian posterior induction (1 equation) | 12 |
| 5 | [Social Cognition and Mirror Resonance](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_5/main.tex) | `social_cognition.md` | SAB(t) operationalization (2 equations) | 22 |
| 6 | [Creativity and Innovation](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_6/main.tex) | `creativity_innovation.md` | DMN–ECN coupling ODE (3 equations) | 15 |
| 7 | [Carbon-Silicon Symbiosis](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_7/main.tex) | `carbon_silicon_symbiosis.md` | "Knowing when to stop" EFE formalization (2 equations) | 12 |
| 8 | [Education by Field](https://github.com/Ultima0369/dao-science/blob/main/paper/preprint_8/main.tex) | `education_by_field.md` | Four great field design principles | 12 |

All preprints are compiled with standard LaTeX (`pdflatex main.tex` × 2). See `paper/README.md` for details.

---

## Evidence Badges

| Badge | Level | Meaning |
|-------|-------|---------|
| **F** | Formal | Formalized definition or mathematical analogy |
| **P** | Physical / First-principles | Grounded in physics, biology, or first-principles reasoning |
| **S** | Simulation | Supported by runnable simulation |
| **B** | Behavioral | Supported by behavioral/phenomenological evidence |
| **N** | Neural | Supported by neuroscience evidence |
| **M** | Meta-ethical / Normative | Normative claim not purely empirically falsifiable |

For full details see [`NOTATION.en.md`](NOTATION.en.md).

---

> 返回中文版：[`GLOSSARY.md`](GLOSSARY.md)
