FUNCTION bubble_sort(array):
    SET n = LENGTH(array)

    FOR i FROM 0 to n - 1:
        // Loop through the entire array n times
        FOR j FROM 0 to n - i - 2:
            // Compare adjacent elements
            IF array[j] > array[j + 1]:
            // Swap elements if out of order
            TEMP = array[j]
            array[j] = array[j + 1]
            array[j + 1] = TEMP

    RETURN array