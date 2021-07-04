import numpy as np
from numpy import sin, cos


class AngleUnits:
    DEGREES = "degrees"
    RADIANS = "radians"


class Axis:
    X_AXIS = "x_axis"
    Y_AXIS = "y_axis"
    Z_AXIS = "z_axis"


# fmt: off
def get_x_axis_rotation_matrix(angle: float):
    """Gets x-axis rotation matrix

    :param angle :float: Angle to rotate by
    :return: x-axis rotation matrix
    """
    return np.array(
        [
            [1, 0, 0],
            [0, cos(angle), sin(angle)],
            [0, -1 * np.sin(angle), cos(angle)]
         ]
    )


def get_y_axis_rotation_matrix(angle):
    """Gets y-axis rotation matrix

    :param angle :float: Angle to rotate by
    :return: y-axis rotation matrix
    """
    return np.array(
        [
            [cos(angle), 0, -1 * sin(angle)],
            [0, 1, 0],
            [sin(angle), -1 * sin(angle), cos(angle)]
        ]
    )


def get_z_axis_rotation_matrix(angle: float):
    """Gets z-axis rotation matrix

    :param angle :float: Angle to rotate by
    :return: z-axis rotation matrix
    """
    return np.array(
        [
            [cos(angle), sin(angle), 0],
            [-1 * np.sin(angle), cos(angle), 0],
            [0, 0, 1]
        ]
    )
# fmt: on
