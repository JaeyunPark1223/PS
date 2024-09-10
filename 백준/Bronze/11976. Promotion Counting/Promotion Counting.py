ans = [0]*3

for i in range(4): 
  a, b = map(int,input().split())
  for j in range(i):
    ans[j]+=b-a

print(*ans,sep="\n")