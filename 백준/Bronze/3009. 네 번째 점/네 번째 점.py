A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

X = [A[0], B[0], C[0]]
Y = [A[1], B[1], C[1]]

z = []

if X.count(A[0]) == 1:
  z.append(A[0])
if X.count(B[0]) == 1:
  z.append(B[0])
if X.count(C[0]) == 1:
  z.append(C[0])

if Y.count(A[1]) == 1:
  z.append(A[1])
if Y.count(B[1]) == 1:
  z.append(B[1])
if Y.count(C[1]) == 1:
  z.append(C[1])

print(*z)