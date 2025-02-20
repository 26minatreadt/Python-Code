from .library_item import LibraryItem  # Corrected import

class DVD(LibraryItem):
    def __init__(self, item_id, title, author, publication_year, duration, rating):
        super().__init__(item_id, title, author, publication_year)
        self.duration = duration
        self.rating = rating

    def __str__(self):
        return f"{super().__str__()} | Duration: {self.duration} | Rating: {self.rating}"