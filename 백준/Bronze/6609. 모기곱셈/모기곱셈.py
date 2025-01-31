while True:
  try:
    M, P, L, E, R, S, N= map(int, input().split())
    ahrl=M
    dkf=M*E
    dbcnd=L
    qjseprl=P
    for i in range(N):
      ahrl=qjseprl//S
      qjseprl=dbcnd//R
      dbcnd=dkf
      dkf=ahrl*E
    print(ahrl)
  except:
    break

