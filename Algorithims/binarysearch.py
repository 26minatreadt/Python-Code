def binary_search(arr, target):
    # Initialize the low and high pointers to the start and end of the array
    low, high = 0, len(arr) - 1
    
    # Continue searching while the low pointer is less than or equal to the high pointer
    while low <= high:
        # Calculate the middle index of the current search range
        mid = (low + high) // 2
        
        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Target found, return its index
        
        # If the middle element is less than the target, discard the left half
        elif arr[mid] < target:
            low = mid + 1  # Move the low pointer to the right of mid
        
        # If the middle element is greater than the target, discard the right half
        else:
            high = mid - 1  # Move the high pointer to the left of mid
    
    # If the target is not found, return -1
    return -1