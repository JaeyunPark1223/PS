N = int(input())

ans = set()

for i in range(N):
  a, b = input().split()
  if b == "enter":
    ans.add(a)
  else:
    ans.remove(a)

print(*sorted(ans,reverse = True), sep = "\n")

  