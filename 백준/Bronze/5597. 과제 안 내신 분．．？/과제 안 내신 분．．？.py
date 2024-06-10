ans = [0] * 30 

for i in range(28):
  c = int(input()) # 숙제 한 사람의 출석 번호 
  ans[c-1] = 1 # 숙제 했다 --> 1로 바꿔주기 
  # c-1 --> 문제에서는 출석번호를 1부터 센다. 근데 파이썬은 번호를 0부터 세서, 1씩 차이가 난다. 

for i in range(30):
  if ans[i]==0:
    print(i+1)