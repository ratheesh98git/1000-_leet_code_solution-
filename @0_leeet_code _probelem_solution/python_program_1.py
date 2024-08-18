#1 In the array find the second largest number 
#input [5,10,15,2,4,6,20,16,2,16]
#output 16

def find_second_largest(arr):
    # Check if the array has fewer than 2 elements
    if len(arr)< 2:
        return None
    
    # Initialize variables to store the largest and second largest numbers
    first_largest = second_largest = -3  # Using -3 as the initial value
    
    # Iterate through the array
    for num in arr:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    
    # If second_largest is still -3, it means there was no valid second largest number
    if second_largest == -3:
        return None
    
    return second_largest

# Test case
input_var = [5, 10, 15, 2, 4, 6, 20, 16, 2, 16]
output = find_second_largest(input_var)
print(f'This is the output variable: {output}')