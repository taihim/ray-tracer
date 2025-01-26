from src.ray_tracer.matrix import RTMatrix
from src.ray_tracer.tuples import CustomTuple


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

def test_matrix_multiply_4x4() -> None:
    m1 = RTMatrix(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
    m2 = RTMatrix(matrix=[[-2, 1, 2, 3], [3, 2, 1, -1], [4, 3, 6, 5], [1, 2, 7, 8]])

    assert m1 * m2 == RTMatrix(matrix=[[20, 22, 50, 48], [44, 54, 114, 108], [40, 58, 110, 102], [16, 26, 46, 42]])


def test_matrix_multiply_4x1() -> None:
    m1 = RTMatrix(matrix=[[1, 2, 3, 4], [2, 4, 4, 2], [8, 6, 4, 1], [0, 0, 0, 1]])
    t1 = CustomTuple(1, 2, 3, 1)

    assert isinstance(m1 * t1, CustomTuple)
    assert m1 * t1 == CustomTuple(18.0, 24.0, 33.0, 1.0)

def test_matrix_identity_1x1() -> None:
    i1 = RTMatrix.identity(1, 1)
    assert i1 == RTMatrix(matrix=[[1]])


def test_matrix_identity_2x2() -> None:
    i1 = RTMatrix.identity(2, 2)
    assert i1 == RTMatrix(matrix=[[1, 0], [0, 1]])


def test_matrix_identity_3x3() -> None:
    i1 = RTMatrix.identity(3, 3)
    assert i1 == RTMatrix(matrix=[[1, 0, 0], [0, 1, 0], [0, 0, 1]])


def test_matrix_identity_4x4() -> None:
    i1 = RTMatrix.identity()
    i2 = RTMatrix.identity(4, 4)
    identity = RTMatrix(matrix=[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    assert i1 == identity
    assert i2 == identity


def test_matrix_identity_multiplication() -> None:
    i1 = RTMatrix.identity()
    m1 = RTMatrix(matrix=[[0, 1, 2, 4], [1, 2, 4, 8], [2, 4, 8, 16], [4, 8, 16, 32]])

    assert m1 * i1 == m1


def test_tuple_identity_multiplication() -> None:
    i1 = RTMatrix.identity()
    t1 = CustomTuple(1, 2, 3, 4)

    assert i1 * t1 == t1

def test_transpose() -> None:
    m1 = RTMatrix(matrix=[[0, 9, 3, 0], [9, 8, 0, 8], [1, 8, 5, 3], [0, 0, 5, 8]])
    m1.transpose(inplace=True)

    assert m1 == RTMatrix(matrix=[[0, 9, 1, 0], [9, 8, 8, 0], [3, 0, 5, 5], [0, 8, 3, 8]])


def test_identity_transpose() -> None:
    i1 = RTMatrix.identity()
    i2 = i1.transpose()

    assert i1 == i2

def test_determinant_2x2() -> None:
    m1 = RTMatrix(matrix=[[1, 5], [-3, 2]])

    assert m1.determinant() == 17

def test_submatrix_3x3() -> None:
    m1 = RTMatrix(matrix=[[1, 5, 0], [-3, 2, 7], [0, 6, -3]])

    s1 = m1.submatrix(0, 2)

    assert s1 == RTMatrix(matrix=[[-3, 2], [0, 6]])

def test_submatrix_4x4() -> None:
    m1 = RTMatrix(matrix=[[-6, 1, 1, 6], [-8, 5, 8, 6], [-1, 0, 8, 2], [-7, 1, -1, 1]])

    s1 = m1.submatrix(2, 1)

    assert s1 == RTMatrix(matrix=[[-6, 1, 6], [-8, 8, 6], [-7, -1, 1]])

def test_minor_3x3() -> None:
    m1 = RTMatrix(matrix=[[3, 5, 0], [2, -1, -7], [6, -1, 5]])

    assert m1.minor(1, 0) == 25

def test_cofactor_3x3() -> None:
    m1 = RTMatrix(matrix=[[3, 5, 0], [2, -1, -7], [6, -1, 5]])

    assert m1.minor(0, 0) == -12
    assert m1.cofactor(0, 0) == -12
    assert m1.minor(1, 0) == 25
    assert m1.cofactor(1, 0) == -25
