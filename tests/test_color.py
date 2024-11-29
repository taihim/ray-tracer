from src.ray_tracer import ColorTuple, compare_float


def test_color() -> None:
    c1 = ColorTuple(-0.5, 0.4, 1.7)

    assert compare_float(c1.red, -0.5)
    assert compare_float(c1.green, 0.4)
    assert compare_float(c1.blue, 1.7)


def test_addition() -> None:
    c1 = ColorTuple(0.9, 0.6, 0.75)
    c2 = ColorTuple(0.7, 0.1, 0.25)

    assert c1 + c2 == ColorTuple(1.6, 0.7, 1.0)


def test_subtraction() -> None:
    c1 = ColorTuple(0.9, 0.6, 0.75)
    c2 = ColorTuple(0.7, 0.1, 0.25)

    assert c1 - c2 == ColorTuple(0.2, 0.5, 0.5)


def test_scalar_mult() -> None:
    c1 = ColorTuple(0.2, 0.3, 0.4)
    assert c1 * 2 == ColorTuple(0.4, 0.6, 0.8)


def test_hadamard_product() -> None:
    c1 = ColorTuple(1, 0.2, 0.4)
    c2 = ColorTuple(0.9, 1, 0.1)

    assert c1 * (c2) == ColorTuple(0.9, 0.2, 0.04)
