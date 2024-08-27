#second largest element in the array
def find_second_largest(arr):
    # Check if the array has fewer than 2 elements
    # If it does, return None because we can't find a second-largest element
    if len(arr) < 2:
        return None
    
    # Initialize the largest element with the first element of the array
    largest = arr[0]
    # Initialize second_largest as None because we haven't found it yet
    second_largest = None
    
    # First loop: Traverse the array to find the largest element
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
        # Debug: Print the current status after each iteration
        print(f"After checking index {i}, largest is: {largest}")

    # Second loop: Traverse the array again to find the second-largest element
    for i in range(0, len(arr)):
        if arr[i] != largest:  # Skip the largest element
            if second_largest is None:  # If we haven't found a second-largest yet
                second_largest = arr[i]
            elif arr[i] > second_largest:  # If the current element is larger than second_largest
                second_largest = arr[i]
        # Debug: Print the current status after each iteration
        print(f"After checking index {i}, second_largest is: {second_largest}")
    
    return second_largest

# Example array
s = [1, 210, 5, 3, 2, 0]

# Call the function to find the second-largest element
second_largest = find_second_largest(s)

# Print the result
print("Second Largest Element:", second_largest)
