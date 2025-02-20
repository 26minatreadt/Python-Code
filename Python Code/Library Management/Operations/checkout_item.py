# operations/checkout_item.py

from models.member import Member

def checkout_item(library_collection, members):
    print("\n--- Check Out Item ---")
    member_id = input("Enter Member ID: ")
    member = next((m for m in members if m.member_id == member_id), None)

    if not member:
        print("Member not found. Please register first.\n")
        return

    item_id = input("Enter Item ID to check out: ")
    item = next((i for i in library_collection if i.item_id == item_id), None)

    if not item:
        print("Item not found.\n")
        return

    member.borrow_item(item)
    print()