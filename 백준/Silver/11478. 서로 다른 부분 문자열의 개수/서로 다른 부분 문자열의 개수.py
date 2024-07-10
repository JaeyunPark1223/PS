S = input()

A = set()

for i in range(len(S)):
  for j in range(i+1, len(S)+1):
    a = S[i:j]
    A.add(a)

print(len(A))