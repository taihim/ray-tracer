import math
from typing import cast

from src.ray_tracer import Canvas, ColorTuple, CustomTuple
from src.ray_tracer.matrix.transforms import Transform

cv = Canvas(100, 100, (0, 0, 0))

mid = 100 // 2
radius = mid // 2  # pixels. i.e the distance from origin(50, 50) to any time spot


origin = CustomTuple.point(0, 0, 0)

data = cv.canvas_to_ppm()
cv.save(data=data, path="./images/sphere.ppm")
