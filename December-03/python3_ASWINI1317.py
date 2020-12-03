a=input()
start=930
end=1700
res=[]
for i in range (len(a)-1):
    if (a[i+1][0] - a[i][1]) >=100:
        res.append([a[i][1],a[i+1][0]])

if (a[0][0]-start) >=100:
    res.append([start,a[0][0]])
if(end-a[len(a)-1][1]) >=100:
    res.append([a[len(a)-1][1],end])
print(res)