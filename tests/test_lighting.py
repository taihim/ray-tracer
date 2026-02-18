from math import sqrt

from src.ray_tracer.lights import PointLight, lighting
from src.ray_tracer.material import Material
from src.ray_tracer.tuples import ColorTuple, CustomTuple


def test_lighting_between():
    """Eye is between light and surface"""
    m = Material(ColorTuple(1, 1, 1), 0.1, 0.9, 0.9, 200.0)
    position = CustomTuple(0, 0, 0, 1)

    eye_vec = CustomTuple(0, 0, -1)
    normal_vec = CustomTuple(0, 0, -1)
    light = PointLight(CustomTuple(0, 0, -10, 1), ColorTuple(1, 1, 1))

    result = lighting(m, light, position, eye_vec, normal_vec)
    assert result == ColorTuple(1.9, 1.9, 1.9)


def test_lighting_45_degree():
    """Eye is at a 45 degree angle to surface"""
    m = Material(ColorTuple(1, 1, 1), 0.1, 0.9, 0.9, 200.0)
    position = CustomTuple(0, 0, 0, 1)

    eye_vec = CustomTuple(0, sqrt(2) / 2, -sqrt(2) / 2)
    normal_vec = CustomTuple(0, 0, -1)
    light = PointLight(CustomTuple(0, 0, -10, 1), ColorTuple(1, 1, 1))

    result = lighting(m, light, position, eye_vec, normal_vec)
    assert result == ColorTuple(1.0, 1.0, 1.0)


def test_lighting_45_degree_off():
    """Light is at a 45 degree angle to surface"""
    m = Material(ColorTuple(1, 1, 1), 0.1, 0.9, 0.9, 200.0)
    position = CustomTuple(0, 0, 0, 1)

    eye_vec = CustomTuple(0, 0, -1)
    normal_vec = CustomTuple(0, 0, -1)
    light = PointLight(CustomTuple(0, 10, -10, 1), ColorTuple(1, 1, 1))

    result = lighting(m, light, position, eye_vec, normal_vec)
    assert result == ColorTuple(0.7364, 0.7364, 0.7364)


def test_lighting_eye_in_path_of_reflection():
    """Light is at a 45 degree angle to surface and eye is in the path of the reflection"""
    m = Material(ColorTuple(1, 1, 1), 0.1, 0.9, 0.9, 200.0)
    position = CustomTuple(0, 0, 0, 1)

    eye_vec = CustomTuple(0, -sqrt(2) / 2, -sqrt(2) / 2)
    normal_vec = CustomTuple(0, 0, -1)
    light = PointLight(CustomTuple(0, 10, -10, 1), ColorTuple(1, 1, 1))

    result = lighting(m, light, position, eye_vec, normal_vec)
    assert result == ColorTuple(1.6364, 1.6364, 1.6364)


def test_lighting_reflection_away_from_eye():
    """Light is in front of surface, reflection vector points away from eye"""
    m = Material(ColorTuple(1, 1, 1), 0.1, 0.9, 0.9, 200.0)
    position = CustomTuple(0, 0, 0, 1)

    eye_vec = CustomTuple(0, 0, 1)
    normal_vec = CustomTuple(0, 0, -1)
    light = PointLight(CustomTuple(0, 0, -10, 1), ColorTuple(1, 1, 1))

    result = lighting(m, light, position, eye_vec, normal_vec)
    assert result == ColorTuple(1.0, 1.0, 1.0)


def test_lighting_light_behind_surface():
    """Light is at a 45 degree angle to surface and eye is in the path of the reflection"""
    m = Material(ColorTuple(1, 1, 1), 0.1, 0.9, 0.9, 200.0)
    position = CustomTuple(0, 0, 0, 1)

    eye_vec = CustomTuple(0, 0, -1)
    normal_vec = CustomTuple(0, 0, -1)
    light = PointLight(CustomTuple(0, 0, 10, 1), ColorTuple(1, 1, 1))

    result = lighting(m, light, position, eye_vec, normal_vec)
    assert result == ColorTuple(0.1, 0.1, 0.1)
