N = int(input())

a = list(map(int,input().split()))
ans = 0
a.sort(reverse=True)

for i in range(N):
  if ans<=a[i]:
    ans+=1
  else : break

print(ans)
    