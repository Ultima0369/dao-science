#!/usr/bin/env python3
"""Integration demo: wave scheduler + hardware breaker + auditable memory.

This script simulates a small compute node that:
1. Allocates power across a 3x3 grid using a travelling-wave schedule.
2. Monitors local thermal boundaries with a hardware breaker FSM.
3. Stores each step as an auditable experience record.
4. Prints an audit summary for the run.

Run with:
    python examples/auditable_node_demo.py
"""

from __future__ import annotations

from datetime import datetime, timezone

from dao_science.experience import AuditableMemory, ExperienceRecord
from dao_science.hardware import BreakerFSM, SensorReading, State
from dao_science.scheduler import WaveScheduler


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def main() -> None:
    scheduler = WaveScheduler(shape=(3, 3), total_power_budget=9.0, wave_amp=0.5)
    breaker = BreakerFSM(p_max=12.0, t_max=2.5, dtdt_max=1.0)
    memory = AuditableMemory()

    print("t\tstate\tgrid_sum\tpeak_node")
    for t in range(20):
        grid = scheduler.step(float(t))
        peak = float(grid.max())
        # Synthetic temperature derived from peak node power.
        temp = 1.0 + 0.15 * peak
        dt_dt = abs(peak - 1.0) * 0.1

        reading = SensorReading(p_watts=peak, t_junction=temp, dt_dt=dt_dt)
        state = breaker.transition(reading)

        memory.store(
            ExperienceRecord(
                timestamp=timestamp(),
                context_hash="auditable-node-demo",
                decision=f"wave-step-{t}",
                outcome=float(state == State.NORMAL),
                confidence=0.9,
                audit_log={
                    "peak_node": peak,
                    "temperature": temp,
                    "dt_dt": dt_dt,
                    "state": state.name,
                },
            )
        )

        print(f"{t}\t{state.name}\t{grid.sum():.2f}\t\t{peak:.2f}")

    print("\nAudit summary:")
    print(memory.audit("auditable-node-demo"))


if __name__ == "__main__":
    main()
