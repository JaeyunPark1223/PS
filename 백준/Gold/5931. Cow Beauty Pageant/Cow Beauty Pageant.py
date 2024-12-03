import sys
sys.setrecursionlimit(100000)


dx = [0,0,-1,1]
dy = [-1,1,0,0]

def isValid(x,y) : 
  return 0 <= x < N and 0 <= y < M

def DFS(i,j,v,p) : 
  if v[i][j] : return 
  pattern[i][j] = p 
  if p == 1 : 
    coor1.append((i,j))
  else : 
    coor2.append((i,j))
  v[i][j] = 1
  for x in range(4) : 
    nx,ny = i + dx[x] , j + dy[x]
    if isValid(nx,ny) and pattern[nx][ny] == "X" : 
      DFS(nx,ny,v,p)
  
def check(p) :
  visited = [ [0] * M for _ in range(N) ]
  for i in range(N) : 
    for j in range(M) : 
      if pattern[i][j] == "X" : 
        DFS(i,j,visited,p)
        return 
        
N,M = map(int,input().split())
pattern = [] 
coor1 = []
coor2 = []
for i in range(N):
  pattern.append(list(input()))
check(1) 
check(2) 

ans = float("inf")

for i in range(len(coor1)):
  for j in range(len(coor2)):
    if abs(coor1[i][0]-coor2[j][0]) + abs(coor1[i][1]-coor2[j][1]) < ans:
      ans = abs(coor1[i][0]-coor2[j][0]) + abs(coor1[i][1]-coor2[j][1])
      
print(ans-1)