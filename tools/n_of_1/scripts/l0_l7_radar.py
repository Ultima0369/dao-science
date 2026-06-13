#!/usr/bin/env python3
"""Generate an L0-L7 cognitive-relational radar chart from five dimension scores.

Usage:
    python l0_l7_radar.py --share 2 --revise 4 --validate 2 --relation 5 --update 3 \
        --label "我感到被忽视" --out ~/my_nof1/l0l7_2026-06-14.png

Or run interactively:
    python l0_l7_radar.py

The script follows the prioritised level-assignment rules from
0_motivation/L0_L7_operationalization.md:
    1. Revisability + prediction-error update  -> L1-L4 vs L5-L7
    2. Relational consequence                  -> healthy vs rupture
    3. Shareability + validation mode          -> exact level
"""

import argparse
import sys
from pathlib import Path

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np


def _set_cjk_font() -> None:
    """Try to use a system font that supports CJK glyphs."""
    candidates = [
        "Microsoft YaHei",
        "SimHei",
        "SimSun",
        "Noto Sans CJK SC",
        "WenQuanYi Micro Hei",
        "Source Han Sans SC",
        "Arial Unicode MS",
    ]
    available = {f.name for f in fm.fontManager.ttflist}
    for name in candidates:
        if name in available:
            plt.rcParams["font.sans-serif"] = [name]
            plt.rcParams["axes.unicode_minus"] = False
            return


_set_cjk_font()

DIMENSIONS = [
    "可共享性\nShareability",
    "可修正性\nRevisability",
    "主体间验证\nIntersubjective\nvalidation",
    "关系后果\nRelational\nconsequence",
    "预测误差更新\nPrediction-error\nupdate",
]


def assess_level(scores: dict[str, int]) -> tuple[str, str]:
    """Return (primary_level, note) using the operational rules."""
    sh = scores["shareability"]
    re = scores["revisability"]
    va = scores["validation"]
    rl = scores["relation"]
    up = scores["update"]

    # Rule 1: revisability + update
    can_update = (re + up) / 2.0 >= 4.0
    # Rule 2: relational consequence
    connects = rl >= 4.0

    if can_update and connects:
        # L1-L4: use shareability + validation to decide
        if va >= 6 and sh >= 5:
            return "L1/L4", "公共事实或理性协议层"
        if sh >= 4 and va >= 4:
            return "L3", "群体共识/文化传承层"
        return "L2", "个体实情层（需要被承认）"

    if not can_update and not connects:
        # L5-L7
        if rl <= 1:
            return "L7", "关系频谱负向终点——建议寻求真人支持"
        if re <= 2 and up <= 2:
            return "L6", "信念闭环/概念空转"
        return "L5", "关系断裂/回避层"

    # Mixed: can update but disconnects, or cannot update but connects
    if can_update and not connects:
        return "L4→L5", "理性上可修正，但关系后果已受损"
    return "L2/L3", "关系上仍连接，但修正机制已变弱"


def functional_assessment(scores: dict[str, int]) -> str:
    """Return a one-word functional trajectory label."""
    re = scores["revisability"]
    up = scores["update"]
    rl = scores["relation"]
    if re >= 4 and up >= 4 and rl >= 4:
        return "健康轨迹"
    if rl <= 2 or (re <= 2 and up <= 2):
        return "负向轨迹"
    return "需持续观察"


def draw_radar(scores: dict[str, int], label: str, out_path: Path | None) -> None:
    values = [
        scores["shareability"],
        scores["revisability"],
        scores["validation"],
        scores["relation"],
        scores["update"],
    ]
    values += values[:1]  # close the polygon
    angles = np.linspace(0, 2 * np.pi, len(DIMENSIONS), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)  # type: ignore[attr-defined]
    ax.set_theta_direction(-1)  # type: ignore[attr-defined]

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(DIMENSIONS, fontsize=9)
    ax.set_ylim(0, 7)
    ax.set_yticks([1, 3, 5, 7])
    ax.set_yticklabels(["1", "3", "5", "7"], color="grey", size=8)
    ax.grid(True)

    ax.plot(angles, values, linewidth=2, linestyle="solid", color="#1565c0")
    ax.fill(angles, values, alpha=0.25, color="#1565c0")

    level, note = assess_level(scores)
    func = functional_assessment(scores)
    title = f"{label}\n主要层级：{level}  |  功能评估：{func}"
    ax.set_title(title, fontsize=11, pad=20)

    fig.text(
        0.5,
        0.02,
        f"判定说明：{note}",
        ha="center",
        fontsize=9,
        style="italic",
        color="#333333",
    )

    plt.tight_layout(rect=(0, 0.05, 1, 1))

    if out_path:
        out_path = Path(out_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(out_path, dpi=150, bbox_inches="tight")
        print(f"Radar chart saved to: {out_path}")
    else:
        plt.show()


def interactive_input() -> dict[str, int]:
    print("请输入 1–7 分（1=极弱，7=极强）：")
    keys = [
        ("shareability", "可共享性"),
        ("revisability", "可修正性"),
        ("validation", "主体间验证"),
        ("relation", "关系后果"),
        ("update", "预测误差更新"),
    ]
    scores: dict[str, int] = {}
    for key, name in keys:
        while True:
            raw = input(f"  {name} (1-7): ").strip()
            try:
                val = int(raw)
                if 1 <= val <= 7:
                    scores[key] = val
                    break
                print("    请输入 1 到 7 之间的整数。")
            except ValueError:
                print("    请输入整数。")
    return scores


def main() -> None:
    parser = argparse.ArgumentParser(
        description="L0-L7 cognitive-relational radar chart generator"
    )
    parser.add_argument("--share", type=int, help="Shareability (1-7)")
    parser.add_argument("--revise", type=int, help="Revisability (1-7)")
    parser.add_argument("--validate", type=int, help="Intersubjective validation (1-7)")
    parser.add_argument("--relation", type=int, help="Relational consequence (1-7)")
    parser.add_argument("--update", type=int, help="Prediction-error update (1-7)")
    parser.add_argument("--label", default="L0-L7 Snapshot", help="Title label")
    parser.add_argument("--out", type=Path, help="Output PNG path (omit to show)")
    args = parser.parse_args()

    provided = [
        args.share,
        args.revise,
        args.validate,
        args.relation,
        args.update,
    ]

    if any(v is None for v in provided):
        if any(v is not None for v in provided):
            print("Error: provide all five scores or none for interactive mode.")
            sys.exit(1)
        scores = interactive_input()
    else:
        for v in provided:
            if not 1 <= v <= 7:
                print("Error: all scores must be integers between 1 and 7.")
                sys.exit(1)
        scores = {
            "shareability": args.share,
            "revisability": args.revise,
            "validation": args.validate,
            "relation": args.relation,
            "update": args.update,
        }

    level, note = assess_level(scores)
    func = functional_assessment(scores)
    print(f"主要层级：{level}")
    print(f"判定说明：{note}")
    print(f"功能评估：{func}")

    draw_radar(scores, args.label, args.out)


if __name__ == "__main__":
    main()
