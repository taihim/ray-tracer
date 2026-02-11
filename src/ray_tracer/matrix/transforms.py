import math
from typing import Union, cast

from src.ray_tracer.matrix import RTMatrix
from src.ray_tracer.tuples import CustomTuple


class Transform:
    """Base Transform class for the ray tracer."""

    def __init__(self, dim: int = 4) -> None:
        self.dims = (dim, dim)
        self.transformation_matrix: RTMatrix = RTMatrix.identity(self.dims[0], self.dims[1])

    def translate(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> "Transform":
        """Create and return a translation matrix."""
        translation_matrix = RTMatrix.identity(self.dims[0], self.dims[0])
        translation_matrix[0][3] = x
        translation_matrix[1][3] = y
        translation_matrix[2][3] = z

        self.transformation_matrix = cast("RTMatrix", translation_matrix * self.transformation_matrix)

        return self

    def scale(self, x: float = 1.0, y: float = 1.0, z: float = 1.0) -> "Transform":
        """Create and return a scaling matrix."""
        scaling_matrix = RTMatrix.identity(self.dims[0], self.dims[1])
        scaling_matrix[0][0] = x
        scaling_matrix[1][1] = y
        scaling_matrix[2][2] = z

        self.transformation_matrix = cast("RTMatrix", scaling_matrix * self.transformation_matrix)

        return self

    def rotate_x(self, rad: float) -> "Transform":
        """Create and return a rotation matrix for the x axis."""
        rotation_matrix = RTMatrix.identity(self.dims[0], self.dims[0])

        rotation_matrix[1][1] = math.cos(rad)
        rotation_matrix[1][2] = -math.sin(rad)
        rotation_matrix[2][1] = math.sin(rad)
        rotation_matrix[2][2] = math.cos(rad)

        self.transformation_matrix = cast("RTMatrix", rotation_matrix * self.transformation_matrix)

        return self

    def rotate_y(self, rad: float) -> "Transform":
        """Create and return a rotation matrix for the y axis."""
        rotation_matrix = RTMatrix.identity(self.dims[0], self.dims[0])

        rotation_matrix[0][0] = math.cos(rad)
        rotation_matrix[0][2] = math.sin(rad)
        rotation_matrix[2][0] = -math.sin(rad)
        rotation_matrix[2][2] = math.cos(rad)

        self.transformation_matrix = cast("RTMatrix", rotation_matrix * self.transformation_matrix)

        return self

    def rotate_z(self, rad: float) -> "Transform":
        """Create and return a rotation matrix for the z axis."""
        rotation_matrix = RTMatrix.identity(self.dims[0], self.dims[0])

        rotation_matrix[0][0] = math.cos(rad)
        rotation_matrix[0][1] = -math.sin(rad)
        rotation_matrix[1][0] = math.sin(rad)
        rotation_matrix[1][1] = math.cos(rad)

        self.transformation_matrix = cast("RTMatrix", rotation_matrix * self.transformation_matrix)

        return self

    def shear(self, x_y: float, x_z: float, y_x: float, y_z: float, z_x: float, z_y: float) -> "Transform":
        """Create and return a shear matrix."""
        shear_matrix = RTMatrix.identity(self.dims[0], self.dims[0])

        shear_matrix[0][1] = x_y
        shear_matrix[0][2] = x_z
        shear_matrix[1][0] = y_x
        shear_matrix[1][2] = y_z
        shear_matrix[2][0] = z_x
        shear_matrix[2][1] = z_y

        self.transformation_matrix = cast("RTMatrix", shear_matrix * self.transformation_matrix)

        return self

    def __mul__(
        self, multiplier: Union[CustomTuple, "Transform", RTMatrix]
    ) -> Union["Transform", RTMatrix, CustomTuple]:
        """__mul__ implementation for Transform objects."""
        if isinstance(multiplier, Transform):
            self.transformation_matrix = cast("RTMatrix", self.transformation_matrix * multiplier.transformation_matrix)
            return self
        return self.transformation_matrix * multiplier

    def __rmul__(
        self, multiplicand: Union[CustomTuple, "Transform", RTMatrix]
    ) -> Union["Transform", RTMatrix, CustomTuple]:
        """__rmul__ implementation for Transform objects."""
        if isinstance(multiplicand, Transform):
            self.transformation_matrix = cast(
                "RTMatrix", self.transformation_matrix * multiplicand.transformation_matrix
            )
            return self
        return self.transformation_matrix * multiplicand

    def inverse(self) -> "Transform":
        """Calculate reverse transformation matrix."""
        result = Transform(self.dims[0])
        result.transformation_matrix = self.transformation_matrix.inverse()

        return result
