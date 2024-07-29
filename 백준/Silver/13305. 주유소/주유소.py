N = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))

a = 0
min_cost = cost[0] # float("inf") --> max 
for i in range(N-1):
  if min_cost>=cost[i]:
    min_cost = cost[i]
  a = a+dist[i]*min_cost
 
print(a)
