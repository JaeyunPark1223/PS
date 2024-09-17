N = int(input())
alphabet = { "B" : [0,0], "E" : [0,0], "S" : [0,0], "I" : [0,0], "G" : [0,0], "O" : [0,0], "M" : [0,0] }

for i in range(N) : 
    a,n = input().split()
    alphabet[a][(int(n)%2)] += 1 

ans = 0 

for B in range(2): 
    for E in range(2): 
        for S in range(2): 
            for I in range(2): 
                for G in range(2): 
                    for O in range(2): 
                        for M in range(2): 
                            if ((B+E+S+S+I+E)*(G+O+E+S)*(M+O+O)) % 2 == 0 : 
                                ans += alphabet["B"][B] * alphabet["E"][E]* alphabet["S"][S]*alphabet["I"][I]*alphabet["G"][G]*alphabet["O"][O]*alphabet["M"][M]

print(ans)

      