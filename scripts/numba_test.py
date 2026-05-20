import numpy as np
from numba import njit
import time
import math


# @njit
# def dot_loop_numba(n):
#     total = 0.0
#     for _ in range(n):
#         total += 1.0 * 4.0 + 2.0 * 5.0 + 3.0 * 6.0
#     return total
# def dot_loop_python(n):
#     total = 0.0
#     for _ in range(n):
#         total += 1.0 * 4.0 + 2.0 * 5.0 + 3.0 * 6.0
#     return total
# n = 100_000_000
# # Warm up numba (first call compiles)
# dot_loop_numba(1)

# start = time.perf_counter()
# res1 = dot_loop_numba(n)
# print(f"numba:  {time.perf_counter() - start:.3f}s")
# print(res1)
# start = time.perf_counter()
# res2 = dot_loop_python(n)
# print(f"python: {time.perf_counter() - start:.3f}s")
# print(res2)


@njit
def dot(ax, ay, az, bx, by, bz):
    return ax * bx + ay * by + az * bz

@njit
def intersect_sphere(ox, oy, oz, dx, dy, dz, inv):
    new_ox = inv[0,0] * ox + inv[0, 1] * oy + inv[0, 2] * oz + inv[0,3]
    new_oy = inv[1,0] * ox + inv[1, 1] * oy + inv[1, 2] * oz + inv[1,3]
    new_oz = inv[2,0] * ox + inv[2, 1] * oy + inv[2, 2] * oz + inv[2,3]

    new_dirx = inv[0,0] * dx + inv[0, 1] * dy + inv[0, 2] * dz
    new_diry = inv[1,0] * dx + inv[1, 1] * dy + inv[1, 2] * dz
    new_dirz = inv[2,0] * dx + inv[2, 1] * dy + inv[2, 2] * dz

    new_origin = (new_ox, new_oy, new_oz) 

    # sphere_to_ray = new_origin - (0.0, 0.0, 0.0)
    sphere_to_ray = new_origin

    a = dot(new_dirx, new_diry, new_dirz, new_dirx, new_diry, new_dirz)
    b = 2 * dot(new_dirx, new_diry, new_dirz, sphere_to_ray[0], sphere_to_ray[1], sphere_to_ray[2])
    c = dot(sphere_to_ray[0], sphere_to_ray[1], sphere_to_ray[2], sphere_to_ray[0], sphere_to_ray[1], sphere_to_ray[2]) - 1

    discriminant = (b**2) - (4 * a * c)

    if discriminant < 0:
        return (-1.0, -1.0)

    t1 = float((-b - math.sqrt(discriminant)) / (2 * a))
    t2 = float((-b + math.sqrt(discriminant)) / (2 * a))

    return t1, t2

@njit
def normalize(x, y, z, w=0):
    mag = math.sqrt(x**2 + y**2 + z**2 + w**2)

    x /= mag
    y /= mag
    z /= mag

    return (x, y, z)

@njit
def normal_at_sphere(px, py, pz, inv):
    opx = inv[0,0] * px + inv[0,1] * py + inv[0,2] * pz + inv[0, 3]
    opy = inv[1,0] * px + inv[1,1] * py + inv[1,2] * pz + inv[1, 3]
    opz = inv[2,0] * px + inv[2,1] * py + inv[2,2] * pz + inv[2, 3]

    wnx = inv[0,0] * opx + inv[1,0] * opy + inv[2,0] * opz 
    wny = inv[0,1] * opx + inv[1,1] * opy + inv[2,1] * opz
    wnz = inv[0,2] * opx + inv[1,2] * opy + inv[2,2] * opz

    return normalize(wnx, wny, wnz)


@njit
def lighting_phong(mat_r, mat_g, mat_b, mat_ambient, mat_diffuse, mat_specular, mat_shininess, lx, ly, lz, li_r, li_g, li_b, px, py, pz, ex, ey, ez, nx, ny, nz):
    eff_r = mat_r * li_r
    eff_g = mat_g * li_g
    eff_b = mat_b * li_b

    ldx, ldy, ldz = normalize(lx - px, ly - py, lz - pz)
    
    amb_r = eff_r * mat_ambient
    amb_g = eff_g * mat_ambient
    amb_b = eff_b * mat_ambient

    light_dot_normal = dot(ldx, ldy, ldz, nx, ny, nz)
    
    if light_dot_normal < 0:
        return amb_r, amb_g, amb_b
    
    diff_r = eff_r * mat_diffuse * light_dot_normal
    diff_g = eff_g * mat_diffuse * light_dot_normal
    diff_b = eff_b * mat_diffuse * light_dot_normal

    neg_ldx, neg_ldy, neg_ldz = -ldx, -ldy, -ldz
    d = dot(neg_ldx, neg_ldy, neg_ldz, nx, ny, nz)
    ref_x = neg_ldx - nx * 2.0 * d
    ref_y = neg_ldy - ny * 2.0 * d
    ref_z = neg_ldz - nz * 2.0 * d

    reflect_dot_eye = dot(ref_x, ref_y, ref_z, ex, ey, ez)

    if reflect_dot_eye <= 0:
        return amb_r + diff_r, amb_g + diff_g, amb_b + diff_b

    factor = reflect_dot_eye ** mat_shininess
    spec_r = li_r * mat_specular * factor
    spec_g = li_g * mat_specular * factor
    spec_b = li_b * mat_specular * factor
    
    return amb_r + diff_r + spec_r, amb_g + diff_g + spec_g, amb_b + diff_b + spec_b 

# def reflect(self, normal: "CustomTuple") -> "CustomTuple":
#         """Reflect a vector about a normal vector."""
#         if compare_float(self.w, 0.0) and compare_float(normal.w, 0.0):
#             return self - (normal * 2 * self.dot(normal))
#         raise ValueError("Can only reflect vectors.")




# @njit
# def lighting_phong(
#     # material: color rgb, ambient, diffuse, specular, shininess
#     mat_r, mat_g, mat_b, mat_ambient, mat_diffuse, mat_specular, mat_shininess,
#     # light: position xyz, intensity rgb
#     lx, ly, lz, li_r, li_g, li_b,
#     # hit point, eye vector, normal vector
#     px, py, pz, ex, ey, ez, nx, ny, nz,
# ):
#     # effective_color = material.color * light.intensity
#     eff_r = mat_r * li_r
#     eff_g = mat_g * li_g
#     eff_b = mat_b * li_b
#     # light direction
#     ldx, ldy, ldz = normalize(lx - px, ly - py, lz - pz)
#     # ambient
#     amb_r = eff_r * mat_ambient
#     amb_g = eff_g * mat_ambient
#     amb_b = eff_b * mat_ambient
#     light_dot_normal = dot(ldx, ldy, ldz, nx, ny, nz)
#     if light_dot_normal < 0:
#         return amb_r, amb_g, amb_b
#     # diffuse
#     dif_r = eff_r * mat_diffuse * light_dot_normal
#     dif_g = eff_g * mat_diffuse * light_dot_normal
#     dif_b = eff_b * mat_diffuse * light_dot_normal
#     # reflect(-light_vec, normal)
#     # reflect formula: incoming - normal * 2 * dot(incoming, normal)
#     neg_ldx, neg_ldy, neg_ldz = -ldx, -ldy, -ldz
#     d = dot(neg_ldx, neg_ldy, neg_ldz, nx, ny, nz)
#     ref_x = neg_ldx - nx * 2.0 * d
#     ref_y = neg_ldy - ny * 2.0 * d
#     ref_z = neg_ldz - nz * 2.0 * d
#     reflect_dot_eye = dot(ref_x, ref_y, ref_z, ex, ey, ez)
#     if reflect_dot_eye <= 0:
#         return amb_r + dif_r, amb_g + dif_g, amb_b + dif_b
#     factor = reflect_dot_eye ** mat_shininess
#     spec_r = li_r * mat_specular * factor
#     spec_g = li_g * mat_specular * factor
#     spec_b = li_b * mat_specular * factor
#     return amb_r + dif_r + spec_r, amb_g + dif_g + spec_g, amb_b + dif_b + spec_b









from src.ray_tracer import CustomTuple, Ray, Sphere, intersect, ColorTuple
import numpy as np

# Set up a simple test: ray pointing at a unit sphere
origin = CustomTuple.point(0, 0, -5)
direction = CustomTuple.vector(0, 0, 1)
ray = Ray(origin, direction)
sphere = Sphere()
# Your existing code
inv = sphere.transform.inverse()

xs = intersect(ray, sphere, inv)
print(f"existing: t1={xs[0].t}, t2={xs[1].t}")
# Numba version -- same inputs as raw floats
inv_np = np.array(inv.transformation_matrix.data, dtype=np.float64)  # 4x4 numpy array
t1, t2 = intersect_sphere(0.0, 0.0, -5.0, 0.0, 0.0, 1.0, inv_np)
print(f"numba:    t1={t1}, t2={t2}")
#You should get t1=4.0, t2=6.0 from both.
#Then try a transformed sphere to exercise the matrix path:

from src.ray_tracer.matrix.transforms import Transform
from src.ray_tracer.sphere import normal_at
from typing import cast

sphere2 = Sphere()
sphere2.set_transform(Transform().scale(2.0, 2.0, 2.0))
inv2 = sphere2.transform.inverse()
xs2 = intersect(ray, sphere2, inv2)
print(f"existing scaled: t1={xs2[0].t}, t2={xs2[1].t}")
inv2_np = np.array(inv2.transformation_matrix.data, dtype=np.float64)
t1, t2 = intersect_sphere(0.0, 0.0, -5.0, 0.0, 0.0, 1.0, inv2_np)
print(f"numba scaled:    t1={t1}, t2={t2}")

# ── normal_at_sphere tests ──────────────────────────────────────────

EPS = 1e-5

def check_normal(label, sphere, point_xyz, inv_np):
    px, py, pz = point_xyz
    point = CustomTuple.point(px, py, pz)

    # existing
    existing = normal_at(sphere, point)

    # numba
    nx, ny, nz = normal_at_sphere(px, py, pz, inv_np)

    dx = abs(existing.x - nx)
    dy = abs(existing.y - ny)
    dz = abs(existing.z - nz)
    ok = dx < EPS and dy < EPS and dz < EPS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}")
    print(f"    existing: ({existing.x:.6f}, {existing.y:.6f}, {existing.z:.6f})")
    print(f"    numba:    ({nx:.6f}, {ny:.6f}, {nz:.6f})")

print("\n── normal_at_sphere tests ──")

# Test 1: unit sphere, normal on +x axis
s = Sphere()
inv_np = np.array(s.transform.inverse().transformation_matrix.data, dtype=np.float64)
check_normal("unit sphere, +x axis", s, (1.0, 0.0, 0.0), inv_np)

# Test 2: unit sphere, normal on +y axis
check_normal("unit sphere, +y axis", s, (0.0, 1.0, 0.0), inv_np)

# Test 3: unit sphere, normal on +z axis
check_normal("unit sphere, +z axis", s, (0.0, 0.0, 1.0), inv_np)

# Test 4: unit sphere, normal at non-axial point
v = math.sqrt(3) / 3
check_normal("unit sphere, diagonal", s, (v, v, v), inv_np)

# Test 5: translated sphere
s_trans = Sphere()
s_trans.set_transform(Transform().translate(0.0, 1.0, 0.0))
inv_trans_np = np.array(s_trans.transform.inverse().transformation_matrix.data, dtype=np.float64)
check_normal("translated sphere", s_trans, (0.0, 1.70711, -0.70711), inv_trans_np)

# Test 6: scaled + rotated sphere (non-uniform transform)
s_xform = Sphere()
s_xform.set_transform(cast("Transform", Transform().scale(1.0, 0.5, 1.0) * Transform().rotate_z(math.pi / 5)))
inv_xform_np = np.array(s_xform.transform.inverse().transformation_matrix.data, dtype=np.float64)
check_normal("scaled+rotated sphere", s_xform, (0.0, math.sqrt(2) / 2, -math.sqrt(2) / 2), inv_xform_np)

# ── lighting_phong tests ────────────────────────────────────────────

from src.ray_tracer.lights import lighting
from src.ray_tracer.lights.point import PointLight
from src.ray_tracer.material import Material


def check_lighting(label, mat, light, position, eye_vec, normal_vec):
    # existing
    existing = lighting(mat, light, position, eye_vec, normal_vec)

    # numba
    nr, ng, nb = lighting_phong(
        mat.color.red, mat.color.green, mat.color.blue,
        mat.ambient, mat.diffuse, mat.specular, mat.shininess,
        light.position.x, light.position.y, light.position.z,
        light.intensity.red, light.intensity.green, light.intensity.blue,
        position.x, position.y, position.z,
        eye_vec.x, eye_vec.y, eye_vec.z,
        normal_vec.x, normal_vec.y, normal_vec.z,
    )

    dr = abs(existing.red - nr)
    dg = abs(existing.green - ng)
    db = abs(existing.blue - nb)
    ok = dr < EPS and dg < EPS and db < EPS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}")
    print(f"    existing: ({existing.red:.6f}, {existing.green:.6f}, {existing.blue:.6f})")
    print(f"    numba:    ({nr:.6f}, {ng:.6f}, {nb:.6f})")


print("\n── lighting_phong tests ──")

m = Material(ColorTuple(1, 1, 1), 0.1, 0.9, 0.9, 200.0)

# Test 1: eye between light and surface (straight on)
check_lighting(
    "eye between light and surface",
    m,
    PointLight(CustomTuple.point(0, 0, -10), ColorTuple(1, 1, 1)),
    CustomTuple.point(0, 0, 0),
    CustomTuple.vector(0, 0, -1),
    CustomTuple.vector(0, 0, -1),
)

# Test 2: eye offset 45 degrees
check_lighting(
    "eye offset 45 degrees",
    m,
    PointLight(CustomTuple.point(0, 0, -10), ColorTuple(1, 1, 1)),
    CustomTuple.point(0, 0, 0),
    CustomTuple.vector(0, math.sqrt(2) / 2, -math.sqrt(2) / 2),
    CustomTuple.vector(0, 0, -1),
)

# Test 3: light offset 45 degrees
check_lighting(
    "light offset 45 degrees",
    m,
    PointLight(CustomTuple.point(0, 10, -10), ColorTuple(1, 1, 1)),
    CustomTuple.point(0, 0, 0),
    CustomTuple.vector(0, 0, -1),
    CustomTuple.vector(0, 0, -1),
)

# Test 4: eye in path of reflection vector
check_lighting(
    "eye in reflection path",
    m,
    PointLight(CustomTuple.point(0, 10, -10), ColorTuple(1, 1, 1)),
    CustomTuple.point(0, 0, 0),
    CustomTuple.vector(0, -math.sqrt(2) / 2, -math.sqrt(2) / 2),
    CustomTuple.vector(0, 0, -1),
)

# Test 5: light behind surface
check_lighting(
    "light behind surface",
    m,
    PointLight(CustomTuple.point(0, 0, 10), ColorTuple(1, 1, 1)),
    CustomTuple.point(0, 0, 0),
    CustomTuple.vector(0, 0, -1),
    CustomTuple.vector(0, 0, -1),
)

# Test 6: non-default material with colored light
check_lighting(
    "colored material + colored light",
    Material(ColorTuple(0.8, 0.2, 0.1), 0.2, 0.7, 0.5, 50.0),
    PointLight(CustomTuple.point(-10, 10, -10), ColorTuple(0.9, 0.9, 0.7)),
    CustomTuple.point(0, 0, 0),
    CustomTuple.vector(0, 0, -1),
    CustomTuple.vector(0, 0, -1),
)