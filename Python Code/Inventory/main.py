
# main.py

from item import Item
from inventory import Inventory

def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\nInventory Management System")
    print("---------------------------")
    print("1. Add an item")
    print("2. Update item quantity")
    print("3. Show inventory")
    print("4. Exit")

def main():
    """
    The main function that runs the inventory management system.
    """
    inventory = Inventory()
    
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            # Add a new item to the inventory
            try:
                item_id = int(input("Enter item ID: "))
                name = input("Enter item name: ")
                quantity = int(input("Enter item quantity: "))
                price = float(input("Enter item price: "))
                
                # Create an Item object
                item = Item(item_id, name, quantity, price)
                
                # Add the item to the inventory
                inventory.add_item(item)
            except ValueError:
                print("Invalid input. Please enter numeric values for ID, quantity, and price.")
        
        elif choice == '2':
            # Update the quantity of an existing item
            try:
                item_id = int(input("Enter item ID to update: "))
                amount = int(input("Enter quantity to add/remove: "))
                
                # Update the item's quantity
                updated = inventory.update_item(item_id, amount)
                if not updated:
                    print("Please try again with a valid item ID.")
            except ValueError:
                print("Invalid input. Please enter numeric values for ID and quantity.")
        
        elif choice == '3':
            # Show all items in the inventory
            inventory.show_inventory()
        
        elif choice == '4':
            # Exit the program
            print("Exiting the Inventory Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()