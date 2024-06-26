T = int(input())

for i in range(T):
  n, m = map(int,input().split())
  A = 0
  for a in range(1,n-1):
    for b in range(a+1, n):
      if (a**2+b**2+m) % (a*b) == 0:
        A+=1
  print(A)
        