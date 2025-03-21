import math
from typing import cast

from src.ray_tracer import Canvas, ColorTuple, CustomTuple
from src.ray_tracer.matrix.transforms import Transform

cv = Canvas(500, 500, (0, 0, 0))

mid = 500 // 2
radius = mid // 2  # pixels. i.e the distance from origin(250, 250) to any time spot


origin = CustomTuple.point(0, 0, 0)
twelve = CustomTuple.point(0, 0, 1)

points = [twelve]
for hour in range(1, 12):
    rotation = Transform().rotate_y(hour * (math.pi / 6))
    hour_position = cast(CustomTuple, rotation * twelve)
    points.append(hour_position)


for point in points:
    point.x *= radius
    point.z *= radius

    point.x += mid
    point.z += mid

    cv.pixels[int(-point.z)][int(point.x)] = ColorTuple(1, 1, 1)

data = cv.canvas_to_ppm()
cv.save(data=data)
