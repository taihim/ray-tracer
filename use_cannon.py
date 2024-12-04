from src.cannon import Environment, Projectile, tick
from src.ray_tracer import Canvas, ColorTuple, CustomTuple

cv = Canvas(550, 900, (0, 0, 0))
p1 = CustomTuple.point(0, 1, 0)
p2 = CustomTuple.point(1, 0.5, 0)
v1 = CustomTuple.vector(1, 1.8, 0).normalize() * 11.25
v2 = CustomTuple.vector(1, 1, 0).normalize() * 15.25
c1 = ColorTuple(0, 0, 0)

gravity = CustomTuple.vector(0, -0.1, 0)
wind = CustomTuple.vector(-0.01, 0, 0)

projectile = Projectile(p1, v1)
projectile2 = Projectile(p2, v2)

environment = Environment(gravity, wind)


print(cv.width)
print(cv.height)
print(projectile.position)
cv.pixels[-(int(projectile.position.y) + 1)][int(projectile.position.x)] = ColorTuple(1, 1, 1)
while projectile.position.y > 0:
    projectile = tick(environment, projectile)
    if int(projectile.position.x) >= cv.width or int(projectile.position.y) >= cv.height:
        print("yes", projectile.position, cv.width, cv.height)
        continue
    else:
        cv.pixels[-(int(projectile.position.y + 1))][int(projectile.position.x)] = ColorTuple(1, 1, 1)

while projectile2.position.y > 0:
    projectile2 = tick(environment, projectile2)
    if int(projectile2.position.x) >= cv.width or int(projectile2.position.y) >= cv.height:
        print("yes", projectile2.position, cv.width, cv.height)
        continue
    else:
        cv.pixels[-(int(projectile2.position.y + 1))][int(projectile2.position.x)] = ColorTuple(1, 1, 1)


data = cv.canvas_to_ppm()
cv.save(data=data)
