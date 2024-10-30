N = int(input())

x = []
y = []

for i in range(N):
  a = list(map(int,input().split()))
  if a[1] == 1:
    x.append(a[0])
  if a[1] == 0:
    y.append(a[0])

x.sort()
y.sort()

tmp = 1000000000

for i in range(len(y)):
  for j in range(len(x)):
    if abs(y[i]-x[j])<tmp:
      tmp = abs(y[i]-x[j])

ans = 0

for i in range(len(x)-1):
  if x[i+1]-x[i]>=tmp:
    ans+=1


print(ans+1)
