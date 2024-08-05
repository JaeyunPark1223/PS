N = int(input())
ans = [0]*1001

for i in range(N):
  s,t,b = map(int,input().split())
  for j in range(s,t+1) : 
    ans[j] += b

print(max(ans))
  