T = int(input())

for i in range(T):
  N = int(input())
  a = list(map(int, input(). split()))
  ans = set()
  for j in range(N-1):
    if a[j] == a[j+1]:
      ans.add(a[j])
  for j in range(N-2):
    if a[j] == a[j+2]:
      ans.add(a[j])
  if len(ans) == 0:
    print(-1)
  else: print(*sorted(ans))