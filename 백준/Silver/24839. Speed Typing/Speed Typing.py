T = int(input())

for i in range(T):
  a = list(input())
  b = list(input())
  A = len(a)
  B = len(b)
  y = 0
  Y = a[0]
  for j in range(B):
    if b[j]==Y:
      y+=1
  if y >= A:
    print("Case #"+str(i+1)+":",B-A)
  else: print("Case #"+str(i+1)+":","IMPOSSIBLE")