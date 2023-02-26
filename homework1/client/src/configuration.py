def get_communication_type_user_input() -> str:
    print("What kind of communication you want to establish?")
    print("1 - TCP")
    print("2 - UDP")

    response = ""
    while response == "":
        response = input(" >> ")
        try:
            resp_int = int(response)
            if resp_int not in [1, 2]:
                print("Invalid input: %s. Needs to be 1 or 2!" % response)
                response = ""
        except:
            print("Invalid input: %s. Needs to be an integer value!" % response)
            response = ""

    resp_int = int(response)
    if resp_int == 1:
        return "TCP"

    return "UDP"


def get_communication_mode_user_input() -> str:
    print("How should the communication be performed?")
    print("1 - Streaming mechanism")
    print("2 - Stop-and-wait mechanism")

    response = ""
    while response == "":
        response = input(" >> ")
        try:
            resp_int = int(response)
            if resp_int not in [1, 2]:
                print("Invalid input: %s. Needs to be 1 or 2!" % response)
                response = ""
        except:
            print("Invalid input: %s. Needs to be an integer value!" % response)
            response = ""

    resp_int = int(response)
    if resp_int == 1:
        return "STREAMING"

    return "STOP_AND_WAIT"


def get_configuration_from_console_input() -> (str, str):
    communication_type: str = get_communication_type_user_input()
    communication_mode: str = get_communication_mode_user_input()

    return communication_type, communication_mode
