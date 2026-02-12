from src.ray_tracer.material import Material
from src.ray_tracer.sphere import Sphere
from src.ray_tracer.tuples import ColorTuple


def test_sphere_material():
    """Test the material of a sphere."""
    sphere = Sphere()
    material = Material(ColorTuple(0, 1, 1), 0.2, 0.8, 0.76, 100.0)
    sphere.set_material(material)

    assert sphere.material == material
    assert sphere.material.color == ColorTuple(0, 1, 1)
    assert sphere.material.ambient == 0.2
    assert sphere.material.diffuse == 0.8
    assert sphere.material.specular == 0.76
    assert sphere.material.shininess == 100.0
