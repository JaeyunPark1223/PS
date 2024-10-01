N = int(input())

X = [[40001,0],[40001,0]] # [minx1,maxx1], [minx2,maxx2]
Y = [[40001,0],[40001,0]] # [miny1,maxy1], [miny2,maxy2]
tmp = []

for i in range(N):
  x, y = map(int, input(). split())
  tmp.append([x,y])
  
  if x<X[0][0]:
    X[1][0]=X[0][0]
    X[0][0]=x
  elif x>=X[0][0] and x<X[1][0]:
    X[1][0]=x
  if x>X[0][1]:
    X[1][1]=X[0][1]
    X[0][1]=x
  elif x<=X[0][1] and x>X[1][1]:
    X[1][1]=x
  if y<Y[0][0]:
    Y[1][0]=Y[0][0]
    Y[0][0]=y
  elif y>=Y[0][0] and y<Y[1][0]:
    Y[1][0]=y
  if y>Y[0][1]:
    Y[1][1]=Y[0][1]
    Y[0][1]=y
  elif y<=Y[0][1] and y>Y[1][1]: 
    Y[1][1]=y

  
ans = (X[0][1]-X[0][0]) * (Y[0][1]-Y[0][0])

for i in range(N) : 
  x,y = tmp[i][0], tmp[i][1]
  minx, maxx = X[0][0], X[0][1]
  miny, maxy = Y[0][0], Y[0][1]

  if x == minx : minx = X[1][0]
  if x == maxx : maxx = X[1][1]
  if y == miny : miny = Y[1][0]
  if y == maxy : maxy = Y[1][1]


  ans = min(ans, (maxx-minx) * (maxy-miny))

print(ans)
 