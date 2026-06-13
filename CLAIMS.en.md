# Project Claim Registry and Evidence Status

## 项目主张登记册与证据状态

---

> **This document is not an authoritative catalogue of conclusions. It is a public map of the project's uncertainties.**
>
> Each claim is labeled with its current evidence status, falsification condition, and known limitations.
> Readers should treat this registry not as a "directory of truths" but as an "invitation to test."

---

## How to read this registry

| Field | Meaning |
|---|---|
| **Claim** | A core proposition or formal definition in the project |
| **Evidence badges** | F (Formal), S (Simulation), B (Behavioral), N (Neural), M (Meta-ethical/Normative) |
| **Confidence** | Current overall judgment: High / Medium / Low / To be tested |
| **Falsification condition** | What evidence would weaken or refute the claim |
| **Related files** | Formalization, simulation, protocol, or application |
| **Open questions** | Key unresolved issues |

---

## I. Core Axioms

### C01: Dao ≡ Gradient Flow of Expected Free Energy

**Claim**: Dao is the movement of a cognitive-action system along the direction of expected free energy minimization, formalized as $\text{Dao} \equiv -\nabla_\theta G(\pi_\theta)$, with discrete form $\pi_{\text{accord}} = \arg\min_\pi G(\pi)$.

| Field | Content |
|---|---|
| Evidence badges | **F** |
| Confidence | Medium |
| Falsification condition | Proof that, under reasonable parameterizations, $-\nabla_\theta G(\pi_\theta)$ or $\arg\min_\pi G(\pi)$ cannot describe strategy updating in any cognitive-action system; or systematic demonstration that optimal human/AI strategies in standard tasks deviate from local free-energy minimization |
| Related files | `1_first_principles/01_dao_as_process.md`, `NOTATION.en.md` |
| Open questions | How to define gradients rigorously over discrete strategy indices? What is the precise neural implementation of expected free energy? |

---

### C02: One = Awareness Bandwidth

**Claim**: "One" is operationalized as unobstructed awareness bandwidth, $AB(t) = 1 - [R_{\text{DMN}}(t) - R_0]/[R_{\text{max}} - R_0]$.

| Field | Content |
|---|---|
| Evidence badges | **F + N** |
| Confidence | Medium-High |
| Falsification condition | Large samples show DMN down-regulation is unrelated to subjective awareness clarity; or fMRI/EEG studies find no linear relationship between DMN and awareness bandwidth |
| Related files | `1_first_principles/02_one_as_bandwidth.md` |
| Open questions | Individual calibration standards for $R_0$ and $R_{\text{max}}$; do different contemplative traditions' "One" map to the same neural index? |

---

### C03: Mental Content Is 100% Representation, Not the Totality of Things

**Claim**: All conscious experience is an internal model constructed by the brain's predictive machinery (appearance/map), not external reality itself (thing-in-itself/territory).

| Field | Content |
|---|---|
| Evidence badges | **F + N + B + M** |
| Confidence | High |
| Falsification condition | Discovery of a perceptual process that does not rely on generative models; or evidence that conscious experience maps one-to-one to physical stimuli with no information loss |
| Related files | `1_first_principles/03_map_not_territory.md` |
| Open questions | Can "territory" be accessed in any way at all? What is the relation between L0 (awareness itself) and "territory"? |

---

### C04: L0-L7 Spectrum Is a Cognitive-Relational Terrain

**Claim**: The eight-layer structure from L0 (awareness itself/noumenon) to L7 (relational collapse/self-destruction) describes a continuous spectrum of facts and relations from healthy to pathological.

| Field | Content |
|---|---|
| Evidence badges | **F + B + M** |
| Confidence | Medium |
| Falsification condition | Key phenomena cannot be classified into any L0-L7 layer; or the same phenomenon is consistently classified into different layers across cultures/individuals |
| Related files | `0_motivation/L0_L7_spectrum.md`, `0_motivation/L0_L7_operationalization.md` |
| Open questions | Should L0 be treated as a "layer" at all? Are transition criteria between L5-L7 sufficiently precise? |

---

## II. Models of Mind

### C05: Attention Is Precision Optimization

**Claim**: Attention is the allocation of precision (inverse variance) across sensory channels or hypotheses; focus-global switching is regulated by parameter α.

| Field | Content |
|---|---|
| Evidence badges | **F + S + N + B** |
| Confidence | High |
| Falsification condition | Predictive coding framework refuted; or large-scale experiments show attention allocation is unrelated to precision weighting |
| Related files | `2_models/attention_model.md`, `verifiable_units/vu_05_attention_precision_optimization.md` |
| Open questions | How can α be measured and trained at the individual level? |

---

### C06: 100ms Amygdala-Prefrontal Competition Window

**Claim**: There is an approximately 100ms competition window between emotional/instinctive responding and prefrontal regulation; interventions such as body anchors during this window can alter the response trajectory.

| Field | Content |
|---|---|
| Evidence badges | **F + S + N + B** |
| Confidence | Medium-High |
| Falsification condition | Electrophysiological studies show no intervenable time window between amygdala response and PFC regulation; or behavioral interventions within the 100ms window prove ineffective |
| Related files | `2_models/100ms_model.md`, `verifiable_units/vu_02_amygdala_pfc.md` |
| Open questions | Does the exact window duration vary by stimulus type and individual differences? |

---

### C07: DMN Down-Regulation Releases Awareness Bandwidth

**Claim**: Reduced Default Mode Network activity, associated with decreased self-referential processing, releases cognitive resources for awareness and task execution.

| Field | Content |
|---|---|
| Evidence badges | **F + S + N + B** |
| Confidence | High |
| Falsification condition | Long-term meditators show no DMN down-regulation; or DMN down-regulation is unrelated to subjective reports and improved task performance |
| Related files | `2_models/dmn_self_model.md`, `verifiable_units/vu_01_dmn_insula.md` |
| Open questions | Is DMN down-regulation sufficient for awareness enhancement? Must other networks co-vary? |

---

### C08: Neuroplasticity Follows a 3–5 Year Window

**Claim**: Long-term meditation/contemplative training produces stable trait changes over a 3–5 year timescale through Hebbian learning, LTP/LTD, and metaplasticity.

| Field | Content |
|---|---|
| Evidence badges | **F + N + B** |
| Confidence | Medium |
| Falsification condition | Longitudinal MRI studies show no detectable structural or functional changes after 5 years of meditation practice; or changes fully reverse within months of stopping practice |
| Related files | `2_models/neuroplasticity_loop.md` |
| Open questions | Is 3–5 years a universal rule? Do different practice types (focused attention, open monitoring, compassion) have different time constants? |

---

### C09: Systematic Knowledge Can Form Mental Veils

**Claim**: Any long-term exposure to a logically self-consistent thought system builds neural circuits and may solidify into a new cognitive filter that obscures rather than reveals reality.

| Field | Content |
|---|---|
| Evidence badges | **F + B + M** |
| Confidence | Medium |
| Falsification condition | Discovery that long immersion in an ideology does not change supporters' cognitive bias patterns; or that all thought systems are easily revised |
| Related files | `2_models/neuroplasticity_loop.md`, `1_first_principles/05_first_person_epistemology.md` |
| Open questions | How to distinguish "deepening understanding" from "forming a veil"? |

---

### C21: Relational Attunement Can Reduce Vital Tension

**Claim**: By allocating attentional precision to another (being seen) and actively taking over leadership at the critical point where the other's impulse fatigues, a relational system can transform antagonistic tension into a cooperative ascending spiral, thereby reducing overall free energy.

| Field | Content |
|---|---|
| Evidence badges | **F + S + B + M** |
| Confidence | Medium |
| Falsification condition | Rigorously controlled experiments show that increasing one agent's attentional precision toward another does not change the other's physiological or behavioral markers; or complementary (anti-phase) interaction is never more effective than in-phase collaboration |
| Related files | `2_models/relational_attunement.md`, `2_models/attention_model.md`, `2_models/social_cognition.md`, `4_applications/management_field_theory.md`, `verifiable_units/vu_08_relational_attunement_oscillator.md` |
| Open questions | How can vital tension $T(t)$ and the critical handover point $t^*$ be measured in real interpersonal interaction? |

---

## III. Emergence and Spacetime

### C10: Emergence ≠ Phase Transition

**Claim**: Emergence is the ongoing generation of new properties through internal organizational relations, whereas phase transition is a state flip caused by an external parameter crossing a threshold.

| Field | Content |
|---|---|
| Evidence badges | **F + S + M** |
| Confidence | Medium |
| Falsification condition | Complex systems science proves all macro-level properties reducible to micro-rules with no new causal power |
| Related files | `1_first_principles/06_emergence.md`, `verifiable_units/vu_04_emergence_vs_phase_transition.md` |
| Open questions | Does strong emergence really exist, or is it merely rhetorical packaging for weak emergence? |

---

### C11: Space and Time Are Mind-Constructed Reference Frames

**Claim**: Space itself is formless and time itself is not clock-ticking; both are efficient models constructed by the human mind for action.

| Field | Content |
|---|---|
| Evidence badges | **F + M** |
| Confidence | Medium-High |
| Falsification condition | Physics proves space and time possess essential properties completely independent of any observer's mind; or discovery of physical facts understandable without any reference frame |
| Related files | `1_first_principles/08_space_time_and_modeling.md` |
| Open questions | Are space and time already presupposed at the level of L0 (awareness itself)? |

---

### C12: Reference Frames Prevent Consciousness Overload

**Claim**: Without human-constructed reference frames, the human mind cannot identify differences and consciousness would fail from information overload.

| Field | Content |
|---|---|
| Evidence badges | **F + B + M** |
| Confidence | Medium |
| Falsification condition | Discovery that humans can process all-scale variation simultaneously without a reference frame and without functional impairment |
| Related files | `1_first_principles/08_space_time_and_modeling.md`, `2_models/attention_model.md` |
| Open questions | What is the relationship between reference-frame switching ability and mental health? |

---

### C22: Nodes Are Non-Doing Translation Layers

**Claim**: In complex systems, nodes are invisible hubs that enable heterogeneous flows to connect, translate, and emerge. A well-functioning node is overlooked by the system yet cannot be removed without causing blockage; treating a node as a controllable valve increases free energy and blocks flow.

| Field | Content |
|---|---|
| Evidence badges | **F + M** |
| Confidence | Medium |
| Falsification condition | Discovery that complex systems can efficiently connect heterogeneous subsystems without any translation node; or proof that all nodes inevitably become valves |
| Related files | `1_first_principles/09_node_and_translation.md`, `2_models/relational_attunement.md`, `4_applications/management_field_theory.md`, `4_applications/carbon_silicon_symbiosis.md` |
| Open questions | How can a node's "transparency" and "appropriability" be quantified? |

---

### C23: De Is Vital-Energy Attention Allocation; Ming Is Innate Optimization Capacity

**Claim**: "De" is a living system's capacity for attentional allocation of vital energy. Its sole test is whether, from thought through action to effect feedback, it maintains and improves the existence quality of individuals and groups. "Ming" is the capacity to judge De in real time: a penetrating awareness that, under bandwidth constraints, unifies yin and yang, identifies patterns (constants) and real-time signals (variables), and outputs determinate action. Attentional hijacking disrupts Ming's yin-yang balance, causing the system to deviate from the path of least action.

| Field | Content |
|---|---|
| Evidence badges | **F + S + B + N + M** |
| Confidence | Medium-High |
| Falsification condition | Discovery that living systems can persist long-term with completely random or non-optimized energy allocation; or proof that some allocation improves individual A's existence quality while necessarily harming individual B and cannot be reallocated; or proof that attentional hijacking does not degrade decision quality or survival outcomes |
| Related files | `1_first_principles/10_de_and_ming.md`, `1_first_principles/01_dao_as_process.md`, `2_models/attention_model.md`, `2_models/100ms_model.md`, `2_models/dmn_self_model.md`, `verifiable_units/vu_09_de_ming_energy_allocation.md` |
| Open questions | How can De be quantified around improvement in existence quality? How can Ming's "effective-range hit rate" be quantified? |

---

## IV. Deviation and Ethics

### C13: Cost of Deviation Can Be Formalized

**Claim**: The cost of departing from an optimal cognitive-action path can be formalized as $Cost(\pi_{\text{dev}}) = G(\pi_{\text{actual}}) - G(\pi_{\text{opt}})$.

| Field | Content |
|---|---|
| Evidence badges | **F** |
| Confidence | Medium |
| Falsification condition | Discovery that this cost function cannot predict any observable mental, bodily, or systemic consequence |
| Related files | `1_first_principles/07_cost_of_deviation.md` |
| Open questions | How is $G(\pi_{\text{opt}})$ determined in real systems? |

---

### C14: First-Person Data Cannot Be Fully Reduced to Third-Person Data

**Claim**: Individual pain, clarity, meaningfulness, and other L2 experiences are in principle not directly accessible to others; they can only be inferred through reports and behavior.

| Field | Content |
|---|---|
| Evidence badges | **F + B + M** |
| Confidence | High |
| Falsification condition | Invention of a device that directly reads another's subjective experience; or philosophical proof that subjectivity does not exist |
| Related files | `1_first_principles/05_first_person_epistemology.md` |
| Open questions | To what extent could future brain-computer interfaces bridge this gap? |

---

## V. Applications

### C15: AI Safety Requires Built-In "Knowing When to Stop" Protocols

**Claim**: AI systems should embed stopping mechanisms that pause and request human judgment when uncertainty about behavioral consequences is too high or rules conflict with the situation.

| Field | Content |
|---|---|
| Evidence badges | **F + S + M** |
| Confidence | Medium |
| Falsification condition | Proof that all AI safety problems can be solved by static rules without dynamic stopping mechanisms |
| Related files | `4_applications/ai_governance.md`, `verifiable_units/vu_06_ai_stopping_protocol.md` |
| Open questions | How to implement reliable stopping mechanisms without degrading system usability? |

---

### C16: Management Is First a Training of the Manager's Own Mind

**Claim**: The legitimate entry point for management is how managers optimize their own attention, emotional regulation, and decision quality—not how to manipulate others.

| Field | Content |
|---|---|
| Evidence badges | **F + B + M** |
| Confidence | Medium |
| Falsification condition | Discovery that a manager's mental state has no systematic effect on organizational performance; or that all organizational performance can be fully explained by structure and systems |
| Related files | `4_applications/management.md`, `4_applications/management_field_theory.md` |
| Open questions | How to quantify the mediating effect of "manager mental state" on organizational outcomes? |

---

### C17: Environmental Design Shapes Organizational Behavior

**Claim**: Through design of physical, informational, narrative, relational, and ritual fields, organizations can release rather than capture members' attention and creativity.

| Field | Content |
|---|---|
| Evidence badges | **F + B** |
| Confidence | Medium |
| Falsification condition | Proof that environmental variables have no causal effect on cognition and behavior; or that all environmental design necessarily leads to manipulation |
| Related files | `4_applications/management_field_theory.md`, `4_applications/education_by_field.md` |
| Open questions | What objective criteria distinguish a "releasing field" from a "capturing field"? |

---

### C18: Healthy Carbon-Silicon Symbiosis Is Niche Complementarity

**Claim**: Carbon-based intelligence is irreplaceable at L0/L2, silicon-based intelligence is superior at L1/L4, and the two collaborate in L3 creative interpretation.

| Field | Content |
|---|---|
| Evidence badges | **F + S + M** |
| Confidence | Medium |
| Falsification condition | AI systems develop genuine first-person experience; or humans are proven forever superior to AI at L1/L4 tasks |
| Related files | `4_applications/carbon_silicon_symbiosis.md`, `verifiable_units/vu_07_carbon_silicon_symbiosis.md` |
| Open questions | Is "being needed" a sufficient criterion for silicon existence? |

---

### C24: AI Expansion Is Constrained by Earth's Thermodynamic Radiative Limit

**Claim**: Even with unlimited energy input, global AI computational expansion is constrained by Earth's physical limit for radiating waste heat into space. Sustained heat emission beyond this limit would alter Earth's energy balance and threaten the global ecosystem.

| Field | Content |
|---|---|
| Evidence badges | **F + S + M** |
| Confidence | High |
| Falsification condition | Proof that Earth can maintain steady-state temperature at arbitrary waste-heat power; or proof that computation can occur with zero entropy production |
| Related files | `4_applications/ai_governance.md`, `1_first_principles/10_de_and_ming.md`, `verifiable_units/vu_10_planetary_ai_thermodynamics.md` |
| Open questions | What is the practical global AI heat budget? How can an enforceable planetary thermodynamic governance protocol be established? |

---

### C25: Creativity Arises from Dynamic DMN-ECN Coupling

**Claim**: Creativity is not the product of either the Default Mode Network (DMN) or the Executive Control Network (ECN) operating alone, but of their dynamic coupling as the system switches between incubation and insight. Highly creative individuals are characterized by DMN→ECN coupling weights that can be rapidly reconfigured between low values (free association) and high values (precise capture).

| Field | Content |
|---|---|
| Evidence badges | **F + S + N + B** |
| Confidence | Medium-High |
| Falsification condition | Longitudinal studies show no relationship between DMN-ECN coupling flexibility and creative output; or highly creative individuals show the same coupling patterns as less creative individuals during idea generation and evaluation |
| Related files | `4_applications/creativity_innovation.md`, `verifiable_units/vu_03_dmn_ecn.md` |
| Open questions | Does this coupling pattern generalize across creative domains (verbal, visual, musical)? Can coupling flexibility be improved through training?

---

## VI. Methodology

### C19: N-of-1 Experiments Can Produce Valid Personal Knowledge

**Claim**: Through systematic prediction, repeated measurement, and explicit causal design, an individual can test whether an intervention works for them.

| Field | Content |
|---|---|
| Evidence badges | **F + B + M** |
| Confidence | Medium-High |
| Falsification condition | Proof that single-subject designs cannot in principle produce causal knowledge; or that all N-of-1 results fail to replicate |
| Related files | `3_methodology/n_of_1_protocol.md`, `tools/n_of_1/` |
| Open questions | What are the external validity boundaries of N-of-1 conclusions? |

---

### C20: The Four Practices Can Reshape Maladaptive Neural Circuits

**Claim**: The four practices (embracing suffering, flowing with causes, seeking nothing, acting in accordance), through down-regulating narrative-self prior precision, reducing rumination, and promoting action-awareness coordination, produce measurable mental and bodily changes.

| Field | Content |
|---|---|
| Evidence badges | **F + B + N** |
| Confidence | Medium |
| Falsification condition | RCTs show the Four Practices have no effect on anxiety, depression, attention, or related indicators |
| Related files | `3_methodology/xing_ru/`, `4_applications/clinical_mental_health.md` |
| Open questions | Can the Four Practices be decomposed into independent active ingredients, or must they be practiced as an integrated path? |

---

## VII. Overview

| Claim | Badges | Confidence | Key falsification condition |
|---|---|---|---|
| C01 Dao ≡ −∇G(π) | F | Medium | Active inference inconsistent |
| C02 One = AB(t) | F + N | Medium-High | DMN down-regulation unrelated to awareness |
| C03 Mental content = representation | F + N + B + M | High | Perception without generative models |
| C04 L0-L7 spectrum | F + B + M | Medium | Key phenomena unclassifiable |
| C05 Attention = precision optimization | F + S + N + B | High | Predictive coding refuted |
| C06 100ms window | F + S + N + B | Medium-High | 100ms interventions ineffective |
| C07 DMN down-regulation releases bandwidth | F + S + N + B | High | Meditators show no DMN change |
| C08 3–5 year neuroplasticity | F + N + B | Medium | No structural change after 5 years |
| C09 Knowledge can form mental veils | F + B + M | Medium | Ideologies do not alter biases |
| C10 Emergence ≠ phase transition | F + S + M | Medium | All macro properties reducible |
| C11 Space/time are mind-constructed | F + M | Medium-High | Space/time independent of mind |
| C12 Reference frames prevent overload | F + B + M | Medium | No-reference-frame processing possible |
| C22 Nodes are non-doing translation layers | F + M | Medium | Subsystems connect efficiently without nodes |
| C23 De is energy allocation, Ming is innate optimization | F + S + B + N + M | Medium-High | Random energy allocation sustains life |
| C13 Cost of deviation formalizable | F | Medium | Cost function predicts nothing |
| C14 First-person irreducible | F + B + M | High | Direct subjective-experience reader |
| C15 AI needs stopping protocols | F + S + M | Medium | Static rules solve all AI safety |
| C16 Management is self-training | F + B + M | Medium | Manager mind irrelevant to performance |
| C17 Environmental design shapes behavior | F + B | Medium | Environment has no causal effect |
| C18 Carbon-silicon niche complementarity | F + S + M | Medium | AI has first-person experience |
| C24 AI expansion constrained by Earth's thermodynamic limit | F + S + M | High | Earth radiates arbitrary heat or zero-entropy computation |
| C25 Creativity arises from DMN-ECN coupling | F + S + N + B | Medium-High | DMN-ECN coupling flexibility unrelated to creative output |
| C19 N-of-1 produces personal knowledge | F + B + M | Medium-High | Single-subject designs invalid |
| C20 Four Practices reshape circuits | F + B + N | Medium | RCTs show Four Practices ineffective |
| C21 Relational attunement reduces tension | F + S + B + M | Medium | Attentional presence cannot regulate interpersonal tension |

---

## VIII. Statement

This registry itself is a map. The "confidence" levels and "evidence badges" it assigns will be updated as new evidence arrives. If a falsification condition for any claim is ever satisfied, that claim will be revised or removed—this is precisely the project's proclaimed L4 (rational cooperation/contractual spirit) applied at the meta-level.

---

> Return to navigation: [`0_motivation/project_map.md`](0_motivation/project_map.md)
