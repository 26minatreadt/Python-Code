while True:
    user_input = input("Please enter a number: ")
    try:
        number = int(user_input)  # Attempt to convert input to an integer
        print(f"Thank you! You entered the number: {number}")
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Invalid input. Please enter a valid number.")
