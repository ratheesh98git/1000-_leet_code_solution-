#30  write a simple inverted pattern program


rows=int(input("enter the numbers"))

ascii_value=65

for i in range(rows):
    for j in range(i+1):
        values=chr(ascii_value)
        print(values,end=" ")
        
    ascii_value+=1

    print()