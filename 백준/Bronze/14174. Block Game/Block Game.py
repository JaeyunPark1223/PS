def check(word): 
  a = [0] * 26 
  for w in word:
    a[ord(w)-ord("a")]+=1

  return a 

N = int(input())

ans = [0]*26

for i in range (N):
  a,b = input().split()
  cnt_a, cnt_b = check(a), check(b)

  for j in range(26) : 
    ans[j] += max(cnt_a[j] , cnt_b[j])
    
print(*ans,sep = "\n")

