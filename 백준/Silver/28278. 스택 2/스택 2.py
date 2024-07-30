import sys
input = sys.stdin.readline

N = int(input())

A = []

for i in range(N):
  a = list(map(int,input().split()))
  if len(a) == 1:
    b = a[0]
    if b == 2:
      if len(A)>0:
        print(A.pop())
      else:
        print(-1)
    elif b == 3:
      print(len(A))
    elif b == 4:
      if len(A) == 0:
        print(1)
      else:
        print(0)
    elif b == 5:
      if len(A)>0:
        print(A[-1])
      else:
        print(-1)
  else:
    A.append(a[1])
