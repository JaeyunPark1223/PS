n, m=map(int, input().split())
l=[]
for i in range(m):
  l.append(list(input().split()))
l.sort()
check=[[0, 0] for _ in range(n)]
for i in range(m):
  if l[i][1]=="P":
    if l[i][2]=="1":
      check[int(l[i][0])-1][0]=1
    else:
      check[int(l[i][0])-1][0]=-1
  if l[i][1]=="M":
    if l[i][2]=="0":
      check[int(l[i][0])-1][1]=1
    else:
      check[int(l[i][0])-1][1]=-1
minn=0
maxx=0
for i in range(n):
  if check[i][0]==1 and check[i][1]==1:
    minn+=1
    maxx+=1
  elif check[i]==[1, 0] or check[i]==[0, 1]:
    maxx+=1
  elif check[i]==[0, 0]:
    maxx+=1
print(minn, maxx)
      