# operations/return_item.py

from models.member import Member

def return_item(library_collection, members):
    print("\n--- Return Item ---")
    member_id = input("Enter Member ID: ")
    member = next((m for m in members if m.member_id == member_id), None)

    if not member:
        print("Member not found. Please register first.\n")
        return

    item_id = input("Enter Item ID to Return out: ")
    item = next((i for i in library_collection if i.item_id == item_id), None)

    if not item:
        print("Item not found.\n")
        return

    member.return_item(item)
    print()