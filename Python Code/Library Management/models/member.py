class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_items = []  # Initialize borrowed_items as an empty list

    def borrow_item(self, item):
        # Assuming 'item' has an 'is_checked_out' attribute
        if item.is_checked_out:
            item.check_out()  # Check out the item
            self.borrowed_items.append(item)  # Add item to borrowed_items
            print(f"{item} borrowed successfully.")  # Display borrowing confirmation
        else:
            print(f"{item} is unavailable.")  # Display item unavailable message

    def return_item(self, item):
        if item in self.borrowed_items:
            item.return_item()  # Return the item
            self.borrowed_items.remove(item)  # Remove from borrowed_items
            print(f"{item} returned successfully.")  # Display return confirmation
        else:
            print(f"{item} was not borrowed by this member.")  # Display item not borrowed message

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Email: {self.email}, Borrowed Items: {self.borrowed_items}"