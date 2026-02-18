from src.ray_tracer.lights.point import PointLight
from src.ray_tracer.material import Material
from src.ray_tracer.tuples import ColorTuple, CustomTuple


def lighting(
    m: Material, light: PointLight, position: CustomTuple, eye_vec: CustomTuple, normal_vec: CustomTuple
) -> ColorTuple:
    """Calculate the lighting at a point on a surface."""

    return ColorTuple(1, 2, 3)
