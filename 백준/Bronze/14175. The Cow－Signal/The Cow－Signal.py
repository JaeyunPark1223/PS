
M, N, K = map(int,input().split())

for i in range(M):
  a = input()
  b = []
  for j in range(N):
    b.append(a[j]*K)
  for k in range(K):
    print(*b,sep = "")

