N = int(input())
a = []
cows = { "Bessie" : 7, "Elsie" : 7 , "Mildred" : 7}

for i in range(N):
  day, cow , change = input().split()
  a.append([ int(day), cow, int(change)])

a.sort() 

max_cow = set() 
ans = 0 
for i in range(N) : 
    cows[a[i][1]] += a[i][2]
    tmp = max_cow.copy()
    max_value = -1 
    for name,output in cows.items()  : 
        if output > max_value : 
            max_value = output 
            tmp = {name}
        elif output == max_value : 
            tmp.add(name)  
    if tmp != max_cow : 
        max_cow = tmp 
        ans += 1 

print(ans)