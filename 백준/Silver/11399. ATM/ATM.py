N = int(input())

A = list(map(int,input().split()))

A.sort()

a = 0


for i in range(1):
  for j in range(N):
    a = a+(sum(A[i:j+1]))

print(a)