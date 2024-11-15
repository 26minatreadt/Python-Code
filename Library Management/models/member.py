class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_items = []

    def borrow_item(self, item):
        if not item.is_checked_out:
            item.is_checked_out = True
            self.borrowed_items.append(item)
            print(f"Item '{item.title}' has been borrowed by {self.name}.")
        else:
            print(f"Item '{item.title}' is currently unavailable.")

    def return_item(self, item):
        if item in self.borrowed_items:
            item.is_checked_out = False
            self.borrowed_items.remove(item)
            print(f"Item '{item.title}' has been returned by {self.name}.")
        else:
            print(f"Item '{item.title}' was not borrowed by {self.name}.")

    def __str__(self):
        borrowed_titles = ', '.join(item.title for item in self.borrowed_items)
        return f"Member ID: {self.member_id}, Name: {self.name}, Email: {self.email}, Borrowed Items: {borrowed_titles}"
