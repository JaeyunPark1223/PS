def solve() :
  for i in range(9):
    for j in range(i+1, 9):
      # sum(A) - A[i] - A[j] == 100 
      # i , j 번째 난쟁이를 뺀다! 
      if sum(A) - A[i] - A[j] == 100:
        A.remove(A[i]) 
        A.remove(A[j-1])
        A.sort()
        print(*A,sep="\n")
        return 

  
A = []

for i in range(9):
  a = int(input())
  A.append(a)


solve() 