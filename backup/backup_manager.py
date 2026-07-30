from datetime import datetime
import os


def save_backup(device_name, configuration):
    """
    Save the running configuration of a device to a timestamped file.
    """

    os.makedirs("backup", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"backup/{device_name}_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(configuration)

    print(f"[+] Backup saved: {filename}")

    return filename