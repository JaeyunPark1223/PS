a = ""
g = ""

for i in range(3):
  a += input()

for i in range(3):
  g += input()

a = list(a)
g = list(g) 

green = 0
yellow = 0

for i in range(9):
  if a[i] == g[i]:
    green+=1
    a[i] = 0 
    g[i] = 0

for i in range(9):
  for j in range(9):
    if a[i] == g[j] and g[j] != 0 :
      yellow+=1
      a[i] = 0 
      g[j] = 0

print(green)
print(yellow)