fre = {}
def most_frequent(m):
    for x in m:
        if x in fre:
            fre[x]+=1
        else:
            fre[x]=1

w=str(input('Please enter a string '))
most_frequent(w)
import operator
fre=dict(sorted(fre.items(),key=operator.itemgetter(1),reverse=True))
print(fre)
