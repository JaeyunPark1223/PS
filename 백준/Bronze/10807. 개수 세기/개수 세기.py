a = int(input())
b = list(map(int,input().split()))
c = int(input())
x = 0
for i in range(a):
  if b[i] == c:
    x+=1
print(x)