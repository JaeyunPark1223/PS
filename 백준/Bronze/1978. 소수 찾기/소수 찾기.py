N = int(input())

a = list(map(int,input().split()))

ans = 0

for i in range(N):
  A = 2
  for j in range(2, a[i]):
    if a[i]%j != 0:
      A+=1
  if A == a[i]:
    ans+=1

print(ans)