N, K = map(int,input().split())

a = [0]*10001

for i in range(N):
  a[int(input())]+=1

ans = 0

for i in range(10001-K):
  x = 0
  for j in range(K+1):
    x += a[i+j]
    if x>ans:
      ans = x

print(ans)

