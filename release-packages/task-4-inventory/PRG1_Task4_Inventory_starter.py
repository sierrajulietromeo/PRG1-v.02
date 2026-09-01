"""
Inventory Tracker

Tracks stock levels for a small warehouse. This program already
works: it can create an inventory, add stock, and look up how much
of an item is currently held.

The warehouse also needs to be able to remove stock when items are
shipped out, and to flag items that are running low. That part is
not built yet: it is your job to add it, using the functions already
here rather than working around them.
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

    Use get_quantity to check the current stock level; do not read
    inventory[item_name] directly, since the item might not exist yet.
    """
    pass


def low_stock_items(inventory, threshold):
    """Return a list of every item name in inventory whose quantity is
    at or below threshold."""
    pass


if __name__ == "__main__":
    inventory = create_inventory()
    add_stock(inventory, "Widget", 10)
    add_stock(inventory, "Gadget", 2)
    print(f"Widget stock: {get_quantity(inventory, 'Widget')}")
    print(f"Gadget stock: {get_quantity(inventory, 'Gadget')}")
