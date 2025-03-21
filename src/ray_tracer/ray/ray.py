from src.ray_tracer.tuples import CustomTuple


class Ray:
    """Primitive Ray object for the Ray Tracer."""

    def __init__(self, origin: CustomTuple, direction: CustomTuple) -> None:
        self.origin = origin
        self.direction = direction
