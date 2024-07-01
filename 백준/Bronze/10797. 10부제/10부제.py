A = int(input())
B = list(map(int, input().split()))
C = 0

for i in range(5):
  if B[i] == A:
    C+=1

print(C)