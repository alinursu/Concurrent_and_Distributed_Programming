import socket
import time


class TCPServer:
    def __init__(self, host: str, port: int, communication_mode: str):
        self.host = host
        self.port = port
        self.communication_mode = communication_mode

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen()
        self.int_msg_dimension = 2

        # Metrics
        self.protocol = "TCP"
        self.number_of_messages_read = 0
        self.number_of_bytes_read = 0
        self.zero_bytes_messages_number = 0

    def read_message(self, conn, number_of_bytes: int):
        message = conn.recv(number_of_bytes)

        self.number_of_messages_read += 1
        self.number_of_bytes_read += len(message)

        if self.communication_mode == "STOP_AND_WAIT":
            self.send_acknowledge(conn)

        return message

    def send_acknowledge(self, conn):
        # print("Sending acknowledge...")

        ack_flag = 1
        # time.sleep(10)
        try:
            conn.send(ack_flag.to_bytes(self.int_msg_dimension, "big"))
            time.sleep(0.000001)
        except:
            pass

    def communicate_with_client(self):
        print("Waiting for client...")
        conn, addr = self.socket.accept()

        with conn:
            print(f"Connected by {addr}")

            while True:
                bytearray_size = self.read_message(conn, self.int_msg_dimension)
                # print(f"Received bytes: {bytearray_size}")

                bytearray_size = int.from_bytes(bytearray_size, "big")
                # print(f"Bytes are equal to value of {bytearray_size}")

                if bytearray_size == 0:
                    # print("Received 0 bytes")
                    self.zero_bytes_messages_number += 1

                    if self.zero_bytes_messages_number == 1000:
                        print("Received too many 0 bytes messages")
                        break

                # print(f"Reading {bytearray_size} bytes, the image.")
                message = self.read_message(conn, bytearray_size)  # Read image as bytearray

                if self.is_end_stream_flag(bytearray_size, message):
                    break

    def is_end_stream_flag(self, message_size: int, message) -> bool:
        if message_size != 3:
            return False

        end_stream_flag = "END"
        try:
            message_str = message.decode("utf-8")
            return message_str == end_stream_flag
        except:
            print("Exception thrown while checking end stream flag")
            return True

    def print_metrics(self):
        print("=======================================")
        print(f"Used protocol: {self.protocol}")
        print(f"Communication mechanism: {self.communication_mode}")
        print(f"I've read {self.number_of_messages_read} messages")
        print(f"I've read {self.number_of_bytes_read} bytes")
        print("=======================================")
