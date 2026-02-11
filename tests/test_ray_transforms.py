from src.ray_tracer import CustomTuple, Ray
from src.ray_tracer.matrix.transforms import Transform


def test_ray_translate():
    ray = Ray(CustomTuple(1, 2, 3, 1), CustomTuple(0, 1, 0))
    matrix = Transform().translate(3, 4, 5)
    transformed_ray = ray.transform(matrix)

    assert transformed_ray.origin == CustomTuple(4, 6, 8, 1)
    assert transformed_ray.direction == CustomTuple(0, 1, 0)


def test_ray_scale():
    ray = Ray(CustomTuple(1, 2, 3, 1), CustomTuple(0, 1, 0))
    matrix = Transform().scale(2, 3, 4)
    transformed_ray = ray.transform(matrix)

    assert transformed_ray.origin == CustomTuple(2, 6, 12, 1)
    assert transformed_ray.direction == CustomTuple(0, 3, 0)
