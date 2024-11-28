import pytest

from src.ray_tracer.custom_tuple import CustomTuple
from src.ray_tracer.utils import compare_float


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
    assert str(exc2.value) == "Can only add CustomTuples to a CustomTuple."


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
    assert str(exc2.value) == "Can only subtract CustomTuples from a CustomTuple."


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
