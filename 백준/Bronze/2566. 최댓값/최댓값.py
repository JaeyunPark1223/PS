B = []
for i in range(9):
  A= list(map(int,input().split()))
  B.append(A)

C = 0
D = (1, 1)

for i in range(9):
  for j in range(9):
    if B[i][j] > C:
      C = B[i][j]
      D = (i+1 , j+1)

print(C)
print(D[0],D[1])
