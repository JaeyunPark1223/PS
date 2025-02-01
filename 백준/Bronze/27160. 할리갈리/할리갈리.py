N=int(input())
check=[0,0,0,0]
for i in range(N):
  a, b= input().split()
  b=int(b)
  if a=="STRAWBERRY":
    check[0]+=b
  elif a=="BANANA":
    check[1]+=b
  elif a=="LIME":
    check[2]+=b
  else:
    check[3]+=b
if 5 in check:
  print("YES")
else:
  print("NO")