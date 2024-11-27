N = int(input())
a = input()
ans = 0

for i in range(N):
  l,r = 0,0 
  
  for j in range(i-1,-1,-1) : 
    if a[i] == a[j] : break
    l += 1 
    
  for j in range(i+1,N) : 
    if a[i] == a[j] : break
    r += 1 

  ans += max(0,l-1) + r*l + max(0,r-1) 

print(ans)
