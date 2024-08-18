#this is leet code program python_program 	 3.py 
def find_top_k_largest(arr, k):
    # Initialize a list to store the k largest numbers found so far
    k_largest = [-float('inf')] * k
    
    
    # Iterate over the array
    for i in range(len(arr)):
        # Compare the current element with elements in k_largest
        for j in range(k):
            if arr[i] > k_largest[j]:
                # Shift elements in k_largest to the right
                for l in range(k-1, j, -1):
                    k_largest[l] = k_largest[l-1]
                k_largest[j] = arr[i]
                break
    
    return k_largest

# Test case to find the top 3 largest numbers
input_var = [5, 10, 15, 2, 4, 6, 20, 16, 2, 16]
k = 6 # Change this value to find the top k largest elements
output = find_top_k_largest(input_var, k)
print(f'The top {k} largest elements are: {output}')
