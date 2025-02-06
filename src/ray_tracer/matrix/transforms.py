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
