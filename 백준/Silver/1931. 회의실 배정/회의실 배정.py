N = int(input())

a = []

for i in range(N):
  A, B = map(int,input().split())
  a.append([A,B])


a.sort(key = lambda x : (x[1],x[0]))  

ans = 1 
last = a[0][1]

for i in range(1,N):
  if a[i][0] >= last : 
    ans += 1 
    last = a[i][1]

print(ans)