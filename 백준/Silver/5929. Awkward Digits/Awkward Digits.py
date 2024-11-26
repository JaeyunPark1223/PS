a = list(input()) 
b = list(input()) 

tmp = []

for i in range(len(a)):
  A = []
  for j in range(len(a)):
    A.append(int(a[j])) 
  if A[i] == 1:
    A[i] = 0
  elif A[i] == 0:
    A[i] = 1
  x = 0
  for j in range(1, len(a)+1):
    x+=A[-j]*(2**(j-1))
  tmp.append(x)

for i in range(len(b)):
  B = []
  for j in range(len(b)):
    B.append(int(b[j]))
  
  for j in range(2): 
    if B[i] == 1:
      t = 1 
      if j == 0:
        B[i] = 0
      else: B[i] = 2
    elif B[i] == 2:
      t = 2 
      if j == 0:
        B[i] = 0
      else: B[i] = 1
    elif B[i] == 0:
      t = 0
      if j == 0:
        B[i] = 1
      else: B[i] = 2
    y = 0
    
    for j in range(1, len(b)+1):
      y+=B[-j]*(3**(j-1))

    B[i] = t 
    if y in tmp:
      print(y)
      exit()
