from .environment import Environment
from .projectile import Projectile


def tick(env: Environment, proj: Projectile) -> Projectile:
    """Simulates a unit of time passing for the projectile."""
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind

    return Projectile(position, velocity)
