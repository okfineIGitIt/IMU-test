from src.models.graphics_model import IMULinesModel
from src.views.graphics_view import RenderFrame


class GraphicsController:
    def __init__(self, frame, window):
        self.imu_lines_model = IMULinesModel(
            x_line_length=100, y_line_length=100, z_line_length=100
        )
        self.graphics_view = RenderFrame(frame, window)

        # starting position
        x_line_start_coords = self.imu_lines_model.x_line_coords
        y_line_start_coords = self.imu_lines_model.y_line_coords
        z_line_start_coords = self.imu_lines_model.x_line_coords

        self.graphics_view.draw_line("x_line", x_line_start_coords, color="red")
        self.graphics_view.draw_line("y_line", y_line_start_coords, color="green")
        self.graphics_view.draw_line("z_line", z_line_start_coords, color="blue")

    def update_x_line(self, x_angle, y_angle, z_angle):
        """Update line along the x-axis of the IMU

        :param x_angle:
        :param y_angle:
        :param z_angle:
        :return:
        """
        self.imu_lines_model.rotate_x_line(x_angle, y_angle, z_angle)
        self.graphics_view.update_line("x_line", self.imu_lines_model.x_line_coords)

    def update_y_line(self, x_angle, y_angle, z_angle):
        """Update line along the y-axis of the IMU

        :param x_angle:
        :param y_angle:
        :param z_angle:
        :return:
        """
        self.imu_lines_model.rotate_y_line(x_angle, y_angle, z_angle)
        self.graphics_view.update_line("y_line", self.imu_lines_model.y_line_coords)

    def update_z_line(self, x_angle, y_angle, z_angle):
        """Update line along the z-axis of the IMU

        :param x_angle:
        :param y_angle:
        :param z_angle:
        :return:
        """
        self.imu_lines_model.rotate_z_line(x_angle, y_angle, z_angle)
        self.graphics_view.update_line("z_line", self.imu_lines_model.z_line_coords)
