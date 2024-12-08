from ..utils import compare_float


class RTMatrix:
    """Class representing matrices used in the Raytracer."""

    def __init__(self, rows: int = 1, cols: int = 1) -> None:
        self.rows = rows
        self.cols = cols

        self.data: list[list[float]] = [[0.0] * cols for _ in range(rows)]

    def __repr__(self) -> str:
        """String representation of an RTMatrix object."""
        return f"RTMatrix Object(rows={self.rows}, columns={self.cols})"

    def __getitem__(self, index: int | tuple[int, int]) -> list[float] | float:
        """Access a row or specific element in the matrix."""
        if isinstance(index, int):
            return self.data[index]

        raise TypeError("Index should be an int or a tuple of two integers.")

    def __setitem__(self, index: int, value: list[float]) -> None:
        """Assign a value to a specific position in the matrix."""
        if isinstance(index, int):
            if len(value) == self.cols:
                self.data[index] = [float(val) for val in value]
            else:
                raise ValueError(f"Expected {self.cols} columns, got {len(value)}.")
        else:
            raise TypeError(f"Expected index of type Int, got {type(index)}.")


compare_float(1.1, 2.3)
m1 = RTMatrix(3, 3)
m1[2] = [0.67, 1, 0]
print(m1.data)
