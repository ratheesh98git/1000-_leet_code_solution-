#20 array sorting in python with out using bulit in  function show array in asscending order

arr=[95,15,20,13,14,45,74]


leng=len(arr)

for i in range(0,leng):
    for j in range(i+1,leng):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)
 