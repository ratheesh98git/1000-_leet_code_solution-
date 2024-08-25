#24 algorithm linear search 



def linear_search(values,target):
    lent=len(values)
    for i in range(0,lent):
        if values[i]==target:
            return i
        
        
    return -1

index=linear_search([1,2,100,4,5,10,12,10],13)
print(f"this is index {index}")