print("Counter A: ",end="")
a=list(map(str,input().split()))
print("Counter B: ",end="")
b=list(map(str,input().split()))
res=[]
j=0
k=0
min1=min(len(a),len(b))
if(len(a)<len(b)):
    for i in range(min1-1):
        res.append(b[j])
        res.append(b[j+1])
        res.append(a[k])
        j+=2
        k+=1
else:
    for i in range(min1-2):
        res.append(b[j])
        res.append(b[j+1])
        res.append(a[k])
        j+=2
        k+=1
if j<len(b):
    for i in range(j,len(b)):
        res.append(b[i])
if k<len(a):
    for i in range(k,len(a)):
        res.append(a[i])
for i in res:
    print(i,end=" ")