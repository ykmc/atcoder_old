N,M = map(int,input().split())
R = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):
    x,y = map(int,input().split())
    R[x-1][y-1] = 1
    R[y-1][x-1] = 1
for i in range(N):
    R[i][i] = 1

Ans = 0
i = 0
check = False
while i < 2**N:
    bit = bin(i)[2:].zfill(N)
    check = True
    G = []
    for j in range(N):
        if bit[j] == "1":
            G.append(j)
    for g1 in G:
        for g2 in G:
            if R[g1][g2] == 0:
                check = False
    if check:
        Ans = max(Ans, bit.count("1"))
    i += 1

print(Ans)
