#!/usr/bin/env python3
"""Generate English stub files for all Chinese content Markdown files.

This script scans the project's content directories and creates a corresponding
.en.md file for every .md file that does not yet have one. Each stub contains:
- An English title placeholder
- A notice that the full English translation is in progress
- A link back to the Chinese source file

Human translators should later replace these stubs with proper translations.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CONTENT_DIRS = [
    "0_motivation",
    "1_first_principles",
    "2_models",
    "3_methodology",
    "4_applications",
    "verifiable_units",
]

TITLE_MAP = {
    "L0_L7_operationalization.md": "L0-L7 Operationalization Criteria",
    "L0_L7_spectrum.md": "L0-L7 Fact and Relation Spectrum",
    "abstraction_dialogue.md": "Two Trees: A Dialogue on Abstraction",
    "cognition_in_progress.md": "Cognition in Progress: An Entry from Misunderstanding",
    "objections_and_replies.md": "Objections and Replies: Challenges to the Framework",
    "project_map.md": "Project Map and Reading Paths",
    "why_this_matters.md": "Why This Matters: Three Crises and a Dao-Scientific Response",
    "01_dao_as_process.md": "Dao as Process: Predictive Coding Gradient Flow",
    "02_one_as_bandwidth.md": "One as Bandwidth: The Neuroscience of Awareness Bandwidth",
    "03_map_not_territory.md": "Map Not Territory: Appearance Is Not the Thing Itself",
    "04_philosophy_of_science.md": "Philosophy of Science: Cognitive Layers of Scientific Knowledge",
    "05_first_person_epistemology.md": "First-Person Epistemology: The Individual as Irreducible Data Source",
    "06_emergence.md": "Emergence: From Sum of Parts to Level Transitions",
    "07_cost_of_deviation.md": "Cost of Deviation: Warning Signals and Value Misalignment",
    "100ms_model.md": "The 100ms Model: Amygdala-PFC Competition Dynamics",
    "attention_model.md": "Attention Dynamics: Flexibility of Focus",
    "dmn_self_model.md": "DMN-Self-Interoception Triangle",
    "hypoxia_fifty_demons.md": "Hypoxia and the Fifty Demons: Neurophysiology of Meditative Hallucinations",
    "neuroplasticity_loop.md": "The Neuroplasticity Loop: Post-Training Engineering Description",
    "social_cognition.md": "Social Cognition and Mirror Resonance",
    "li_ru.md": "Li Ru: Establishing the View",
    "n_of_1_protocol.md": "N-of-1 Protocol: Turning First-Person Experience into Testable Data",
    "01_embrace_suffering.md": "Embracing Suffering",
    "02_flow_with_causes.md": "Flowing with Causes",
    "03_seek_nothing.md": "Seeking Nothing",
    "04_act_in_accordance.md": "Acting in Accordance with Reality",
    "ai_governance.md": "AI Governance: Knowing When to Stop",
    "carbon_silicon_symbiosis.md": "Carbon-Silicon Symbiosis: From It to Thou",
    "clinical_mental_health.md": "Clinical Mental Health",
    "creativity_innovation.md": "Creativity and Innovation",
    "education_by_field.md": "Education by Field: Environmental Design as Pedagogy",
    "management.md": "Management: The Manager as First-Person Node",
    "management_field_theory.md": "Field Construction: The Manager as Architect of Environments",
    "vu_01_dmn_insula.md": "VU-01: DMN-Insula Bistability",
    "vu_02_amygdala_pfc.md": "VU-02: Amygdala-PFC Competition Window",
    "vu_03_dmn_ecn.md": "VU-03: DMN-ECN Insight Coupling",
}


def extract_chinese_title(path: Path) -> str:
    with path.open(encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith("# "):
                return stripped[2:].strip()
    return path.stem


def main() -> None:
    for dirname in CONTENT_DIRS:
        for src in (ROOT / dirname).rglob("*.md"):
            if src.name.endswith(".en.md"):
                continue
            dst = src.with_suffix(".en.md")
            if dst.exists():
                continue

            english_title = TITLE_MAP.get(src.name, extract_chinese_title(src))
            rel_to_src = src.relative_to(src.parent)
            depth = len(src.relative_to(ROOT).parts) - 1
            contributing_prefix = "../" * depth

            content = f"""# {english_title}

## {src.stem}

---

> **English translation in progress.**
>
> This page is currently available in Chinese only. A full English translation
> is being prepared. You can read the complete content here:
> [`{src.name}`]({src.name})
>
> If you would like to contribute a translation, please see
> [`CONTRIBUTING.en.md`]({contributing_prefix}CONTRIBUTING.en.md).

---

> 返回中文版：[`{src.name}`]({src.name})
"""
            dst.write_text(content, encoding="utf-8")
            print(f"Created stub: {dst.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
