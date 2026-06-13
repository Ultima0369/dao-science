# Relational Attunement Model: Attention as the Dance of Vital Tension

## 关系调谐模型：注意力作为生命张力的共舞

---

> **Evidence class**: Formal [F] + Behavioral prediction [B] + Meta-ethical [M]

---

## 1. Core Metaphor: Dynamic Attunement in Partner Dance

### 1.1 Basic Scene

Imagine two dance partners:

- Each has their own life rhythm, intention, and bodily tension.
- If both forcefully lead, the dance conflicts, stiffens, and wastes energy.
- If one completely submits, the other loses response, and the dance collapses into dragging.
- The smoothest state is: **both are seen, tension and relaxation alternate, firmness and softness switch dynamically**.

This scene applies not only to interpersonal dance but also to:

- Manager-team relationships
- Parent-child interactions
- Therapist-client dynamics
- Carbon-silicon collaboration
- Any system requiring emergent collective intelligence

### 1.2 Key Operational Concepts

| Traditional expression | Formal object | Technical meaning |
|---|---|---|
| Vital tension | $T(t)$ | Activation level, expressive impulse, sense of presence in the relation |
| Soft overcoming hard | $A(t)$ | Allocating attentional precision to the other to dissolve opposition by presence |
| Being seen | $\hat{T}_{\text{other}}(t)$ | One's internal model of the other's tension state |
| Critical handover | $t^*$ | The inflection point where the partner's impulse peaks and begins to fatigue |
| Firmness within softness | $\alpha(t)$ | Dynamic switching between focal and global attention in the relation |
| Double-helix ascent | Lyapunov function of the coupled system | Relation moves from dissipative structure to a lower free-energy collaborative state |

## 2. Formal Framework

### 2.1 Individual Tension Dynamics

Let two agents (human, team, AI, etc.) have vital tensions $T_1(t)$ and $T_2(t)$. Tension follows impulsive dynamics with decay:

$$\tau_i \frac{dT_i}{dt} = -T_i + I_i(t) + \eta_i(t)$$

where:
- $\tau_i$: tension decay time constant
- $I_i(t) \geq 0$: external or internal impulsive input
- $\eta_i(t)$: noise

**Key observation**: Impulses cannot last. Every $I_i(t)$ is a finite pulse, so $T_i(t)$ naturally goes through a rise-peak-fatigue cycle.

### 2.2 Attention as Relational Precision

When agent $i$ focuses attention on agent $j$, it allocates its precision resources to estimating $j$'s state:

$$\Pi_{ij}(t) = \Pi_0 \cdot A_i(t)$$

where $A_i(t) \in [0,1]$ is $i$'s attentional strength toward $j$. In the project's attention model (`2_models/attention_model.md`), this is:

$$A_i(t) = \alpha_i(t) \cdot \text{softmax}(\text{relevance}_j) + (1 - \alpha_i(t)) \cdot \text{uniform}$$

In relational attunement, high $A_i(t)$ means:

- $i$'s perceptual precision toward $j$ increases.
- $i$'s inference about $j$'s state becomes more accurate.
- $j$ can "feel being seen."

### 2.3 The Social Signal of Being Seen

Why does "being seen" have a regulatory effect? Because it reduces the other's uncertainty:

$$\Delta F_j^{\text{seen}} = -\frac{1}{2} \ln \left( 1 + \frac{\Pi_{ij}(t)}{\Pi_j^{\text{prior}}} \right)$$

When $i$ increases attentional precision toward $j$, $j$'s variational free energy drops, equivalent to $j$ receiving external regulatory support. This support needs no language because precision allocation itself is the signal.

### 2.4 Critical Handover: Detecting the Fatigue Point

Define the rate of change of $j$'s impulse:

$$\dot{T}_j(t) = \frac{dT_j}{dt}$$

When $T_j(t)$ peaks and begins to decline, $\dot{T}_j(t)$ changes from positive to negative. The critical handover point $t^*$ satisfies:

$$t^* = \arg\min_t \left\{ \dot{T}_j(t) < -\theta \quad \text{and} \quad T_j(t) > T_{\text{min}} \right\}$$

where $\theta$ is a rate threshold and $T_{\text{min}}$ avoids handover only when the other has fallen completely silent.

At $t^*$, agent $i$ switches from "following/witnessing" to "leading/pushing":

$$\alpha_i(t^+) = 1 - \alpha_i(t^-)$$

That is, switching from high global awareness (open) to high focal attention (focused), or vice versa.

### 2.5 Soft-Hard Coupling and Double-Helix Ascent

The interaction of the two agents can be written as a coupled system:

$$\tau_1 \frac{dT_1}{dt} = -T_1 + I_1 + \kappa \, A_2(t) \cdot T_2(t) \cdot f(T_1, T_2)$$

$$\tau_2 \frac{dT_2}{dt} = -T_2 + I_2 + \kappa \, A_1(t) \cdot T_1(t) \cdot f(T_2, T_1)$$

where:
- $\kappa$: coupling strength
- $f(T_i, T_j)$: handover function, positive when $j$ is in the fatigue-critical state, otherwise suppressed

When handover is correct, the system enters anti-phase synchronization: one rises while the other falls, like the "advance-retreat" of partner dance. Sustained anti-phase coupling drives the relational system toward lower free energy, manifesting as:

- Reduced conflict energy
- Higher collaboration efficiency
- Emergent collective capacity

This is the dynamic counterpart of the "double-helix ascent": two independent chains rise together through complementary tension, rather than collapsing through in-phase superposition.

## 3. Relation to Existing Models

| Existing model | Role in relational attunement |
|---|---|
| `attention_model.md` | Provides formal basis for $A(t)$ and $\alpha(t)$ |
| `100ms_model.md` | Provides neural mechanism for detecting the other's tension change within a 100 ms window |
| `dmn_self_model.md` | Explains that "letting go of the narrative self" raises attentional precision toward the other |
| `social_cognition.md` | Explains how mirror resonance makes "being seen" a real signal |
| `neuroplasticity_loop.md` | Explains how long-term relational training reshapes the neural circuitry of handover |

## 4. Application Scenarios

### 4.1 Management and Leadership

An excellent manager is like a dance partner:

- When the team is high, accompany with high awareness (open), letting creativity flow.
- When the team fatigues, precisely take over leadership (focused), pushing the next step.
- Neither forcefully suppress nor let drift.

### 4.2 Psychotherapy

The therapist's stable attentional presence lowers the client's free energy; when the client defends or the impulse fatigues, the therapist gently takes over the direction of the topic.

### 4.3 Parent-Child Relationship

The parent's "seeing" of the child is itself a regulation. When the child's emotional impulse peaks and begins to fall, the parent's stable handover helps the child internalize self-regulation.

### 4.4 Carbon-Silicon Collaboration

AI can provide stable low-energy support when the human is high (soft overcoming hard), and take over computational and executive leadership when the human is tired (critical handover). Their complementary coupling forms system-level viability.

## 5. Falsification Conditions

Evidence that would weaken this model:

1. In strictly controlled experiments, increasing one agent's attentional precision toward another does not change the other's physiological or behavioral markers.
2. Humans or animals cannot detect the critical fatigue point of the other's impulse.
3. Complementary (anti-phase) interaction is less effective than in-phase collaboration in all tasks.
4. The feeling of "being seen" can be fully reduced to linguistic content, independent of attentional precision.

## 6. Current Limitations

- The neural/physiological proxy for tension $T(t)$ is not yet clear.
- The concrete form of the handover function $f(T_i, T_j)$ remains heuristic.
- The model has not been fitted to real interpersonal data (dual motion capture, heart-rate synchronization, etc.).
- The model is currently dyadic; it has not been extended to multi-agent relational networks.

---

> Project Dao.Science (2026). Relational Attunement Model: Attention as the Dance of Vital Tension. `2_models/relational_attunement.md`.

---

> Back to claim registry: [`CLAIMS.en.md`](../CLAIMS.en.md)
