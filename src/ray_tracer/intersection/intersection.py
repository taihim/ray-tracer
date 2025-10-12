from src.ray_tracer import Ray
from src.ray_tracer import Sphere


class Intersection:
    def __init__(self, t: float, obj: Ray | Sphere) -> None:
        self.t = t
        self.object = obj
    