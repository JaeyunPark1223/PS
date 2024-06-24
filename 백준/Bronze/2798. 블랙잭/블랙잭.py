N, M = map(int,input().split())

A  = list(map(int,input().split()))

Z = 0

for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      X = A[i] + A[j] + A[k]
      Y = M - X
      if Y > -1 and X > Z:
        Z = X
print(Z)
    