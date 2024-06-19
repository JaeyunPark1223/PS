x = 11
y = 11
while x != 0 and y != 0:
  x, y = map(int,input().split())
  if x+y != 0:
    print(x+y)