"""
1. Receive data from serial port
2. Flag set to open data receiving
"""
import time

import serial

ARDUINO_COM_PORT = "COM3"
BAUD_RATE = 115200


class ArduinoConnection:
    """Receives data from Arduino through com port"""
    # TODO: place in a different file

    def __init__(self):
        self._serial_conn = None

    @property
    def arduino_is_connected(self):
        """Return True if Serial connection object exists and False if not"""
        if self._serial_conn is None:
            return False

        return True

    def create_arduino_serial_connection(
        self, com_port=ARDUINO_COM_PORT, arduino_baudrate=BAUD_RATE
    ):
        """Get Serial connection object for a connected Arduino if possible

        :param com_port:
        :param arduino_baudrate:
        :return:
        """
        try:
            self._serial_conn = serial.Serial(
                com_port, baudrate=arduino_baudrate, dsrdtr=False
            )
        except serial.SerialException as se:
            print(f"Could not get serial connection\n{se}")
            self._serial_conn = None

    def get_arduino_serial_connection(self):
        return self._serial_conn

    def flush_io_buffers(self):
        """Flush the input and output buffers of a serial connection."""
        if self.arduino_is_connected is False:
            raise ArduinoNotConnectedError(
                f"read_port_data() only works when the Arduino is connected!"
            )

        print("Flushing buffers...")
        while self._serial_conn.in_waiting:
            print("flushing input buffer...")
            self._serial_conn.reset_input_buffer()
            time.sleep(3)

        while self._serial_conn.out_waiting:
            print("flushing output buffer...")
            self._serial_conn.reset_output_buffer()
            time.sleep(3)

        print("flushed")

    def read_port_data(self):
        """Read data from the com port

        Currently only data from COM3 is read
        """
        if self.arduino_is_connected is False:
            raise ArduinoNotConnectedError(
                f"read_port_data() only works when the Arduino is connected!"
            )

        response = self._serial_conn.read_until()
        response_str = response.decode("utf-8").rstrip("\n")
        response_str = response_str.strip("\r")
        # print(f"response_str: {response_str}")

        return response_str


class ArduinoNotConnectedError(Exception):
    pass
