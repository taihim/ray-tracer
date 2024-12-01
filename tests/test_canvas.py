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
