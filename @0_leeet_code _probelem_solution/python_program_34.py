#35 stort the array ascending order with out using bult in function


def array(arr):
    
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:    #for discending order <
                arr[i],arr[j]=arr[j],arr[i]
    return arr
s=[1,210,5,3,2,0]

array(s)
print(s[-1])