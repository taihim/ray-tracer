import math
from typing import cast

from src.ray_tracer import CustomTuple, Sphere
from src.ray_tracer.matrix.transforms import Transform
from src.ray_tracer.sphere import normal_at


def test_normal_at_x_axis():
    s = Sphere()
    v = normal_at(s, CustomTuple(1, 0, 0, 1))

    assert v == CustomTuple(1, 0, 0)


def test_normal_at_y_axis():
    s = Sphere()
    v = normal_at(s, CustomTuple(0, 1, 0, 1))

    assert v == CustomTuple(0, 1, 0)


def test_normal_at_z_axis():
    s = Sphere()
    v = normal_at(s, CustomTuple(0, 0, 1, 1))

    assert v == CustomTuple(0, 0, 1)


def test_normal_at_non_axial():
    s = Sphere()
    v = normal_at(s, CustomTuple(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3, 1))

    assert v == CustomTuple(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3)


def test_normal_at_translated_sphere():
    s = Sphere()
    s.set_transform(Transform().translate(0, 1, 0))

    v = normal_at(s, CustomTuple(0, 1.70711, -0.70711, 1))

    assert v == CustomTuple(0, 0.70711, -0.70711)


def test_normal_at_rotated_sphere():
    s = Sphere()
    s.set_transform(cast("Transform", Transform().scale(1, 0.5, 1) * Transform().rotate_z(math.pi / 5)))

    v = normal_at(s, CustomTuple(0, math.sqrt(2) / 2, -(math.sqrt(2)) / 2, 1))

    assert v == CustomTuple(0, 0.97014, -0.24254)
