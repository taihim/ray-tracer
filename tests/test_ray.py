from src.ray_tracer import CustomTuple, Ray, Sphere


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
    r1 = Ray(CustomTuple(2, 3, 4, 1), CustomTuple(1, 0, 0))
    s1 = Sphere()

    print(s1.id)
    assert 1==2