import tkinter as tk

from src.views.generic_tk_frame import GenericFrame

X_ORIGIN = 100
Y_ORIGIN = 100


class RenderFrame(GenericFrame):
    """Frame with 3d render if current IMU orientation"""

    def __init__(self, frame, parent_window):
        super().__init__(frame, parent_window)
        self.canvas = None
        self.configure_ui()

    def configure_ui(self):
        self.canvas = tk.Canvas(self.frame)
        self.canvas.pack()

    def draw_line(self, line_name: str, coords):
        x, y, _ = coords
        self.canvas.create_line(0, 0, X_ORIGIN, Y_ORIGIN, width=3, tags=line_name)
        self.window.update_idletasks()

    def update_line(self, line_name: str, coords):
        x, y, _ = coords
        self.canvas.coords(line_name, X_ORIGIN, Y_ORIGIN, x, y)
        # print(f"update_line: z coords: {coords}")
        self.window.update_idletasks()


def adjust_2d_coords_origin(x, y, x_shift=X_ORIGIN, y_shift=Y_ORIGIN):
    return x + x_shift, y + y_shift
