def simulirano_ohlajanja(G,t):
    n = len(G)
    for a in range(0, n): #spremenimo diagonalo da ima same 0
        if G[a][a] == 1:
            G[a][a] = 0
    d1 = int(n / 2)
    X = list(range(0, d1)) #vektorja indeksov vozlišč
    Y = list(range(d1, n))
    trenutna=[X, Y]
    najboljsi = trenutna
    while #nekej
        for i in X:
            for j in Y:
                x = X.index(i)
                y = Y.index(j)
                #kle morm dodat nova vektorja A in B tko da se X in Y ne spremenita
                A[x] = j
                B[y] = i
                R=[A,B]
                if kvaliteta(R,A,B) < kvaliteta(S,X,Y) or una vrjetnost pač
                    S=R
                zmanjšamo t
                if kvaliteta(trenutna)<kvaliteta(najboljsi)
                    najboljsi = trenutna
    return najboljsi

        #izracunamo kvaliteto X in Y- torej število povezav med X in Y


def kvaliteta(I,C,D): #izracuna stevilo povezav med mnozicama C,D v grafu
    d=len(C)
    stevilo=0
    for i in C:
        for j in D:
            if I[i][j]==1:
                stevilo +=1
    return stevilo

