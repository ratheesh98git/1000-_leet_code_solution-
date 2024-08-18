#this is leet code program python_program 	 4.py 
def find_top_k_largest(arr, k):
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
    
    # Initialize a list to store the k largest numbers found so far
    k_largest = [-float('inf')] * k
    
    # Iterate over the sorted list to get the top k largest numbers
    for i in range(min(k, len(unique_list))):
        k_largest[i] = unique_list[i]
    
    return k_largest

# Test case to find the top 6 largest unique numbers
input_var = [5, 10, 15, 2, 4, 6, 20, 16, 2, 16]
k = 6  # Change this value to find the top k largest elements
output = find_top_k_largest(input_var, k)
print(f'The top {k} largest unique elements are: {output}')
