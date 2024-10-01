N, Q = map(int, input(). split())

c = list(map(int, input(). split()))
t = list(map(int, input(). split()))
x = []
for i in range(N):
  x.append(c[i]-t[i])

x.sort(reverse=True)

tmp = []

for i in range(Q):
  v, s = map(int, input(). split())
  if x[v-1]>s:
    print("YES")
  else:
    print("NO")
