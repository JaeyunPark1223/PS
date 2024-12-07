T = int(input())

for i in range(T):
  a = list(input())
  b = list(input())
  A = len(a)
  B = len(b)
  y = 0
  Y = a[0]
  for j in range((A)-1):
    if a[j] != a[j+1]:
      y+=1
  if y == 0:
    for j in range(B):
      if b[j]==Y:
        y+=1
    if y >= A:
      print("Case #"+str(i+1)+":",B-A)
    else: print("Case #"+str(i+1)+":","IMPOSSIBLE")
  else:
    tmp = 0
    for j in range(A):
      x = 0
      tmp1 = 0
      for k in range(x, B):
        if a[j] == b[k]:
          b[k] = "#"
          x = k
          tmp+=1
          tmp1+=1
          break
      if tmp1==0: 
        print("Case #"+str(i+1)+":","IMPOSSIBLE")
        break
      elif tmp == A:
        print("Case #"+str(i+1)+":",B-tmp)
        break
