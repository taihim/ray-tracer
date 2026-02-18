import math
from multiprocessing import Pool
from typing import cast

from src.ray_tracer import Canvas, ColorTuple, CustomTuple, Ray, Sphere, hit, intersect
from src.ray_tracer.lights import lighting
from src.ray_tracer.lights.point import PointLight
from src.ray_tracer.matrix.transforms import Transform
from src.ray_tracer.sphere import normal_at

canvas_pixels = 250

ray_origin = CustomTuple.point(0, 0, -5)
s1 = Sphere()
s1.material.color = ColorTuple(1, 0, 0)
s1.set_transform(Transform().scale(1, 0.95, 1))
# s1.set_transform(cast("Transform", Transform().shear(1, 0, 0, 0, 0, 0) * Transform().scale(0.5, 1, 1)))
# s1.set_transform(cast("Transform", Transform().rotate_z(math.pi / 4) * Transform().scale(0.5, 1, 1)))

light_position = CustomTuple(-10, 10, -10, 1)
light_color = ColorTuple(1, 1, 1)
light = PointLight(light_position, light_color)


wall_z = 10
wall_size = 7
pixel_size = wall_size / canvas_pixels
half = wall_size / 2


def render_row(y: int) -> list[tuple[int, int, tuple[float, float, float]]]:
    """Render a single row of pixels."""
    results: list[tuple[int, int, tuple[float, float, float]]] = []
    world_y = half - pixel_size * y
    for x in range(canvas_pixels):
        world_x = -half + pixel_size * x

        position = CustomTuple.point(world_x, world_y, wall_z)
        r = Ray(ray_origin, (position - ray_origin).normalize())
        xs = intersect(r, s1)

        hit_1 = hit(xs)
        if hit_1:
            point = Ray.position(r, hit_1.t)
            normal = normal_at(cast("Sphere", hit_1.object), point)
            eye = -r.direction
            # color = (1.0, 0.0, 0.0) if world_y > 0 else (1.0, 1.0, 1.0)
            color = lighting(cast("Sphere", hit_1.object).material, light, point, eye, normal)
            results.append((y, x, (color.red, color.green, color.blue)))

    return results


if __name__ == "__main__":
    cv = Canvas(canvas_pixels, canvas_pixels, (0, 0, 0))

    with Pool() as pool:
        rows = pool.map(render_row, range(canvas_pixels))

    for row_results in rows:
        for y, x, color in row_results:
            cv.pixels[y][x] = ColorTuple(*color)

    data = cv.canvas_to_ppm()
    Canvas.save(data=data, path="./images/sphere.ppm")
