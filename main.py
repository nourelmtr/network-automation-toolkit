from inventory.loader import load_inventory, validate_inventory
from ping.ping import ping_device


inventory = load_inventory("inventory/devices.yaml")

if inventory:
    try:
        validate_inventory(inventory)

        print("===== Network Inventory =====\n")

        for device in inventory["devices"]:

            # Ping the device
            ping_result = ping_device(device["ip"])

            # Display device information
            print(f"Name   : {device['name']}")
            print(f"IP     : {device['ip']}")
            print(f"Type   : {device['device_type']}")

            # Display ping status
            print(
                f"Status : {'Reachable' if ping_result['reachable'] else 'Unreachable'}"
            )

            print("-" * 30)

    except ValueError as error:
        print(f"Inventory Error: {error}")