import math
from typing import cast

from src.ray_tracer import CustomTuple
from src.ray_tracer.matrix.transforms import Transform


def test_translation() -> None:
    t1 = Transform().translate(5, -3, 2)

    p1 = CustomTuple.point(-3, 4, 5)
    v1 = CustomTuple.vector(-3, 4, 5)

    assert t1 * p1 == CustomTuple.point(2, 1, 7)
    assert t1 * v1 == v1


def test_translation_inverse() -> None:
    t1 = Transform().translate(5, -3, 2)
    t1_inv = t1.inverse()

    p1 = CustomTuple.point(-3, 4, 5)
    v1 = CustomTuple.vector(-3, 4, 5)

    assert t1_inv * p1 == CustomTuple.point(-8, 7, 3)
    assert t1 * v1 == v1


def test_scaling() -> None:
    t1 = Transform().scale(2, 3, 4)

    p1 = CustomTuple.point(-4, 6, 8)
    v1 = CustomTuple.vector(-4, 6, 8)

    assert t1 * p1 == CustomTuple.point(-8, 18, 32)
    assert t1 * v1 == CustomTuple.vector(-8, 18, 32)


def test_scaling_inverse() -> None:
    t1 = Transform().scale(2, 3, 4)
    t1_inv = t1.inverse()

    p1 = CustomTuple.point(-4, 6, 8)
    v1 = CustomTuple.vector(-4, 6, 8)

    assert t1_inv * p1 == CustomTuple.point(-2, 2, 2)
    assert t1_inv * v1 == CustomTuple.vector(-2, 2, 2)


def test_reflection() -> None:
    # reflection just means multiplying by -1

    t1 = Transform().scale(-1, 1, 1)

    p1 = CustomTuple.point(2, 3, 4)
    v1 = CustomTuple.vector(2, 3, 4)

    assert t1 * p1 == CustomTuple.point(-2, 3, 4)
    assert t1 * v1 == CustomTuple.vector(-2, 3, 4)


def test_rotation_x() -> None:
    t1 = Transform().rotate_x(math.pi / 2)  # 90 deg rotation
    t2 = Transform().rotate_x(math.pi / 4)  # 45 deg rotation
    t3 = Transform().rotate_x(
        math.pi
    )  # 180 deg rotation (puts it on opposite side of starting point. i.e. -1 in this case)

    p1 = CustomTuple.point(0, 1, 0)

    assert t1 * p1 == CustomTuple.point(0, 0, 1)
    assert t2 * p1 == CustomTuple.point(0, math.sqrt(2) / 2, math.sqrt(2) / 2)
    assert t3 * p1 == CustomTuple.point(0, -1, 0)


def test_rotation_x_inverse() -> None:
    t1 = Transform().rotate_x(math.pi / 4)  # 90 deg rotation
    t1_inv = t1.inverse()

    p1 = CustomTuple.point(0, 1, 0)

    assert t1_inv * p1 == CustomTuple.point(0, math.sqrt(2) / 2, -math.sqrt(2) / 2)


def test_rotation_y() -> None:
    t1 = Transform().rotate_y(math.pi / 2)  # 90 deg rotation
    t2 = Transform().rotate_y(math.pi / 4)  # 45 deg rotation
    t3 = Transform().rotate_y(
        math.pi
    )  # 180 deg rotation (puts it on opposite side of starting point. i.e. -1 in this case)

    p1 = CustomTuple.point(0, 0, 1)

    assert t1 * p1 == CustomTuple.point(1, 0, 0)
    assert t2 * p1 == CustomTuple.point(math.sqrt(2) / 2, 0, math.sqrt(2) / 2)
    assert t3 * p1 == CustomTuple.point(0, 0, -1)


def test_rotation_z() -> None:
    t1 = Transform().rotate_z(math.pi / 2)  # 90 deg rotation
    t2 = Transform().rotate_z(math.pi / 4)  # 45 deg rotation
    t3 = Transform().rotate_z(
        math.pi
    )  # 180 deg rotation (puts it on opposite side of starting point. i.e. -1 in this case)

    p1 = CustomTuple.point(0, 1, 0)

    assert t1 * p1 == CustomTuple.point(-1, 0, 0)
    assert t2 * p1 == CustomTuple.point(-math.sqrt(2) / 2, math.sqrt(2) / 2, 0)
    assert t3 * p1 == CustomTuple.point(0, -1, 0)


def test_shear_xy() -> None:
    t1 = Transform().shear(1, 0, 0, 0, 0, 0)

    p1 = CustomTuple.point(2, 3, 4)

    assert t1 * p1 == CustomTuple.point(5, 3, 4)


def test_shear_xz() -> None:
    t1 = Transform().shear(0, 1, 0, 0, 0, 0)

    p1 = CustomTuple.point(2, 3, 4)

    assert t1 * p1 == CustomTuple.point(6, 3, 4)


def test_shear_yx() -> None:
    t1 = Transform().shear(0, 0, 1, 0, 0, 0)

    p1 = CustomTuple.point(2, 3, 4)

    assert t1 * p1 == CustomTuple.point(2, 5, 4)


def test_shear_yz() -> None:
    t1 = Transform().shear(0, 0, 0, 1, 0, 0)

    p1 = CustomTuple.point(2, 3, 4)

    assert t1 * p1 == CustomTuple.point(2, 7, 4)


def test_shear_zx() -> None:
    t1 = Transform().shear(0, 0, 0, 0, 1, 0)

    p1 = CustomTuple.point(2, 3, 4)

    assert t1 * p1 == CustomTuple.point(2, 3, 6)


def test_shear_zy() -> None:
    t1 = Transform().shear(0, 0, 0, 0, 0, 1)

    p1 = CustomTuple.point(2, 3, 4)

    assert t1 * p1 == CustomTuple.point(2, 3, 7)


def test_tranforms_sequential() -> None:
    t1 = Transform().rotate_x(math.pi / 2)
    t2 = Transform().scale(5, 5, 5)
    t3 = Transform().translate(10, 5, 7)

    p1 = CustomTuple.point(1, 0, 1)

    p2_rotated = t1 * p1
    assert p2_rotated == CustomTuple.point(1, -1, 0)

    p3_scaled = t2 * p2_rotated
    assert p3_scaled == CustomTuple.point(5, -5, 0)

    p4_translated = t3 * p3_scaled
    assert p4_translated == CustomTuple.point(15, 0, 7)


def test_tranforms_chained() -> None:
    t1 = Transform().rotate_x(math.pi / 2)
    t2 = Transform().scale(5, 5, 5)
    t3 = Transform().translate(10, 5, 7)

    transform1 = Transform().rotate_x(math.pi / 2).scale(5, 5, 5).translate(10, 5, 7)
    transform2 = cast(Transform, t3 * t2 * t1)
    p1 = CustomTuple.point(1, 0, 1)

    assert transform1.transformation_matrix == transform2.transformation_matrix

    assert transform1 * p1 == CustomTuple.point(15, 0, 7)
    assert transform2 * p1 == CustomTuple.point(15, 0, 7)
