import time

import serial

from data_plotting import IMUPlot
from utils import data_format_conversions as dfc

ARDUINO_COM_PORT = "COM3"
BAUD_RATE = 115200


def flush_io_buffers(serial_conn: serial.Serial):
    """
    Flush the input and output buffers of a serial connection.
    """

    # clear buffer
    print("Flushing buffers...")
    while serial_conn.in_waiting:
        print("flushing input buffer...")
        serial_conn.reset_input_buffer()
        time.sleep(3)

    while serial_conn.out_waiting:
        print("flushing output buffer...")
        serial_conn.reset_output_buffer()
        time.sleep(3)

    print("flushed")


if __name__ == "__main__":
    ser = serial.Serial(ARDUINO_COM_PORT, baudrate=BAUD_RATE, dsrdtr=False)
    imu_plot = IMUPlot()

    i = 0
    while True:
        response = ser.read_until()
        response_str = response.decode("utf-8").rstrip("\n")
        response_str = response_str.strip("\r")
        print(f"response_str: {response_str}")

        rot_data = dfc.parse_rotation_string_to_dict(response_str)

        if rot_data is None:
            continue

        rot_x = rot_data["X"]
        imu_plot.add_data_point(i, rot_x)
        i = i + 1


