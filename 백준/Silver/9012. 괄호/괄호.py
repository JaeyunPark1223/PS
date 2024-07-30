N = int(input())

for i in range(N):
  a = input()
  b = 0
  for j in range(len(a)):
    if a[j] == "(":
      b+=1
    elif a[j] == ")":
      b-=1
    if b < 0:
      print("NO")
      break
  if b > 0:
    print("NO")
  elif b == 0:
    print("YES")