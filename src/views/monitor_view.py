import tkinter as tk

from src.views.generic_tk_frame import GenericFrame


class MonitorFrame(GenericFrame):
    """Frame with serial monitor output from IMU"""

    def __init__(self, frame, parent_window):
        super().__init__(frame, parent_window)
        self.elements = {}
        self.configure_ui()

    def configure_ui(self):
        self.elements = {
            "btns": {
                "connect": tk.Button(self.frame, text="Connect"),
                "disconnect": tk.Button(self.frame, text="Disconnect"),
                "flush_editor": tk.Button(self.frame, text="Flush Editor"),
            },
            "text_edts": {
                "monitor": tk.Text(self.frame)
            }
        }

        self.elements["text_edts"]["monitor"].pack()
        self.elements["btns"]["connect"].pack()
        self.elements["btns"]["disconnect"].pack()
        self.elements["btns"]["flush_editor"].pack()

        monitor = self.elements["text_edts"]["monitor"]
        monitor["state"] = tk.DISABLED

    def print_to_monitor(self, text: str, add_newline: bool = True):
        """Print text to the text editor

        :param text: Text to print to the text editor
        :param add_newline: if True, a newline is added to the end of the text string
        :return:
        """
        monitor = self.elements["text_edts"]["monitor"]

        if add_newline:
            text = text + "\n"

        monitor.insert(tk.END, text)
