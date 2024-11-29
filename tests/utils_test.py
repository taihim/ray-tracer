import pytest

from src.ray_tracer import compare_float


def test_compare_float() -> None:

    assert(compare_float(0, 0))
    assert(compare_float(1, 1.0))
    assert(compare_float(4.5, 4.5))
    assert(compare_float(-3.7867, -3.7867))
    # smaller difference than EPSILON
    assert(compare_float(6.12345689, 6.12345681))
    assert(compare_float(1.1, 2.1) is False)
    assert(compare_float(-1.1, 1.1) is False)

    with pytest.raises(TypeError) as exc:
        compare_float(1, "2")  # type: ignore[arg-type]
    assert str(exc.value) == "This function only supports integers and floating point numbers."

    with pytest.raises(TypeError) as exc2:
        compare_float("1", 2)  # type: ignore[arg-type]
    assert str(exc2.value) == "This function only supports integers and floating point numbers."

