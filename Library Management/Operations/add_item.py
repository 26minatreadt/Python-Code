from models import Book, DVD, Magazine  # Importing necessary classes

def add_item(library_collection):
    # Display item types to add
    print("Select item type to add: Book, Magazine, DVD")
    user_choice = input("Enter your choice: ")

    # Get common item details
    item_id = input("Enter item ID: ")
    title = input("Enter title: ")
    author = input("Enter author or director: ")
    publication_year = input("Enter publication year: ")

    if user_choice.lower() == "book":
        genre = input("Enter genre: ")
        isbn = input("Enter ISBN: ")
        new_item = Book(item_id, title, author, publication_year, genre, isbn)  # Create Book instance
    elif user_choice.lower() == "magazine":
        issue_number = input("Enter issue number: ")
        month = input("Enter month: ")
        new_item = Magazine(item_id, title, author, publication_year, issue_number, month)  # Create Magazine instance
    elif user_choice.lower() == "dvd":
        duration = input("Enter duration: ")
        rating = input("Enter rating: ")
        new_item = DVD(item_id, title, author, publication_year, duration, rating)  # Create DVD instance
    else:
        print("Invalid choice. Exiting function.")
        return  # Exit function

    library_collection.append(new_item)  # Add the new item to library_collection
    print("Item added successfully!")  # Display success message