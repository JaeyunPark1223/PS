N = int(input())

A = list(map(int, input().split()))

B = 0
C = 1001


for i in range(N):
  if A[i]>B:
    B = A[i]
  if A[i]<C:
    C = A[i]

print(B - C)
