def clamp(value: float, min_value: float, max_value: float) -> float:
    """Clamps a value between a minimum and maximum value.

    Args:
        value: the value to clamp
        min_value: the minimum allowed value
        max_value: the maximum allowed value
    """
    return max(min_value, min(value, max_value))
