from math import sqrt

from src.ray_tracer.tuples import CustomTuple
from src.ray_tracer.utils import compare_float


def test_reflect_45_degrees():
    vector = CustomTuple(1, -1, 0)
    normal = CustomTuple(0, 1, 0)
    reflected = vector.reflect(normal)

    assert compare_float(reflected.x, 1)
    assert compare_float(reflected.y, 1)
    assert compare_float(reflected.z, 0)


def test_reflect_slanted():
    vector = CustomTuple(0, -1, 0)
    normal = CustomTuple(sqrt(2) / 2, sqrt(2) / 2, 0)
    reflected = vector.reflect(normal)

    assert compare_float(reflected.x, 1)
    assert compare_float(reflected.y, 0)
    assert compare_float(reflected.z, 0)
