from cannon import Environment, Projectile, tick
from ray_tracer import ColorTuple, CustomTuple

p1 = CustomTuple.point(0, 1, 0)
v1 = CustomTuple.vector(1, 1, 0)

gravity = CustomTuple.vector(0, -0.1, 0)
wind = CustomTuple.vector(-0.01, 0, 0)

projectile = Projectile(p1, v1)
environment = Environment(gravity, wind)

while projectile.position.y > 0:
    projectile = tick(environment, projectile)
    print(projectile.position)

c1 = ColorTuple(1, 2, 3)
c2 = ColorTuple(4, 5, 6)

print(c1)

print(c1 + c2)
print(c1 - c2)
print(c1 * 3)
print(c1.hadamard(c2))
