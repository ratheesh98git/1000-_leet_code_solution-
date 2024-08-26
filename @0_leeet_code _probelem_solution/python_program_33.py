#33 python program to add two number with out using +operator


num1=int(input("eneter the value"))
num2=10

while num2!=0:
   c=num1&num2
   
   num1=num1^num2
   
   num2=c>>1
print(num1)