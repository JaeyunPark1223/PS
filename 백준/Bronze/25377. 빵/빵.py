test = int(input())
A = 1001
for i in range(test):
  x, y = map(int,input().split())
  if x <= y and A>y:
    A = y
  else:
    A = -1
print(A)
