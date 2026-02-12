from typing import cast
from uuid import uuid4

from src.ray_tracer.material import Material
from src.ray_tracer.matrix.transforms import Transform
from src.ray_tracer.tuples import ColorTuple, CustomTuple


# for now we assume all spheres are centered at the origin and are unit sphere (radius of 1)
class Sphere:
    """A sphere object."""

    def __init__(
        self,
        radius: float = 1.0,
    ) -> None:
        self.id = uuid4()
        self.origin = CustomTuple(0, 0, 0, 1)  # centered at origin
        self.radius = radius

        self.material = Material(ColorTuple(1, 1, 1), 0.1, 0.9, 0.9, 200.0)
        self.transform = Transform()

    def set_transform(self, transform: Transform) -> None:
        """Set the transform of the sphere."""
        self.transform = transform

    def set_material(self, material: Material) -> None:
        """Set the material of the sphere."""
        self.material = material


def normal_at(sphere: "Sphere", world_point: CustomTuple) -> CustomTuple:
    """Calculate the normal vector at a given point on the sphere.

    Args:
        sphere (Sphere): The sphere object.
        world_point (CustomTuple): The point on the sphere.

    Returns:
        CustomTuple: The normal vector at the given point.
    """
    object_point = cast("CustomTuple", sphere.transform.transformation_matrix.inverse() * world_point)
    object_normal = object_point - CustomTuple(0, 0, 0, 1)

    world_normal = cast("CustomTuple", sphere.transform.transformation_matrix.inverse().transpose() * object_normal)
    world_normal.w = 0

    return world_normal.normalize()
