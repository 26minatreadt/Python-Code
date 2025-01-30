class Book:
    """Class representing a book."""
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_open = False  # Book is initially closed

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def open_book(self):
        self.is_open = True
        print(f"You opened the book: {self.title}")

    def close_book(self):
        self.is_open = False
        print(f"You closed the book: {self.title}")

    def status(self):
        return "open" if self.is_open else "closed"

# Creating instances of the Book class
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

# Interacting with the Book objects
print(book1)  # Should print the string representation
book1.open_book()  # Open the book
print(f"The book '{book1.title}' is currently {book1.status()}.")  # Check status

book1.close_book()  # Close the book
print(f"The book '{book1.title}' is currently {book1.status()}.")  # Check status

print(book2)  # Should print the string representation
book2.open_book()  # Open the book
print(f"The book '{book2.title}' is currently {book2.status()}.")  # Check status
