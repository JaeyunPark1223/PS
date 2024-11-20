import sys
sys.setrecursionlimit(10**6)

N = int(input())

a = [ list(input()) for _ in range(N) ]

visited = [ [False] * N for _ in range(N) ]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def make_area() : 
  for i in range(N):
    for j in range(N):
      if a[i][j] == "R":
        a[i][j] = "G"
      visited[i][j] = False 

def get_area(x,y) : 
  if visited[x][y] : return 

  visited[x][y] = True 
  curr = a[x][y] 

  for i in range(4) : 
    nx = x + dx[i]
    ny = y + dy[i] 

    if 0 <= nx < N and 0 <= ny < N and a[nx][ny] == curr : 
      get_area(nx,ny)

cnt = 0 

for i in range(N) : 
  for j in range(N) : 
    if not visited[i][j] : 
      get_area(i,j)
      cnt += 1 

make_area() 

cnt2 = 0 
for i in range(N) : 
  for j in range(N) : 
    if not visited[i][j] : 
      get_area(i,j)
      cnt2 += 1 

print(cnt, cnt2)
