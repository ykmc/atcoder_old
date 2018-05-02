N,M = map(int,input().split())
G = [[10**5 for _ in range(N)] for _ in range(N)]
E = []
Ans = 0

for i in range(M):
    a,b,c = map(int,input().split())
    G[a-1][b-1] = c
    G[b-1][a-1] = c
    E.append((a-1,b-1,c))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:
                G[i][j] = 0
            else:
                G[i][j] = min(G[i][j], G[i][k]+G[k][j])


for i in range(M):
    a,b,c = E[i]
    for j in range(N):
        if G[j][b] == G[j][a] + c:
           break
    else:
        Ans += 1

print(Ans)

