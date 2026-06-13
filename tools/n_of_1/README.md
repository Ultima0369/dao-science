# N-of-1 Toolkit

## 第一人称经验数据工具包

---

This directory contains a minimal operational toolkit for running N-of-1 (single-subject) experiments on your own first-person experience. It is designed to work with the protocol described in `3_methodology/n_of_1_protocol.md`.

本目录包含一套最小可行的 N-of-1（单被试）实验工具，用于把个人的第一人称经验转化为可分析的数据。设计与 `3_methodology/n_of_1_protocol.md` 中的协议配套使用。

---

## Design principles

1. **Local-first**: All your data stays on your machine. No cloud, no accounts.
2. **Plain-text friendly**: Logs are Markdown/CSV so you can edit them with any tool.
3. **Privacy by default**: No names, locations, or device identifiers are collected unless you choose to add them.
4. **Minimal action**: Each tool does one thing and does it without friction.

---

## Directory structure

```
tools/n_of_1/
├── README.md                 # This file
├── schema.yaml               # Data schema for N-of-1 observations
├── templates/                # Markdown templates
│   ├── experiment_design.md  # Design your N-of-1 experiment
│   ├── daily_log.md          # Daily structured log
│   └── weekly_review.md      # Weekly aggregation and reflection
├── scripts/                  # Python helpers
│   ├── log_entry.py          # Create a structured log entry
│   └── analyze.py            # Analyze CSV data and generate report
└── examples/                 # Example data and report
    ├── sample_data.csv
    └── sample_report.md
```

---

## Quick start

### 1. Design your experiment

Copy `templates/experiment_design.md` to your private workspace and fill it out:

```bash
cp templates/experiment_design.md ~/my_nof1/experiment_design.md
```

### 2. Record observations

Use the daily log template, or use the CLI helper:

```bash
python scripts/log_entry.py \
  --data-dir ~/my_nof1 \
  --phase baseline \
  --variables anxiety=6 sleep=5 energy=4
```

This appends one row to `~/my_nof1/data.csv`.

### 3. Analyze

After collecting data, run:

```bash
python scripts/analyze.py \
  --data ~/my_nof1/data.csv \
  --out ~/my_nof1/report.md
```

It will compute means by phase, simple effect sizes, and produce a Markdown report with optional plots.

---

## Data ownership

- Your data belongs to you.
- This toolkit does not send anything anywhere.
- If you want to share results, export and anonymize first.

---

## Relation to Project Dao.Science

This toolkit operationalizes the first-person epistemology in `1_first_principles/05_first_person_epistemology.md`: **individual experience is not noise; it is irreducible data that can be structured, measured, and cross-validated.**

It also embodies the principle of least action: the tools are as simple as possible so that the cognitive cost of recording does not exceed the value of the data.

---

> 返回协议文档：[`3_methodology/n_of_1_protocol.md`](../../3_methodology/n_of_1_protocol.md)
