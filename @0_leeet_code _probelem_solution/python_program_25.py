#25 palindrom number using python


num=int(input("enter the number"))



if num<0:
    print("eneter the positive number")
    
else:
    stri=str(num)
    revers=stri[::-1]
    if revers==stri:
        print("it's a palindrom")
    else:
        print("it is not a palindrom")
        