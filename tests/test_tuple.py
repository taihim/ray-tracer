from math import sqrt

import pytest

from src.ray_tracer.rt_tuple import CustomTuple, compare_float


def test_point() -> None:
    p = CustomTuple.point(4.3, -4.2, 3.1)

    assert compare_float(p.x, 4.3)
    assert compare_float(p.y, -4.2)
    assert compare_float(p.z, 3.1)
    assert compare_float(p.w, 1.0)


def test_vector() -> None:
    v = CustomTuple.vector(4.3, -4.2, 3.1)

    assert compare_float(v.x, 4.3)
    assert compare_float(v.y, -4.2)
    assert compare_float(v.z, 3.1)
    assert compare_float(v.w, 0.0)


def test_addition() -> None:
    v1 = CustomTuple.vector(1, -2, 3)
    v2 = CustomTuple.vector(4, 5, 6)
    p1 = CustomTuple.point(7, 8, 9)
    p2 = CustomTuple.point(10, 11, -12)

    assert v1 + v2 == CustomTuple.vector(5, 3, 9)
    assert p1 + v1 == CustomTuple.point(8, 6, 12)
    assert v2 + p2 == CustomTuple.point(14, 16, -6)

    with pytest.raises(ValueError) as exc:
        p1 + p2
    assert str(exc.value) == "Cannot add two points."

    with pytest.raises(TypeError) as exc2:
        p2 + 1
    assert str(exc2.value) == f"Unsupported operand of type {int}. Can only add CustomTuples to a CustomTuple."


def test_subtraction() -> None:
    v1 = CustomTuple.vector(1, -2, 3)
    v2 = CustomTuple.vector(4, 5, 6)
    p1 = CustomTuple.point(7, 8, 9)
    p2 = CustomTuple.point(10, 11, -12)

    assert v1 - v2 == CustomTuple.vector(-3, -7, -3)
    assert p1 - v1 == CustomTuple.point(6, 10, 6)
    assert p2 - p1 == CustomTuple.vector(3, 3, -21)

    with pytest.raises(ValueError) as exc:
        v2 - p2
    assert str(exc.value) == "Cannot subtract a point from a vector."

    with pytest.raises(TypeError) as exc2:
        p2 - 1
    assert str(exc2.value) == f"Unsupported operand of type {int}. Can only subtract CustomTuples from a CustomTuple."


def test_equality() -> None:
    v1 = CustomTuple.vector(1, -2, 3)
    v2 = CustomTuple.vector(4, 5, 6)
    p1 = CustomTuple.point(7, 8, 9)
    p2 = CustomTuple.point(10, 11, -12)

    assert v1 == CustomTuple.vector(1, -2, 3)
    assert v2 != CustomTuple.point(4, 5, 6)
    assert p1 == CustomTuple.point(7, 8, 9)
    assert p2 != CustomTuple.vector(10, 11, -12)

    with pytest.raises(TypeError) as exc:
        p2 == "test_str"
    assert str(exc.value) == "Can only compare CustomTuples to a CustomTuple."


def test_negation() -> None:
    v1 = CustomTuple.vector(1, -2, 3)

    assert -v1 == CustomTuple(-1, 2, -3)


def test_multiplication() -> None:
    v1 = CustomTuple(1, -2, 3, -4)
    assert v1 * 3.5 == CustomTuple(3.5, -7, 10.5, -14)

    v2 = CustomTuple(1, -2, 3, -4)
    assert v2 * 0.5 == CustomTuple(0.5, -1, 1.5, -2)


def test_divison() -> None:
    v1 = CustomTuple(1, -2, 3, -4)
    assert v1 / 2 == CustomTuple(0.5, -1, 1.5, -2)

def test_magnitude() -> None:
    v1 = CustomTuple.vector(0, 1, 0)
    v2 = CustomTuple.vector(0, 0, 1)
    v3 = CustomTuple.vector(1, 2, 3)
    v4 = CustomTuple.vector(-1, -2, -3)
    p1 = CustomTuple.point(1, 2, 3)
    t1 = CustomTuple(4, 5, 6, 7)

    assert compare_float(v1.magnitude(), 1.0)
    assert compare_float(v2.magnitude(), 1.0)
    assert compare_float(v3.magnitude(), sqrt(14))
    assert compare_float(v4.magnitude(), sqrt(14))

    with pytest.raises(ValueError) as exc1:
        p1.magnitude()
    assert str(exc1.value) == "Can only calculate magnitude for vectors (w == 0)."

    with pytest.raises(ValueError) as exc2:
        t1.magnitude()
    assert str(exc2.value) == "Can only calculate magnitude for vectors (w == 0)."


def test_normalization() -> None:
    v1 = CustomTuple.vector(4, 0, 0)
    v2 = CustomTuple.vector(1, 2, 3)
    v3 = CustomTuple.vector(1, 2, 3)
    assert v1.normalize() == CustomTuple.vector(1, 0, 0)
    assert v2.normalize() == CustomTuple.vector(0.2672612, 0.5345224, 0.8017837)
    assert v3.normalize().magnitude() == 1

    p1 = CustomTuple.point(1, 2, 3)
    t1 = CustomTuple(4, 5, 6, 7)

    with pytest.raises(ValueError) as exc1:
        p1.normalize()
    assert str(exc1.value) == "Can only normalize vectors (w == 0)."

    with pytest.raises(ValueError) as exc2:
        t1.normalize()
    assert str(exc2.value) == "Can only normalize vectors (w == 0)."
