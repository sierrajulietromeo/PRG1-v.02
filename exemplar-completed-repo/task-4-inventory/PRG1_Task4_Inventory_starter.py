"""
Inventory Tracker

Tracks stock levels for a small warehouse.
"""


def create_inventory():
    """Return a new, empty inventory."""
    return {}


def add_stock(inventory, item_name, quantity):
    """Add quantity units of item_name to inventory, creating the entry
    if it does not already exist. Changes inventory in place."""
    inventory[item_name] = inventory.get(item_name, 0) + quantity


def get_quantity(inventory, item_name):
    """Return the quantity of item_name in inventory, or 0 if it is not
    in the inventory at all."""
    return inventory.get(item_name, 0)


def remove_stock(inventory, item_name, quantity):
    """Remove quantity units of item_name from inventory, if there is
    enough stock. Return True and update inventory if successful.
    Return False and leave inventory unchanged if there is not enough
    stock, or if item_name is not in the inventory at all.
    """
    current = get_quantity(inventory, item_name)
    if current >= quantity:
        inventory[item_name] = current - quantity
        return True
    return False


def low_stock_items(inventory, threshold):
    """Return a list of every item name in inventory whose quantity is
    at or below threshold."""
    result = []
    for item_name in inventory:
        if inventory[item_name] <= threshold:
            result.append(item_name)
    return result


if __name__ == "__main__":
    inventory = create_inventory()
    add_stock(inventory, "Widget", 10)
    add_stock(inventory, "Gadget", 2)
    print(f"Widget stock: {get_quantity(inventory, 'Widget')}")
    print(f"Gadget stock: {get_quantity(inventory, 'Gadget')}")
    remove_stock(inventory, "Widget", 8)
    print(f"Low stock items: {low_stock_items(inventory, 2)}")
