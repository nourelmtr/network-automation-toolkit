from inventory.loader import load_inventory, validate_inventory

inventory = load_inventory("inventory/devices.yaml")

if inventory:
    try:
        validate_inventory(inventory)

        print("===== Network Inventory =====\n")

        for device in inventory["devices"]:
            print(f"Name : {device['name']}")
            print(f"IP   : {device['ip']}")
            print(f"Type : {device['device_type']}")
            print("-" * 30)

    except ValueError as error:
        print(f"Inventory Error: {error}")