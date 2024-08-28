N, B = map(int,input().split())
a = []

for i in range(N):
  a.append(list(map(int,input().split())))

ans = B

for i in range(N) : 
  for j in range(N):
    x = a[i][0] +1 
    y = a[j][1] +1 
    z = [0]*4

    for k in range(N):
      if a[k][0]> x and a[k][1]< y:
        z[0]+=1
      elif a[k][0]<x and a[k][1]<y:
        z[1]+=1
      elif a[k][0]>x and a[k][1]>y:
        z[2]+=1
      elif a[k][0]<x and a[k][1]>y:
        z[3]+=1
    if max(z)<ans:
      ans = max(z)

print(ans)