N,M = map(int,input().split())
L0 = []
INF = float("inf")
M1 = [[INF for _ in range(N)] for _ in range(N)]
for i in range(M):
    u,v,l = map(int,input().split())
    if u==1:
        L0.append((v-1,l))
    else:
        M1[u-1][v-1] = l
        M1[v-1][u-1] = l

for k in range(N):
    for i in range(N):
        for j in range(N):
            M1[i][j] = min(M1[i][j], M1[i][k]+M1[k][j])

Ans = INF
for li in L0:
    for lj in L0:
        if li != lj:
            n1,d1 = li
            n2,d2 = lj
            Ans = min(Ans, d1+d2+M1[n1][n2])

print(Ans if Ans != INF else -1)