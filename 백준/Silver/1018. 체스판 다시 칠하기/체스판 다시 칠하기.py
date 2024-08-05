def check(i,j,board) : 
  W , B = 0, 0  
  for n in range(8) : 
    for m in range(8) : 
      if (n+m) % 2 == 0 : # even 
        if board[i+n][j+m] != "B" : 
          B += 1 
        elif board[i+n][j+m] != "W" : 
          W += 1 
      else : # 홀수일 때, W로 시작했으면 B가 있어야 하고 B로 시작했으면 W가 있어야 한다. 
        if board[i+n][j+m] != "B" : 
          W += 1 
        elif board[i+n][j+m] != "W" : 
          B += 1 
          
  return min(W,B) 

N , M = map(int,input().split())
board = [] 
ans = 50 * 50 

for i in range(N) : board.append(input())

for i in range(N-7) : 
  for j in range(M-7) : 
    count = check(i,j,board) 
    ans = min(ans,count)

print(ans)