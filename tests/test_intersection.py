from src.ray_tracer import Intersection, Sphere

def test_intersection_init() -> None:
    s1 = Sphere()
    i1 = Intersection(3.5, s1)

    assert i1.t == 3.5
    assert i1.object == s1
