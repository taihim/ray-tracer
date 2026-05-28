from src.ray_tracer.world import World
from src.ray_tracer.lights import PointLight
from src.ray_tracer.tuples import ColorTuple, CustomTuple

def test_create_empty_world():
    w1 = World()

    assert w1.light == None
    assert w1.objects == None

def test_create_default_world():
    w1 = World.default_world()
    light = PointLight(CustomTuple(-10, 10, -10), ColorTuple(1, 1, 1))

    assert w1.light.position == light.position
    assert w1.light.intensity == light.intensity