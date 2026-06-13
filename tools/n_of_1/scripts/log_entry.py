#!/usr/bin/env python3
"""Append a structured N-of-1 observation to a local CSV file.

Example:
    python log_entry.py \\
        --data-dir ~/my_nof1 \\
        --phase intervention \\
        --variables anxiety=6,sleep_quality=5,energy=4
"""

import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path


def parse_variables(text: str) -> dict[str, str]:
    """Parse 'a=1,b=2' into dict."""
    result: dict[str, str] = {}
    if not text:
        return result
    for pair in text.split(","):
        if "=" not in pair:
            raise ValueError(f"Variable must be key=value, got: {pair}")
        key, value = pair.split("=", 1)
        result[key.strip()] = value.strip()
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Append N-of-1 log entry.")
    parser.add_argument("--data-dir", required=True, help="Directory to store data.csv")
    parser.add_argument("--phase", required=True,
                        choices=["baseline", "intervention", "withdrawal", "follow_up"],
                        help="Experimental phase")
    parser.add_argument("--variables", default="",
                        help="Comma-separated key=value pairs, e.g., anxiety=6,sleep=7")
    parser.add_argument("--note", default="", help="Free-text note")
    parser.add_argument("--timestamp", default=None,
                        help="ISO timestamp (default: now)")
    args = parser.parse_args()

    data_dir = Path(args.data_dir).expanduser()
    data_dir.mkdir(parents=True, exist_ok=True)
    csv_path = data_dir / "data.csv"

    variables = parse_variables(args.variables)
    timestamp = args.timestamp or datetime.now(timezone.utc).isoformat()

    row = {
        "timestamp": timestamp,
        "phase": args.phase,
        "note": args.note,
        **variables,
    }

    file_exists = csv_path.exists()
    with csv_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(row.keys()))
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

    print(f"Logged entry to {csv_path}")
    print(f"  timestamp: {timestamp}")
    print(f"  phase: {args.phase}")
    for k, v in variables.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
