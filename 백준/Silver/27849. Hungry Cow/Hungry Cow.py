N, T = map(int,input().split())

D = []
B = []

for i in range(N):
  d, b = map(int,input().split())
  D.append(d)
  B.append(b)

ans = 0

for i in range(N-1):
  if D[i+1]-D[i] > B[i]:
    ans+= B[i]
  if D[i+1]-D[i] <= B[i]:
    ans+=D[i+1]-D[i]  
    B[i+1]+= B[i]-(D[i+1]-D[i]) 

if B[-1]>=T-D[-1]+1:
  ans+=T-D[-1]+1
if B[-1]<T-D[-1]+1:
   ans+=B[-1]

print(ans)