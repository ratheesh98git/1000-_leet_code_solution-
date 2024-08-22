#18 MATRIX TRANSPOSE IN PYTHON 

A=[[1,2,34],[3,4,5],[4,5,65]]


print("befor transpose")
for i in range(len(A)):
    for j in range(len(A)):
        print(A[i][j]," ",end=" ")
    print()
print("after transpose matrix")

for i in range(len(A)):
    for j in range(len(A)):
        print(A[j][i]," ",end=" ")
    print()