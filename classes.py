from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    """Represents a point"""
    x: float
    y: float

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


@dataclass
class Circle:
    """Represents a moving circle"""
    radius: float
    center: Point
    velocity: Point

    def update(self, width: int, height: int):
        if self.center.x + self.radius >= width / 2 or self.center.x - self.radius <= -width / 2:
            self.velocity = Point(self.velocity.x * -1, self.velocity.y)
        if self.center.y + self.radius >= height / 2 or self.center.y - self.radius <= -height / 2:
            self.velocity = Point(self.velocity.x, self.velocity.y * -1)
        self.center = self.center + self.velocity

    def draw_function(self, x: float, y: float) -> float:
        return self.radius / (((x - self.center.x) ** 2 + (y - self.center.y) ** 2) ** .5)
