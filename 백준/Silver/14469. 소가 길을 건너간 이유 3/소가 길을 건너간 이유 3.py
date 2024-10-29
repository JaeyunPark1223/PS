N = int(input())

a = []

for i in range(N):
  a.append(list(map(int,input().split())))

a.sort()

ans = 0

for i in range(N):
  if a[i][0] > ans:
    ans = a[i][0]+a[i][1]
  else: 
    ans+=a[i][1]

print(ans)