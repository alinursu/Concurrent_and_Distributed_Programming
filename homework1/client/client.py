import os

from src.image_handler import discover_images
from src import configuration
from src.TCPClient import TCPClient
from src.UDPClient import UDPClient


def main():
    print("This is the client.")

    # Configuration
    server_host = "3.65.197.254"
    server_port = 65432

    # Console input
    communication_type, communication_mode = configuration.get_configuration_from_console_input()
    print(f"Client will communicate with the server using the {communication_type} protocol and the {communication_mode} mechanism")

    # Discover images
    print("Discovering images on disk...")
    images: list[dict] = discover_images(os.path.join(".", "data"))
    print(f"Discovered {len(images)} images!")

    # Creation of client
    print("Creating client...")
    client = TCPClient(server_host, server_port, communication_mode) if communication_type == "TCP" \
        else UDPClient(server_host, server_port, communication_mode)

    # Connect to and communicate with server
    client.communicate_with_server(images)

    # Print metrics
    client.print_metrics()


if __name__ == "__main__":
    main()