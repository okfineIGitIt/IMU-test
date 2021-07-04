import numpy as np

from src.math_constants import (
    AngleUnits, Axis,
    get_x_axis_rotation_matrix,
    get_y_axis_rotation_matrix,
    get_z_axis_rotation_matrix
)


class IMULinesModel:
    """Hold position data of graphic representing the IMU"""

    def __init__(self, x_line_length=1, y_line_length=1, z_line_length=1):
        self._x_line_base = np.array([x_line_length, 0, 0])
        self._y_line_base = np.array([0, y_line_length, 0])
        self._z_line_base = np.array([0, 0, z_line_length])

        self.x_line = self._x_line_base
        self.y_line = self._y_line_base
        self.z_line = self._z_line_base

    @property
    def x_line_coords(self):
        return self.x_line

    @property
    def y_line_coords(self):
        return self.y_line

    @property
    def z_line_coords(self):
        return self.z_line

    def rotate_x_line(self, x_angle, y_angle, z_angle):
        self.x_line = self._x_line_base
        self.x_line = rotate_vector_around_axis(self.x_line, x_angle, Axis.X_AXIS)
        self.x_line = rotate_vector_around_axis(self.x_line, y_angle, Axis.Y_AXIS)
        self.x_line = rotate_vector_around_axis(self.x_line, z_angle, Axis.Z_AXIS)

    def rotate_y_line(self, x_angle, y_angle, z_angle):
        self.y_line = self._y_line_base
        self.y_line = rotate_vector_around_axis(self.y_line, x_angle, Axis.X_AXIS)
        self.y_line = rotate_vector_around_axis(self.y_line, y_angle, Axis.Y_AXIS)
        self.y_line = rotate_vector_around_axis(self.y_line, z_angle, Axis.Z_AXIS)

    def rotate_z_line(self, x_angle, y_angle, z_angle):
        self.z_line = self._z_line_base
        self.z_line = rotate_vector_around_axis(self.z_line, x_angle, Axis.X_AXIS)
        self.z_line = rotate_vector_around_axis(self.z_line, y_angle, Axis.Y_AXIS)
        self.z_line = rotate_vector_around_axis(self.z_line, z_angle, Axis.Z_AXIS)


def rotate_vector_around_axis(
    vector, angle: float, axis: int, angle_units: str = AngleUnits.DEGREES
):
    """

    :param vector:
    :param angle:
    :param axis:
    :param angle_units:
    :return np.array: rotated vector
    """
    rot_matrix = np.array([])

    if angle_units == AngleUnits.DEGREES:
        angle = np.radians(angle)

    if axis == Axis.X_AXIS:
        rot_matrix = get_x_axis_rotation_matrix(angle)
    elif axis == Axis.Y_AXIS:
        rot_matrix = get_y_axis_rotation_matrix(angle)
    elif axis == Axis.Z_AXIS:
        rot_matrix = get_z_axis_rotation_matrix(angle)

    v_p = np.matmul(vector, rot_matrix)
    v_p = np.around(v_p, 2)

    return v_p
