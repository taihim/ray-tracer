from src.ray_tracer.tuples import ColorTuple


class Material:
    """Material class represents a material with color, ambient, diffuse, specular, and shininess properties."""

    def __init__(self, color: ColorTuple, ambient: float=0.1, diffuse: float=0.9, specular: float=0.9, shininess: float=200.0) -> None:
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
