N = int(input())

A = [  int(input())  for i in range(N) ]

x = sum(A)

ans = [0]*N

for i in range(N):
  tmp  = x - A[i]
  for j in range(1,N+1):
    ans[i] += tmp
    tmp -= A[(i+j)%N]
    

print(min(ans))
    