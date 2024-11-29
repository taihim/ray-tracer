from ray_tracer import CustomTuple


class Environment:
    """An environment object."""

    def __init__(self, gravity: CustomTuple, wind: CustomTuple) -> None:
        self.gravity = gravity
        self.wind = wind
