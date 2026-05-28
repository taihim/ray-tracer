from src.ray_tracer.ray import Ray
from src.ray_tracer.sphere import Sphere
from src.ray_tracer.lights import PointLight
from src.ray_tracer.material import Material
from src.ray_tracer.matrix.transforms import Transform
from src.ray_tracer.tuples import ColorTuple, CustomTuple

class World:
    """World class for the ray tracer"""

    def __init__(self, light: PointLight | None=None, objects: list[Sphere] | None=None) -> None:
        self.light = light
        self.objects = objects

    @staticmethod
    def default_world() -> "World":
        light = PointLight(CustomTuple(-10, 10, -10), ColorTuple(1, 1, 1))
        mat1 = Material(color=ColorTuple(0.8, 1.0, 0.6), diffuse=0.7, specular=0.2)
        sph1 = Sphere()
        sph1.set_material(mat1)
        tfm1 = Transform().scale(0.5, 0.5, 0.5)
        sph2 = Sphere()
        sph2.set_transform(tfm1)
        objects = [sph1, sph2]

        return World(light=light, objects=objects)




def intersect_world(world: "World", ray: Ray) -> None:
    """Return intersections for a ray and all objects in a world object.

    Args:
        world:
        ray:
    
    Returns:
        
    """
    return None

    
