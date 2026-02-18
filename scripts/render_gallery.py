"""Render multiple sphere variants for the gallery."""
import math
import os
import subprocess
from multiprocessing import Pool
from typing import cast

from src.ray_tracer import Canvas, ColorTuple, CustomTuple, Ray, Sphere, hit, intersect
from src.ray_tracer.lights import lighting
from src.ray_tracer.lights.point import PointLight
from src.ray_tracer.material import Material
from src.ray_tracer.matrix.transforms import Transform
from src.ray_tracer.sphere import normal_at

CANVAS_PIXELS = 300
WALL_Z = 10
WALL_SIZE = 7
PIXEL_SIZE = WALL_SIZE / CANVAS_PIXELS
HALF = WALL_SIZE / 2

ray_origin = CustomTuple.point(0, 0, -5)
light = PointLight(CustomTuple(-10, 10, -10, 1), ColorTuple(1, 1, 1))

# Module-level sphere mutated before each Pool fork
s1: Sphere = Sphere()


def render_row(y: int) -> list[tuple[int, int, tuple[float, float, float]]]:
    """Render a single row of pixels."""
    results: list[tuple[int, int, tuple[float, float, float]]] = []
    world_y = HALF - PIXEL_SIZE * y
    for x in range(CANVAS_PIXELS):
        world_x = -HALF + PIXEL_SIZE * x
        position = CustomTuple.point(world_x, world_y, WALL_Z)
        r = Ray(ray_origin, (position - ray_origin).normalize())
        xs = intersect(r, s1)
        hit_result = hit(xs)
        if hit_result:
            point = Ray.position(r, hit_result.t)
            normal = normal_at(cast("Sphere", hit_result.object), point)
            eye = -r.direction
            color = lighting(cast("Sphere", hit_result.object).material, light, point, eye, normal)
            results.append((y, x, (color.red, color.green, color.blue)))
    return results


def render(sphere: Sphere, out_png: str) -> None:
    """Render a sphere and save the result as a PNG."""
    global s1
    s1 = sphere

    cv = Canvas(CANVAS_PIXELS, CANVAS_PIXELS, (0, 0, 0))
    with Pool() as pool:
        rows = pool.map(render_row, range(CANVAS_PIXELS))

    for row_results in rows:
        for y, x, color in row_results:
            cv.pixels[y][x] = ColorTuple(*color)

    ppm_path = out_png.replace(".png", ".ppm")
    Canvas.save(data=cv.canvas_to_ppm(), path=ppm_path)
    subprocess.run(["magick", ppm_path, out_png], check=True)
    os.remove(ppm_path)
    print(f"  saved {out_png}")


GALLERY = "gallery"

VARIANTS: list[tuple[str, str, Sphere]] = []


def make_sphere(
    color: tuple[float, float, float],
    transform: Transform | None = None,
    ambient: float = 0.1,
    diffuse: float = 0.9,
    specular: float = 0.9,
    shininess: float = 200.0,
) -> Sphere:
    s = Sphere()
    s.material = Material(ColorTuple(*color), ambient, diffuse, specular, shininess)
    if transform is not None:
        s.set_transform(transform)
    return s


variants: list[tuple[str, str, Sphere]] = [
    (
        "squash",
        "Squashed (scale Y×0.5)",
        make_sphere((1.0, 0.5, 0.1), Transform().scale(1.0, 0.5, 1.0)),
    ),
    (
        "wide_ellipsoid",
        "Wide ellipsoid (scale X×1.5, Y×0.5)",
        make_sphere((0.1, 0.8, 0.8), Transform().scale(1.5, 0.5, 1.0)),
    ),
    (
        "tilted_oval",
        "Tilted oval (rotate_z 45° + scale X×0.5)",
        make_sphere(
            (0.6, 0.1, 0.9),
            cast("Transform", Transform().rotate_z(math.pi / 4) * Transform().scale(0.5, 1.0, 1.0)),
        ),
    ),
    (
        "shear",
        "Shear (x∝y) + scale X×0.5",
        make_sphere(
            (0.9, 0.8, 0.1),
            cast("Transform", Transform().shear(1, 0, 0, 0, 0, 0) * Transform().scale(0.5, 1.0, 1.0)),
        ),
    ),
    (
        "matte",
        "Matte surface (specular≈0, shininess=10)",
        make_sphere((0.1, 0.7, 0.2), specular=0.05, shininess=10.0),
    ),
    (
        "shiny",
        "High-gloss surface (specular=1, shininess=400)",
        make_sphere((0.1, 0.3, 1.0), diffuse=0.4, specular=1.0, shininess=400.0),
    ),
]

if __name__ == "__main__":
    os.makedirs(GALLERY, exist_ok=True)
    for slug, label, sphere in variants:
        print(f"Rendering: {label}")
        render(sphere, f"{GALLERY}/{slug}.png")
    print("Done.")
