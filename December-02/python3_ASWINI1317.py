from itertools import permutations  
  
dict1={'2' : 'ABC', '3' : 'DEF', '4' : 'GHI', '5' : 'JKL', '6' : 'MNO', '7' : 'PQRS', '8' : 'TUV'  , '9' : 'WXYZ'}
x= input()
l=[]
a=[]
res=[]
for i in x:
    l.append(i)
for i in l:
    if i in dict1.keys():
        a.append(dict1[i])
for i in a[0]:
    for j in a[1]:
        res.append(i+j)
print(res)