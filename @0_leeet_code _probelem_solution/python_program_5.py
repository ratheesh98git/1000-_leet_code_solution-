#this is leet code program python_program 	 5.py 
def find_kth_largest(arr, k):
    # Use a set to remove duplicates
    unique_elements = {}
    unique_list = []
    
    # Add unique elements to the list manually
    for i in range(len(arr)):
        if arr[i] not in unique_elements:
            unique_elements[arr[i]] = True
            unique_list.append(arr[i])
    
    # Sort the unique list manually (simple bubble sort for illustration)
    for i in range(len(unique_list)):
        for j in range(0, len(unique_list) - i - 1):
            if unique_list[j] < unique_list[j + 1]:
                unique_list[j], unique_list[j + 1] = unique_list[j + 1], unique_list[j]
    
    # Check if k is within the bounds of the unique list
    if k <= len(unique_list):
        return unique_list[k - 1]
    else:
        return None  # Return None if k is out of bounds

# Test case to find the k-th largest unique number
input_var = [5, 10, 15, 2, 4, 6, 20, 16, 2, 16]
k = 1  # Change this value to find the k-th largest element
output = find_kth_largest(input_var, k)
print(f'The {k}-th largest unique element is: {output}')
