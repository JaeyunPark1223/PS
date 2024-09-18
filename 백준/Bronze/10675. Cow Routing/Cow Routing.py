A, B, N = map(int,input().split())

ans = 1001

for i in range(N):
  x, y = map(int,input().split())
  a = list(map(int,input().split()))
  tmp = 0
  for j in range(y):
    if a[j] == A:
      tmp+=1
    elif a[j] == B and tmp == 1:
      tmp+=1
  if tmp == 2 and x<ans:
    ans = x

if ans == 1001:
  print(-1)
    
else: print(ans)