🔢 Second Largest Number in a List (Python)

This is a simple Python program that finds the second largest number in a list provided by the user.

📌 Features

Takes space-separated numbers as input

Finds second largest element without using sorting

Handles edge cases

Beginner-friendly logic

Interview-focused implementation

💻 Technology Used

Python 3

🚀 How It Works

Takes input as space-separated numbers.

Converts input into a list of integers.

Iterates through the list.

Keeps track of the largest and second largest values.

Prints the second largest number.

📝 Code
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
▶️ Example

Input:

10 5 20 8 15

Output:

Second largest number is: 15
🎯 Learning Concepts

List handling

Looping

Conditional logic

Basic algorithm thinking

Edge case handling
