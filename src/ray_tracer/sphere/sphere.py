from uuid import uuid4
from src.ray_tracer.tuples import CustomTuple

# for now we assume all spheres are centered at the origin and are unit sphere (radius of 1)
class Sphere:
    "A sphere object."

    def __init__(self, radius: float = 1.0):
        self.id = uuid4()
        self.origin = CustomTuple(0, 0, 0, 1) # centered at origin
        self.radius = radius
        