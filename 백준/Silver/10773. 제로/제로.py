N = int(input())

a = []

for i in range(N):
  b = int(input())
  if b != 0:
    a.append(b)
  else:
    a.pop()

print(sum(a))