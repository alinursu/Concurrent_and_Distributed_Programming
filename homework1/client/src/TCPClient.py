import datetime
import math
import socket
import time

from src.image_handler import read_image_as_bytearray


class TCPClient:
    def __init__(self, host: str, port: int, communication_mode: str):
        self.host = host
        self.port = port
        self.communication_mode = communication_mode

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.int_msg_dimension = 2

        # Metrics
        self.protocol = "TCP"
        self.number_of_messages_sent = 0
        self.number_of_bytes_sent = 0
        self.start_time = 0
        self.end_time = 0

    def send_message(self, bytes):
        # print("Sending byte message to server...")
        self.socket.send(bytes)
        time.sleep(0.000001)

        self.number_of_messages_sent += 1
        self.number_of_bytes_sent += len(bytes)

        if self.communication_mode == "STOP_AND_WAIT":
            self.await_acknowledge()

    def await_acknowledge(self):
        # print("Awaiting acknowledge...")
        self.socket.recv(self.int_msg_dimension)

    def communicate_with_server(self, images: list[dict]):
        print("Connecting to server...")
        self.socket.connect((self.host, self.port))
        print("Connected!")

        self.start_time = datetime.datetime.now()

        for image in images:
            image_as_bytes: bytearray = read_image_as_bytearray(image['path'])
            bytearray_size = len(image_as_bytes)

            # print(f"Image as bytearray has a size of {bytearray_size} bytes")

            message_size = 4096
            for i in range(0, math.ceil(bytearray_size / message_size)):
                start_index = i * message_size
                stop_index = min(bytearray_size, (i+1) * message_size)

                partition_size: int = stop_index - start_index
                self.send_message(partition_size.to_bytes(self.int_msg_dimension, "big"))
                self.send_message(image_as_bytes[start_index:stop_index])

        print("Sending end stream flag...")
        self.send_end_stream_flag()

        self.end_time = datetime.datetime.now()

    def send_end_stream_flag(self):
        end_stream_flag = "END"
        end_stream_size = 3
        self.send_message(end_stream_size.to_bytes(self.int_msg_dimension, "big"))
        self.send_message(end_stream_flag.encode("utf-8"))

    def print_metrics(self):
        print("=======================================")
        print(f"Used protocol: {self.protocol}")
        print(f"Communication mechanism: {self.communication_mode}")
        print(f"I've sent {self.number_of_messages_sent} messages")
        print(f"I've sent {self.number_of_bytes_sent} bytes")
        print(f"Time elapsed: {self.end_time - self.start_time}")
        print("=======================================")
