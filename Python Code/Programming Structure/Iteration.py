start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start > end:
    print("Starting number should be less than or equal to the ending number.")
else:
    print("Even numbers between", start, "and", end, "are:")
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number)
