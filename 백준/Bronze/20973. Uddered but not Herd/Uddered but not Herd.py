
a = input()

x = input()

b = 0

ans = 0

while b < len(x):
  for j in a:
    if j == x[b]:
      b+=1
      if b >= len(x) : break
  ans+=1

print(ans)