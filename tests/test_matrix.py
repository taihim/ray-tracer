import pytest

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

def test_determinant_3x3() -> None:
    m1 = RTMatrix(matrix=[[1, 2, 6], [-5, 8, -4], [2, 6, 4]])

    assert m1.cofactor(0, 0) == 56
    assert m1.cofactor(0, 1) == 12
    assert m1.cofactor(0, 2) == -46
    assert m1.determinant() == -196


def test_determinant_4x4() -> None:
    m1 = RTMatrix(matrix=[[-2, -8, 3, 5], [-3, 1, 7, 3], [1, 2, -9, 6], [-6, 7, 7, -9]])

    assert m1.cofactor(0, 0) == 690
    assert m1.cofactor(0, 1) == 447
    assert m1.cofactor(0, 2) == 210
    assert m1.cofactor(0, 3) == 51
    assert m1.determinant() == -4071

def test_invertable() -> None:
    m1 = RTMatrix(matrix=[[6, 4, 4, 4], [5, 5, 7, 6], [4, -9, 3, -7], [9, 1, 7, -6]])

    assert m1.determinant() == -2120
    assert m1.invertable() is True


def test_noninvertable() -> None:
    m1 = RTMatrix(matrix=[[-4, 2, -2, -3], [9, 6, 2, 6], [0, -5, 1, -5], [0, 0, 0, 0]])

    assert m1.determinant() == 0
    assert m1.invertable() is False

def test_inverse_1() -> None:
    m1 = RTMatrix(matrix=[[-5, 2, 6, -8], [1, -5, 1, 8], [7, 7, -6, -7], [1, -3, 7, 4]])
    m2 = m1.inverse()

    assert m1.determinant() == 532
    assert m1.cofactor(2, 3) == -160
    assert m2[3][2] == -160 / 532
    assert m1.cofactor(3, 2) == 105
    assert m2[2][3] == 105 / 532
    assert m2 == RTMatrix(
        matrix=[
            [0.21805, 0.45113, 0.24060, -0.04511],
            [-0.80827, -1.45677, -0.44361, 0.52068],
            [-0.07895, -0.22368, -0.05263, 0.19737],
            [-0.52256, -0.81391, -0.30075, 0.30639],
        ]
    )


def test_inverse_2() -> None:
    m1 = RTMatrix(matrix=[[8, -5, 9, 2], [7, 5, 6, 1], [-6, 0, 9, 6], [-3, 0, -9, -4]])
    m2 = m1.inverse()

    assert m2 == RTMatrix(
        matrix=[
            [-0.15385, -0.15385, -0.28205, -0.53846],
            [-0.07692, 0.12308, 0.02564, 0.03077],
            [0.35897, 0.35897, 0.43590, 0.92308],
            [-0.69231, -0.69231, -0.76923, -1.92308],
        ]
    )


def test_inverse_3() -> None:
    m1 = RTMatrix(matrix=[[9, 3, 0, 9], [-5, -2, -6, -3], [-4, 9, 6, 4], [-7, 6, 6, 2]])
    m2 = m1.inverse()

    assert m2 == RTMatrix(
        matrix=[
            [-0.04074, -0.07778, 0.14444, -0.22222],
            [-0.07778, 0.03333, 0.36667, -0.33333],
            [-0.02901, -0.14630, -0.10926, 0.12963],
            [0.17778, 0.06667, -0.26667, 0.33333],
        ]
    )

def test_inverse_multiplication() -> None:
    m1 = RTMatrix(matrix=[[3, -9, 7, 3], [3, -8, 2, -9], [-4, 4, 4, 1], [-6, 5, -1, 1]])
    m2 = RTMatrix(matrix=[[8, 2, 2, 2], [3, -1, 7, 0], [7, 0, 5, 4], [6, -2, 0, 5]])

    m3 = m1 * m2
    assert m3 * m2.inverse() == m1


def test_matrix_repr():
    m1 = RTMatrix(2, 3)
    assert repr(m1) == "RTMatrix Object(rows=2, columns=3)"


def test_matrix_getitem_tuple():
    m1 = RTMatrix(matrix=[[1, 2], [3, 4]])
    assert m1[0, 1] == 2
    assert m1[1, 0] == 3


def test_matrix_getitem_invalid():
    m1 = RTMatrix(matrix=[[1, 2], [3, 4]])
    with pytest.raises(TypeError, match="Index should be an int or a tuple of two integers"):
        m1["bad"]


def test_matrix_setitem_wrong_cols():
    m1 = RTMatrix(2, 2)
    with pytest.raises(ValueError, match="Expected 2 columns"):
        m1[0] = [1.0, 2.0, 3.0]


def test_matrix_setitem_invalid_index():
    m1 = RTMatrix(2, 2)
    with pytest.raises(TypeError, match="Expected index of type Int"):
        m1["bad"] = [1.0, 2.0]


def test_matrix_eq_non_matrix():
    m1 = RTMatrix(matrix=[[1, 2], [3, 4]])
    with pytest.raises(NotImplementedError):
        m1 == "not a matrix"


def test_matrix_eq_mismatched_dims():
    m1 = RTMatrix(matrix=[[1, 2], [3, 4]])
    m2 = RTMatrix(matrix=[[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError, match="Can only compare matrices with the same dimensions"):
        m1 == m2


def test_matrix_mul_non_4_rows():
    m1 = RTMatrix(matrix=[[1, 2], [3, 4]])
    m2 = RTMatrix(matrix=[[5, 6], [7, 8]])
    with pytest.raises(NotImplementedError, match="Multiplication for all dimensions not implemented"):
        m1 * m2


def test_matrix_rmul():
    m1 = RTMatrix(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
    m2 = RTMatrix(matrix=[[-2, 1, 2, 3], [3, 2, 1, -1], [4, 3, 6, 5], [1, 2, 7, 8]])
    assert m2.__rmul__(m1) == m2 * m1


def test_determinant_non_square():
    m1 = RTMatrix(2, 3)
    with pytest.raises(ValueError, match="Determinant only defined for square matrices"):
        m1.determinant()


def test_determinant_too_large():
    m1 = RTMatrix(5, 5)
    for i in range(5):
        m1[i] = [float(j) for j in range(5)]
    with pytest.raises(ValueError, match="Only matrices with dimensions upto 4x4 are supported"):
        m1.determinant()


def test_minor_too_large():
    m1 = RTMatrix(5, 5)
    with pytest.raises(ValueError, match="Minor calculation only implemented for upto 4x4"):
        m1.minor(0, 0)


def test_cofactor_too_large():
    m1 = RTMatrix(5, 5)
    with pytest.raises(ValueError, match="Cofactor calculation only implemented for upto 4x4"):
        m1.cofactor(0, 0)


def test_inverse_singular():
    m1 = RTMatrix(matrix=[[-4, 2, -2, -3], [9, 6, 2, 6], [0, -5, 1, -5], [0, 0, 0, 0]])
    with pytest.raises(ValueError, match="Matrix is not invertable"):
        m1.inverse()


def test_matrix_init_invalid_type():
    with pytest.raises(TypeError, match="Expected both rows and cols to be lists"):
        RTMatrix(matrix=[1, 2, 3])
