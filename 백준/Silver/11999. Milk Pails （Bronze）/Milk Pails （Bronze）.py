X, Y, M = map(int,input().split())

ans = 0

for i in range(M//X+1):
  for j in range(M//Y+1):
    a = X*i+Y*j
    if a>ans and a<=M:
      ans = a

print(ans)