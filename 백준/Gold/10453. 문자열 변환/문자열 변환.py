T = int(input())

for i in range(T):
  x, y = input().split()
  a = []
  b = []
  for j in range(len(x)):
    if x[j] == "b":
      a.append(j)
  for j in range(len(y)):
    if y[j] == "b":
      b.append(j)
  if len(a) == len(b):
    ans = 0
    for j in range(len(a)):
      ans+=abs(b[j]-a[j])
    print(ans)
  else:
    print(-1)