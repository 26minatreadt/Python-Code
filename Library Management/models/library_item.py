class LibraryItem:
    def __init__(self, item_id, title, author, publication_year):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_checked_out = False  # Initialize as not checked out

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True  # Mark as checked out
            print(f"{self.title} has been checked out.")  # Confirmation message
        else:
            print(f"{self.title} is already checked out.")  # Already checked out message

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False  # Mark as available
            print(f"{self.title} has been returned.")  # Return confirmation
        else:
            print(f"{self.title} was not checked out.")  # Not checked out message

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Status: {status}"  # Item details