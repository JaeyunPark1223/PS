N = int(input())

a = []

for i in range(N):
  a.append(int(input()))

ans = float("inf")

for i in range(101):
  x = 0
  for j in range(N):
    tmp = 0
    if i>a[j]:
      tmp+=i-a[j]
    elif i+17<a[j]:
      tmp+=a[j]-(i+17)
    x+=tmp*tmp
  if x<ans:
    ans = x

print(ans)
      