T = int(input()) 

for i in range(T) : 
  r,s=input().split()
  r = int(r)
  n=0
  while n<len(s):
    print(r*s[n],end = "")
    n+=1
  print()