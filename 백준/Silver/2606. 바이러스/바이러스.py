import sys
sys.setrecursionlimit(10**5)

N = int(input())
M = int(input())
R = 1

graph = [[] for i in range(N+1)]

for i in range(M):
  x, y =  map(int, input(). split())
  graph[x].append(y)
  graph[y].append(x)

visited = [0] * (N+1)
cnt = 1

def dfs(graph, R, visited):
  global cnt 
  visited[R] = cnt
  for i in sorted(graph[R],reverse=True): 
    if not visited[i]:
      cnt += 1
      dfs(graph, i, visited)
       
dfs(graph, R, visited)

ans = 0

for i in range(len(visited)):
  if visited[i] !=0:
    ans+=1
    

print(ans-1)
