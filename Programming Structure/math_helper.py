def calculate_stats(numbers):
    """Calculate basic statistics for a list of numbers.
    Returns: total, average, minimum, maximum"""
    if not numbers:
        raise ValueError("List cannot be empty")
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, average, minimum, maximum