FUNCTION binary_search(array, target):
    SET low = 0
    SET high = LENGTH(array) - 1

    WHILE low <= high:
        SET mid = (low + high) // 2 //calculate the middle index

        IF array[mid] == target:
            RETURN mid // Target found index mid

        ELSE IF array[mid] < target:
            SET low = mid + 1 // Target is in the right half

        ELSE:
            SET high = mid - 1 // Target is in the left half

    RETURN -1  // Targetnot found