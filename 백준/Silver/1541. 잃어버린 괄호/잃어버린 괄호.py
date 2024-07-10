A = input().split("-")

for i in range(len(A)):
  tmp = A[i].split("+")
  a = 0
  for t in tmp : 
    a+=int(t) 
  A[i] = a
x = A[0]
for i in range(1,len(A)):
  x-=A[i]

print(x)
  