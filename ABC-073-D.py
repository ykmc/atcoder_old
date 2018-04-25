from itertools import permutations
N,M,R = map(int,input().split())
r = list(map(int,input().split()))
Ans = 10**10
A = [[10**10 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    A[a-1][b-1] = c
    A[b-1][a-1] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            A[i][j] = min(A[i][j], A[i][k]+A[k][j])
P = list(permutations(r))
for p in P:
    d = 0
    for i in range(R-1):
        d += A[p[i]-1][p[i+1]-1]
    Ans = min(Ans,d)
print(Ans)