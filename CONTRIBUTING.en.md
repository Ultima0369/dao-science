# Contribution Guidelines

## 贡献指南

---

## Branch Strategy

- `main`: Only merges from `develop` are allowed; protected. Pushes to `main` automatically trigger GitHub Pages deployment.
- `develop`: Integration branch; daily development happens here.
- `feature/<name>`: New features or modules.
- `doc/<name>`: Pure documentation changes.
- `paper/<name>`: Preprint-related work.

---

## Commit Convention

Follow Conventional Commits: `type(scope): description`

Types: `feat`, `fix`, `docs`, `refactor`, `chore`, `paper`

---

## Core Disciplines

1. All content must have both scientific and classical foundations.
2. First-person empirical cases must be anonymized.
3. Pull requests must be reviewed by core maintainers.

---

## Repository Structure

```
dao-science/
├── POSITIONING.md                      # What Dao.Science is: positioning statement
├── FINAL_VISION.md                     # Ultimate vision: staying alive in complexity
├── README.md                           # Project vision, core axioms, quick start
├── CONTRIBUTING.md                     # This file
├── GLOSSARY.md                         # Concept index and glossary
├── NOTATION.md                         # Notation conventions and evidence levels
├── mkdocs.yml                          # MkDocs Material config + navigation tree
├── requirements.txt                    # Python dependencies
│
├── 0_motivation/                       # Motivation layer
├── 1_first_principles/                 # First principles
├── 2_models/                           # Models of mind
├── 3_methodology/                      # Practice methods
├── 4_applications/                     # Application layer
├── verifiable_units/                   # Verifiable units (formalization + simulation + protocol)
├── simulations/                        # Runnable Python simulation scripts
├── scripts/                            # Doc sync, audit, and CI helper scripts
├── paper/                              # Academic preprints (LaTeX)
└── .github/workflows/                   # CI/CD
```

---

## How to Contribute

### Adding a Content Module

1. Determine which layer the module belongs to (motivation / first principles / model / method / application).
2. Follow the existing module format:
   - Bilingual title and abstract (Chinese + English)
   - 5–10 keywords (bilingual)
   - Body (mixed Chinese-English; key concepts keep original Chinese + English translation)
   - Complete DOI citations
   - Cross-reference paragraph to the L0–L7 spectrum
   - Navigation links to related modules
3. Update the navigation tree in `mkdocs.yml`.
4. If adding a new model or methodology, ensure bidirectional cross-references in related modules.

### Modifying Existing Content

1. Submit a PR on the appropriate branch.
2. In the PR description, explain the scientific or classical basis for the change.
3. If modifying a core proposition, provide argumentation at the first-principles level.

### Building Preprints

```bash
cd paper/preprint_1  # or preprint_2
pdflatex main.tex
bibtex main          # if a .bib file exists
pdflatex main.tex
pdflatex main.tex    # twice to resolve cross-references
```

### Local MkDocs Preview

```bash
pip install -r requirements.txt
mkdocs serve
# Visit http://127.0.0.1:8000
```

---

## Content Standards

### Principle of Least-Action Editing

The project follows the principle of least action in `POSITIONING.md`: every contribution should reduce the total cognitive action needed to understand the whole project.

- A new concept must serve an irreplaceable function.
- A new equation must eliminate ambiguity, not create confusion.
- A new module must link back to the core framework (Dao, One, Map ≠ Territory, L0–L7, emergence, cost of deviation).
- A new application must include abuse risks and countermeasures.
- If removing a passage does not affect understanding, prefer removal.

### Bilingual Content

- The default language of the project is Chinese.
- English translations use the `.<locale>.md` suffix convention (e.g., `README.en.md`).
- English versions should preserve the conceptual precision of the Chinese original; literal translation is secondary.
- See [`TRANSLATION.en.md`](TRANSLATION.en.md) for the project's translation policy, including which Chinese terms must be kept untranslated.
- When a full English translation is not yet available, create a stub with title, abstract, and a note stating "Full English translation in progress."

### Citation Format

- **Journal article**: Author (Year). Title. *Journal*, *Volume*(Issue), pages. doi:DOI
- **Book**: Author (Year). *Title*. Publisher.
- **Classical text**: Traditional author (approx. century). *Text name*. (Commentary reference)

### Mathematical Formalization

- Use LaTeX math mode: `$inline$`, `$$block$$`
- Define all symbols on first appearance
- Number equations

### Cross-References

- Use relative paths for in-project modules: `` `path/to/file.md` ``
- Every file must include a paragraph linking it to the L0–L7 spectrum
- Footer navigation should link to previous/next related modules

---

## Reporting Issues

- Bug reports, content corrections, and translation suggestions are welcome.
- For sensitive ethical concerns about potential misuse, please open a private issue or contact the maintainers directly.

---

> 返回中文版：[`CONTRIBUTING.md`](CONTRIBUTING.md)
