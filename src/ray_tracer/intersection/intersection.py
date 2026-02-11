from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from src.ray_tracer.ray import Ray
    from src.ray_tracer.sphere import Sphere


class Intersection:
    """Represents an intersection between a ray and an object."""

    def __init__(self, t: float, obj: "Ray | Sphere") -> None:
        self.t = t
        self.object = obj

    def __lt__(self, other: "Intersection") -> bool:
        """Sort based on value of t."""
        return self.t < other.t

    def __str__(self) -> str:
        return f"Intersection object with t: {self.t} and object: {self.object}"


def intersections(*args: Intersection) -> tuple[Intersection, ...]:
    return tuple(sorted(args))
