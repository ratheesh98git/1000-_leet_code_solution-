#14  write the program to merge two sorted list

def merge_sorted_list(list1,list2):
    sorted_array=[]
    i=j=0
    while i<len(list1) and j<len(list2):
        if list1[i]<=list2[j]:
            sorted_array.append(list1[i])
            i+=1
        else:
            sorted_array.append(list2[j])
            j+=1
    while i<len(list1):
            sorted_array.append(list1[i])
            i+=1
    while j<len(list2):
        sorted_array.append(list2[j])
        j+=1
    return sorted_array
list1=[1,2,3]
list2=[2,3,4]
print(merge_sorted_list(list1,list2))


        