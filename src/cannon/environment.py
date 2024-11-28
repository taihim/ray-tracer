from ray_tracer.rt_tuple import CustomTuple


class Environment:
    """An environment object."""

    def __init__(self, gravity: CustomTuple, wind: CustomTuple):
        self.gravity = gravity
        self.wind = wind
