import socket
import time


class UDPServer:
    def __init__(self, host: str, port: int, communication_mode: str):
        self.host = host
        self.port = port
        self.communication_mode = communication_mode

        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((host, port))
        self.int_msg_dimension = 2

        # Metrics
        self.protocol = "UDP"
        self.number_of_messages_read = 0
        self.number_of_bytes_read = 0

    def read_message(self, number_of_bytes: int):
        size = number_of_bytes
        if size == -1:
            size = self.int_msg_dimension

        message, address = self.socket.recvfrom(size)

        self.number_of_messages_read += 1
        self.number_of_bytes_read += len(message)

        if self.communication_mode == "STOP_AND_WAIT":
            self.send_acknowledge(address)

        return message, address

    def send_acknowledge(self, address):
        print("Sending acknowledge...")

        ack_flag = 1
        # time.sleep(10)
        self.socket.sendto(ack_flag.to_bytes(self.int_msg_dimension, "big"), address)
        time.sleep(0.000001)

    def communicate_with_client(self):
        number_of_bytes = -1

        while True:
            print("Waiting for client...")

            message, address = self.read_message(number_of_bytes)
            print(f"Received message from {address}")

            if len(message) == self.int_msg_dimension:
                print("Message received represents number of bytes.")
                print(f"Bytes received: {message}")
                message = int.from_bytes(message, "big")
                print(f"Bytes are equal to value of {message}")
                number_of_bytes = message
            else:
                print("Message received represents part of image.")
                number_of_bytes = -1

                if self.is_end_stream_flag(number_of_bytes, message):
                    break

    def is_end_stream_flag(self, message_size: int, message) -> bool:
        if message_size != 3:
            return False

        end_stream_flag = "END"
        message_str = message.decode("utf-8")
        return message_str == end_stream_flag

    def print_metrics(self):
        print("=======================================")
        print(f"Used protocol: {self.protocol}")
        print(f"Communication mechanism: {self.communication_mode}")
        print(f"I've read {self.number_of_messages_read} messages")
        print(f"I've read {self.number_of_bytes_read} bytes")
        print("=======================================")
