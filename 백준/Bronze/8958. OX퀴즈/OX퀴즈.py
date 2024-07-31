N = int(input())

def OX(x):
  y = 0
  for i in range(x+1):
    y+=i
  return y
  
for i in range(N):
  a = input().split("X")
  ans = 0
  for j in range(len(a)):
    ans+=OX(len(a[j]))
  print(ans)