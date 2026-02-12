from src.ray_tracer.material import Material
from src.ray_tracer.tuples import ColorTuple


def test_material_init():
    """Test the initialization of a material."""
    material = Material(ColorTuple(1, 1, 1), 0.1, 0.9, 0.9, 200.0)
    assert material.color == ColorTuple(1, 1, 1)
    assert material.ambient == 0.1
    assert material.diffuse == 0.9
    assert material.specular == 0.9
    assert material.shininess == 200.0
