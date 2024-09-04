# 48 common characeter in a string

str1=input("eneter the string 1 :")
str2=input("enter the string 2")


d=set(str1)
second=set(str2)

final= d & second

print(final)