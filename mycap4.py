l1=[]
i=1
x=0
z=0
i=int(input("enter the no of elements to be entered in to the list"))
print('enter the insert numbers')
while x<i:
    n=int(input())
    l1.append(n)
    x+=1
print("list:",l1)
for x in l1:
    if x<=0:
        l1.remove(x)
print(l1)
