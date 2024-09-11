K, N = map(int,input().split())

a = []
ans = 0

for i in range(K):
  a.append(list(map(int,input().split())))

for j in range(N): # i : cow1'id 
  for i in range(N): # j : cow2'id
    sign = True 
    for k in range(K): # idx
      c1,c2 = -1,-1
      for l in range(N) : #idx   
          if a[k][l] == j+1 : 
            c1 = l
          elif a[k][l] == i+1 : 
            c2 = l 

      if c1 > c2 : sign = False 
    if sign : ans +=1 

print(ans)