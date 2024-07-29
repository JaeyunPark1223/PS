T = int(input())

for _ in range(T):
  n = int(input())
  a = []
  b = 0
  while n > 0:
    if n%2 == 1:
      a.append(b)
    b+=1
    n = n//2

  print(*a)
