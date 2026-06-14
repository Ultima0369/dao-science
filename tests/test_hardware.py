"""Unit tests for dao_science.hardware breaker FSM."""
from __future__ import annotations

from dao_science.hardware import BreakerFSM, SensorReading, State


def _reading(p_watts: float, t_junction: float, dt_dt: float) -> SensorReading:
    return SensorReading(p_watts=p_watts, t_junction=t_junction, dt_dt=dt_dt)


def test_normal_state_when_all_boundaries_respected():
    breaker = BreakerFSM(p_max=100.0, t_max=80.0, dtdt_max=10.0)
    assert breaker.transition(_reading(50.0, 60.0, 2.0)) == State.NORMAL


def test_over_power_triggers_throttle():
    breaker = BreakerFSM(p_max=100.0, t_max=80.0, dtdt_max=10.0)
    assert breaker.transition(_reading(150.0, 70.0, 5.0)) == State.THROTTLE


def test_repeated_violation_escalates_to_halt():
    breaker = BreakerFSM(p_max=100.0, t_max=80.0, dtdt_max=10.0)
    over = _reading(150.0, 70.0, 5.0)
    assert breaker.transition(over) == State.THROTTLE
    assert breaker.transition(over) == State.HALT


def test_temperature_violation_also_triggers():
    breaker = BreakerFSM(p_max=100.0, t_max=80.0, dtdt_max=10.0)
    assert breaker.transition(_reading(50.0, 90.0, 2.0)) == State.THROTTLE


def test_rate_of_change_violation_also_triggers():
    breaker = BreakerFSM(p_max=100.0, t_max=80.0, dtdt_max=10.0)
    assert breaker.transition(_reading(50.0, 60.0, 15.0)) == State.THROTTLE


def test_trip_interface_alias():
    breaker = BreakerFSM(p_max=100.0, t_max=80.0, dtdt_max=10.0)
    assert breaker.trip(_reading(50.0, 60.0, 2.0)) == State.NORMAL
