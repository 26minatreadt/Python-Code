from library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, item_id, title, author, publication_year, issue_number, month):
        super().__init__(item_id, title, author, publication_year)
        self.issue_number = issue_number
        self.month = month

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, Issue Number: {self.issue_number}, Month: {self.month}"
