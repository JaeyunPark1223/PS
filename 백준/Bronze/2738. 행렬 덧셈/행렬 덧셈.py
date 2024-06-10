N, M = map(int,input().split()) # N --> 가로, M --> 세로 

A = []
B = []

for i in range(N): 
  A.append(list(map(int,input().split())))

for i in range(N): 
  B.append(list(map(int,input().split())))

C = []
D = []
for i in range(N):
  for x in range(M):
    E = A[i][x]+B[i][x] # C[0] : [1,2,3] / C[0][0] : 1 
    print(E,end=" ")
  print()
