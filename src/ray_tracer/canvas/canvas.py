from pathlib import Path

from src.ray_tracer.tuples import ColorTuple

from .utils import clamp


class Canvas:
    """Defines a canvas object for the raytracer to draw on."""

    def __init__(self, rows: int = 0, columns: int = 0, default_val: tuple[float, float, float] = (0, 0, 0)) -> None:
        self.pixels = [[ColorTuple(*default_val)] * columns for _ in range(rows)]
        self.width = columns
        self.height = rows

    def __getitem__(self, index: tuple[int, int] | int) -> ColorTuple | list[ColorTuple]:
        """Get a value from the 2d pixel array.

        Args:
            index: a tuple/integer specifying the position of the item to be fetched
        """
        if isinstance(index, tuple) and len(index) == 2:
            row, col = index
            return self.pixels[row][col]
        return self.pixels[index]

    def __setitem__(self, index: tuple[int, int], value: ColorTuple) -> None:
        """Set a value in the 2d pixel array.

        Args:
        index: a tuple/integer specifying the position of insertion
        value: the value being inserted
        """
        if not isinstance(value, ColorTuple):
            raise TypeError("This class only supports ColorTuples.")
        if isinstance(index, tuple) and len(index) == 2:
            row, col = index
            self.pixels[row][col] = value
        else:
            raise TypeError("Index must be a tuple of two integers (row, col).")

    def save(self, path: str = "./canvas.ppm") -> str:
        """Saves the pixel array to a PPM file.

        Args:
            path: the path to save the file to.
        """
        min_val = 0
        max_val = 255
        max_chars_per_line = 70
        data = ""
        header = f"P3\n{self.width} {self.height}\n{max_val}\n"
        line_len = 0
        for row in self.pixels:
            col_str = ""
            line_len = 0
            for c_idx, col in enumerate(row):
                for idx, color_val in enumerate([col.red, col.green, col.blue]):
                    val_str = f"{int(clamp(color_val * max_val, min_val, max_val))}{"\n" if idx == 2 and c_idx == self.width - 1 else " "}"
                    line_len += len(val_str)
                    if line_len > max_chars_per_line:
                        val_str.replace("\n", " ")
                        col_str = col_str.strip()
                        col_str += "\n"
                        line_len = 0
                    col_str += val_str

            data += col_str

        with Path(path).open("w") as f:
            f.write(header + data)

        return header + data
