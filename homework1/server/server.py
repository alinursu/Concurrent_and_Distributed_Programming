from src import configuration
from src.TCPServer import TCPServer
from src.UDPServer import UDPServer


def main():
    print("This is the server.")

    # Configuration
    host = "127.0.0.1"
    port = 65432

    # Console input
    communication_type, communication_mode = configuration.get_configuration_from_console_input()
    print(f"Server will communicate with the client using the {communication_type} protocol and the {communication_mode} mechanism")

    # Creation of server
    print("Creating server...")
    server = TCPServer(host, port, communication_mode) if communication_type == "TCP" \
        else UDPServer(host, port, communication_mode)

    # Wait for and communicate with client
    try:
        server.communicate_with_client()
    except Exception as e:
        print(e)

    # Print metrics
    server.print_metrics()


if __name__ == "__main__":
    main()