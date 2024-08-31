

l=[2,3,4,5,6,7,8,9]

leng=len(l)
init=0
while init<leng:
    for i in range(init,leng-1):
        l[i]=l[i+1]
    leng-=1
    if init<leng:
        print(l[init])
    init+=1