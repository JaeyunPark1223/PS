from collections import deque 
import sys 
input = sys.stdin.readline

N = int(input())
q = deque()

for i in range(N):
  a = input().split()
  if len(a) == 2:
    q.append(int(a[1]))
  else:
    a = a[0]
    if a == "pop":
      if len(q) == 0:
        print(-1)
      else:
        print(q.popleft())
    elif a == "size":
      print(len(q))
    elif a == "empty":
      if len(q) == 0:
        print(1)
      else:
        print(0)
    elif a == "front":
      if len(q) == 0:
        print(-1)
      else:
        print(q[0])
    else:
      if len(q) == 0:
        print(-1)
      else:
        print(q[-1])