import math
import time
from multiprocessing import Pool
from typing import cast
from scripts.numba_test import render_image_numba
import numpy as np

from src.ray_tracer import Canvas, ColorTuple, CustomTuple, Ray, Sphere, hit, intersect
from src.ray_tracer.lights import lighting
from src.ray_tracer.lights.point import PointLight
from src.ray_tracer.matrix.transforms import Transform
from src.ray_tracer.sphere import normal_at

canvas_pixels = 800

ray_origin = CustomTuple.point(0, 0, -5)
s1 = Sphere()
s1.material.color = ColorTuple(1, 0, 0)
s1_inverse = s1.transform.inverse()

light_position = CustomTuple(-10, 10, -10, 1)
light_color = ColorTuple(1, 1, 1)
light = PointLight(light_position, light_color)

wall_z = 10
wall_size = 7
pixel_size = wall_size / canvas_pixels
half = wall_size / 2


def save_ppm_from_array(image, path):
    """Save image as PPM P3 (text) format with 70-char line wrapping."""
    h, w, _ = image.shape
    max_line_len = 70

    with open(path, "w") as f:
        f.write(f"P3\n{w} {h}\n255\n")
        for y in range(h):
            line = ""
            for x in range(w):
                r = max(0, min(255, int(image[y, x, 0] * 255)))
                g = max(0, min(255, int(image[y, x, 1] * 255)))
                b = max(0, min(255, int(image[y, x, 2] * 255)))
                for val in (r, g, b):
                    val_str = str(val)
                    if line and len(line) + 1 + len(val_str) > max_line_len:
                        f.write(line + "\n")
                        line = val_str
                    elif line:
                        line += " " + val_str
                    else:
                        line = val_str
            if line:
                f.write(line + "\n")


def save_ppm_p6(image, path):
    """Save image as PPM P6 (binary) format. Much faster than P3."""
    h, w, _ = image.shape
    np.clip(image, 0,1, out=image)
    image *= 255
    clamped = image.astype(np.uint8)
    with open(path, "wb") as f:
        f.write(f"P6\n{w} {h}\n255\n".encode())
        f.write(clamped.tobytes())

if __name__ == "__main__":
    # cv = Canvas(canvas_pixels, canvas_pixels, (0, 0, 0))

    mat = s1.material
    inv_np = np.array(s1.transform.inverse().transformation_matrix.data, dtype=np.float64)
    
    # render_row_numba(0, canvas_pixels, wall_size, half, wall_z, 
    #                 ray_origin.x, ray_origin.y, ray_origin.z, 
    #                 light.position.x, light.position.y, light.position.z,
    #                 light.intensity.red, light.intensity.green, light.intensity.blue,
    #                 mat.color.red, mat.color.green, mat.color.blue, mat.ambient, mat.diffuse, mat.specular, mat.shininess,
    #                 inv_np)


    render_image_numba(1, wall_size, half, wall_z, 
                    ray_origin.x, ray_origin.y, ray_origin.z, 
                    light.position.x, light.position.y, light.position.z,
                    light.intensity.red, light.intensity.green, light.intensity.blue,
                    mat.color.red, mat.color.green, mat.color.blue, mat.ambient, mat.diffuse, mat.specular, mat.shininess,
                    inv_np)
    start = time.perf_counter()

    image = render_image_numba(canvas_pixels, wall_size, half, wall_z, 
                    ray_origin.x, ray_origin.y, ray_origin.z, 
                    light.position.x, light.position.y, light.position.z,
                    light.intensity.red, light.intensity.green, light.intensity.blue,
                    mat.color.red, mat.color.green, mat.color.blue, mat.ambient, mat.diffuse, mat.specular, mat.shininess,
                    inv_np)
    print(f"render: {time.perf_counter() - start:.3f}s")
    # for y in range(canvas_pixels):
        # row = render_row_numba(y, canvas_pixels, wall_size, half, wall_z, 
        #             ray_origin.x, ray_origin.y, ray_origin.z, 
        #             light.position.x, light.position.y, light.position.z,
        #             light.intensity.red, light.intensity.green, light.intensity.blue,
        #             mat.color.red, mat.color.green, mat.color.blue, mat.ambient, mat.diffuse, mat.specular, mat.shininess,
        #             inv_np)
        # for x in range(canvas_pixels):
            # cv.pixels[y][x] = ColorTuple(row[x][0], row[x][1], row[x][2])    
    start = time.perf_counter()
    save_ppm_p6(image=image, path="./images/sphere_numba.ppm")
    print(f"save (P6): {time.perf_counter() - start:.3f}s")
