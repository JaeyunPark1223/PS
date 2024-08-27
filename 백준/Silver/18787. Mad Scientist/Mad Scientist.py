N = int(input())

A = input()
B = input()
sign = False 
ans = 0
for i in range(N):
  if A[i] != B[i] : 
    sign = True 
  else: 
    if sign : ans += 1 
    sign = False

print(ans)