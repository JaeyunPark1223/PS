
N, M = map(int,input().split())

A = set()
B = set()

for i in range(N):
  a = input()
  A.add(a)

for i in range(M):
  b = input()
  B.add(b)

C = sorted(A&B)

print(len(C))

for i in C : 
  print(i)
  