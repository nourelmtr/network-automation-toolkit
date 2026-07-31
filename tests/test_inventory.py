from inventory.loader import load_inventory


def test_inventory_load():

    inventory = load_inventory("inventory/devices.yaml")

    assert inventory is not None

    assert "devices" in inventory

    assert len(inventory["devices"]) > 0