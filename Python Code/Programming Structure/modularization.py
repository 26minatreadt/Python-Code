from math_helper import calculate_stats

# Test data
test_data = [
    [10, 20, 30, 40, 50],
    [5, 15, 25],
    [100, 200, 300, 400],
    [],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
]

# Iterate over the test data and call the function
for data in test_data:
    try:
        total, average, minimum, maximum = calculate_stats(data)
        print(f"Statistics for {data}: Total = {total}, Average = {average}, Minimum = {minimum}, Maximum = {maximum}")
    except ValueError as e:
        print(f"Error processing {data}: {e}")
