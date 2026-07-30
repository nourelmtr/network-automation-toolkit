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


def main():

    # Initialize the logger
    logger = setup_logger()
    logger.info("Starting Network Automation Toolkit")

    inventory = load_inventory("inventory/devices.yaml")

    if not inventory:
        logger.error("Failed to load inventory.")
        return

    logger.info("Inventory loaded successfully.")

    try:
        validate_inventory(inventory)

        # Store all results for the CSV report
        report_data = []

        print("===== Network Inventory =====\n")

        for device in inventory["devices"]:

            # ---------------------------------
            # Ping the device
            # ---------------------------------
            ping_result = ping_device(device["ip"])

            print(f"Name    : {device['name']}")
            print(f"IP      : {device['ip']}")
            print(f"Type    : {device['device_type']}")
            print(
                f"Status  : {'Reachable' if ping_result['reachable'] else 'Unreachable'}"
            )

            if ping_result["latency"]:
                print(f"Latency : {ping_result['latency']}")

            # Log the ping result
            logger.info(
                f"{device['name']} - "
                f"{'Reachable' if ping_result['reachable'] else 'Unreachable'}"
            )

            # ---------------------------------
            # SSH Connection
            # ---------------------------------
            connection = connect_to_device(device)

            if connection:

                print("\nSSH Connection : Successful")
                logger.info(f"SSH connection established with {device['name']}")

                print("\nExecuting command: show version\n")

                output = execute_command(connection, "show version")

                if output:
                    print(output)
                    logger.info(f"'show version' executed on {device['name']}")

                # Backup configuration
                backup_device(connection, device)
                logger.info(f"Backup completed for {device['name']}")

                # Disconnect
                disconnect_device(connection)
                logger.info(f"Disconnected from {device['name']}")

            else:

                print("\nSSH Connection : Failed")
                logger.error(f"SSH connection failed for {device['name']}")

                # Temporary backup until GNS3 migration
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

            print("-" * 40)

            # ---------------------------------
            # Save data for CSV report
            # ---------------------------------
            report_data.append(
                {
                    "name": device["name"],
                    "ip": device["ip"],
                    "device_type": device["device_type"],
                    "reachable": ping_result["reachable"],
                    "latency": ping_result["latency"],
                }
            )

        # ---------------------------------
        # Generate CSV Report
        # ---------------------------------
        generate_csv_report(report_data)

        logger.info("CSV report generated successfully.")

        print("\nCSV report generated successfully!")

    except ValueError as error:
        logger.error(error)
        print(f"Inventory Error: {error}")


if __name__ == "__main__":
    main()