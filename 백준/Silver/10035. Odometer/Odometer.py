x, y = map(int,input().split())

ans = 0

for digit in range(3,18): # 111. 1111. 11111
  for i in range(10) : # i로 숫자를 다 채운다
    a = [str(i)] * digit #["0","0","0"]
    for j in range(10) :  # 한 자리를 어떤 숫자로 바꿀 지 결정 
      if i == j : continue
      for k in range(digit) :  # k번째 자리 숫자를 J로 바꿔본다. 
        a[k] = str(j)
        if a[0] != '0' and y >= int("".join(a)) >= x:
          ans+=1
        a[k] = str(i)


print(ans)