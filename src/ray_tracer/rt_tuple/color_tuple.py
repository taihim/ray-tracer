from .custom_tuple import CustomTuple


class ColorTuple(CustomTuple):
    """Tuple representing a color."""

    def __init__(self, r: float, b: float, g: float) -> None:
        # w value for color is 3, this is an arbitrary choice
        super().__init__(r, b, g, -1)
        self.r = r
        self.b = b
        self.g = g

    def __repr__(self) -> str:
        """Return string representation of the class."""
        return f"Color: (Red={self.r}, Blue={self.b}, Green={self.g})"

    def __add__(self, t2: "CustomTuple") -> "ColorTuple":
        """Define addition behaviour for CustomTuple."""
        if not isinstance(t2, ColorTuple):
            raise TypeError(f"Unsupported operand of type {type(t2)}. Can only add ColorTuples to a ColorTuple.")

        return ColorTuple(self.x + t2.x, self.y + t2.y, self.z + t2.z)

    def __sub__(self, t2: "CustomTuple") -> "ColorTuple":
        """Define subtraction behaviour for CustomTuple."""
        if not isinstance(t2, ColorTuple):
            raise TypeError(f"Unsupported operand of type {type(t2)}. Can only subtract ColorTuples from a ColorTuple.")

        return ColorTuple(self.x - t2.x, self.y - t2.y, self.z - t2.z)

    def hadamard(self, c2: "ColorTuple") -> "ColorTuple":
        """Defines Hadamard product for two colors."""
        if not isinstance(c2, ColorTuple):
            raise TypeError(
                f"Unsupported operand of type {type(c2)}. Can only calculate Hadamard product for ColorTuples."
            )
        return ColorTuple(self.r * c2.r, self.b * c2.b, self.g * c2.g)
