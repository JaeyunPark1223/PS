a = input()
b = 1

for i in range(1,len(a)):
  b += 1 
  if a[i] == "=" : 
    if a[i-1] == "z" : 
      if i > 1 and a[i-2] == "d" : 
        b -= 2
      else : 
        b -= 1 

    elif a[i-1] == "c" or a[i-1] == "s" : 
      b -= 1 
        
  elif a[i] == "-" : 
    if a[i-1] == "c":
      b-=1

    if a[i-1] == "d":
      b-=1

  elif a[i] == "j" : 
    if a[i-1] == "l":
      b-=1

    if a[i-1] == "n":
      b-=1
  

print(b) 