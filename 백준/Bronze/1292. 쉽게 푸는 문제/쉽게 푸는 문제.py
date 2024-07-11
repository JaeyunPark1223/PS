A, B = map(int,input().split())

a = []

for i in range(1, B+1):
  for j in range(i):
    a.append(i)


ans = []
ans.append(a[A-1:B])

print(sum(*ans))