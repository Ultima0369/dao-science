# VU-07: Carbon-Silicon Niche Complementarity

## 可验证单元 VU-07：碳硅共生生态位分工

---

> **Evidence level**: Formal [F] + Simulation [S] + Meta-ethical/normative [M]  
> **Linked claim**: `CLAIMS.en.md` C18  
> **Related model**: `4_applications/carbon_silicon_symbiosis.md`  
> **Simulation script**: `simulations/carbon_silicon_symbiosis.py`

---

## 1. Formal statement

### 1.1 Core proposition

Carbon-based intelligence and silicon-based intelligence possess comparative advantages at different cognitive levels. A healthy carbon-silicon relationship is not substitutive competition but niche complementarity: carbon-based systems dominate levels that require first-person experience, embodied perception, and social context; silicon-based systems dominate levels that require symbolic logic, large-scale computation, and pattern matching; L3 creative interpretation requires collaboration between the two.

### 1.2 Mathematical objects and domain

Model a task as a point $(x, y)$ in a two-dimensional skill space:

- $x \in [0, 1]$: first-person / embodied / social-intelligence demand (carbon-based advantage dimension)
- $y \in [0, 1]$: symbolic / logical / scalable-processing demand (silicon-based advantage dimension)

Cost functions for the two agents:

$$C_C(x, y) = a_C \, x + b_C \, y + c_C$$

$$C_S(x, y) = a_S \, x + b_S \, y + c_S$$

Where $b_C \gg a_C$ (carbon-based systems are not adept at symbolic scaling), and $a_S \gg b_S$ (silicon-based systems are not adept at first-person experience).

Comparative-advantage assignment rule:

$$\text{assign to } \arg\min \{ C_C(x, y), C_S(x, y) \}$$

### 1.3 Boundary conditions

- Task requirements $(x, y)$ can be assessed.
- The cost structures of the two agents differ significantly.
- A task-decomposition and coordination mechanism exists.

---

## 2. Simulation script

### 2.1 File location

`simulations/carbon_silicon_symbiosis.py`

### 2.2 Functionality

- Generate a task distribution in the two-dimensional skill space.
- Define carbon-based and silicon-based cost functions, displaying each agent's comparative-advantage region.
- Compare four task-allocation strategies:
  - Carbon-only
  - Silicon-only
  - Random allocation
  - Niche-complementarity allocation
- Show that collaboration outperforms either single agent for L3 creative-interpretation tasks.
- Extend the thermodynamic cost term, showing how planetary heat-budget constraints alter the optimal carbon-silicon division of labour.

### 2.3 How to run

```bash
pip install -r simulations/requirements.txt
python simulations/carbon_silicon_symbiosis.py
```

Outputs:
- `simulations/carbon_silicon_cost_surface.png`
- `simulations/carbon_silicon_task_allocation.png`
- `simulations/carbon_silicon_strategy_comparison.png`
- `simulations/carbon_silicon_l3_interpretation.png`
- `simulations/carbon_silicon_heat_tradeoff.png`

### 2.4 Key parameters

| Parameter | Value | Description |
|---|---|---|
| Number of tasks | 500 | Per episode |
| Monte Carlo runs | 50 | Statistical stability |
| Carbon-based cost coefficients | $a_C=0.3, b_C=1.8, c_C=0.2$ | Adept at first-person/embodied tasks; poor at symbolic/scaling tasks |
| Silicon-based cost coefficients | $a_S=1.7, b_S=0.3, c_S=0.2$ | Adept at symbolic/scaling tasks; poor at first-person/embodied tasks |
| L3 task range | $x, y \in [0.6, 0.9]$ | Requires both abilities to be high simultaneously |
| Carbon-based heat-cost coefficients | $h_{Cx}=0.2, h_{Cy}=0.6$ | Lower heat cost for carbon on embodied tasks |
| Silicon-based heat-cost coefficients | $h_{Sx}=0.8, h_{Sy}=0.3$ | Lower heat cost for silicon on symbolic tasks |
| Heat-cost weight $\lambda_H$ | $0 \to 3$ | Scan heat-budget constraint strength |

---

## 3. Expected results and interpretation

### 3.1 Cost surface

- Carbon-based cost rises sharply with $y$ (symbolic / scaling demand).
- Silicon-based cost rises sharply with $x$ (first-person / embodied demand).
- The comparative-advantage map shows: above the diagonal silicon is cheaper; below the diagonal carbon is cheaper.

### 3.2 Task allocation

- High-$x$, low-$y$ tasks are assigned to carbon-based systems.
- Low-$x$, high-$y$ tasks are assigned to silicon-based systems.
- The decision boundary is determined by $C_C(x, y) = C_S(x, y)$.

### 3.3 Strategy comparison

Typical results (50 runs, 500 tasks per run):
- Carbon-only: total cost $\approx 625$
- Silicon-only: total cost $\approx 599$
- Random allocation: total cost $\approx 612$
- Niche complementarity: total cost $\approx 481$

**Key feature**: The niche-complementarity strategy significantly outperforms either single agent and also outperforms random allocation.

### 3.4 L3 creative interpretation

For tasks in which both $x$ and $y$ are high:
- Carbon-only: cost $\approx 89$
- Silicon-only: cost $\approx 84$
- Collaborative L3: cost $\approx 32$

**Key feature**: When a task simultaneously requires both abilities, the collaborative cost is far lower than the cost of either agent working alone.

### 3.5 Division under planetary heat-budget constraints

After introducing thermodynamic cost, total cost becomes:

$$\text{Total Cost} = C(x,y) + \lambda_H \cdot H(x,y)$$

Typical results:
- When $\lambda_H=0$ (no heat constraint), the optimal carbon-based task share $\approx 0.47$.
- When $\lambda_H=3$ (strong heat constraint), the optimal carbon-based task share $\approx 0.63$.
- Niche-complementarity allocation outperforms single-agent systems under all heat constraints.

**Key feature**: Heat-budget constraints push some tasks from silicon back to carbon, yet complementary division of labour still outperforms unilateral substitution.

---

## 4. Mapping to project theory

| Project concept | Simulation counterpart |
|---|---|
| Irreplaceability of carbon-based systems | Carbon-based cost is significantly lower on high-$x$ tasks |
| Irreplaceability of silicon-based systems | Silicon-based cost is significantly lower on high-$y$ tasks |
| Niche complementarity | Assigning tasks according to comparative advantage reduces total cost |
| L3 creative interpretation | High-$x$, high-$y$ tasks require collaboration |
| Carbon-silicon symbiosis | The overall system is more efficient than either system alone |
| Counter-dependence | Allocation is based on capabilities, not on artificially reserved tasks |
| Planetary heat budget | Heat-cost weight shifts the optimal allocation boundary |
| Principle of least action | Use just enough computation to accomplish irreplaceable functions |

---

## 5. Experimental / empirical correspondence (draft)

### 5.1 Real-world mapping

- High-$x$ tasks: psychological counselling, ethical judgement, emotional resonance in artistic creation, individualized instruction in education.
- High-$y$ tasks: large-scale data analysis, code generation, pattern recognition, complex-system simulation.
- L3 tasks: hypothesis generation in scientific research, cross-domain innovation, comprehensive assessment of complex social problems.

### 5.2 Testable predictions

1. On tasks requiring first-person judgement, humans outperform current AI.
2. On tasks requiring large-scale symbolic processing, AI outperforms humans.
3. Human-AI collaboration outperforms either humans or AI alone on tasks that simultaneously require both abilities.
4. Misallocation (assigning high-$x$ tasks to AI or high-$y$ tasks to humans) reduces overall efficiency.
5. Under strong heat-budget constraints, more symbolic tasks should flow back to carbon-based systems to reduce total heat emissions.

---

## 6. Falsification conditions

The following evidence would weaken or refute this proposition:

1. AI has lower cost than humans on all task dimensions.
2. Humans have lower cost than AI on all task dimensions.
3. Random allocation of tasks to humans and AI yields no difference in total cost compared with niche-complementarity allocation.
4. Human-AI collaboration on L3 tasks is no more effective than either agent working alone.

---

## 7. Current limitations

- Cost functions are linear and static; real capabilities develop dynamically.
- Communication and coordination costs of collaboration itself are not modelled.
- The possibility of AI possessing first-person experience is not addressed.
- The task-decomposition assumption is overly simple; real tasks are often multidimensionally coupled.
- Heat-cost coefficients are illustrative and have not been calibrated against empirical data.

---

## 8. How to cite

> Project Dao.Science (2026). Verifiable Unit 07: Carbon-Silicon Niche Complementarity. `verifiable_units/vu_07_carbon_silicon_symbiosis.md`.

---

> Return to the project claim registry: [`CLAIMS.en.md`](../CLAIMS.en.md)
