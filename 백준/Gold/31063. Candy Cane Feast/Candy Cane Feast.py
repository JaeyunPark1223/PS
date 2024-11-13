import sys
input = sys.stdin.readline

N, M = map(int,input().split())

n = list(map(int,input().split()))
m = list(map(int,input().split()))

for i in range(M):
  a = [m[i], 0]
  for j in range(N):
    if a[0]>n[j] and a[1]<n[j]: 
      tmp = n[j]
      n[j]+=n[j]-a[1]
      a[1] = tmp 
    elif a[0]<=n[j]:  
      n[j]+=a[0]-a[1]
      break
print(*n, sep= "\n")