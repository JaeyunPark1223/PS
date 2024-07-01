A = []
B = 0

for i in range(5):
  x = int(input())
  A.append(x)
  B = B+x

print(B//5)

A.sort()

print(A[2])