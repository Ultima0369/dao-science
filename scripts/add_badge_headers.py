#!/usr/bin/env python3
"""Add evidence-level badge header to Markdown files that lack one."""

from pathlib import Path

FILES = [
    "0_motivation/abstraction_dialogue.md",
    "0_motivation/cognition_in_progress.md",
    "0_motivation/L0_L7_operationalization.md",
    "0_motivation/project_map.md",
    "0_motivation/why_this_matters.md",
    "1_first_principles/02_one_as_bandwidth.md",
    "1_first_principles/04_philosophy_of_science.md",
    "1_first_principles/05_first_person_epistemology.md",
    "1_first_principles/06_emergence.md",
    "1_first_principles/07_cost_of_deviation.md",
    "2_models/hypoxia_fifty_demons.md",
    "2_models/neuroplasticity_loop.md",
    "3_methodology/li_ru.md",
    "3_methodology/n_of_1_protocol.md",
    "3_methodology/xing_ru/01_embrace_suffering.md",
    "3_methodology/xing_ru/02_flow_with_causes.md",
    "3_methodology/xing_ru/03_seek_nothing.md",
    "3_methodology/xing_ru/04_act_in_accordance.md",
    "4_applications/carbon_silicon_symbiosis.md",
    "4_applications/education_by_field.md",
]

BADGES = {
    "abstraction_dialogue.md": "> **证据等级**：形式化 [F] + 元伦理/规范 [M]",
    "cognition_in_progress.md": "> **证据等级**：形式化 [F] + 神经证据 [N] + 元伦理/规范 [M]",
    "L0_L7_operationalization.md": "> **证据等级**：形式化 [F] + 行为预测 [B]",
    "project_map.md": "> **证据等级**：形式化 [F]",
    "why_this_matters.md": "> **证据等级**：形式化 [F] + 神经证据 [N] + 元伦理/规范 [M]",
    "02_one_as_bandwidth.md": "> **证据等级**：形式化 [F] + 神经证据 [N] + 行为预测 [B]",
    "04_philosophy_of_science.md": "> **证据等级**：形式化 [F] + 元伦理/规范 [M]",
    "05_first_person_epistemology.md": "> **证据等级**：形式化 [F] + 神经证据 [N] + 元伦理/规范 [M]",
    "06_emergence.md": "> **证据等级**：形式化 [F] + 神经证据 [N]",
    "07_cost_of_deviation.md": "> **证据等级**：形式化 [F] + 行为预测 [B]",
    "hypoxia_fifty_demons.md": "> **证据等级**：形式化 [F] + 神经证据 [N] + 行为预测 [B]",
    "neuroplasticity_loop.md": "> **证据等级**：形式化 [F] + 神经证据 [N]",
    "li_ru.md": "> **证据等级**：形式化 [F] + 神经证据 [N] + 元伦理/规范 [M]",
    "n_of_1_protocol.md": "> **证据等级**：形式化 [F] + 行为预测 [B] + 元伦理/规范 [M]",
    "01_embrace_suffering.md": "> **证据等级**：形式化 [F] + 神经证据 [N] + 行为预测 [B]",
    "02_flow_with_causes.md": "> **证据等级**：形式化 [F] + 神经证据 [N] + 行为预测 [B]",
    "03_seek_nothing.md": "> **证据等级**：形式化 [F] + 神经证据 [N] + 行为预测 [B]",
    "04_act_in_accordance.md": "> **证据等级**：形式化 [F] + 神经证据 [N] + 行为预测 [B]",
    "carbon_silicon_symbiosis.md": "> **证据等级**：形式化 [F] + 元伦理/规范 [M]",
    "education_by_field.md": "> **证据等级**：形式化 [F] + 神经证据 [N] + 行为预测 [B]",
}


def insert_badge(path: Path, badge: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if "证据等级" in text or "Badge" in text:
        return False
    lines = text.splitlines(keepends=True)
    # Find the first blank line after the second '---' separator.
    dash_count = 0
    insert_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            dash_count += 1
            if dash_count == 2 and insert_idx is None:
                insert_idx = i + 1
                break
    if insert_idx is None:
        # Fallback: insert after first 5 lines.
        insert_idx = min(5, len(lines))
    lines.insert(insert_idx, f"\n{badge}\n\n")
    path.write_text("".join(lines), encoding="utf-8")
    return True


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    for rel in FILES:
        path = root / rel
        badge = BADGES[path.name]
        if insert_badge(path, badge):
            print(f"Added badge to {rel}")
        else:
            print(f"Skipped (already has badge): {rel}")


if __name__ == "__main__":
    main()
