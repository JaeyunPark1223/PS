A= list(map(int,input().split()))

B = A[0]+A[3]
C = A[1]+A[2]

if B>C:
  print(B-C)
else:
  print(C-B)