#6 write a function to generate a first number in fibonacci series

def fibo(var):
    fib=[0,1]
    for  item in range(2,var):
       fib.append(fib[-1]+fib[-2])
    return  fib[:var]
print(fibo(7))