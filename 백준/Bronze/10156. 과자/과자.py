K, N, M = map(int, input().split())

b = K * N

b = b - M

if b > 0:
    print(b)
else:
    print(0)