from src.ray_tracer import CustomTuple
from src.ray_tracer.matrix.transforms import scale, translate


def test_translation() -> None:
    t1 = translate(5, -3, 2)

    p1 = CustomTuple.point(-3, 4, 5)
    v1 = CustomTuple.vector(-3, 4, 5)

    assert t1 * p1 == CustomTuple.point(2, 1, 7)
    assert t1 * v1 == v1


def test_translation_inverse() -> None:
    t1 = translate(5, -3, 2)
    t1_inv = t1.inverse()

    p1 = CustomTuple.point(-3, 4, 5)
    v1 = CustomTuple.vector(-3, 4, 5)

    assert t1_inv * p1 == CustomTuple.point(-8, 7, 3)
    assert t1 * v1 == v1


def test_scaling() -> None:
    t1 = scale(2, 3, 4)

    p1 = CustomTuple.point(-4, 6, 8)
    v1 = CustomTuple.vector(-4, 6, 8)

    assert t1 * p1 == CustomTuple.point(-8, 18, 32)
    assert t1 * v1 == CustomTuple.vector(-8, 18, 32)


def test_scaling_inverse() -> None:
    t1 = scale(2, 3, 4)
    t1_inv = t1.inverse()

    p1 = CustomTuple.point(-4, 6, 8)
    v1 = CustomTuple.vector(-4, 6, 8)

    assert t1_inv * p1 == CustomTuple.point(-2, 2, 2)
    assert t1_inv * v1 == CustomTuple.vector(-2, 2, 2)


def test_reflection() -> None:
    # reflection just means multiplying by -1

    t1 = scale(-1, 1, 1)

    p1 = CustomTuple.point(2, 3, 4)
    v1 = CustomTuple.vector(2, 3, 4)

    assert t1 * p1 == CustomTuple.point(-2, 3, 4)
    assert t1 * v1 == CustomTuple.vector(-2, 3, 4)
