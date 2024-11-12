N, M = map(int,input().split())

n = []
m = []

for i in range(N):
  x, y = map(int,input().split())
  for j in range(y):
    n.append(x)

for i in range(M):
  x, y = map(int,input().split())
  for j in range(y):
    m.append(x)

ans = 0
tmp1 = -1
b,e = 0,0
for i in range(len(n)):
  b+=n[i]
  e+=m[i]
  tmp = 0
  if b>e:
    tmp = 1
  if b<e:
    tmp = 0
  if tmp!= tmp1:
    ans+=1
    tmp1 = tmp
print(ans-1)
  
