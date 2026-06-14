"""Hardware abstraction layer and unconditional breaker.

Provides abstract interfaces for power control and thermal sensing, plus a
small finite-state machine (FSM) that implements a three-state hardware breaker:
``NORMAL → THROTTLE → HALT``. State transitions depend only on local sensor
thresholds, so the breaker can protect the system even when the software layer
is deadlocked.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto

__all__ = [
    "State",
    "SensorReading",
    "ThermalSensor",
    "PowerController",
    "HardwareBreaker",
    "BreakerFSM",
]


class State(Enum):
    """Breaker states."""

    NORMAL = auto()
    THROTTLE = auto()
    HALT = auto()


@dataclass
class SensorReading:
    """Local sensor snapshot."""

    p_watts: float
    t_junction: float
    dt_dt: float


class ThermalSensor(ABC):
    """Abstract thermal sensor."""

    @abstractmethod
    def read(self) -> SensorReading: ...


class PowerController(ABC):
    """Abstract power actuator."""

    @abstractmethod
    def set_duty(self, fraction: float) -> None: ...


class HardwareBreaker(ABC):
    """Abstract hardware-level breaker."""

    @abstractmethod
    def trip(self, reading: SensorReading) -> State: ...


class BreakerFSM(HardwareBreaker):
    """Three-state hardware breaker FSM.

    Args:
        p_max: Maximum allowed power (W).
        t_max: Maximum allowed junction temperature (arbitrary units).
        dtdt_max: Maximum allowed temperature rate of change.
    """

    def __init__(
        self,
        p_max: float,
        t_max: float,
        dtdt_max: float,
    ) -> None:
        self.p_max = p_max
        self.t_max = t_max
        self.dtdt_max = dtdt_max
        self.state = State.NORMAL

    def _any_boundary_violated(self, r: SensorReading) -> bool:
        return (
            r.p_watts > self.p_max
            or r.t_junction > self.t_max
            or r.dt_dt > self.dtdt_max
        )

    def transition(self, r: SensorReading) -> State:
        """Update breaker state from a sensor reading.

        - If any hard boundary is violated and the current state is ``NORMAL``,
          move to ``THROTTLE``.
        - If violated again while already in ``THROTTLE``, escalate to ``HALT``.
        - Otherwise, return to / remain in ``NORMAL``.
        """
        if self._any_boundary_violated(r):
            if self.state == State.THROTTLE:
                self.state = State.HALT
            else:
                self.state = State.THROTTLE
        else:
            self.state = State.NORMAL
        return self.state

    def trip(self, reading: SensorReading) -> State:
        """Alias for ``transition``; satisfies ``HardwareBreaker`` interface."""
        return self.transition(reading)
