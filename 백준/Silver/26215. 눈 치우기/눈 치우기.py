N = int(input())

a = list(map(int,input().split()))
a.append(0)

ans = 0

while True:
  a.sort()
  if a[-1] == 0:
    break
  a[-1]-=1
  a[-2]-=1
  ans+=1

if ans<1441:
  print(ans)

else:
  print(-1)