from src.ray_tracer.matrix import RTMatrix


def translation(x: float, y: float, z: float) -> RTMatrix:
    """Create and return a translation matrix."""
    t_matrix = RTMatrix.identity()
    t_matrix[0][3] = x
    t_matrix[1][3] = y
    t_matrix[2][3] = z

    return t_matrix
