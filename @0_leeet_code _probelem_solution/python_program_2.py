# find the largest number  max and minimum
def find_largest_number(arr):
    # Initialize a variable to store the largest number
    length=len(arr)
    max=arr[0]
    min=arr[0]
    # Iterate over the array to find the largest number
    for i in range(0,length):
        if arr[i]>max:
           max=arr[i]
    print(max)
    for j in range(0,length):
        if arr[j]<min:
            min=arr[j]
    print(min)        
    
input_var = [5, 10, 15, 2, 4, 6, 20, 16, 2, 16]
output = find_largest_number(input_var)
print(f'This is the output variable: {max} ')
