
N, K, P = map(int, input().split())

bread = list(map(int, input().split()))
ans = 0
for i in range(N):
  b=0
  for j in range(K):
    b += bread[i*K+j]
  if b > K - P :
    ans += 1

print(ans)
