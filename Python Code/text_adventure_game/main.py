from item import Item
from inventory import Inventory

def display_menu():
    print("\nInventory Management System")
    print("1. Add an Item")
    print("2. Update Item Quantity")
    print("3. Show Inventory")
    print("4. Exit")

def main():
    inventory = Inventory()
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == "1":
            try:
                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))
                item = Item(item_id, name, quantity, price)
                inventory.add_item(item)
                print("Item added successfully")
            except ValueError as e:
                print(f"Invalid input: {e}")
        elif choice == "2":
            item_id = input("Enter item ID: ")
            try:
                amount = int(input("Enter amount to update: "))
                if inventory.update_item(item_id, amount):
                    print("Item quantity updated successfully")
                else:
                    print("Item not found")
            except ValueError as e:
                print(f"Invalid input: {e}")
        elif choice == "3":
            inventory.show_inventory()
        elif choice == "4":
            print("Exiting program")
            break
        else:
            print("Invalid option, please try again")

    
