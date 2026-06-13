# Project Dao.Science

[![CI Checks](https://github.com/Ultima0369/dao-science/actions/workflows/ci-checks.yml/badge.svg)](https://github.com/Ultima0369/dao-science/actions/workflows/ci-checks.yml)
[![Deploy MkDocs to GitHub Pages](https://github.com/Ultima0369/dao-science/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/Ultima0369/dao-science/actions/workflows/deploy-pages.yml)
[![Site](https://img.shields.io/badge/site-ultima0369.github.io%2Fdao--science-blue)](https://ultima0369.github.io/dao-science/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Ultima0369/dao-science/blob/main/LICENSE)

> **Staying alive—flexible, open, and capable of insight—while facing infinite complexity with finite computational power.**

**Read online**: https://ultima0369.github.io/dao-science/ (Bilingual Chinese/English support; switch languages via the header. Full English translations of content modules are being added progressively.)

---

## One-line positioning

Dao.Science is neither anti-science nor pseudo-science. It is an **open-source operating manual for the mind**—aligning first-person Eastern contemplative practice with predictive coding, neuroscience, and active inference so that it becomes empirically testable technical language.

Full positioning statement: [`POSITIONING.en.md`](POSITIONING.en.md).

---

## What this repository is (and isn't)

- **Is**: An open-source bilingual research handbook aligning first-person Eastern contemplative practice with predictive coding, neuroscience, active inference, and complex systems so that it becomes empirically testable technical language.
- **Is**: A set of runnable Python simulation scripts (`simulations/`), each paired with a verifiable unit in `verifiable_units/`.
- **Is**: A claim registry (`CLAIMS.md`) that labels every proposition with its evidence level and falsification conditions.
- **Isn't**: A `pip install`-able software library; there is no stable Python API and no backward-compatibility guarantee.
- **Isn't**: A theory that has already passed large-scale experimental validation; it is in the "theory construction + operationalization" stage, and the VUs and simulations are being progressively subjected to independent scrutiny.

If you prefer to start from code and formalization, the recommended path is:
`POSITIONING.en.md` → `CLAIMS.en.md` → `verifiable_units/vu_01_dmn_insula.en.md` → `simulations/dmn_insula_bistable.py`.

---

## Who is this manual for?

| You might be | What this can help you with |
|---|---|
| Researcher | Switching between "tight" and "loose" states when stuck on a concept |
| Decision-maker | Keeping large-scale and small-scale perspectives fluid in conflict |
| Engineer | Reconnecting with the source of insight in complex systems |
| AI practitioner | Compiling "knowing when to stop" into executable safety constraints |
| Mental-health professional | Understanding rigidity, hijacking, and recovery in neuroscientific terms |
| Everyday explorer | Finding a viable path when fear and desire take turns hijacking you |

---

## Core axioms (one-liner version)

| Concept | Technical expression | Meaning |
|---|---|---|
| **Dao** | `π_顺道 = argmin_π G(π)` | The direction of minimum expected free energy for the cognitive-action system |
| **One** | `AB(t) = 1 - [R_DMN(t) - R_0]/[R_max - R_0]` | Awareness bandwidth: cognitive resources released by DMN down-regulation |
| **Map ≠ Territory** | `P(world\|mind) ≠ world` | Mental content is an appearance of things, not the totality of things |
| **L0–L7** | Cognitive terrain spectrum | Seven-layer structure of facts from noumenon to relational collapse |
| **Emergence** | `G(system) ≠ ΣG(parts)` | New properties arise from level transitions that cannot be reduced |
| **Cost of deviation** | `Cost(π_dev) = G(π_actual) - G(π_opt)` | Quantifiable warning signal of straying from Dao |

---

## Double-helix architecture

| Helix | Form | Purpose | Entry |
|---|---|---|---|
| **GitHub repository** | Markdown + Mermaid + Python simulations | Executable, modifiable technical manual | This page |
| **Academic preprints** | LaTeX → PDF | Citable, peer-reviewable papers | [`paper/README.md`](https://github.com/Ultima0369/dao-science/blob/main/paper/README.md) |
| **MkDocs site** | Online rendering | Most comfortable reading experience | [Read online](https://ultima0369.github.io/dao-science/) |

---

## Recommended reading paths

| Goal | Starting point | Estimated time |
|---|---|---|
| Why this project matters | [`0_motivation/why_this_matters.md`](0_motivation/why_this_matters.md) | 15 min |
| Enter through first-person experience | [`0_motivation/cognition_in_progress.md`](0_motivation/cognition_in_progress.md) | 10 min |
| Build a cognitive framework | [`0_motivation/L0_L7_spectrum.md`](0_motivation/L0_L7_spectrum.md) | 20 min |
| See formalized definitions | [`1_first_principles/01_dao_as_process.md`](1_first_principles/01_dao_as_process.md) | 25 min |
| Run executable simulations | [`verifiable_units/vu_01_dmn_insula.md`](verifiable_units/vu_01_dmn_insula.md) | 30 min |
| See emergence vs phase-transition simulation | [`verifiable_units/vu_04_emergence_vs_phase_transition.md`](verifiable_units/vu_04_emergence_vs_phase_transition.md) | 25 min |
| See attention precision optimization simulation | [`verifiable_units/vu_05_attention_precision_optimization.md`](verifiable_units/vu_05_attention_precision_optimization.md) | 20 min |
| See AI stopping protocol simulation | [`verifiable_units/vu_06_ai_stopping_protocol.md`](verifiable_units/vu_06_ai_stopping_protocol.md) | 20 min |
| See carbon-silicon task allocation simulation | [`verifiable_units/vu_07_carbon_silicon_symbiosis.md`](verifiable_units/vu_07_carbon_silicon_symbiosis.md) | 20 min |
| See relational attunement oscillator | [`verifiable_units/vu_08_relational_attunement_oscillator.md`](verifiable_units/vu_08_relational_attunement_oscillator.md) | 20 min |
| See De-Ming energy allocation model | [`verifiable_units/vu_09_de_ming_energy_allocation.md`](verifiable_units/vu_09_de_ming_energy_allocation.md) | 20 min |
| See planetary thermodynamic boundary for AI | [`verifiable_units/vu_10_planetary_ai_thermodynamics.md`](verifiable_units/vu_10_planetary_ai_thermodynamics.md) | 20 min |
| Learn about relational attunement | [`2_models/relational_attunement.md`](2_models/relational_attunement.md) | 20 min |
| Learn about nodes and non-doing translation | [`1_first_principles/09_node_and_translation.md`](1_first_principles/09_node_and_translation.md) | 20 min |
| Learn about De and Ming | [`1_first_principles/10_de_and_ming.md`](1_first_principles/10_de_and_ming.md) | 20 min |
| Check the evidence status of each claim | [`CLAIMS.md`](CLAIMS.md) | 15 min |
| Look up terms | [`GLOSSARY.md`](GLOSSARY.md) | On demand |

---

## Repository structure

```
dao-science/
├── POSITIONING.md              # Positioning statement
├── FINAL_VISION.md             # Ultimate vision
├── README.md                   # This file
├── CLAIMS.md                   # Claim registry: evidence status and falsification conditions
├── 0_motivation/               # Motivation and cognitive framework
├── 1_first_principles/         # First principles
├── 2_models/                   # Models of mind
├── 3_methodology/              # Practice methods (li-ru + xing-ru)
├── 4_applications/             # Applications (AI, education, clinical, creativity, carbon-silicon symbiosis)
├── verifiable_units/           # Verifiable units: formalization + simulation notes + experimental protocols (document entry)
├── simulations/                # Runnable Python simulation scripts (one-to-one with VUs)
├── paper/                      # 8 LaTeX academic preprints
├── scripts/                    # Doc sync, audit, and CI helper scripts
├── GLOSSARY.md                 # Glossary
├── NOTATION.md                 # Notation and evidence levels
└── CONTRIBUTING.md             # Contribution guide
```

---

## Local build

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Sync docs/ mirror
python scripts/sync_docs.py

# 3. Build site in strict mode
mkdocs build --strict

# 4. Local preview
mkdocs serve
```

CI also runs link audit, math delimiter audit, nav coverage audit, and Python simulations.

---

## Evidence levels

This project uses `F/S/B/N/M/P` badges to mark the evidential status of each claim, preventing the conflation of formalization with evidence:

- **F**ormal: formalized definition
- **S**imulation: runnable simulation
- **B**ehavioral: behavioral/phenomenological evidence
- **N**euroscience: neuroscience evidence
- **M**eta-ethical / Normative: meta-ethical or normative claim, not empirically falsifiable on its own

See [`NOTATION.en.md`](NOTATION.en.md) for details.

---

## Key numbers

- **26** core content modules
- **10** verifiable units (7 with Python simulations)
- **8** LaTeX academic preprints
- **~8,500** lines of scholarly content
- **100+** academic references
- **30+** mathematical equations / formalized definitions
- **17+** Mermaid flowcharts

---

## Contributing

- Report issues: [Open an Issue](https://github.com/Ultima0369/dao-science/issues)
- Submit improvements: [Open a Pull Request](https://github.com/Ultima0369/dao-science/pulls)
- Contribution guidelines: [`CONTRIBUTING.en.md`](CONTRIBUTING.en.md)

This repository is licensed under the [MIT License](https://github.com/Ultima0369/dao-science/blob/main/LICENSE).
