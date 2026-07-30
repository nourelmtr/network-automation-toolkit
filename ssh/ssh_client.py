from netmiko import ConnectHandler
from netmiko.exceptions import (
    NetmikoAuthenticationException,
    NetmikoTimeoutException,
)


def connect_to_device(device):
    """
    Establish an SSH connection to a network device.
    """

    try:
        connection = ConnectHandler(
            device_type=device["device_type"],
            host=device["ip"],
            username=device["username"],
            password=device["password"],
        )

        print(f"[+] Connected to {device['name']}")

        return connection

    except NetmikoAuthenticationException:
        print(f"[-] Authentication failed for {device['name']}")

    except NetmikoTimeoutException:
        print(f"[-] Connection timeout to {device['name']}")

    except Exception as error:
        print(f"[-] Unexpected error: {error}")

    return None


def execute_command(connection, command):
    """
    Execute a command on the remote device.
    """

    try:
        return connection.send_command(command)

    except Exception as error:
        print(f"[-] Command failed: {error}")
        return None


def disconnect_device(connection):
    """
    Close the SSH connection.
    """

    if connection:
        connection.disconnect()