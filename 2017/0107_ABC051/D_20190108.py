N,M = map(int,input().split())

A = [[9999 for _ in range(N)] for _ in range(N)]
B = []
for i in range(M):
    a,b,c = map(int,input().split())
    A[a-1][b-1] = c
    A[b-1][a-1] = c
    B.append((a-1,b-1,c))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:
                A[i][j] = 0
            else:
                A[i][j] = min(A[i][j], A[i][k]+A[k][j])

ans = 0
for i in range(M):
    a,b,c = B[i]
    for j in range(N):
        if A[j][b] == A[j][a] + c:
            break
    else:
        ans += 1

print(ans)