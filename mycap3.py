x=int(input('enter the number of trems to be displayed:'))
if x<=0:
    x=int(input('enter the positive number:'))
else:
    a=0
    b=1
    s=0
    while s<x:
       print(a)
       f=a+b
       a=b
       b=f
       s+=1
