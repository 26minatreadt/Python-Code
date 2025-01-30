import math

def jump_search(arr, target):
    size = len(arr)
    step = int(math.sqrt(size))

    previous = 0

    while previous < size & arr[min(step, size) - 1] < target:
        previous = step
        step += int(math.sqrt(size))
        if previous >= size:
            return -1
        
    for i in range(previous, min(step, size)):
        if arr[i] == target:
            return i    
    return "Not Found"  
    
arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
target = 18
result = jump_search(arr, target)

print(f"Element {target} is at index: {result}" if result != -1 else "Element not found")