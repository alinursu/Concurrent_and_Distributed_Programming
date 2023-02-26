import datetime
import math
import socket
import time

from src.image_handler import read_image_as_bytearray


class UDPClient:
    def __init__(self, host: str, port: int, communication_mode: str):
        self.host = host
        self.port = port
        self.communication_mode = communication_mode

        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.int_msg_dimension = 2

        # Metrics
        self.protocol = "UDP"
        self.number_of_messages_sent = 0
        self.number_of_bytes_sent = 0
        self.start_time = 0
        self.end_time = 0

    def send_message(self, bytes):
        print("Sending byte message to server...")
        self.socket.sendto(bytes, (self.host, self.port))
        time.sleep(0.000001)

        self.number_of_messages_sent += 1
        self.number_of_bytes_sent += len(bytes)

        if self.communication_mode == "STOP_AND_WAIT":
            self.await_acknowledge()

    def await_acknowledge(self):
        print("Awaiting acknowledge...")
        self.socket.recvfrom(self.int_msg_dimension)

    def communicate_with_server(self, images: list[dict]):
        self.start_time = datetime.datetime.now()

        for image in images:
            image_as_bytes: bytearray = read_image_as_bytearray(image['path'])
            bytearray_size = len(image_as_bytes)

            print(f"Image as bytearray has a size of {bytearray_size} bytes")

            for i in range(0, math.ceil(bytearray_size / 65500)):
                start_index = i * 65500
                stop_index = min(bytearray_size, (i+1) * 65500)

                partition_size: int = stop_index - start_index
                self.send_message(partition_size.to_bytes(self.int_msg_dimension, "big"))
                self.send_message(image_as_bytes[start_index:stop_index])

        print("Sending end stream flag...")
        self.send_end_stream_flag()

        self.end_time = datetime.datetime.now()

    def send_end_stream_flag(self):
        end_stream_flag = 0
        self.send_message(end_stream_flag.to_bytes(self.int_msg_dimension, "big"))

    def print_metrics(self):
        print("=======================================")
        print(f"Used protocol: {self.protocol}")
        print(f"Communication mechanism: {self.communication_mode}")
        print(f"I've sent {self.number_of_messages_sent} messages")
        print(f"I've sent {self.number_of_bytes_sent} bytes")
        print(f"Time elapsed: {self.end_time - self.start_time}")
        print("=======================================")