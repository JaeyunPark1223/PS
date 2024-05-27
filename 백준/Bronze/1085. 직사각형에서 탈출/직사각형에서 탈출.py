x, y, w, h = map(int, input().split())
z = min(x, y, (w-x), (h-y))
print(z)
