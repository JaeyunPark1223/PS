N, K = map(int,input().split())

a = [0]*12

for i in range(N):
  S, Y = map(int,input().split())
  if Y == 1:
    if S == 0:
      a[0]+=1
    else: 
      a[1]+=1
  if Y == 2:
    if S == 0:
      a[2]+=1
    else: 
      a[3]+=1
  if Y == 3:
    if S == 0:
      a[4]+=1
    else: 
      a[5]+=1
  if Y == 4:
    if S == 0:
      a[6]+=1
    else: 
      a[7]+=1
  if Y == 5:
    if S == 0:
      a[8]+=1
    else: 
      a[9]+=1
  if Y == 6:
    if S == 0:
      a[10]+=1
    else: 
      a[11]+=1


x = 0

for i in range(12):
  if a[i] % K == 0:
    x+=a[i]//K
  else:
    x+=a[i]//K 
    x+=1
print(x)
