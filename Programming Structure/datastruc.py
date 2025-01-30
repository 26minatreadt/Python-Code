# Define a list with predefined numerical values
numbers = [5, 3, 8, 1, 2]

# Print the original list
print("Original list:", numbers)

# Sort the list in ascending order and print it
numbers.sort()
print("Sorted list in ascending order:", numbers)

# Modify the program to allow user input
user_numbers = []
print("Enter numerical values (press Enter without typing a number to finish):")

while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break  # Exit the loop if the input is empty
    try:
        number = float(user_input)  # Convert input to float
        user_numbers.append(number)  # Add to the list
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Sort and display the user-provided list in ascending order
user_numbers.sort()
print("User-provided list sorted in ascending order:", user_numbers)

# Sort the list in descending order and print it
user_numbers.sort(reverse=True)
print("User-provided list sorted in descending order:", user_numbers)
