import numpy as np
import scipy.sparse.csgraph as spg

N,M = map(int,input().split())
INF = float("inf")
A = np.array([[INF]*N]*N)
L = []
for i in range(M):
    u,v,l = map(int,input().split());
    if u==1:
        L.append((v-1,l))
    else:
        A[u-1,v-1] = A[v-1,u-1] = l

A = spg.floyd_warshall(A)

Ans = INF
for li in L:
    for lj in L:
        if li != lj:
            n1,d1 = li
            n2,d2 = lj
            Ans = min(Ans, d1+d2+A[n1][n2])

print(int(Ans) if Ans != INF else -1)
