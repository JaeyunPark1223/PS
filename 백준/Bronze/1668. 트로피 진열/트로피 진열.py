N = int(input())

ans = []

A = 0
B = 0

for i in range(N):
  ans.append(int(input()))

left, right = 0,0
ans_l, ans_r = 0,0 

for i in range(N):
  if ans[i] > left : 
    left = ans[i] 
    ans_l += 1 

for i in range(N):
  if ans[N-(i+1)]>right:
    right = ans[N-(i+1)]
    ans_r +=1

print(ans_l)
print(ans_r)
