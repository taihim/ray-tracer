from src.ray_tracer.utils import compare_float


class CustomTuple:
    """A custom tuple implementation for a ray tracer."""

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 0.0) -> None:
        if w not in (0.0, 1.0):
            raise TypeError("CustomTuple only supports w wiht a value of 1 or 0.")

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
            raise TypeError("Can only add CustomTuples to a CustomTuple.")

        if compare_float(self.w, 1.0) and compare_float(t2.w, 1.0):
            raise ValueError("Cannot add two points.")

        return CustomTuple(self.x + t2.x, self.y + t2.y, self.z + t2.z, self.w + t2.w)

    def __sub__(self, t2: "CustomTuple") -> "CustomTuple":
        """Define subtraction behaviour for CustomTuple."""
        if not isinstance(t2, CustomTuple):
            raise TypeError("Can only subtract CustomTuples from a CustomTuple.")

        if compare_float(self.w, 0.0) and compare_float(t2.w, 1.0):
            raise ValueError("Cannot subtract a point from a vector.")

        return CustomTuple(self.x - t2.x, self.y - t2.y, self.z - t2.z, self.w - t2.w)


if __name__ == "__main__":
    t1 = CustomTuple.vector(1.2, 2.2, 3.2)
    t2 = CustomTuple.point(0, 2, 3)

    print(t1 + t2)
    print(t2 - t1)
