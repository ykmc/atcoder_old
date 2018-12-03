N,M = map(int,input().split())
S = [" "]*N
for i in range(N):
    S[i] = input()

U = [[0 for _ in range(M)] for _ in range(N)]
D = [[0 for _ in range(M)] for _ in range(N)]
L = [[0 for _ in range(M)] for _ in range(N)]
R = [[0 for _ in range(M)] for _ in range(N)]

for m in range(M):
    for n in range(N):
        if n>0 and S[n][m]=="." and S[n-1][m]==".":
            U[n][m] = U[n-1][m]+1
        else:
            U[n][m] = 0

for m in range(M):
    for n in range(N):
        if n>0 and S[N-1-n][m]=="." and S[N-1-n+1][m]==".":
            D[N-1-n][m] = D[N-1-n+1][m]+1
        else:
            D[N-1-n][m] = 0


for n in range(N):
    for m in range(M):
        if m>0 and S[n][m]=="." and S[n][m-1]==".":
            L[n][m] = L[n][m-1]+1
        else:
            L[n][m] = 0

for n in range(N):
    for m in range(M):
        if m>0 and S[n][M-1-m]=="." and S[n][M-1-m+1]==".":
            R[n][M-1-m] = R[n][M-1-m+1]+1
        else:
            R[n][M-1-m] = 0

Ans = 0
for n in range(N):
    for m in range(M):
        Ans += D[n][m]*L[n][m] + L[n][m]*U[n][m] + U[n][m]*R[n][m] + R[n][m]*D[n][m]

print(Ans)

