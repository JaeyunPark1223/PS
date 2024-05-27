x=input()
a=0
for i in range(len(x)):
  if x[i] in "ABC" : 
    a+=3
  if x[i] in "DEF" : 
    a+=4
  if x[i] in "GHI" : 
    a+=5
  if x[i] in "JKL" : 
    a+=6
  if x[i] in "MNO" : 
    a+=7
  if x[i] in "PQRS" : 
    a+=8
  if x[i] in "TUV" : 
    a+=9
  if x[i] in "WXYZ" : 
    a+=10
print(a)