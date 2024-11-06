def check(word) : 
  for a in range(4) : 
    for b in range(4) : 
      for c in range(4) : 
        for d in range(4) : 
          if (a != b != c != d) and ( b != d != a != c ):
            res = 0 
            choose = [a,b,c,d]
            for i in range(len(word)) : 
              if word[i] in x[choose[i]] : 
                res += 1 
            if res == len(word) : return True 
  return False 

N = int(input())
x = []
for i in range(4):
  x.append(input())


for i in range(N) : 
  word = input() 
  if check(word) : 
    print("YES")
  else : 
    print("NO")
