"""Display main GUI and run application"""
import tkinter as tk

from arduino_receiver import read_port_data, get_arduino_serial_connection
from src.controllers.graphics_controller import GraphicsController


def update_graphics_with_arduino_data(controller):
    ser = get_arduino_serial_connection()

    while True:
        data = read_port_data(ser)

        if data is None:
            continue

        controller.update_x_line(data["X"], data["Y"], data["Z"])
        controller.update_y_line(data["X"], data["Y"], data["Z"])
        controller.update_z_line(data["X"], data["Y"], data["Z"])


if __name__ == "__main__":
    window = tk.Tk()

    window.rowconfigure(1, weight=1, minsize=50)
    window.rowconfigure(2, weight=1, minsize=50)
    window.columnconfigure(1, weight=1, minsize=75)
    window.columnconfigure(2, weight=1, minsize=75)

    render_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
    render_frame.grid(row=1, column=1)

    graphics_controller = GraphicsController(render_frame, window)

    # arduino_ser = get_arduino_serial_connection()
    window.after(3000, lambda: update_graphics_with_arduino_data(graphics_controller))
    window.mainloop()
