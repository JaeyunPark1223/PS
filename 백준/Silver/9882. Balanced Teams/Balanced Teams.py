from itertools import combinations 

a = []

for i in range(12):
  a.append(int(input()))

ans = float("inf")

for i in combinations(range(12), 3) : 
  tmp = []
  for j in range(12):
    if j not in i:
      tmp.append(j)
  for j in combinations(tmp, 3):
    tmp1 = []
    for k in tmp:
      if k not in j:
        tmp1.append(k)
    for k in combinations(tmp1,3):
      tmp2 = [] 
      for q in tmp1:
        if q not in k:
          tmp2.append(q)
      t1, t2, t3, t4 = sum([a[i[0]], a[i[1]], a[i[2]]]), sum([a[j[0]], a[j[1]], a[j[2]]]), sum([a[k[0]], a[k[1]],a[k[2]]]), sum([a[tmp2[0]], a[tmp2[1]], a[tmp2[2]]])
        
      if max(t1,t2,t3,t4) - min(t1,t2,t3,t4) < ans:
        ans = max(t1,t2,t3,t4) - min(t1,t2,t3,t4)
  

print(ans)
