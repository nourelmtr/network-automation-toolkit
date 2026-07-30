from ssh.ssh_client import execute_command
from backup.backup_manager import save_backup


def backup_device(connection, device):
    """
    Retrieve the running configuration from a device
    and save it as a backup.
    """

    configuration = execute_command(
        connection,
        "show running-config"
    )

    if configuration:
        save_backup(device["name"], configuration)
        return True

    return False