# inventory.py

from item import Item

class Inventory:
    def __init__(self):
        """
        Initializes a new Inventory instance with an empty dictionary to store items.
        """
        self.items = {}

    def add_item(self, item):
        """
        Adds an Item to the inventory.

        Args:
            item (Item): The Item object to add.
        """
        self.items[item.item_id] = item
        print(f"Item '{item.name}' added to inventory.")

    def update_item(self, item_id, amount):
        """
        Updates the quantity of an existing item in the inventory.

        Args:
            item_id (int): The ID of the item to update.
            amount (int): The amount to add or remove from the current quantity.

        Returns:
            bool: True if the item was updated, False if the item was not found.
        """
        if item_id in self.items:
            self.items[item_id].update_quantity(amount)
            print(f"Item ID {item_id} quantity updated by {amount}. New quantity: {self.items[item_id].quantity}")
            return True
        else:
            print(f"Item ID {item_id} not found in inventory.")
            return False

    def show_inventory(self):
        """
        Displays all items in the inventory. If the inventory is empty, and notifies the user.
        """
        if not self.items:
            print("The inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            print("------------------")
            for item in self.items.values():
                print(item)

