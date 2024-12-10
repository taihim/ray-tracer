from typing import overload

from src.ray_tracer.utils import compare_float


class RTMatrix:
    """Class representing matrices used in the Raytracer."""

    def __init__(self, rows: int = 1, cols: int = 1, matrix: list[list[float]] | None = None) -> None:
        if matrix:
            if not isinstance(matrix, list) or not isinstance(matrix[0], list):
                raise TypeError(f"Expected both rows and cols to be lists, got {(type(matrix), type(matrix[0]))}.")
            self.rows = len(matrix)
            self.cols = len(matrix[0])
            self.data = matrix
        else:
            self.rows = rows
            self.cols = cols
            self.data = [[0.0] * cols for _ in range(rows)]

    def __repr__(self) -> str:
        """String representation of an RTMatrix object."""
        return f"RTMatrix Object(rows={self.rows}, columns={self.cols})"

    @overload
    def __getitem__(self, index: int) -> list[float]: ...

    @overload
    def __getitem__(self, index: tuple[int, int]) -> float: ...

    def __getitem__(self, index: int | tuple[int, int]) -> list[float] | float:
        """Access a row or specific element in the matrix."""
        if isinstance(index, int):
            return self.data[index]
        if isinstance(index, tuple) and len(index) == 2:
            row, col = index
            return self.data[row][col]
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

    def __eq__(self, m2: object) -> bool:
        """Compares two matrices."""
        if not isinstance(m2, RTMatrix):
            raise NotImplementedError

        if m2.rows != self.rows or m2.cols != self.cols:
            raise ValueError("Can only compare matrices with the same dimensions.")

        for r_idx, row in enumerate(self.data):
            for col_idx, col in enumerate(row):
                if not compare_float(col, m2[r_idx][col_idx]):
                    return False

        return True
