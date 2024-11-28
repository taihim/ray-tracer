"""Common utility functions."""

from .constants import EPSILON


def compare_float(num1: float, num2: float) -> bool:
    """Compares two floats to see if they are equal and returns the result."""
    if type(num1) not in [float, int] or type(num2) not in [float, int]:
        raise TypeError("This function only supports integers and floating point numbers.")
    return abs(num1 - num2) < EPSILON
