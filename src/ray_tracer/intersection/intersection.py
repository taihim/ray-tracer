from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.ray_tracer.ray import Ray
    from src.ray_tracer.sphere import Sphere

class Intersection:
    def __init__(self, t: float, obj: "Ray | Sphere") -> None:
        self.t = t
        self.object = obj
    
def intersections(*args: Intersection) -> tuple[Intersection, ...]:
    return args