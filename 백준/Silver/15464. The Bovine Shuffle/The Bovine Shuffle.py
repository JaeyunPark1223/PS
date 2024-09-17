N = int(input())

x = list(map(int,input().split()))
a = list(map(int,input().split()))
ans = [0]*N


for j in range(3):
  ans = [0]*N
  for i in range(N):
    ans[i] = a[x[i]-1]
  a = ans 
 
  

print(*ans,sep = "\n")