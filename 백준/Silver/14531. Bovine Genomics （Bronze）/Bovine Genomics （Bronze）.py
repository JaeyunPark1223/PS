N, M = map(int,input().split())

x = "a"
y = "a"

for i in range(N):
  x+=input()
for i in range(N):
  y+=input()

X = ""
Y = ""

for i in range(1, M+1):
  for j in range(N):
    X+=x[i+(j*M)]

for i in range(1, M+1):
  for j in range(N):
    Y+=y[i+(j*M)]

ans = 0

for i in range(0,M*N,N):
  tmp = ""
  tmp1 = 0
  for j in range(N):
    tmp+=X[i+j]
  for j in range(N):
    if Y[i+j] in tmp:
      tmp1+=1
      break
  if tmp1 == 0:
    ans+=1

print(ans)