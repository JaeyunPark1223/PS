N = int(input())
cows = [ list(input()) for _ in range(N) ]
ans = 0 


for i in range(N-1,-1,-1) : 
  for j in range(N-1,-1,-1) : 
    if cows[i][j] == "1" : 
      for k in range(i+1):
        for _ in range(j+1):
          if cows[k][_] == "1":
            cows[k][_] = "0"
          elif cows[k][_] == "0":
            cows[k][_] = "1"    
      ans += 1 

print(ans)