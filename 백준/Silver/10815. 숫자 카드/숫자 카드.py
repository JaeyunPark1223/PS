
N = int(input())
a = set(map(int,input().split()))
M = int(input())
b = list(map(int,input().split()))

ans = []

for c in b : 
  if c in a : 
    ans.append(1) 
  else : ans.append(0)
    
print(*ans) 

