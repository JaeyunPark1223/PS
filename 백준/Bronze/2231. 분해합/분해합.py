N = int(input())
A = 1000000

for i in range(N):
  X = i
  for j in str(i) : 
    X += int(j) 
  if X == N and i<A:
    A = i

if A == 1000000:
  A = 0
print(A)
  