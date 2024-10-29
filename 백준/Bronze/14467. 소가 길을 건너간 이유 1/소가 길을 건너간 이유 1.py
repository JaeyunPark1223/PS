N = int(input())


a = []

for i in range(N):
  a.append(list(map(int,input().split())))

ans = [-1]*11
tmp = 0

for i in range(N):
  if ans[a[i][0]] != -1 and ans[a[i][0]] != a[i][1]:  
    tmp+=1
  ans[a[i][0]] = a[i][1]

print(tmp)