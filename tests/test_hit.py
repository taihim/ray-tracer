from src.ray_tracer import Sphere, Intersection, intersections, hit

def test_hit_all_positive_t() -> None:
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = intersections(i2, i1)
    i = hit(xs)

    assert i == i1


def test_hit_some_negative_t() -> None:
    s = Sphere()
    i1 = Intersection(-1, s)
    i2 = Intersection(1, s)
    xs = intersections(i2, i1)
    i = hit(xs)

    assert i == i2

def test_hit_all_negative_t() -> None:
    s = Sphere()
    i1 = Intersection(-2, s)
    i2 = Intersection(-1, s)
    xs = intersections(i2, i1)
    i = hit(xs)

    assert i == None

def test_hit_lowest_t() -> None:
    s = Sphere()
    i1 = Intersection(5, s)
    i2 = Intersection(7, s)
    i3 = Intersection(-3, s)
    i4 = Intersection(2, s)
    xs = intersections(i1, i2, i3, i4)
    i = hit(xs)

    assert i == i4
