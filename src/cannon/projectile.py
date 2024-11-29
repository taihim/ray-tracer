from ray_tracer import CustomTuple


class Projectile:
    """A projectile object."""

    def __init__(self, position: CustomTuple, velocity: CustomTuple) -> None:
        self.position = position
        self.velocity = velocity
