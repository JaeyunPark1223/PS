a = input()

x,y = 0,0

for i in range(len(a)-1):
  if a[i] == "(" and a[i+1] == "(":
    x += 1
  elif a[i] == ")" and a[i+1] == ")":
    y+= x
    
print(y)
