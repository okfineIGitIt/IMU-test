import tkinter as tk

from control_view import ControlFrame
from graph_view import GraphFrame
from graphics_view import RenderFrame
from monitor_view import MonitorFrame

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

    control = ControlFrame(frame=control_frame, parent_window=window)
    monitor = MonitorFrame(frame=monitor_frame, parent_window=window)
    render = RenderFrame(frame=render_frame, parent_window=window)
    graph = GraphFrame(frame=graph_frame, parent_window=window)

    window.mainloop()
