N,M,X = map(int,input().split())

L,R = [],[]
for i in range(M):
    l,r = map(int,input().split())
    L.append(l-1)
    R.append(r-1)
P,Q = [],[]
for i in range(X):
    p,q = map(int,input().split())
    P.append(p-1)
    Q.append(q-1)

A = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    l,r = L[i],R[i]
    A[r][0] += 1
    A[r][l+1] -= 1
    A[N][0] -= 1 
    A[N][l+1] += 1

for i in range(N):
    for j in range(N):
        A[i+1][j] += A[i][j]
for i in range(N):
    for j in range(N):
        A[i][j+1] += A[i][j]

for i in range(X):
    p,q = P[i],Q[i]
    print(A[q][p])