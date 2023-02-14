import os

import random
arr=[]
arrn=[]
arrs=[]
N=int(input())
for i in range(33,42):
    arrs.append(chr(i))
for i in range(ord('A'),ord('Z')):
    arr.append(chr(i))
for i in range(0,10):
    arrn.append(i)
x=""
for i in range(N):
    ch=random.randint(0,2)
    if(ch==1):
        r=random.randint(0,1)
        if(r):
            x=x+random.choice(arr)
        else:
            x=x+random.choice(arr).lower()
    elif(ch==2):
        x=x+str(random.choice(arrn))
    else:
        x=x+random.choice(arrs)
x=list(x)

    
for b in range(100):
    i=random.randint(0, len(x)-1)
    j=random.randint(0, len(x)-1)
    x[i],x[j]=x[j],x[i]    
print("".join(x))
