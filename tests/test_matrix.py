from src.ray_tracer.matrix import RTMatrix


def test_matrix_init_1x1() -> None:
    m1 = RTMatrix(matrix=[[-3], [1]])

    assert m1[0][0] == -3
    assert m1[1][0] == 1


def test_matrix_init_2x2() -> None:
    m1 = RTMatrix(matrix=[[-3, 5], [1, -2]])

    assert m1[0][0] == -3
    assert m1[0][1] == 5
    assert m1[1][0] == 1
    assert m1[1][1] == -2


def test_matrix_init_3x3() -> None:
    m1 = RTMatrix(matrix=[[-3, 5, 0], [1, -2, -7], [0, 1, 1]])
    assert m1[0][0] == -3
    assert m1[1][1] == -2
    assert m1[2][2] == 1


def test_matrix_init_4x4() -> None:
    m1 = RTMatrix(matrix=[[1, 2, 3, 4], [5.5, 6.5, 7.5, 8.5], [9, 10, 11, 12], [13.5, 14.5, 15.5, 16.5]])

    assert m1[0][0] == 1
    assert m1[0][3] == 4
    assert m1[1][0] == 5.5
    assert m1[1][2] == 7.5
    assert m1[2][2] == 11
    assert m1[3][0] == 13.5
    assert m1[3][2] == 15.5

def test_matrices_equal_1x1() -> None:
    m1 = RTMatrix(matrix=[[-3]])
    m2 = RTMatrix(matrix=[[-3]])

    assert m1 == m2


def test_matrices_equal_2x2() -> None:
    m1 = RTMatrix(matrix=[[-3], [1]])
    m2 = RTMatrix(matrix=[[-3], [1]])

    assert m1 == m2


def test_matrices_equal_3x3() -> None:
    m1 = RTMatrix(matrix=[[-3, 5, 0], [1, -2, -7], [0, 1, 1]])
    m2 = RTMatrix(matrix=[[-3, 5, 0], [1, -2, -7], [0, 1, 1]])

    assert m1 == m2


def test_matrices_equal_4x4() -> None:
    m1 = RTMatrix(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
    m2 = RTMatrix(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])

    assert m1 == m2


def test_matrices_unequal_1x1() -> None:
    m1 = RTMatrix(matrix=[[-3], [1]])
    m2 = RTMatrix(matrix=[[-3], [12]])

    assert m1 != m2


def test_matrices_unequal_2x2() -> None:
    m1 = RTMatrix(matrix=[[-3, 5], [1, -2]])
    m2 = RTMatrix(matrix=[[-3, 5], [12, -2]])

    assert m1 != m2


def test_matrices_unequal_3x3() -> None:
    m1 = RTMatrix(matrix=[[-3, 5, 0], [1, -2, -7], [0, 1, 1]])
    m2 = RTMatrix(matrix=[[-3, 5, 0], [11, -2, -7], [0, 1, 1]])

    assert m1 != m2


def test_matrices_unequal_4x4() -> None:
    m1 = RTMatrix(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
    m2 = RTMatrix(matrix=[[2, 3, 4, 5], [6, 7, 8, 9], [8, 7, 6, 5], [4, 3, 2, 1]])

    assert m1 != m2
