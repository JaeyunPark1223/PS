while True:
  a = int(input())
  if a != -1:
    A = []
    B = []
    for i in range(a):
      if i != 0:
        if a%i == 0:
          A.append(i)
          B.append(i)
          A.append('+')
    if sum(B) == a:
      del(A[-1])
      print(a,'=',end=" ")
      print(*A)
    if sum(B) !=a:
      print(a, 'is NOT perfect.')
  else:
    break
  
  