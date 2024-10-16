from itertools import permutations

N = int(input())

tmp = []

for j in range(N):
  a = input().split()
  x, y = a[0], a[-1]
  tmp.append([x, y])

a = sorted(["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"])
permute = sorted(list(permutations(a)))


for k in range(len(permute)):
  b = 0
  for i in range(7):
    for j in range(N):
      if (permute[k][i] == tmp[j][0] and permute[k][i+1] == tmp[j][1]) or (permute[k][i] == tmp[j][1] and permute[k][i+1] == tmp[j][0]):
        b+=1
  if b == N:
    print(*permute[k], sep= "\n")
    break
