#5 write a function to  factorial of a number


def fib_onic(n):
    if n==0:
        return 1
    else:
        return n*fib_onic(n-1)

d=fib_onic(5)
print("this is fibonaic",d)