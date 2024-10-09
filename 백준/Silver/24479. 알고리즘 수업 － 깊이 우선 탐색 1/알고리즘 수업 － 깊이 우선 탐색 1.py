import sys
sys.setrecursionlimit(10**5)

N, M, R = map(int, input(). split())

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
  for i in sorted(graph[R]): 
    if not visited[i]:
      cnt += 1
      dfs(graph, i, visited)
       
dfs(graph, R, visited)

print(*visited[1:],sep="\n")

