#13 remove  duplicates from a list with out using bulit in function


def remove_duplicate(nums):
    is_nums=[]
    
    for items in nums:
        is_dupicate=False
        for  fin in is_nums:
         if items==fin:
            is_dupicate= True
            break
        if not is_dupicate:
           is_nums.append(items)
    return is_nums

print(remove_duplicate([1,2,2,3,4,5,6]))
  