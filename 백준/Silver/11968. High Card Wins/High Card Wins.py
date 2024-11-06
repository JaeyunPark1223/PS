N = int(input())
e = [0]*(2*N+1)
for i in range(N):
  x = int(input())
  e[x]+=x

ans = 0

for i in range(1, 2*N+1):
  if e[i]!=0 and e[i]!=-1:
    for j in range(i,2*N+1):
      if e[j] == 0:
        ans+=1
        e[j] = -1
        break
print(ans)