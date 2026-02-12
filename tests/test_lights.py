from src.ray_tracer.lights.point import PointLight
from src.ray_tracer.tuples import ColorTuple, CustomTuple


def test_point_init():
    """Test the initialization of a point light source."""
    position = CustomTuple(1, 2, 3)
    intensity = ColorTuple(1, 1, 1)
    light = PointLight(position, intensity)
    assert light.position == position
    assert light.intensity == intensity
