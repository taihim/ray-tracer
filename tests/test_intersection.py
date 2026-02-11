from src.ray_tracer import Intersection, Sphere, intersections

def test_intersection_init() -> None:
    s1 = Sphere()
    i1 = Intersection(3.5, s1)

    assert i1.t == 3.5
    assert i1.object == s1

def test_intersection_aggregation() -> None:
    s1 = Sphere
    i1 = Intersection(1, s1)
    i2 = Intersection(2, s1)

    xs = intersections(i1, i2)
    assert len(xs) == 2
    assert xs[0].t == 1
    assert xs[1].t == 2


def test_intersection_str():
    s1 = Sphere()
    i1 = Intersection(3.5, s1)
    result = str(i1)
    assert "3.5" in result
    assert "Intersection object" in result
