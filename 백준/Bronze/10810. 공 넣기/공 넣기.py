N, b = map(int,input(). split())
a = [0] * N 
for y in range(b):
  i,j,k=map(int,input(). split())
  for x in range(i-1, j, 1):
    a[x] = k 
for z in range(0, N, 1):
  print(a[z],end=" ")