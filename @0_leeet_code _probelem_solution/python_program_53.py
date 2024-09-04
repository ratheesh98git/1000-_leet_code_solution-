#53 Python Program to Find Sum of Array



def find_array(value):
    sums=0
    for i in value:
        sums=sums+i
    return sums


arr = [1, 2, 3]

data=find_array(arr)
print(data)

