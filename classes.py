from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    """Represents a point"""
    x: float
    y: float
