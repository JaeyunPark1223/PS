N = int(input())

a = []

for i in range(N):
  a.append(list(map(int,input().split())) )

a.sort()

for i in range(N):
  print(*a[i])
