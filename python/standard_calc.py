def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """
    return float((angle + 180) % 360 - 180)


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """
    # assumed that 0 difference from first_angle or second_angle is True (in between)
    # since it is not in the reflex angle
    second_to_first = bound_to_180(second_angle - first_angle)
    middle_to_first = bound_to_180(middle_angle - first_angle)
    if second_to_first == -180:
        return True
    if second_to_first >= 0:
        return 0 <= middle_to_first <= second_to_first
    return second_to_first <= middle_to_first <= 0
