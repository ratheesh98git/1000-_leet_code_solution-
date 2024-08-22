#21 character pattern in pytrhon 

user_input=input("enter the user input")

leng=len(user_input)

for i in range(leng):
    for j in range(i+1):
        print(user_input[i],end=" ")
    print()


#OUT PUT
    """
    enter the user inputABCD
A
B B
C C C
D D D D
    
    """