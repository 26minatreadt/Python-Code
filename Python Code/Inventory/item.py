# item.py

class Item:
    def __init__(self, item_id, name, quantity, price):
        """
        Initializes a new Item instance.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the item.
            quantity (int): Quantity of the item in stock.
            price (float): Price of the item.
        """
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount):
        """
        Updates the quantity of the item.

        Args:
            amount (int): The amount to add or remove from the current quantity.
        """
        self.quantity += amount

    def __str__(self):
        """
        Returns a string representation of the item.

        Returns:
            str: Formatted string with item details.
        """
        return f"{self.name} (ID: {self.item_id}): {self.quantity} in stock, ${self.price} each"
