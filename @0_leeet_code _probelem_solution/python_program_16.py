#16  find the missing number in the list


def find_missing_number(nums):
    n=len(nums)+1
    exceped=n*(n+1)//2
    actual=0
    for items in nums:
        actual+=items
    return exceped-actual

print(find_missing_number([1,2,3,4,5,6,7,8,10]))
