from typing import Any

from ..utils import compare_float
from .custom_tuple import CustomTuple


class ColorTuple(CustomTuple):
    """Tuple representing a color."""

    def __init__(self, r: float, g: float, b: float) -> None:
        # w value for color is -1, this is an arbitrary choice
        super().__init__(r, g, b, -1)
        self.red = r
        self.green = g
        self.blue = b

    def __repr__(self) -> str:
        """Return string representation of the class."""
        return f"Color: (Red={self.red}, Green={self.green}, Blue={self.blue})"

    def __eq__(self, t2: object) -> bool:
        """Define equality comparison behaviour for CustomTuple."""
        if not isinstance(t2, ColorTuple):
            raise TypeError("Can only compare ColorTuples to a ColorTuple.")

        return (
            compare_float(self.red, t2.red)
            and compare_float(self.green, t2.green)
            and compare_float(self.blue, t2.blue)
        )

    def __add__(self, t2: "CustomTuple") -> "ColorTuple":
        """Define addition behaviour for CustomTuple."""
        if not isinstance(t2, ColorTuple):
            raise TypeError(f"Unsupported operand of type {type(t2)}. Can only add ColorTuples to a ColorTuple.")

        return ColorTuple(self.red + t2.red, self.green + t2.green, self.blue + t2.blue)

    def __sub__(self, t2: "CustomTuple") -> "ColorTuple":
        """Define subtraction behaviour for CustomTuple."""
        if not isinstance(t2, ColorTuple):
            raise TypeError(f"Unsupported operand of type {type(t2)}. Can only subtract ColorTuples from a ColorTuple.")

        return ColorTuple(self.red - t2.red, self.green - t2.green, self.blue - t2.blue)

    def __mul__(self, multiplier: float | Any) -> "ColorTuple":
        """Define scalar multiplication."""
        if isinstance(multiplier, float | int):
            self.red *= multiplier
            self.green *= multiplier
            self.blue *= multiplier
            return self

        if isinstance(multiplier, ColorTuple):
            return ColorTuple(self.red * multiplier.red, self.green * multiplier.green, self.blue * multiplier.blue)

        raise NotImplementedError
