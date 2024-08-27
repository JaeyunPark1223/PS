N = int(input())
a = list(map(int,input().split()))
ans = []

for i in range(1, N+1):
  x = [0]*N
  x[0] = i
  for j in range(1,N):
    tmp = a[j-1] - x[j-1] 
    if tmp in x or tmp <= 0 : 
      break 
    x[j] = tmp  

  if  0 not in x : 
    print(*x)
    break 