N = int(input())

x = []
for i in range(N):
  x.append(list(map(int,input().split())))

a = [[1,0,0],[0,1,0],[0,0,1]]

ans = 0

for i in range(3):
  A = a[i]
  b = 0
  for j in range(N):
    A[x[j][0]-1],A[x[j][1]-1] = A[x[j][1]-1],A[x[j][0]-1]
    if A[x[j][2]-1] == 1:
      b+=1
  if b>ans:
    ans = b

print(ans)