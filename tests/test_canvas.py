import pytest

from src.ray_tracer import Canvas, ColorTuple


def test_canvas() -> None:
    cv = Canvas(10, 20)
    default_color = ColorTuple(0, 0, 0)

    assert cv.height == 10
    assert cv.width == 20

    for i in range(cv.height):
        for j in range(cv.width):
            assert cv.pixels[i][j] == default_color


def test_canvas_write() -> None:
    cv = Canvas(10, 20)
    new_color = ColorTuple(1, 0, 0)

    cv.pixels[2][3] = new_color

    assert cv.pixels[2][3] == ColorTuple(1, 0, 0)


def test_canvas_to_ppm() -> None:
    cv = Canvas(5, 7, (0.5, 0.3, 0.7))

    output_str = cv.canvas_to_ppm()

    output_split = output_str.split("\n")

    assert output_split[0] == "P3"
    assert output_split[1] == "7 5"
    assert output_split[2] == "255"
    assert output_split[3] == "127 76 178 127 76 178 127 76 178 127 76 178 127 76 178 127 76 178 127"
    assert output_split[4] == "76 178"
    assert output_split[5] == "127 76 178 127 76 178 127 76 178 127 76 178 127 76 178 127 76 178 127"
    assert output_split[6] == "76 178"
    assert output_split[7] == "127 76 178 127 76 178 127 76 178 127 76 178 127 76 178 127 76 178 127"
    assert output_split[8] == "76 178"
    assert output_split[9] == "127 76 178 127 76 178 127 76 178 127 76 178 127 76 178 127 76 178 127"
    assert output_split[10] == "76 178"
    assert output_split[11] == "127 76 178 127 76 178 127 76 178 127 76 178 127 76 178 127 76 178 127"
    assert output_split[12] == "76 178"

    assert output_str[-1] == "\n"


def test_canvas_getitem_tuple():
    cv = Canvas(5, 5, (0.1, 0.2, 0.3))
    assert cv[2, 3] == ColorTuple(0.1, 0.2, 0.3)


def test_canvas_getitem_int():
    cv = Canvas(5, 5, (0.1, 0.2, 0.3))
    row = cv[2]
    assert len(row) == 5
    assert row[0] == ColorTuple(0.1, 0.2, 0.3)


def test_canvas_setitem_tuple():
    cv = Canvas(5, 5)
    cv[1, 2] = ColorTuple(1, 0, 0)
    assert cv[1, 2] == ColorTuple(1, 0, 0)


def test_canvas_setitem_invalid_value():
    cv = Canvas(5, 5)
    with pytest.raises(TypeError, match="This class only supports ColorTuples"):
        cv[0, 0] = "not a color"


def test_canvas_setitem_invalid_index():
    cv = Canvas(5, 5)
    with pytest.raises(TypeError, match="Index must be a tuple of two integers"):
        cv[0] = ColorTuple(1, 0, 0)


def test_canvas_save(tmp_path):
    cv = Canvas(2, 2, (1, 0, 0))
    data = cv.canvas_to_ppm()
    path = str(tmp_path / "test.ppm")
    Canvas.save(data=data, path=path)

    with open(path) as f:
        contents = f.read()
    assert contents == data
