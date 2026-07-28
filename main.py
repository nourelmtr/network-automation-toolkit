from inventory.loader import load_inventory, validate_inventory
from ping.ping import ping_device
from reports.csv_report import generate_csv_report


def main():
    inventory = load_inventory("inventory/devices.yaml")

    if not inventory:
        return

    try:
        validate_inventory(inventory)

        # Store all ping results for the CSV report
        report_data = []

        print("===== Network Inventory =====\n")

        for device in inventory["devices"]:

            # Ping the device
            ping_result = ping_device(device["ip"])

            # Display device information
            print(f"Name    : {device['name']}")
            print(f"IP      : {device['ip']}")
            print(f"Type    : {device['device_type']}")
            print(
                f"Status  : {'Reachable' if ping_result['reachable'] else 'Unreachable'}"
            )

            # Display latency if available
            if ping_result["latency"]:
                print(f"Latency : {ping_result['latency']}")

            print("-" * 30)

            # Save the results for the CSV report
            report_data.append({
                "name": device["name"],
                "ip": device["ip"],
                "device_type": device["device_type"],
                "reachable": ping_result["reachable"],
                "latency": ping_result["latency"]
            })

        # Generate the CSV report
        generate_csv_report(report_data)

        print("\nCSV report generated successfully!")

    except ValueError as error:
        print(f"Inventory Error: {error}")


if __name__ == "__main__":
    main()