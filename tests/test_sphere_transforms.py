from src.ray_tracer import CustomTuple, Ray, Sphere, intersect
from src.ray_tracer.matrix.transforms import Transform


def test_sphere_default_transform():
    sphere = Sphere()
    assert sphere.transform.transformation_matrix == Transform().transformation_matrix


def test_sphere_transform_set():
    sphere = Sphere()
    transform = Transform().translate(2, 3, 4)
    sphere.set_transform(transform)
    assert sphere.transform == transform


def test_sphere_transform_scale_intersection():
    sphere = Sphere()
    transform = Transform().scale(2, 2, 2)
    sphere.set_transform(transform)
    ray = Ray(CustomTuple(0, 0, -5, 1), CustomTuple(0, 0, 1))
    xs = intersect(ray, sphere)
    assert len(xs) == 2
    assert xs[0].t == 3
    assert xs[1].t == 7


def test_sphere_transform_translate_intersection():
    sphere = Sphere()
    transform = Transform().translate(5, 0, 0)
    sphere.set_transform(transform)
    ray = Ray(CustomTuple(0, 0, -5, 1), CustomTuple(0, 0, 1))
    xs = intersect(ray, sphere)
    assert len(xs) == 0
