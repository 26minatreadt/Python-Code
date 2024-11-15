class LibraryItem:
    def __init__(self, item_id, title, author, publication_year):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"Item '{self.title}' has been checked out.")
        else:
            print(f"Item '{self.title}' is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"Item '{self.title}' has been returned.")
        else:
            print(f"Item '{self.title}' was not checked out.")

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return (f"ID: {self.item_id}, Title: {self.title}, Author: {self.author}, "
                f"Year: {self.publication_year}, Status: {status}")