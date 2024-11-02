N, K = map(int,input().split())

a = list(map(int,input().split()))

ans = 1+K

a.sort()

for i in range(N-1):
  if (1+K)*2 > (a[i+1]-a[i])+1+K:
    ans+=(a[i+1]-a[i])
  else:
    ans+= 1+K

print(ans)