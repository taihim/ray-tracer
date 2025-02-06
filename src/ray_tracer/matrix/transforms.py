import math

from src.ray_tracer.matrix import RTMatrix


def translate(x: float, y: float, z: float) -> RTMatrix:
    """Create and return a translation matrix."""
    translation_matrix = RTMatrix.identity()
    translation_matrix[0][3] = x
    translation_matrix[1][3] = y
    translation_matrix[2][3] = z

    return translation_matrix


def scale(x: float, y: float, z: float) -> RTMatrix:
    """Create and return a scaling matrix."""
    scaling_matrix = RTMatrix.identity()
    scaling_matrix[0][0] = x
    scaling_matrix[1][1] = y
    scaling_matrix[2][2] = z

    return scaling_matrix


def rotate_x(rad: float) -> RTMatrix:
    """Create and return a rotation matrix for the x axis."""
    rotation_matrix = RTMatrix.identity()

    rotation_matrix[1][1] = math.cos(rad)
    rotation_matrix[1][2] = -math.sin(rad)
    rotation_matrix[2][1] = math.sin(rad)
    rotation_matrix[2][2] = math.cos(rad)

    return rotation_matrix


def rotate_y(rad: float) -> RTMatrix:
    """Create and return a rotation matrix for the y axis."""
    rotation_matrix = RTMatrix.identity()

    rotation_matrix[0][0] = math.cos(rad)
    rotation_matrix[0][2] = math.sin(rad)
    rotation_matrix[2][0] = -math.sin(rad)
    rotation_matrix[2][2] = math.cos(rad)

    return rotation_matrix


def rotate_z(rad: float) -> RTMatrix:
    """Create and return a rotation matrix for the z axis."""
    rotation_matrix = RTMatrix.identity()

    rotation_matrix[0][0] = math.cos(rad)
    rotation_matrix[0][1] = -math.sin(rad)
    rotation_matrix[1][0] = math.sin(rad)
    rotation_matrix[1][1] = math.cos(rad)

    return rotation_matrix
