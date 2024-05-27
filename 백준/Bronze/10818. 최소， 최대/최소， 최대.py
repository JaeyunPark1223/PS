N = int(input())
a = list(map(int, input().split()))
b = -1000001
c = 1000001
for i in range(N):
  if a[i]>b:
    b=a[i]
  if a[i]<c:
    c=a[i]
print(c,b)
  