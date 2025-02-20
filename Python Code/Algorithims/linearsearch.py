def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

a = [10, 20, 30, 40, 50]
print(linear_search(a, 10)) 