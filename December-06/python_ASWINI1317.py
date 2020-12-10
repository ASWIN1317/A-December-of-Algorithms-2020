from collections import defaultdict
import ast
#[ ['B','C'], [], ['D'], [] ]
def convert(intt):
    d=[]
    numb=set()
    intt=ast.literal_eval(intt)
    for i in range(len(intt)):
        c=[]
        if intt[i]!=[]:
            for j in intt[i]:
                c.append(ord(j)-64)
                numb.add(ord(j)-64)
        else:
            c.append(0)
        d.append(c)
    return d, max(numb)+1
    
def topsort(v,visited,stack,tasks):
    visited[v]=True
    for i in tasks[v]:
        if visited[i]==False:
            topsort(i,visited,stack,tasks)
    stack.insert(0,v)
        
def findCompletionOrderOfTasks(intt):
    l,n=convert(intt)
    tasks=defaultdict(list)
    start=1
    for i in range(len(l)):
        tasks[start]=l[i]
        start+=1
    visited = [False]*n
    stack=[]
    res=[]
    for i in range(n):
        if visited[i]==False:
            topsort(i,visited,stack,tasks)
        #print(stack)
    for i in stack:
        res.append(chr(ord('@')+i))
    for i in range(0,len(res)-1):
        print(res[i],end=" ")
    print()
        
intt=input()
findCompletionOrderOfTasks(intt)