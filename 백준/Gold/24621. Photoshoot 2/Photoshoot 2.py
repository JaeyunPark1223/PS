N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

x = [0] * (N+1)

for i in range(N) : 
  x[b[i]] = i+1 
  


a = [ x[i] for i in a ] #list comprehension

max_,ans = 0,0

for i in a : 
  if i > max_ : max_ = i
  else : ans += 1 
    
print(ans)