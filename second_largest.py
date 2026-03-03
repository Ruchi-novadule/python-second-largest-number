numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if len(numbers) < 2:
    print("List must contain at least two elements")
else:
    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        print("No second largest element found")
    else:
        print("Second largest number is:", second_largest)
