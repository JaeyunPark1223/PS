N = int(input())

a = []

for i in range(N):
  x, y = map(int,input().split())
  a.append([x, y])

ans = 0

for i in range(N):
  T = [0]*1001
  for j in range(N):
    if i == j: continue
    for k in range(a[j][0], a[j][1]):
        T[k] = 1
  if sum(T)>ans:
      ans = sum(T)

print(ans)
    