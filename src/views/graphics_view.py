import tkinter as tk

from .generic_tk_frame import GenericFrame


class RenderFrame(GenericFrame):
    """Frame with 3d render if current IMU orientation"""

    def __init__(self, frame, parent_window):
        super().__init__(frame, parent_window)
        self.configure_ui()

    def configure_ui(self):
        canvas = tk.Canvas(self.frame)

        canvas.pack()
