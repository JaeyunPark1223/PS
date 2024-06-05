N, M = map(int,input(). split())
x1=dict()  # key : name
x2 = dict()  # key : num
for i in range(N):
  a= input()
  x1[a]= i+1
  x2[i+1] = a 
  
for y in range(M):
  z = input()
  if z.isdigit() : 
    print(x2[int(z)])
  else:
    print(x1[z])