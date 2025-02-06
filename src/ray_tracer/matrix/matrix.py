from copy import deepcopy
from typing import Union, overload

from src.ray_tracer.tuples import CustomTuple
from src.ray_tracer.utils import compare_float


class RTMatrix:
    """Class representing matrices used in the Raytracer."""

    def __init__(self, rows: int = 1, cols: int = 1, *, matrix: list[list[float]] | None = None) -> None:
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
        """Compare two matrices."""
        if not isinstance(m2, RTMatrix):
            raise NotImplementedError

        if m2.rows != self.rows or m2.cols != self.cols:
            raise ValueError("Can only compare matrices with the same dimensions.")

        for r_idx, row in enumerate(self.data):
            for col_idx, col in enumerate(row):
                if not compare_float(col, m2[r_idx][col_idx]):
                    return False

        return True

    # for simplicity, multiplcation is limited to matrices with 4 rows.
    # todo: update algorithm to support more dimensions using the following algo:
    # Input: matrices A and B
    # Let C be a new matrix of the appropriate size
    # For i from 1 to n:
    # For j from 1 to p:
    # Let sum = 0
    # For k from 1 to m:
    # Set sum ← sum + Aik * Bkj
    # Set Cij ← sum
    # Return C
    def __mul__(self, mat: Union["RTMatrix", CustomTuple]) -> Union["RTMatrix", CustomTuple]:
        """Multiply two matrices together."""
        if len(self.data) != 4:
            raise NotImplementedError("Multiplication for all dimensions not implemented yet.")

        m2 = RTMatrix(matrix=[[mat.x], [mat.y], [mat.z], [mat.w]]) if isinstance(mat, CustomTuple) else mat

        output_dims = (m2.rows, m2.cols)
        output_matrix = RTMatrix(output_dims[0], output_dims[1])
        for row_idx in range(output_dims[0]):
            for col_idx in range(output_dims[1]):
                output_matrix[row_idx][col_idx] = (
                    self.data[row_idx][0] * m2[0][col_idx]
                    + self.data[row_idx][1] * m2[1][col_idx]
                    + self.data[row_idx][2] * m2[2][col_idx]
                    + self.data[row_idx][3] * m2[3][col_idx]
                )
        return (
            output_matrix
            if not isinstance(mat, CustomTuple)
            else CustomTuple(x=output_matrix[0][0], y=output_matrix[1][0], z=output_matrix[2][0], w=output_matrix[3][0])
        )

    def __rmul__(self, mat: Union["RTMatrix", CustomTuple]) -> Union["RTMatrix", CustomTuple]:
        """__rmul__ implementation for RTMatrix."""
        return self * mat

    @staticmethod
    def identity(rows: int = 4, cols: int = 4) -> "RTMatrix":
        """Return an identity matrix with the given dimensions."""
        matrix = RTMatrix(rows, cols)
        for i in range(rows):
            matrix[i][i] = 1.0

        return matrix

    def transpose(self, inplace: bool = False) -> "RTMatrix":  # noqa: FBT001, FBT002
        """Transpose a matrix. Inplace = True modifies the existing matrix."""
        transposed = []
        for i in range(self.cols):
            new_row = [self.data[j][i] for j in range(self.rows)]
            transposed.append(new_row)
        if inplace:
            self.data = transposed
            return self

        return RTMatrix(matrix=transposed)

    # implementing using cofactor expansion atm
    # LU decomposition better suited for larger matrix sizes O(n^3)
    def determinant(self) -> float:
        """Calculate the determinant of the matrix."""
        if self.rows != self.cols:
            raise ValueError("Determinant only defined for square matrices.")
        if self.rows > 4:
            raise ValueError("Only matrices with dimensions upto 4x4 are supported.")
        if self.rows == 2:
            return (self.data[0][0] * self.data[1][1]) - (self.data[0][1] * self.data[1][0])

        det = 0.0
        for col in range(self.cols):
            det += self.data[0][col] * self.cofactor(0, col)
        return det

    def submatrix(self, row: int, col: int) -> "RTMatrix":
        """Create and return a submatrix from the original matrix.

        Args:
            row: the row to remove from the original matrix
            col: the column to remove from the original matrix
        """
        new_matrix = deepcopy(self.data)
        new_matrix.pop(row)
        for matrix_row in new_matrix:
            matrix_row.pop(col)

        return RTMatrix(matrix=new_matrix)

    # i.e. determinant of submatrix at (row,col)
    def minor(self, row: int, col: int) -> float:
        """Calculate the minor for an element at (row, col) in the 2x2 submatrix of the 3x3 matrix."""
        if self.rows > 4 or self.cols > 4:
            raise ValueError("Minor calculation only implemented for upto 4x4 matrices.")
        return self.submatrix(row, col).determinant()

    # cofactor multiplication rules
    # + - +
    # - + -
    # + - +
    # i.e. if row + col is odd, multiply the minor of that element by -1
    def cofactor(self, row: int, col: int) -> float:
        """Calculate the cofactor for an element at (row, col)."""
        if self.rows > 4 or self.cols > 4:
            raise ValueError("Cofactor calculation only implemented for upto 4x4 matrices.")

        minor = self.minor(row, col)
        if (row + col) % 2 == 0:
            return minor
        return -minor

    def invertable(self) -> bool:
        """Check whether the matrix is invertible."""
        return self.determinant() != 0

    def inverse(self) -> "RTMatrix":
        """Calculate and return the inverse of the matrix."""
        if not self.invertable():
            raise ValueError("Matrix is not invertable.")

        inverse_matrix = RTMatrix(rows=self.rows, cols=self.cols)

        for row in range(self.rows):
            for col in range(self.cols):
                c = self.cofactor(row, col)

                inverse_matrix[col][row] = c / self.determinant()
        return inverse_matrix
