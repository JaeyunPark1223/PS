N, K = map(int,input().split())

A = []

for i in range(1, K+1):
  a = str(N*i)
  A.append(int(a[::-1]))

print(max(A))