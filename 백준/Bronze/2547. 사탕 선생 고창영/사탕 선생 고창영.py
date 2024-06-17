test = int(input())

for i in range(test):
  Z = input()
  A = int(input())
  X = 0
  for j in range(A):
    B = int(input())
    X = X+B
  if X%A == 0:
    print("YES")
  else:
    print("NO")
