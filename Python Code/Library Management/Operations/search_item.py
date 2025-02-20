def search_item(library_collection):

    print("Search options: ")
    print("1: Title")
    print("2: Author/Director")
    
    user_choice = input("Choose your search option (1 or 2): ")
    
    if user_choice == '1':  # Search by Title
        title = input("Enter the title to search for: ").lower()
        results = [item for item in library_collection if title.lower() in item.title.lower()] 

    elif user_choice == '2':  # Search by Author/Director
        author = input("Enter the author or director to search for: ").lower()
        results = [item for item in library_collection if author.lower() in item.author.lower() or author.lower() in item.director.lower()]  
         
    else:
        print("Invalid choice. Please select either 1 or 2.")
        return  # Exit the function

    if results:
        print("Found items:")
        for item in results:
            print(f"Title: {item.title}, Author: {item.author}, Director: {item.director}")
    else:
        print("No items found matching your search.")
