from src.ray_tracer import CustomTuple, Ray, Sphere
from src.ray_tracer.ray.ray import intersect


def test_ray_init() -> None:
    r1 = Ray(CustomTuple(1, 2, 3, 1), CustomTuple(4, 5, 6))

    assert r1.origin == CustomTuple(1, 2, 3, 1)
    assert r1.direction == CustomTuple(4, 5, 6)

def test_ray_position() -> None:
    r1 = Ray(CustomTuple(2, 3, 4, 1), CustomTuple(1, 0, 0))

    assert Ray.position(r1, 0) == CustomTuple(2, 3, 4, 1)
    assert Ray.position(r1, 1) == CustomTuple(3, 3, 4, 1)
    assert Ray.position(r1, -1) == CustomTuple(1, 3, 4, 1)
    assert Ray.position(r1, 2.5) == CustomTuple(4.5, 3, 4, 1)

def test_ray_sphere_intersection() -> None:
    r1 = Ray(CustomTuple(0, 0, -5, 1), CustomTuple(0, 0, 1))
    s1 = Sphere()

    intersections = intersect(r1, s1)
    assert len(intersections) == 2
    assert intersections[0].t == 4.0
    assert intersections[1].t == 6.0

def test_ray_sphere_intersection_tangent() -> None:
    r1 = Ray(CustomTuple(0, 1, -5, 1), CustomTuple(0, 0, 1))
    s1 = Sphere()

    intersections = intersect(r1, s1)
    assert len(intersections) == 2
    assert intersections[0].t == 5.0
    assert intersections[1].t == 5.0

def test_ray_sphere_intersection_miss() -> None:
    r1 = Ray(CustomTuple(0, 2, -5, 1), CustomTuple(0, 0, 1))
    s1 = Sphere()

    intersections = intersect(r1, s1)
    assert len(intersections) == 0

def test_ray_spehere_intersection_inside() -> None:
    r1 = Ray(CustomTuple(0, 0, 0, 1), CustomTuple(0, 0, 1))
    s1 = Sphere()

    intersections = intersect(r1, s1)
    assert len(intersections) == 2
    assert intersections[0].t == -1.0
    assert intersections[1].t == 1.0

def test_ray_spehere_intersection_behind() -> None:
    r1 = Ray(CustomTuple(0, 0, 5, 1), CustomTuple(0, 0, 1))
    s1 = Sphere()

    intersections = intersect(r1, s1)
    assert len(intersections) == 2
    assert intersections[0].t == -6.0
    assert intersections[1].t == -4.0

def test_intersection_objects() -> None:
    r1 = Ray(CustomTuple(0, 0, -5, 1), CustomTuple(0, 0, 1))
    s1 = Sphere()

    xs = intersect(r1, s1)
    assert len(xs) == 2
    assert xs[0].object == s1
    assert xs[1].object == s1
    