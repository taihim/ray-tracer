from src.ray_tracer.tuples import ColorTuple, CustomTuple


class PointLight:
    """A point light source."""

    def __init__(self, position: CustomTuple, intensity: ColorTuple) -> None:
        """Initialize a point light source.

        Args:
            position (CustomTuple): The position of the light source.
            intensity (ColorTuple): The intensity of the light source.
        """
        self.position = position
        self.intensity = intensity
