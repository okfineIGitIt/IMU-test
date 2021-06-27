import tkinter as tk
from abc import ABC

from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


class GenericFrame(ABC):

    def __init__(self, frame, *args, **kwargs):
        self.frame = frame
        super().__init__()

    def configure_ui(self):
        pass


class ControlFrame(GenericFrame):
    """Frame with interactive elements to control aspects of the GUI"""

    def __init__(self, frame):
        super().__init__(frame)
        self.configure_ui()

    def configure_ui(self):
        button = tk.Button(self.frame, text="Please No")
        button1 = tk.Button(self.frame, text="Please Yes")

        button.pack()
        button1.pack()


class GraphFrame(GenericFrame):
    """Frame with graph displaying IMU readings"""

    def __init__(self, frame, window):
        super().__init__(frame)
        self.window = window

        # making figure with data
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        # make tkinter plot
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.canvas.mpl_connect("key_press_event", self.on_key_press)

        self._update_tkinter_app()

    def configure_ui(self):
        pass

    def on_key_press(self, event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, self.canvas, self.toolbar)

    def _update_tkinter_app(self):
        self.window.update_idletasks()
        self.window.update()


class RenderFrame(GenericFrame):
    """Frame with 3d render if current IMU orientation"""

    def __init__(self, frame):
        super().__init__(frame)
        self.configure_ui()

    def configure_ui(self):
        canvas = tk.Canvas(self.frame)

        canvas.pack()


class MonitorFrame(GenericFrame):
    """Frame with serial monitor output from IMU"""

    def __init__(self, frame):
        super().__init__(frame)
        self.configure_ui()

    def configure_ui(self):
        text_editor = tk.Text(self.frame)

        text_editor.pack()


if __name__ == "__main__":
    window = tk.Tk()

    render_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
    graph_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
    control_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
    monitor_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)

    render_frame.grid(row=1, column=1)
    graph_frame.grid(row=1, column=2)
    control_frame.grid(row=2, column=1)
    monitor_frame.grid(row=2, column=2)

    window.columnconfigure(1, weight=1, minsize=75)
    window.rowconfigure(1, weight=1, minsize=50)
    window.columnconfigure(2, weight=1, minsize=75)
    window.rowconfigure(2, weight=1, minsize=50)

    control = ControlFrame(frame=control_frame)
    monitor = MonitorFrame(frame=monitor_frame)
    render = RenderFrame(frame=render_frame)
    graph = GraphFrame(frame=graph_frame, window=window)

    window.mainloop()
