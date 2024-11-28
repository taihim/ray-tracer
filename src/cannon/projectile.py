from ray_tracer.rt_tuple import CustomTuple


class Projectile:
    """A projectile object."""

    def __init__(self, position: CustomTuple, velocity: CustomTuple):
        self.position = position
        self.velocity = velocity
