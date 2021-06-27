import tkinter as tk

from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

from .generic_tk_frame import GenericFrame


class GraphFrame(GenericFrame):
    """Frame with graph displaying IMU readings"""

    def __init__(self, frame, parent_window):
        super().__init__(frame, parent_window)

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)  # A tk.DrawingArea.
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame)

        self.configure_ui()

    def configure_ui(self):

        # make tkinter plot
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.canvas.mpl_connect("key_press_event", self.on_key_press)

        self._update_tkinter_app()

    def on_key_press(self, event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, self.canvas, self.toolbar)

    def _update_tkinter_app(self):
        self.window.update_idletasks()
        self.window.update()

