"""Create Monitor Controller"""
from threading import Thread

from src.models.monitor_model import ArduinoConnection
from src.views.monitor_view import MonitorFrame


class MonitorController:
    def __init__(self, frame, window):
        self._window = window
        self.arduino_conn = ArduinoConnection()
        self.monitor_view = MonitorFrame(frame, window)
        self.monitor_thread = None
        self.connect_buttons()

    def connect_buttons(self):
        """Connect the view buttons to the appropriate functions"""
        buttons = self.monitor_view.elements["btns"]

        buttons["connect"]["command"] = self.start_serial_monitor_stream
        buttons["disconnect"]["command"] = self.stop_serial_monitor_stream
        buttons["flush_editor"]["command"] = self.clear_monitor

    def start_serial_monitor_stream(self):
        """Start sending data to the monitor."""
        self.monitor_thread = Thread(target=self.run_monitor_loop, daemon=True)
        self.monitor_thread.start()

    def stop_serial_monitor_stream(self):
        """Stop sending data to the monitor."""
        self.monitor_thread.join()
        self.monitor_thread = None

    def run_monitor_loop(self):
        print("Starting Serial Monitor...")
        self.monitor_view.print_to_monitor("Starting serial monitor...")

        if not self.arduino_conn.arduino_is_connected:
            self.arduino_conn.create_arduino_serial_connection()

        while True:
            data = self.arduino_conn.read_port_data()
            self.monitor_view.print_to_monitor(data)
            # self._window.update_idletasks()


    def clear_monitor(self):
        """Clear text in monitor."""
        self.monitor_view.clear_monitor()
