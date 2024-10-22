N, K = map(int,input().split())

a = list(input().split())

ans = []

tmp = 0

for i in range(N):
  if tmp+len(a[i])>K:
    print(*ans)
    ans = []
    tmp = len(a[i])
    ans.append(a[i])
  else:
    ans.append(a[i])
    tmp+=len(a[i])

print(*ans)
    