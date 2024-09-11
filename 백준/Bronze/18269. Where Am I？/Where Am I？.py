N = int(input())

a = input()

ans = 0

for i in range(1,N+1):
  x = set()
  for j in range(N-i+1):
    x.add(a[j:j+i])  
  
  if len(x) == (N-i+1) : 
    ans = i 
    break
    
print(ans)