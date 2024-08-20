N = int(input())

A = list(map(int,input().split()))

even = 0
odd = 0

for i in A:
  if i%2 ==0:
    even+=1
  else:
    odd+=1

ans = 0

while odd > even:
  odd-=2
  even+=1
  
if odd < even :   
  print(2*odd+1)
else : 
  print(even+odd)

      