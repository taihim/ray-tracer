from src.ray_tracer import Canvas, ColorTuple, CustomTuple, Ray, Sphere, hit, intersect

canvas_pixels = 200
cv = Canvas(canvas_pixels, canvas_pixels, (0, 0, 0))

mid = canvas_pixels // 2
radius = mid // 2  # pixels. i.e the distance from origin(50, 50) to any time spot


origin = CustomTuple.point(0, 0, 0)

ray_origin = CustomTuple.point(0, 0, -5)
ray_direction = CustomTuple.point(1, 0, 0)
s1 = Sphere()

wall_z = 10
wall_size = 7

pixel_size = wall_size / canvas_pixels

half = wall_size / 2


for y in range(canvas_pixels):
    world_y = half - pixel_size * y
    for x in range(canvas_pixels):
        world_x = -half + pixel_size * x

        position = CustomTuple.point(world_x, world_y, wall_z)
        r = Ray(ray_origin, (position - ray_origin).normalize())
        xs = intersect(r, s1)

        if hit(xs):
            cv.pixels[y][x] = ColorTuple(1, 0, 0)

data = cv.canvas_to_ppm()
cv.save(data=data, path="./images/sphere.ppm")
