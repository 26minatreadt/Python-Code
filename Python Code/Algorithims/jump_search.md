import math

FUNCTION JumpSearch(Array, Target):
    1. Determine the total number of elements in the array:
       SET Size = LENGTH(Array)

    2. Calculate the optimal jump step:
       SET Step = FLOOR(SQUARE_ROOT(Size))

    3. Initialize a variable to track the last checked position:
       SET Previous = 0

    4. **Jumping Phase** (Move ahead in steps):
       WHILE Previous < Size AND Array[MIN(Step, Size) - 1] < Target:
           - Update Previous to current Step position
           - Increase Step by INT(SQUARE_ROOT(Size))
           - IF Previous exceeds the array size, RETURN "Not Found"

    5. **Linear Search Phase** (Search within the identified block):
       FOR i FROM Previous TO MIN(Step, Size) - 1:
           - IF Array[i] == Target:
               RETURN i  // Found Target at index i

    6. IF the loop completes and the Target is not found:
       RETURN "Not Found"

Below is real code:
arr = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
target = 18
result = jump_search(arr, target)

 print(f"Element {target} is at index: {result}" if result != -1 else "Element not found")