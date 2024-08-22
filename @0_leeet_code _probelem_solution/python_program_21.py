#21 character pattern in pytrhon 

user_input=input("enter the user input")

leng=len(user_input)

for i in range(leng):
    for j in range(i+1):
        print(user_input[j],end=" ")
    print()


#OUT PUT

"""
a
a b
a b c"""