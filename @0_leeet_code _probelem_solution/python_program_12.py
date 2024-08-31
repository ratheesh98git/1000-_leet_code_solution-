#6 write a function to generate a first number in fibonacci series

def fibo(value):
    fib=[0,1]
    for i in range(0,value):
        fib.append(fib[-1]+fib[-2])
    return fib[: value]
print(fibo(5))
        
