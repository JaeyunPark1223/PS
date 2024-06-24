X = []


for i in range(5):
     X.append([""] *  15)


for i in range(5): 
  A = input() 
  for j in range(len(A)) : 
    X[i][j] += A[j]


for i in range(15) :
  for j in range(5) : 
    print(X[j][i], end = "")
