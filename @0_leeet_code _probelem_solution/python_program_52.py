#52 Python Program for Compound Interest


def compond_inte(principal,rate,time):
    
    Amount=principal*(pow((1+rate/100),time))
    CI=Amount-principal
    print("the is compound interest",CI)
compond_inte(10000, 10.25, 5)
    


