M, F = map(int,input().split())

a = []

for i in range(M+F):
  a.append(input())

for i in range(M):
  x = []
  for j in range(F):
    ans = 0
    for k in range(M+F):
      tmp = 0
      if k !=i and k!=M+j:
        for q in range(25):
          if a[k][q] == a[i][q] or a[k][q] == a[M+j][q]:
            tmp+=1
          else: break
        if tmp == 25:
          ans+=1
    x.append(ans)
  print(*x)