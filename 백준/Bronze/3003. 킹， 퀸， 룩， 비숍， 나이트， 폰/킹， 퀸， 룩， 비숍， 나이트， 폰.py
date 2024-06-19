
A = list(map(int,input().split()))
B = [1, 1, 2, 2, 2, 8]
C = []
x = 0
for i in range(6):
  x = B[i]-A[i]
  C.append(x)
  
print(*C)
