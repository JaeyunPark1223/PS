Q = int(input())

for i in range(Q):
  a = input()
  tmp = -1
  for j in range(len(a)-2):
    if a[j] == "M" and a[j+1] == "O" and a[j+2] == "O":
      tmp = len(a)-3
  if tmp == -1:
    for j in range(len(a)-2):
      if a[j] == "M" and a[j+1] == "O" and a[j+2] == "M":
          tmp = len(a)-2
      if a[j] == "O" and a[j+1] == "O" and a[j+2] == "O":
        tmp = len(a)-2
  if tmp == -1:
    for j in range(len(a)-2):
      if a[j] == "O" and a[j+1] == "O" and a[j+2] == "M":
          tmp = len(a)-1
  print(tmp)