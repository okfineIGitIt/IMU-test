import time

import serial

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

    while True:
        response = ser.read_until()
        response_str = response.decode("utf-8").rstrip("\n")
        print(f"response_str: {response_str}")
