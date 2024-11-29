from math import sqrt

from .utils import compare_float


# todo: refactor customTuple to an interface and make Vector, point and color inherit
class CustomTuple:
    """A custom tuple implementation for a ray tracer."""

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 0.0) -> None:
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        # w == 0 represents a vector, w == 1 is a point
        self.w = float(w)

    def __repr__(self) -> str:
        """Return string representation of the class."""
        return f"{"Vector" if compare_float(self.w, 0.0) else "Point"}(x={self.x}, y={self.y}, z={self.z}, w={self.w})"

    @staticmethod
    def point(x: float, y: float, z: float) -> "CustomTuple":
        """Construct and return a point."""
        if not isinstance(x, float | int) or not isinstance(y, float | int) or not isinstance(z, float | int):
            raise TypeError("CustomTuple only accepts integer or floating point values.")
        return CustomTuple(x, y, z, 1.0)

    @staticmethod
    def vector(x: float, y: float, z: float) -> "CustomTuple":
        """Construct and return a vector."""
        if not isinstance(x, float | int) or not isinstance(y, float | int) or not isinstance(z, float | int):
            raise TypeError("CustomTuple only accepts integer or floating point values.")
        return CustomTuple(x, y, z, 0.0)

    def __eq__(self, t2: object) -> bool:
        """Define equality comparison behaviour for CustomTuple."""
        if not isinstance(t2, CustomTuple):
            raise TypeError("Can only compare CustomTuples to a CustomTuple.")

        return (
            compare_float(self.x, t2.x)
            and compare_float(self.y, t2.y)
            and compare_float(self.z, t2.z)
            and compare_float(self.w, t2.w)
        )

    def __add__(self, t2: "CustomTuple") -> "CustomTuple":
        """Define addition behaviour for CustomTuple."""
        if not isinstance(t2, CustomTuple):
            raise TypeError(f"Unsupported operand of type {type(t2)}. Can only add CustomTuples to a CustomTuple.")

        if compare_float(self.w, 1.0) and compare_float(t2.w, 1.0):
            raise ValueError("Cannot add two points.")

        return CustomTuple(self.x + t2.x, self.y + t2.y, self.z + t2.z, self.w + t2.w)

    def __sub__(self, t2: "CustomTuple") -> "CustomTuple":
        """Define subtraction behaviour for CustomTuple."""
        if not isinstance(t2, CustomTuple):
            raise TypeError(
                f"Unsupported operand of type {type(t2)}. Can only subtract CustomTuples from a CustomTuple."
            )

        if compare_float(self.w, 0.0) and compare_float(t2.w, 1.0):
            raise ValueError("Cannot subtract a point from a vector.")

        return CustomTuple(self.x - t2.x, self.y - t2.y, self.z - t2.z, self.w - t2.w)

    def __neg__(self) -> "CustomTuple":
        """Define negation behaviour for a vector."""
        return CustomTuple.vector(-self.x, -self.y, -self.z)

    def __mul__(self, scalar: float) -> "CustomTuple":
        """Define scalar multiplication."""
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        self.w *= scalar

        return self

    def __truediv__(self, scalar: float) -> "CustomTuple":
        """Define scalar division."""
        self.x /= scalar
        self.y /= scalar
        self.z /= scalar
        self.w /= scalar

        return self

    # todo: find a better exception than ValueError
    def magnitude(self) -> float:
        """Calculate magnitude of the vector."""
        if compare_float(self.w, 0.0):
            return sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)
        raise ValueError("Can only calculate magnitude for vectors (w == 0).")

    def normalize(self) -> "CustomTuple":
        """Normalize the vector."""
        if compare_float(self.w, 0.0):
            mag = self.magnitude()
            self.x /= mag
            self.y /= mag
            self.z /= mag
            self.w /= mag
            return self
        raise ValueError("Can only normalize vectors (w == 0).")

    # dot product represents the cosine of the angle between unit vectors
    def dot(self, v2: "CustomTuple") -> float:
        """Compute dot product of two vectors."""
        if compare_float(self.w, 0.0) and compare_float(v2.w, 0.0):
            return (self.x * v2.x) + (self.y * v2.y) + (self.z * v2.z) + (self.w * v2.w)
        raise ValueError("Can only compute dot product for vectors.")

    # the new vector is perpendicular to both original vectors
    def cross(self, v2: "CustomTuple") -> "CustomTuple":
        """Compute cross product of two vectors."""
        if compare_float(self.w, 0.0) and compare_float(v2.w, 0.0):
            return CustomTuple.vector(
                ((self.y * v2.z) - (self.z * v2.y)),
                ((self.z * v2.x) - (self.x * v2.z)),
                ((self.x * v2.y) - (self.y * v2.x)),
            )
        raise ValueError("Can only compute cross product for vectors.")
