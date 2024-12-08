from src.cannon import Environment, Projectile, tick
from src.ray_tracer import Canvas, ColorTuple, CustomTuple

cv = Canvas(550, 900, (0, 0, 0))
p1 = CustomTuple.point(0, 0, 0)
p2 = CustomTuple.point(cv.width - 1, 0, 0)
v1 = CustomTuple.vector(1, 1.8, 0).normalize() * 11.25
v2 = CustomTuple.vector(-1, 1.8, 0).normalize() * 11.25
c1 = ColorTuple(0, 0, 0)

gravity = CustomTuple.vector(0, -0.1, 0)
wind = CustomTuple.vector(-0.01, 0, 0)

projectile = Projectile(p1, v1)
projectile2 = Projectile(p2, v2)

environment = Environment(gravity, wind)

count = 0
cv.pixels[-(int(projectile.position.y) + 1)][int(projectile.position.x)] = ColorTuple(1, 1, 1)
cv.pixels[-(int(projectile2.position.y + 1))][int(projectile2.position.x)] = ColorTuple(1, 1, 1)

while projectile.position.y >= 0 and projectile2.position.y >= 0:
    projectile = tick(environment, projectile)
    projectile2 = tick(environment, projectile2)

    if 0 <= int(projectile.position.x) < cv.width and 0 <= int(projectile.position.y) < cv.height:
        cv.pixels[-(int(projectile.position.y + 1))][int(projectile.position.x)] = ColorTuple(1, 1, 1)

    if 0 <= int(projectile2.position.x) < cv.width and 0 <= int(projectile2.position.y) < cv.height:
        cv.pixels[-(int(projectile2.position.y + 1))][int(projectile2.position.x)] = ColorTuple(1, 1, 1)

    data = cv.canvas_to_ppm()
    cv.save(data=data, path=f"./images/canvas_{count}.ppm")
    count += 1

data = cv.canvas_to_ppm()
cv.save(data=data)
