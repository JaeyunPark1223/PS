x = int(input())
N = int(input())
total = 0
for i in range(N):
    a,b = map(int,input().split())
    total = total +  (a*b)
    
if total == x:
    print("Yes")
else:
    print("No")