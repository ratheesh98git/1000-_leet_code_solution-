"""38   

Interview Question:
Problem Statement: Given an array of integers, write a program to remove the first element and print the next element, then remove the next element and print the following element, and continue this pattern until you reach the end of the array.

Constraints:

You must not use built-in functions like pop() or remove().
The solution should handle arrays of any length.
Example:

Input: [2, 11, 13, 8, 6, 7, 8]
Expected Output:
Copy code
11
8
7
Solution Without Built-in Functions:
Here's how you can solve this problem without using any built-in functions:"""



arr = [2, 11, 13, 8, 6, 7, 8]

# Initialize the size of the array
n = len(arr)
index = 0  # Start from the first element

# Iterate while there are elements left to process
while index < n:
    # Shift elements to the left to "remove" the current element
    for i in range(index, n - 1):
        arr[i] = arr[i + 1]

    n -= 1  # Decrease the array size as we "remove" an element

    # Check if there's an element to print
    if index < n:
        print(arr[index])
        index += 1  # Move to the next element

