def solve(x,y) : 
  sign = True 
  step = 1
  curr = x
  ans = 0 

  while True : 
    if sign : 
      goal = x + step
      if curr <= y <= goal   : 
        ans += y - curr 
        return ans 

      ans += goal - curr 
      
    else : 
      goal = x - step
      if goal <= y <= curr  :
        ans += curr - y 
        return ans 

      ans += curr - goal 

  
    step *= 2 
    sign = not(sign)
    curr = goal 



x, y = map(int,input().split())

print(solve(x,y))