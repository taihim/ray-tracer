from src.ray_tracer import CustomTuple
from src.ray_tracer.ray import Ray


def test_ray_init() -> None:
    r1 = Ray(CustomTuple(1, 2, 3, 1), CustomTuple(4, 5, 6))

    assert r1.origin == CustomTuple(1, 2, 3, 1)
    assert r1.direction == CustomTuple(4, 5, 6)
