import tkinter as tk

from src.views.generic_tk_frame import GenericFrame


class ControlFrame(GenericFrame):
    """Frame with interactive elements to control aspects of the GUI"""

    def __init__(self, frame, parent_window):
        super().__init__(frame, parent_window)
        self.configure_ui()

    def configure_ui(self):
        button = tk.Button(self.frame, text="Please No")
        button1 = tk.Button(self.frame, text="Please Yes")

        button.pack()
        button1.pack()
