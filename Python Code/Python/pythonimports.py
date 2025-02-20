# Using the math and random libraries
import math
import random

# print(math.sqrt(16))
# print(random.randint(1, 100))


# # Main File
# import custom_module

# print(custom_module.greet("Alice"))

# using the 'random' library to generate names

names = ["Alice", "Bob", "Charlie", "David"] # assigns names as data in an array
selected_name = random.choice(names) # picks a random name from the , names.
print(f"selected name: {selected_name}") #prints whatever the random name is

first_names = ["Alice", "Bob", "Charlie", "David"] # adds an array for first names
last_names = ["Johnson", "Smith", "Williams", "Jones"] #adds an array for last names

def generate_random_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

for _ in range(5):
    print(generate_random_name())