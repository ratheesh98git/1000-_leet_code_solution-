#31  write a program inverted number pyramid


num=int(input ("eneter the number"))



for i in range(num+1,0,-1):
    for j in range(i-1):
        print("*",end=" ")
        
    print()