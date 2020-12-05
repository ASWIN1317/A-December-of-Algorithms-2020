import ast
class cell: 
      
    def __init__(self, a = 0, b = 0, dist = 0): 
        self.a = a
        self.b = b
        self.dist = dist 

def isInside(a, b, n): 
    if (a>= 1 and a <= n and 
        b >= 1 and b <= n):  
        return True
    return False
        
def minStepToReachTarget(k,t,n):  
    dx = [2, 2, -2, -2, 1, 1, -1, -1] 
    dy = [1, -1, 1, -1, 2, -2, 2, -2] 
    queue = [] 
    queue.append(cell(k[0], k[1], 0)) 
    visited = [[False for i in range(n+1)]   for j in range(n+1)] 
    visited[k[0]][k[1]] = True
    while(len(queue) > 0): 
        q = queue[0] 
        queue.pop(0) 
        if(q.a == t[0] and q.b == t[1]): 
            return q.dist 
        for i in range(8): 
            x = q.a+dx[i] 
            y = q.b+dy[i] 
            if(isInside(x, y, n) and not visited[x][y]): 
                visited[x][y] = True
                queue.append(cell(x, y, q.dist + 1)) 
  
if __name__=='__main__':  
    n= input("Dimension of Board: ").split(" ")
    for i in range(len(n)):
        n[i]=int(n[i])
    k = input("Position of Knight: ").split(" ")
    for i in range(len(k)):
        k[i]=int(k[i])
    t =input("Target Position: ").split(" ")
    for i in range(len(t)):
        t[i]=int(t[i])
    print("Minimum Steps: ",minStepToReachTarget(k,t,n[0]))
                               
      
