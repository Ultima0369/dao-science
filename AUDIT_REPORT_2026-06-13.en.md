# Project Dao.Science Deep Audit Report

> Audit date: 2026-06-13  
> Scope: All 24 Markdown content modules, 8 LaTeX preprints, MkDocs configuration, and open-source governance files  
> Perspective: Content architecture / scientific rigor / technical engineering / accessibility / strategic assessment

---

## I. Overall Diagnosis

Project Dao.Science has moved past the "flash of insight" stage and entered a more dangerous and critical zone: **it looks like a science, but the infrastructure that would let outsiders independently verify it is not yet in place.**

The project's most prominent tension is:

> **Rich formalization, but insufficient operationalization;**  
> **Beautiful conceptual maps, but broken verification chains;**  
> **Powerful manifestos, but the last mile of engineering is not yet complete.**

This is not a dismissal. On the contrary, the project already possesses high-level interdisciplinary ambition, a clear narrative skeleton, and self-reflexive critical awareness (`objections_and_replies.md` is a highlight). But it now faces two risks simultaneously:
1. **Academic risk**: if core formulas remain "metaphorically packaged," serious peer review will reject them quickly;
2. **Accessibility risk**: engineering and usability defects will prevent potential readers, contributors, and collaborators from entering.

The deepest improvement is therefore not "add more modules," but: **establish an answerable interface for every core proposition—formalization, simulation, experiment, and engineering, all four in one.**

---

## II. Four Deep Problems (with Evidence and Recommendations)

### Problem 1: The "Mathematical Sanctification" of Core Formulas—Blurred Boundary Between Metaphor and Model

**Essence**: The project takes `Dao ≡ -∇_π G(π)` as its first axiom and claims that "all core propositions have mathematical formalization." But this equation is not an operational definition of "Dao"; it is a **formal analogy** between the active-inference concept of policy selection and the Daoist concept. More seriously, the mathematical treatment itself has problems:

- In standard active inference, `π` is usually a **discrete policy index**, so writing `∇_π G(π)` with respect to a discrete subscript has no standard mathematical meaning;
- In the same passage the discrete softmax policy selection `P(π)=σ(-γG(π))` is used, conflicting with the continuous picture of "taking the gradient with respect to π";
- Equation (13) `P(π_accord)=σ(-γ·min_π G(π))` feeds a global scalar into softmax, giving all policies the same probability and failing to express "select the policy with minimal EFE."

**Impact**: Any formally trained cognitive scientist or mathematician will immediately ask: is this theory or rhetoric? `objections_and_replies.md` itself admits the formulas are "operationalization pointers" rather than definitions, but `POSITIONING.md` and `GLOSSARY.md` still advertise them with `≡` and "all core propositions have mathematical formalization," creating tension.

**Recommendations**:
1. Distinguish five evidence levels across the project: **F (pure formalization/metaphor) / S (simulation) / B (behavioral prediction) / N (neural evidence) / M (meta-ethical/normative claim)**;
2. Rewrite `Dao ≡ -∇_π G(π)` into one of two defensible forms:
   - Continuous parameterization: `Dao(θ) ≡ -∇_θ G(π_θ)`; or
   - Discrete policy improvement: `π_* = argmin_π G(π)`, `Wu-wei ⇔ max_π G(π) - min_π G(π) < τ`;
3. For every core mapping (Dao / One / De / Guan / Ming / Great Compassion as One Body), create a "metaphor—model" statement that specifies its measurable proxy, domain of application, and falsification condition.

---

### Problem 2: The L0–L7 Spectrum Degenerates from "Cognitive Terrain" into "Universal Classification Label"

**Essence**: The L0–L7 spectrum is the project's most original architecture, but in application it is increasingly used as an after-the-fact classification tool. AI is stuffed into L4, trauma into L2, war into L7, yet **no operational criterion is given for deciding which layer a phenomenon belongs to**. At the same time, the spectrum claims that layer numbers do not imply value hierarchy, while defining L0–L4 as healthy and L5–L7 as negative trajectories—an internal contradiction.

**Impact**: Anyone can dismiss objections as "category errors," and the spectrum degenerates from a testable framework into an all-explaining hindsight tool.

**Recommendations**:
1. Establish **criteria** for each layer: shareability, revisability, mode of intersubjective validation, relational consequences;
2. Allow the same phenomenon to be scored across multiple layers (radar chart) rather than forcing a single-layer assignment;
3. Separate "healthy / negative" from the layer definition and establish functional evaluation standards separately (does it lead to effective updating of prediction error, does it damage relationships);
4. Design a "layer-assignment checklist" and invite independent raters to conduct inter-rater consistency tests.

---

### Problem 3: Key Models Have Inconsistent Units, Missing Operational Definitions, and Formalization Stuck on Paper

**Essence**: Multiple ODEs and formulas have formal problems:

- `AB(t) = C_max - R_DMN(t)`: `C_max` has no independent measurement, `R_DMN` is not a subtractable scalar resource, and it conflicts with the later claim that "DMN is also the neural basis of global awareness / releasing";
- `DMN-insula bistable` switching condition: the left side is an input rate while the right side contains a sigmoid activation threshold, inconsistent units;
- In `100ms_model.md`, the second competition equation's steady-state derivation places `A^*` on both sides with confused units;
- `SAB(t)` and the `DMN-ECN creativity model` only give "maximization conditions" without a concrete form for `f`, so the models cannot be closed and solved.

**Impact**: These models cannot be turned into numerical simulations or derive testable quantitative predictions. The project's so-called "30+ mathematical equations" are mostly "verbal equations."

**Recommendations**:
1. Establish a project-level `NOTATION.md` that unifies symbols, domains, and units;
2. Perform dimensional analysis on every ODE, provide parameter tables, initial conditions, and typical value ranges;
3. Create runnable Python/Julia simulation scripts for each core model, with parameter scans and bifurcation analysis;
4. Give `AB(t)` a standardized operational definition, for example:
   ```
   AB(t) = 1 - [R_DMN(t) - R_0] / [R_max - R_0]
   ```
   where `R_DMN` is the standardized change in PCC/mPFC BOLD relative to baseline.

---

### Problem 4: The Engineering "Last Mile" Is Broken—Site and Preprints Are Not Publishable

**Essence**: The project has numerous engineering defects:

- `mkdocs.yml` does not enable Mermaid or math-formula extensions, so diagrams and equations will not render after deployment;
- The root `README.md` as the MkDocs homepage will error in strict mode;
- Preprints 4 through 8 are in Chinese but use `pdflatex` compilation, which will fail;
- `requirements.txt` does not pin versions, and CI does not read it;
- `.gitignore` lacks `site/` and LaTeX auxiliary files;
- Missing `LICENSE`, `CODE_OF_CONDUCT`, issue/PR templates;
- GitHub Actions only deploys, with no PR quality checks.

**Impact**: Readers cannot read the project properly on GitHub Pages; scholars cannot compile preprints; contributors lack norms; project credibility suffers.

**Recommendations**:
1. In `mkdocs.yml`, enable `pymdownx.superfences` (Mermaid) and `pymdownx.arithmatex` (MathJax);
2. Use `ctexart` + `xelatex` for Chinese preprints;
3. Create `ci.yml` to run `mkdocs build --strict`, link checks, and LaTeX compilation checks on PRs;
4. Add MIT `LICENSE`, `CODE_OF_CONDUCT.md`, and issue/PR templates;
5. Pre-compile PDFs and provide download links.

---

## III. Exclusive Perspective: The Project's Deepest Opportunity and Trap

### 3.1 What Are You Really Building?

Project Dao.Science is not just "an open-source handbook." It has the potential to become a **new kind of knowledge infrastructure**:

> **An open-source research platform for first-person cognitive science.**

This is not a metaphor. The project's core proposition—aligning Eastern contemplative practices with active inference and neuroscience—naturally requires a mixed methodology:
- Mathematical formalization (third-person)
- Personal practice reports (first-person)
- Neuroimaging / behavioral experiments (third-person verification)
- Engineering implementation (AI / education / clinical tools)

Currently, of these four legs, only "mathematical formalization + conceptual narrative" is well developed; the other three are either missing or weak.

### 3.2 The Deepest Trap: "Conceptual Mapping" Replacing "Mechanistic Explanation"

The project's biggest potential trap is **using conceptual correspondences in place of causal-mechanistic explanations**. For example:
- "Embracing Suffering ≈ cognitive reappraisal + ACT acceptance"—but this is only label matching, with no explanation of why the Four Practices combined would be more effective than CBT alone;
- "Knowing When to Stop ≈ AI stopping criterion"—but no concrete meta-controller architecture is given for implementing "knowing when to stop" in an RL agent;
- "The Fifty Demons ≈ hypofrontality from hypoxia"—overly simplified, ignoring expectation effects, cultural scripts, sleep deprivation, and other factors.

**Conceptual mapping is the starting point, not the end point.** The project needs to evolve from "this ancient concept resembles this modern scientific concept" to "this ancient practice produces what measurable effects through what neural / computational mechanism."

### 3.3 The Deepest Direction for Deepening: Establish "Verifiable Units"

I recommend the project introduce a core product: **every core proposition maps to a "Verifiable Unit" (VU)**, containing:
1. **Formal statement** (mathematical object, domain, boundary conditions);
2. **Simulation script** (runnable, parameter-scannable);
3. **Experimental protocol draft** (participants, task, metrics, statistical hypothesis, expected effect size);
4. **Evidence-state badge** (F/S/B/N/M);
5. **Counterfactual condition** (what evidence would weaken or refute the proposition).

This would upgrade the project from an "ambitious program" to a "runnable research program."

### 3.4 Exclusive Strategic Judgment

> **In the next 6–12 months, the project's decisive metric is not "how much new content was written," but "whether an outsider can independently verify or falsify at least one core prediction."**

If it can complete a minimum viable verification—for example:
- a numerical simulation of a DMN-TPN competition model;
- a 4-week "Embracing Suffering" mini-RCT protocol and pilot data;
- a behavioral validation of a "knowing when to stop" RL meta-controller on out-of-distribution tasks—

the project will gain far more academic credibility than conceptually similar works of comparable size.

---

## IV. Actionable Improvement Roadmap

### Near term (1–2 months): Stop the Bleeding and Become Publishable

1. **Fix MkDocs and LaTeX compilation**
   - Enable Mermaid/MathJax extensions;
   - Use `xelatex` for Chinese preprints;
   - Create `ci.yml` for build checks.
2. **Unify symbols and fix mathematical errors**
   - Fix `∇_π G(π)`, softmax equation (13), DMN-insula switching condition, and 100ms-model unit issues;
   - Create `NOTATION.md`.
3. **Complete open-source governance files**
   - Add MIT `LICENSE`, `CODE_OF_CONDUCT.md`, issue/PR templates.
4. **Correct factual claims**
   - Unify phrasing such as "22 modules / 17 Mermaid diagrams";
   - Fix non-existent file paths in `carbon_silicon_symbiosis.md`.

### Medium term (3–6 months): Operationalization and Verification

5. **Establish operational criteria for L0–L7**
   - Define layer-assignment dimensions, boundary cases, radar-chart scoring;
   - Provide observable indicators in applications such as AI governance, clinical practice, and carbon-silicon symbiosis.
6. **Create simulation code for key models**
   - `simulations/` directory: DMN-insula bistability, amygdala-PFC competition, DMN-ECN creativity;
   - Each model should provide parameter scans, bifurcation analysis, and qualitative comparison with known data.
7. **Introduce an evidence-level system**
   - Label `GLOSSARY.md` and every core file with F/S/B/N/M;
   - Rewrite `objections_and_replies.md` to give steelman responses to objections.
8. **Launch a minimum viable experiment**
   - Design a mini-RCT on "4 weeks of Embracing Suffering practice and emotional reactivity";
   - Provide a fillable digital template (Notion/Google Sheets/Markdown form).

### Long term (6–12 months): Internationalization and Community

9. **Bilingual site**
   - Use `mkdocs-static-i18n`;
   - Prioritize translating README, POSITIONING, GLOSSARY, and the four first-principles essays.
10. **Academic preprint release**
    - Auto-generate PDFs in CI and upload to GitHub Releases;
    - Attempt submission to arXiv/OSF/Zenodo to obtain a DOI.
11. **Cross-domain pilot network**
    - Clinical: integrate the Four Practices into CBT/ACT/MBCT workshops;
    - AI: implement a "knowing when to stop" RL meta-controller;
    - Education: A/B test "education by field" in real classrooms or corporate settings.
12. **Citizen-science platform**
    - Open-source web app or Notion system to track practice, scales, and CSV export;
    - Anonymized data hosted on GitHub Releases / OSF.

---

## V. Top 5 Priority Actions

| Priority | Action | Impact | Estimated Effort |
|---|---|---|---|
| P0 | Fix Chinese preprint compilation and MkDocs formula/diagram rendering | Make the project "readable" | 1–2 days |
| P0 | Correct core mathematical errors (∇_π, softmax, units) | Preserve academic credibility | 2–3 days |
| P1 | Establish unified notation table and evidence-level badges | Stop conflating "formal" with "evidenced" | 1 week |
| P1 | Develop operational criteria for L0–L7 | Prevent the spectrum from becoming a universal label | 1–2 weeks |
| P2 | Launch the first Verifiable Unit (simulation + experimental protocol) | Move from program to research process | 1–2 months |

---

## VI. Closing

Project Dao.Science has a rare combination: **deep Eastern contemplative tradition, cutting-edge frameworks in cognitive neuroscience, and the ambition to open-source it all**. Its greatest value is not the 7,300 lines already written, but the possibility it may prove: **first-person experience can be studied seriously, testably, and collectively.**

But to get there, the project must undergo a painful transformation: from "writing a better book" to "building infrastructure that others can independently use, verify, and criticize."

This is not a content problem; it is an **epistemic-attitude problem**—are you willing to expose every core proposition to the risk of falsification? Are you willing to turn the project from an "author's monologue" into a "public experiment"?

If so, Project Dao.Science will not be merely "a Chinese open-source project," but an infrastructure that fields ranging from mind science to AI safety, clinical intervention, and educational design can all cite.

---

*This report was generated by the audit toolchain, integrating findings from content architecture, scientific rigor, technical engineering, and accessibility.*
