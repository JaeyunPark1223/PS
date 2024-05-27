for i in range(3):
  N=int(input())
  S = 0 
  for j in range(N): 
    x = int(input())
    S+=x
  if S<0:
      print("-")
  if S>0:
      print("+")
  if S==0:
      print("0")