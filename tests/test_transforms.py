from src.ray_tracer import CustomTuple
from src.ray_tracer.matrix.transforms import translation


def test_translation() -> None:
    t1 = translation(5, -3, 2)

    p1 = CustomTuple.point(-3, 4, 5)
    v1 = CustomTuple.vector(-3, 4, 5)

    assert t1 * p1 == CustomTuple.point(2, 1, 7)
    assert t1 * v1 == v1


def test_translation_inverse() -> None:
    t1 = translation(5, -3, 2)
    t1_inv = t1.inverse()

    p1 = CustomTuple.point(-3, 4, 5)
    v1 = CustomTuple.vector(-3, 4, 5)

    assert t1_inv * p1 == CustomTuple.point(-8, 7, 3)
    assert t1 * v1 == v1
