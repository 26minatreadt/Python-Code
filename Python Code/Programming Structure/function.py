def modify_number(num):
    """Function that modifies a single number by adding 10."""
    return num + 10

# Main program to test the function with various inputs
result1 = modify_number(5)
result2 = modify_number(10)
result3 = modify_number(-3)

print(f"Results of modify_number with different inputs: {result1}, {result2}, {result3}")

def modify_two_numbers(num1, num2):
    """Function that modifies two numbers by multiplying them and adding 5."""
    return (num1 * num2) + 5

# Testing the modified function with pairs of numbers
result4 = modify_two_numbers(2, 3)
result5 = modify_two_numbers(0, 10)
result6 = modify_two_numbers(-1, -1)

print(f"Results of modify_two_numbers with different pairs: {result4}, {result5}, {result6}")
