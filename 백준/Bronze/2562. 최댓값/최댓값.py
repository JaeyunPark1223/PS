b=0
c=0
d=0
for i in range(9):
  a=int(input())
  c+=1
  if a>b:
    b=a
    d=c
print(b)
print(d)