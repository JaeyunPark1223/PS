N = int(input())

oldest = ["", 0, 0, 0]
youngest = ["", 31, 12, 9999]

for i in range(N):
  name, d, m, y = input().split()
  d, m, y = int(d), int(m), int(y)
  a= [name, d, m, y]
  if a[3] > oldest[3]:
    oldest = a
  if a[3] == oldest[3]:
    if a[2] > oldest[2]:
      oldest = a
  if a[3] == oldest[3]:
    if a[2] == oldest[2]:
      if a[1] > oldest[1]:
        oldest = a
  if a[3] < youngest[3]:
    youngest = a
  if a[3] == youngest[3]:
    if a[2] < youngest[2]:
      youngest = a
  if a[3] == youngest[3]:
    if a[2] == youngest[2]:
      if a[1] < youngest[1]:
        youngest = a

print(oldest[0])
print(youngest[0])