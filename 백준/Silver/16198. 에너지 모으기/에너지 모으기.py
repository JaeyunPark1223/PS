n=int(input())
l=list(map(int, input().split()))

def iwanttogohome(l, energy):
  if len(l)==2:
    return energy
  maxx=0
  for i in range(1,len(l)-1):
    energy2=l[i+1]*l[i-1]
    new=l[:i]+l[i+1:]
    maxx=max(maxx, iwanttogohome(new, energy2+energy))
  return maxx
#집에가고싶어요
print(iwanttogohome(l, 0))
    
    
    