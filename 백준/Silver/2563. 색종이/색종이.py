paper = []
for i in range(100):
  tmp = [] 
  for j in range(100):
    tmp.append(0)
  paper.append(tmp)

N = int(input())

for i in range(N):
  x, y = map(int, input().split())
  for j in range(10):
    for k in range(10):
      paper[x+j][y+k] = 1
      

A = 0
for i in range(100) :
  for j in range(100):
    if paper[i][j] == 1:
      A+=1

print(A)