"""Display main GUI and run application"""
import time
import tkinter as tk
from threading import Thread, Event

from src.controllers.graph_controller import GraphController
from src.controllers.graphics_controller import GraphicsController
from src.controllers.monitor_controller import MonitorController
from src.utils.data_format_conversions import parse_data_string

kill_conn_thread = Event()


def update_graphics_with_arduino_data(
        graphics_controller, monitor_controller, graph_controller
):
    if not monitor_controller.arduino_conn.arduino_is_connected:
        monitor_controller.arduino_conn.create_arduino_serial_connection()

    while not kill_conn_thread.is_set():
        data_string = monitor_controller.arduino_conn.read_port_data()

        if data_string is None:
            continue

        monitor_controller.monitor_view.print_to_monitor(data_string)

        data = parse_data_string(data_string)

        if data is None:
            continue

        graphics_controller.update_all_lines(data["X"], data["Y"], data["Z"])
        graph_controller.add_data_point(time.perf_counter(), data["X"], "x_data")

    kill_conn_thread.clear()


def run_graphics_thread(graphics_controller, monitor_controller, graph_controller):
    graphics_thread = Thread(
        target=update_graphics_with_arduino_data, args=(
            graphics_controller, monitor_controller, graph_controller
        ),
        daemon=True
    )

    graphics_thread.start()


def run():
    window = tk.Tk()

    window.rowconfigure(1, weight=1, minsize=50)
    window.rowconfigure(2, weight=1, minsize=50)
    window.columnconfigure(1, weight=1, minsize=75)
    window.columnconfigure(2, weight=1, minsize=75)

    render_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
    render_frame.grid(row=1, column=1)

    monitor_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
    monitor_frame.grid(row=1, column=2)

    control_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
    control_frame.grid(row=2, column=1)

    graph_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
    graph_frame.grid(row=2, column=2)

    graphics_controller = GraphicsController(render_frame, window)
    monitor_controller = MonitorController(monitor_frame, window)
    graph_controller = GraphController(graph_frame, window)

    start_button = tk.Button(
        control_frame, text="START",
        command=lambda: run_graphics_thread(
            graphics_controller, monitor_controller, graph_controller
        )
    )
    stop_button = tk.Button(
        control_frame, text="STOP",
        command=kill_conn_thread.set
    )

    start_button.pack()
    stop_button.pack()

    # arduino_ser = get_arduino_serial_connection()
    # window.after(500, lambda: run_graphics_thread(graphics_controller))
    window.mainloop()
