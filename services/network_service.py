from inventory.loader import load_inventory, validate_inventory
from ping.ping import ping_device
from reports.csv_report import generate_csv_report
from ssh.ssh_client import (
    connect_to_device,
    execute_command,
    disconnect_device,
)
from backup.backup_manager import save_backup
from backup.backup_service import backup_device
from utils.logger import setup_logger

from configuration.config import (
    INVENTORY_FILE,
    SHOW_VERSION,
)


def run_ping():
    """
    Ping all devices and return the results.
    """

    logger = setup_logger()

    inventory = load_inventory(INVENTORY_FILE)

    if not inventory:
        logger.error("Failed to load inventory.")
        return []

    validate_inventory(inventory)

    report_data = []

    print("===== Network Inventory =====\n")

    for device in inventory["devices"]:

        ping_result = ping_device(device["ip"])

        print(f"Name    : {device['name']}")
        print(f"IP      : {device['ip']}")
        print(f"Type    : {device['device_type']}")
        print(
            f"Status  : {'Reachable' if ping_result['reachable'] else 'Unreachable'}"
        )

        if ping_result["latency"]:
            print(f"Latency : {ping_result['latency']}")

        print("-" * 40)

        logger.info(
            f"{device['name']} - "
            f"{'Reachable' if ping_result['reachable'] else 'Unreachable'}"
        )

        report_data.append(
            {
                "name": device["name"],
                "ip": device["ip"],
                "device_type": device["device_type"],
                "reachable": ping_result["reachable"],
                "latency": ping_result["latency"],
            }
        )

    return report_data


def run_ssh():
    """
    Connect to all devices through SSH and create backups.
    """

    logger = setup_logger()

    inventory = load_inventory(INVENTORY_FILE)

    if not inventory:
        logger.error("Failed to load inventory.")
        return

    validate_inventory(inventory)

    for device in inventory["devices"]:

        connection = connect_to_device(device)

        if connection:

            print("\nSSH Connection : Successful")
            logger.info(f"SSH connection established with {device['name']}")

            print(f"\nExecuting command: {SHOW_VERSION}\n")

            output = execute_command(connection, SHOW_VERSION)

            if output:
                print(output)
                logger.info(f"'{SHOW_VERSION}' executed on {device['name']}")

            backup_device(connection, device)
            logger.info(f"Backup completed for {device['name']}")

            disconnect_device(connection)
            logger.info(f"Disconnected from {device['name']}")

        else:

            print("\nSSH Connection : Failed")
            logger.error(f"SSH connection failed for {device['name']}")

            # Temporary backup until we migrate to GNS3
            sample_configuration = f"""
hostname {device['name']}

interface GigabitEthernet0/0
 ip address {device['ip']} 255.255.255.0
 no shutdown

ip ssh version 2

username admin privilege 15 secret admin123
"""

            save_backup(device["name"], sample_configuration)
            logger.info(f"Sample backup created for {device['name']}")


def run_report(report_data):
    """
    Generate the CSV report.
    """

    logger = setup_logger()

    generate_csv_report(report_data)

    logger.info("CSV report generated successfully.")

    print("\nCSV report generated successfully!")


def run_all():
    """
    Run the complete network automation workflow.
    """

    logger = setup_logger()
    logger.info("Starting Network Automation Toolkit")

    report_data = run_ping()

    run_ssh()

    run_report(report_data)