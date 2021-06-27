import tkinter as tk

from src.views.generic_tk_frame import GenericFrame


class MonitorFrame(GenericFrame):
    """Frame with serial monitor output from IMU"""

    def __init__(self, frame, parent_window):
        super().__init__(frame, parent_window)
        self.configure_ui()

    def configure_ui(self):
        text_editor = tk.Text(self.frame)

        text_editor.pack()
