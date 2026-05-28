from src.ray_tracer.ray import Ray
from src.ray_tracer.world import World, intersect_world
from src.ray_tracer.lights import PointLight
from src.ray_tracer.tuples import ColorTuple, CustomTuple

def test_create_empty_world():
    w1 = World()

    assert w1.light == None
    assert w1.objects == []

def test_create_default_world():
    w1 = World.default_world()
    light = PointLight(CustomTuple(-10, 10, -10), ColorTuple(1, 1, 1))

    assert w1.light.position == light.position
    assert w1.light.intensity == light.intensity

def test_intersect_world():
    w1 = World.default_world()
    r1 = Ray(CustomTuple(0, 0, -5, 1), CustomTuple(0, 0, 1))

    xs = intersect_world(w1, r1)

    assert len(xs) == 4
    assert xs[0].t == 4
    assert xs[1].t == 4.5
    assert xs[2].t == 5.5
    assert xs[3].t == 6
    