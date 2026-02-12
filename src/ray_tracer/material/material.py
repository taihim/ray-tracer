from src.ray_tracer.tuples import ColorTuple


class Material:
    """Material class represents a material with color, ambient, diffuse, specular, and shininess properties."""

    def __init__(self, color: ColorTuple, ambient: float, diffuse: float, specular: float, shininess: float) -> None:
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
