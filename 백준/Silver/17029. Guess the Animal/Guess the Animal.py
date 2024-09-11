N = int(input())
K = []
for i in range(N) : 
  tmp = input().split() 
  K.append(set(tmp[2:])) 

y = 0

for i in range(N-1):
  for j in range(i+1, N):
    x =  len(K[i] & K[j])
    if x>y: y = x

print(y+1)
    