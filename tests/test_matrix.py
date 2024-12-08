from src.ray_tracer.matrix import RTMatrix


def test_matrix_init() -> None:
    m1 = RTMatrix(matrix=[[1, 2, 3, 4], [5.5, 6.5, 7.5, 8.5], [9, 10, 11, 12], [13.5, 14.5, 15.5, 16.5]])

    assert m1[0][0] == 1
    assert m1[0][3] == 4
    assert m1[1][0] == 5.5
    assert m1[1][2] == 7.5
    assert m1[2][2] == 11
    assert m1[3][0] == 13.5
    assert m1[3][2] == 15.5
