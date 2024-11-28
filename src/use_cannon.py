from cannon import Environment, Projectile, tick
from ray_tracer import CustomTuple

p1 = CustomTuple.point(0, 1, 0)
v1 = CustomTuple.vector(1, 1, 0)

gravity = CustomTuple.vector(0, -0.1, 0)
wind = CustomTuple.vector(-0.01, 0, 0)

projectile = Projectile(p1, v1)
environment = Environment(gravity, wind)

while projectile.position.y > 0:
    projectile = tick(environment, projectile)
    print(projectile.position)
