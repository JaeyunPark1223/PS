a = input()

tmp = [[-1,-1] for i in range(26) ]
 
for i in range(len(a)):
   if tmp[ord(a[i])-65][0] ==-1:
     tmp[ord(a[i])-65][0] = i
   else:
     tmp[ord(a[i])-65][1] = i

x = [-1]*26

ans = 0
for i in range(26):
  for j in range(26):
    if tmp[i][0]<tmp[j][0] < tmp[i][1] < tmp[j][1]: # ABAB
      ans+=1
      
print(ans)