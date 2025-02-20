from models.member import Member
from Operations.add_item import add_item
from Operations.search_item import search_item
from Operations.checkout_item import checkout_item
from Operations.return_item import return_item
from Utils.helper import generate_unique_id, validate_email


def display_main_menu():
    print("=== Library Management System ===")
    print("1. Add New Item")
    print("2. Search Items")
    print("3. Register New Member")
    print("4. Check Out Item")
    print("5. Return Item")
    print("6. View Members")
    print("7. View All Items")
    print("8. Exit")

def register_member(members):
    # --- Register New Member ---
    member_id = generate_unique_id([m.member_id for m in members], prefix='MEM')
    name = input("Enter Member Name: ")
    email = input("Enter Member Email: ")

    if not validate_email(email):
        print("Invalid email format. Registration failed.\n")
        return

    new_member = Member(member_id, name, email)  # Assuming Member takes these arguments
    members.append(new_member)
    print(f"Member '{name}' registered successfully with Member ID: {member_id}\n")


def view_members(members):
    # --- Registered Members ---
    if not members:  # Check if the members list is empty
        print("No members registered yet.\n")
        return
    for member in members:
        print(member)
    print()


def view_all_items(library_collection):
    print("\n--- Library Collection ---")
    if not library_collection:
        print("No items in the library.\n")
        return
    for item in library_collection:  # Iterate through the library collection
        print(item)
    print()


def main():
    library_collection = []
    members = []

    while True:
        display_main_menu()
        choice = input("Select an option (1-8): ")

        if choice == '1':
            add_item(library_collection)  # Pass the library collection to add_item
        elif choice == '2':
            search_item(library_collection)  # Pass the library collection to search_item
        elif choice == '3':
            register_member(members)  # Pass the members list to register_member
        elif choice == '4':
            checkout_item(library_collection, members)  # Pass the library collection and members list to checkout_item
        elif choice == '5':
            return_item(library_collection, members)  # Pass the library collection and members list to return_item
        elif choice == '6':
            view_members(members)  # Pass the members list to view_members
        elif choice == '7':
            view_all_items(library_collection)  # Pass the library collection to view_all_items
        elif choice == '8':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")


if __name__ == "__main__":
    main()