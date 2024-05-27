while True:
  x = input()
  if x == "#" : 
    break
  b=0
  for i in range(len(x)):
    if x[i] == 'a' or x[i] =='i' or x[i] =='e' or x[i] == 'o' or x[i] == 'u' or x[i] == 'A' or x[i] =='I' or x[i] =='E' or x[i] == 'O' or x[i] == 'U':
      b+=1
  print(b)