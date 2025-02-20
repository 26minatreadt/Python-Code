from .library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, item_id, title, author, publication_year, genre, isbn):
        super().__init__(item_id, title, author, publication_year)
        self.genre = genre
        self.isbn = isbn

    def __str__(self):
        return f"{super().__str__()} - Genre: {self.genre}, ISBN: {self.isbn}"

