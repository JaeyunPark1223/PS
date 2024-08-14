N = int(input())

d = []

for i in range(5*N):
  d.append(input())

ans = []
x = 36

for i in range(N):
  for j in range(i+1,N): 
    a = 0
    for k in range(5):
      for _ in range(7):
        if d[5*i+k][_] != d[5*j+k][_]:
          a+=1
    if x>a:
      x = a
      ans = [i+1, j+1]

print(*ans)
