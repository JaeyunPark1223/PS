N=int(input())
ans =0
if N<=2:
  print(N)
else:
  while N!=2:
    if N%2 == 0:
      N//=2
      ans+=1
    else:
      N = (N+1)//2
      ans+=1
  
  print(ans+2)
  