import sys
input = sys.stdin.readline

def x_beats_y(A,B) : 
  score_a,score_b = 0,0
  for a in A : 
    for b in B : 
      if a > b : score_a += 1
      elif b > a : score_b += 1
  if score_a > score_b :  return True
  return False

def solve(A,B) : 
  for a in range(1,11): 
    for b in range(1,11) : 
      for c in range(1,11) : 
        for d in range(1,11) : 
          if x_beats_y([a,b,c,d],A) and x_beats_y(B,[a,b,c,d]) : 
            return "yes"
  return "no"

T = int(input())

for t in range(T): 
  dice = list(map(int,input().split()))
  if x_beats_y(dice[:4],dice[4:]) : 
    A, B = dice[:4],dice[4:]
  else : 
    A, B = dice[4:],dice[:4]
  print(solve(A,B))