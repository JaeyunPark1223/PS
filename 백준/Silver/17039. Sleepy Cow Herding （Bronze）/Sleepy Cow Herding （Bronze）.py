A = list(map(int,input().split()))

A.sort() 

a = A[0]
b = A[1]
c = A[2]

if a+1 == b and b+1 == c:
  min_ = 0

elif b+2 == c or a+2 == b:
  min_ = 1

else: min_ = 2

max_ = max(c-b, b-a)-1

print(min_)
print(max_)

  

      