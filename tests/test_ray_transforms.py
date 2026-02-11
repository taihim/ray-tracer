from src.ray_tracer import CustomTuple, Ray, Sphere, intersect
from src.ray_tracer.matrix.transforms import Transform


def test_ray_translate():
    ray = Ray(CustomTuple(1, 2, 3), CustomTuple(0, 1, 0))
    matrix = Transform().translate(3, 4, 5)
    transformed_ray = ray.transform(matrix)

    assert transformed_ray.origin == CustomTuple(4, 6, 8)
    assert transformed_ray.direction == CustomTuple(0, 1, 0)
