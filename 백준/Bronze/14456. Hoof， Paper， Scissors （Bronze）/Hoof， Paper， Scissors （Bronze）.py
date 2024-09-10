N = int(input()) 

ans = [0]*2

for i in range(N): 
  a,b = map(int,input().split())
  if a == 1 and b ==3:
    ans[0] +=1
  elif a == 3 and b == 1:
    ans[1] +=1
  elif a > b:
    ans[0] +=1
  elif a< b:
    ans[1] +=1
          
print(max(ans))