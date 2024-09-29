N, S = map(int, input(). split())

a = []

for i in range(N):
  a.append(list(map(int, input(). split())))
 

n = S-1
k = 1
ans = 0

if a[n][0] == 1 and a[n][1] <= abs(k):
  a[n][0] = -1
  ans+=1
elif a[n][0] == 0:
  k=-(k)
  if k<0:
    k-=a[n][1]
  else:
    k+=a[n][1]

n+=k
for i in range(1000000):
  if a[n][0] == 1 and a[n][1] <= abs(k):
    a[n][0] = -1
    ans+=1
  elif a[n][0] == 0:
    k=-(k)
    if k<0:
      k-=a[n][1]
    else:
      k+=a[n][1]
  n+=k
  if n<0 or n>N-1:
    break
  
print(ans)