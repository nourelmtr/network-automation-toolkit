import yaml


def load_inventory(file_path):
    """
    Load the device inventory from a YAML file.
    """

    try:
        with open(file_path, "r") as file:
            inventory = yaml.safe_load(file)

        if inventory is None:
            raise ValueError("Inventory file is empty.")

        return inventory

    except FileNotFoundError:
        print(f"Error: '{file_path}' was not found.")
        return None

    except yaml.YAMLError as error:
        print(f"YAML Error: {error}")
        return None

    except ValueError as error:
        print(error)
        return None
def validate_inventory(inventory):
    """
    Validate the inventory structure.
    """

    required_fields = [
        "name",
        "ip",
        "username",
        "password",
        "device_type"
    ]

    for device in inventory["devices"]:

        for field in required_fields:

            if field not in device:
                raise ValueError(
                    f"Device '{device.get('name', 'Unknown')}' is missing '{field}'."
                )

    return True