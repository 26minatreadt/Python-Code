# open and read a file
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("output.txt", "w") as file:
#     file.write("This is an example of a file being written to. \n")
#     file.write("You can write multiple lines at a time. \n")


# # Error handling
# try:
#     with open("nonexistent_file.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("Error: The file does not exist.")

# Simple gradebook program to store student grades in a file

# students = {"Alice": 85, "Bob": 90, "Charlie": 78}

# with open("grades.txt", "w") as file:
#     for name, grade in students.items():
#         file.write(f"{name}: {grade}\n")
# print("Grades have been saved to 'grades.txt'.")

