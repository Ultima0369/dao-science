# Deep Audit Report: Optimization Directions for a Computer-Science Audience

**Audit date**: 2026-06-14  
**Scope**: Entire repository (`1_first_principles/`, `2_models/`, `3_methodology/`, `4_applications/`, `verifiable_units/`, `simulations/`, `tools/n_of_1/`, `scripts/`, site configuration and workflows)  
**Target audience assumption**: The primary readers on GitHub and academic preprints have strong backgrounds in computer science, engineering, or logic, but may not be familiar with cognitive science, complex systems, or non-classical logics.  
**Audit method**: Three read-only exploration subagents reviewed formalization, navigability, and toolchain reproducibility in parallel; the parent agent synthesized findings and prioritized them.

---

## 1. Core Conclusion

The project has already reached a high level of completion in **conceptual framework, notation unification, Verifiable Unit (VU) architecture, and bilingual site**, especially:

- `NOTATION.md` unifies symbol conventions;
- `CLAIMS.md` links theoretical commitments to evidence levels;
- Every VU points to a runnable `simulations/*.py` script;
- MkDocs + `mkdocs-static-i18n` implements the bilingual suffix mode.

However, for a **logically rigorous but interdisciplinary CS reader**, the biggest friction is not that the content is not deep enough, but:

> **The "trust signals" of the map and toolchain are still unstable**—inconsistent symbols, a forest of English stubs, incomplete VU experimental designs, CI not covering all simulations, and unpinned dependencies.

These flaws can make a careful CS reader conclude "this project is not ready" within five minutes, even though the underlying ideas are already solid.

---

## 2. Audience Personas and Inferred Reading Paths

| Reader type | First question | Current experience | Optimization lever |
|---|---|---|---|
| Engineer / open-source contributor | "Is this a library? A framework? A theory handbook?" | README does not clearly distinguish | Add a "What this repo is (and isn’t)" box at the top of README |
| Researcher / reviewer | "Do the claims have evidence? Can they be reproduced?" | CLAIMS/VU architecture is good, but badge usage is inconsistent | Clean badges, complete VU experimental designs, add automated consistency checks |
| English reader | "Is the English version readable?" | 27 `.en.md` files are still stubs | Prioritize translation or temporarily hide untranslated pages |
| Code contributor | "How do I run tests? How do I install dependencies?" | No pytest, dependencies not fully pinned, CI runs only 3 simulations | Add test matrix, pin dependencies, run all simulations |
| General reader | "Where do I start?" | Reading paths are interest-based, no CS-specific entry | Add an "Engineer / CS fast-track" section to POSITIONING |

---

## 3. Issues and Recommendations by Theme

### 3.1 Content Formalization: Discipline of Symbols and Badges

| ID | Severity | Location | Issue | Recommended fix |
|----|----------|----------|-------|-----------------|
| F1 | **Critical** | `GLOSSARY.md:224`, `project_map.md:20`, `FINAL_VISION.md:223` | `AB(t)` still written as `Cmax − RDMN(t)`, contradicting the normalized form in `NOTATION.md` and `02_one_as_bandwidth.md` | Unify the whole repo to `AB(t) = 1 − [R_DMN(t) − R_0]/[R_max − R_0]`; add CI lint scanning for the old string |
| F2 | **Critical** | `11_scale_and_moral_silence.md` | Uses undefined `[P]` badge | Define `[P]` in `NOTATION.md` or replace with `[B]` |
| F3 | **Critical** | Header of `10_de_and_ming.md`, `CLAIMS.md` C23 | Claims `[N]` neural evidence while the same file admits "neural correspondence not yet precisely located" | Downgrade to `[F/B/M]` to match `VU-09` |
| F4 | **Critical** | `08_space_time_and_modeling.md` | `[M]` used as "mathematical" rather than the "meta-ethical/normative" definition in `NOTATION.md`; compressed `[N/B]` notation is non-standard | Add a `[Math]` badge or use plain text; split into `[N] + [B]` |
| F5 | **Critical** | `.en.md` files for VU-04 to VU-07 | 4 English stubs contain only "English translation in progress" | Prioritize translation or temporarily remove them from English navigation |
| F6 | **Critical** | VU-08/09/10 | Only formalization + simulation; missing experimental protocol (participants, task, primary metrics, statistical hypotheses) | Complete experimental design drafts following the VU-01/02/03 template |
| F7 | Medium | `2_models/neuroplasticity_loop.md` | File is in Models directory but lacks a standard plasticity update equation | Add Hebbian / BCM / STDP equations and a parameter table |
| F8 | Medium | `2_models/hypoxia_fifty_demons.md` | Causal language stronger than evidence; no simulation | Soften to "testable hypothesis" and add limitations; if formalized, add a VU + simulation |
| F9 | Medium | `1_first_principles/09_node_and_translation.md` | Admits lack of "node quality quantification metric" | Propose at least one computable proxy, such as translation-layer mutual-information preservation or reconstruction loss |
| F10 | Medium | `1_first_principles/04_philosophy_of_science.md` | Mapping philosophers to L0–L7 is more conceptual analogy than formalization, yet tagged `[F]` | Change to `[Conceptual]` or clarify formalization standards |

**Key signal for the formalization theme**: CS readers are extremely sensitive to "symbol inconsistency" and "badge inflation." F1–F4 are low-level "map vs. territory" errors that directly erode trust.

### 3.2 Navigation and Onboarding: Reducing First-Impression Friction

| ID | Severity | Location | Issue | Recommended fix |
|----|----------|----------|-------|-----------------|
| N1 | **Critical** | 27 `.en.md` files | English version is largely stubs; language-switch experience collapses | Prioritize translating `README`, `POSITIONING`, `L0_L7_spectrum`, `01_dao_as_process`, `CLAIMS`; or temporarily hide untranslated pages |
| N2 | Critical | `README.md` | Does not clearly answer "Is this a library/framework/theory?" | Add a "What this repo is (and isn’t)" box |
| N3 | Critical | `README.md` | Relationship between `verifiable_units/` and `simulations/` is unexplained | Add a row in the project-structure table: VUs are documents, simulation scripts live in `simulations/` |
| N4 | Critical | `CONTRIBUTING.md` | High barrier, missing "first contribution" path | Add low-barrier task list: fix citations, translate paragraphs, add docstrings, check badges |
| N5 | Medium | `0_motivation/project_map.md` | Mermaid diagram lacks `management.md` and `management_field_theory.md` application nodes | Add MGMT and FIELD nodes to the Layer 4 subgraph |
| N6 | Medium | `GLOSSARY.en.md` | English glossary says "see Chinese GLOSSARY.md for full version" | Complete core entries or add a coverage note at the top |
| N7 | Medium | `mkdocs.yml` | `nav_translations` manually maintained, prone to drift | Extend `audit_nav_coverage.py` to check that every Chinese title has a translation |
| N8 | minor | `tools/n_of_1/README.md` | Not connected to MkDocs navigation | Add a toolkit entry under "Appendices" or "Methodology" |
| N9 | minor | `agent/future-spec.md` | Orphan file, not referenced in nav or README | Decide public/private; if public, add to appendices |

### 3.3 Toolchain and Reproducibility: From "It Runs" to "Trustworthy"

| ID | Severity | Location | Issue | Recommended fix |
|----|----------|----------|-------|-----------------|
| T1 | **Key** | `simulations/amygdala_pfc_hijack.py`, `dmn_ecn_creativity.py` | No `matplotlib.use("Agg")`; will crash headless / in CI | Add `matplotlib.use("Agg")` to all plotting scripts |
| T2 | **Key** | `.github/workflows/ci-checks.yml` | CI runs only 3 simulations; the other 7 may break silently | Discover/run all `simulations/*.py`, or maintain an explicit manifest and validate it |
| T3 | Critical | All `scripts/` | No tests, type checks, or lint | Add `pytest` suite; run `ruff` + `mypy` in CI |
| T4 | Critical | `simulations/requirements.txt` | Uses `>=`; future dependencies may break reproducibility | Pin exact versions; add a lockfile (`pip-compile` / `uv pip compile`) |
| T5 | Critical | `tools/n_of_1/` | No `requirements.txt` | Add pinned `requirements.txt` and document installation in README |
| T6 | Critical | `.github/workflows/deploy-pages.yml` | Deployment does not run audit scripts | Add `audit_links.py`, `audit_nav_coverage.py`, `audit_math_delimiters.py` to the deploy flow |
| T7 | Critical | Repository overall | No `.gitattributes`; persistent CRLF/LF warnings | Add `.gitattributes` enforcing LF |
| T8 | Medium | `scripts/sync_docs.py` | `docs/` mirror does not remove deleted source files; `docs/GLOSSARY.md` tracked causes confusion | Make sync clear before copying; untrack `docs/GLOSSARY.md` or generate it dynamically from root |
| T9 | Medium | `scripts/audit_links.py` | Does not check anchors, image/asset links, or external links | Extend to support anchors, assets, and external links (with caching) |
| T10 | Medium | `scripts/audit_nav_coverage.py` | Parses nav with regex, may miss commented or quoted entries | Use a YAML loader or stricter parsing |
| T11 | Medium | `tools/n_of_1/scripts/l0_l7_radar.py` | CJK font fallback missing macOS fonts | Add `PingFang SC`, `Hiragino Sans GB`, etc. |
| T12 | Medium | `tools/n_of_1/schema.yaml` | Documentation only, not loaded for validation in scripts | Add a validation module shared by `log_entry.py` and `analyze.py` |
| T13 | Suggested | Root | No `pyproject.toml` | Add a minimal `pyproject.toml` with metadata, optional dependency groups, and `ruff`/`mypy`/`pytest` config |
| T14 | Suggested | `simulations/` | Output PNG/CSV files mixed with source | Move to `simulations/output/` or `assets/simulations/`, add `.gitignore` |

---

## 4. Priorities and Action Roadmap

### Phase 1: Stop the Bleeding (1–3 days, boost trust signals)

1. Fix `AB(t)` formula drift (F1).
2. Clean up badge violations: F2, F3, F4.
3. Add `matplotlib.use("Agg")` to all plotting simulations (T1).
4. Add `.gitattributes` to force LF (T7).
5. Add "What this repo is / isn’t" and `verifiable_units/` vs `simulations/` explanation at the top of README (N2, N3).

### Phase 2: Complete (1–2 weeks, make VUs truly verifiable)

6. Add experimental designs to VU-08/09/10 (F6).
7. Translate or hide English stubs for VU-04–07 (F5).
8. Pin `simulations/requirements.txt` and `tools/n_of_1/requirements.txt` (T4, T5).
9. Run all simulation scripts in CI (T2).
10. Extend `audit_links.py` and `audit_nav_coverage.py` (T9, T10).

### Phase 3: Engineering (2–4 weeks, establish maintainable infrastructure)

11. Add `pytest` test matrix covering scripts and simulations (T3).
12. Add `ruff` + `mypy` + pre-commit (T3, T13).
13. Add all audit scripts to the deploy workflow (T6).
14. Add `pyproject.toml` with optional dependency groups (T13).
15. Complete core entries in `GLOSSARY.en.md` (N6).

### Phase 4: Experience Optimization (ongoing)

16. Add a "CS / Engineer fast-track" section to `POSITIONING.md`.
17. Add a standard footer to every content module: previous / next / back to project map / corresponding CLAIMS entry.
18. Auto-generate and maintain an equation index.

---

## 5. One-Sentence Summary

> For a CS reader, the project's "hardcore content" already exists, but the "hardcore engineering packaging" is still one breath short. The highest-return investment right now is not to write more philosophy, but to make symbols, badges, VU experimental designs, English translations, and CI testing so tight that a logician cannot find a flaw.

---

*Report generated: 2026-06-14*  
*Generation method: parallel exploration subagents + parent synthesis*
