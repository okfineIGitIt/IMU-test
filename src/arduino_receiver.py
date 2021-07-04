import time

import serial

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


def read_port_data(serial_obj):
    response = serial_obj.read_until()
    response_str = response.decode("utf-8").rstrip("\n")
    response_str = response_str.strip("\r")
    # print(f"response_str: {response_str}")

    return dfc.parse_angle_string_to_dict(response_str)


def get_arduino_serial_connection(
    com_port=ARDUINO_COM_PORT, arduino_baudrate=BAUD_RATE
):
    return serial.Serial(com_port, baudrate=arduino_baudrate, dsrdtr=False)
