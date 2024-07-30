N = int(input())
a = list(map(int,input().split())) 
M = int(input())
b = list(map(int,input().split()))

d = {}

for c in a : 
  if c in d : 
    d[c]+=1
  else : 
    d[c] = 1  



for i in range(M):
  if b[i] in d : print(d[b[i]], end = " ")
  else: print(0, end = " ")